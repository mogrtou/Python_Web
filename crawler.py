import requests


# 一些辅助函数

def ensure(condition, msg):
    # condition 是 True/False
    # 如果是 False，则会打印 msg，然后终止程序
    assert condition, msg


# 从 string 字符串中找到 left 字符串和 right 字符串中间的字符串
# 比如 <span>abc</span>
# left 是 <span>, right 是 </span> 
# 会返回 abc
# 如果没找到的话，就会返回 None
def string_between(string, left, right):
    i1 = string.find(left)
    start = i1 + len(left)
    end = string.find(right, start)

    if i1 == -1 or end == -1:
        return None
    else:
        return string[start: end]


# 业务函数

def html_from_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0',
    }
    r = requests.get(url, headers=headers)
    return r.text


def movie_name_list(html):
    result = []

    left = '<span class="title">'
    index = html.find(left)
    while index != -1:
        sub_str = html[index:]
        name = string_between(sub_str, left, '</span>')

        # 过滤掉没用数据
        if not name.startswith('&nbsp;/&nbsp;'):        
            result.append(name)
        index = html.find(left, index + len(left))

    return result


def movie_url_list(html):
    result = []

    left = '<div class="pic">'
    index = html.find(left)
    while index != -1:
        sub_str = html[index]
        url = string_between(sub_str, '<a href="', '">')

        result.append(url)
        index = html.find(left, index + len(left))

    return result


def merge_data(name_list, url_list):
    result = []
    for i in range(len(name_list)):
        name = name_list[i]
        url = url_list[i]
        d = {
            'name': name,
            'url': url,
        }
        result.append(d)
    return result


# 下面是一些测试函数

def test_string_between1():
    s = '#a#'
    expected = 'a'
    actual = string_between(s, '#', '#')
    ensure(expected == actual, 'test_string_between1')


def tests():
    test_string_between1()


# 程序主入口

def main():
    url = 'https://movie.douban.com/top250'
    html = html_from_url(url)
    name_list = movie_name_list(html)
    url_list = movie_url_list(html)
    data = merge_data(name_list, url_list)
    print('data', data)


if __name__ == '__main__':
    main()

    # 跑测试
    # tests()
