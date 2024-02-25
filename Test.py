import requests

url = 'https://movie.douban.com/top250'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}


KeyLenth = 150

def Get_Content_From_Url(url, headers):
    r = requests.get(url, headers=headers)
    return r

def Analysis_Content(Html):
    Key_Prefix = 'class=""><spanclass="title">'
    Key_Suffix_1 = '</span><spanclass="title">&nbsp;/&nbsp'
    Key_Suffix_2 = '</span><spanclass="other">&nbsp;/&nbsp'
    MovieName = []
    Length = len(Key_Prefix)
    title2 = title1 = title3 = index = 0
    Html = "".join(Html.text.split())
    while((title2 != -1 ) and (title3 != -1 ) and (title1 != -1)):
        title1 = Html.find(Key_Prefix, index)
        title2 = Html.find(Key_Suffix_1, index)
        title3 = Html.find(Key_Suffix_2, index)
        if(((title2 - title1) > (title3 - title1) ) and (title3 != -1)):
            t = Html[title1 + Length: title3]
        elif((title1 != -1)):
            t = Html[title1 + Length: title2]
        if(title1 != -1):
            # print(t)
            MovieName.append(t)
        index = title1 + KeyLenth
    return MovieName

def Analysis_Movie_Link(Html):
    Key_Prefix = '<divclass="hd"><ahref="'
    Key_Suffix = '"class=""><spanclass="title">'
    Movielink = []
    Length = len(Key_Prefix)
    title2 = title1 = title3 = index = 0
    Html = "".join(Html.text.split())
    t = "0"
    while((title2 != -1 ) and (title3 != -1 ) and (title1 != -1)):
        title1 = Html.find(Key_Prefix, index)
        title2 = Html.find(Key_Suffix, index)
        # title3 = Html.find(Key_Suffix_2, index)
        # if(((title2 - title1) > (title3 - title1) ) and (title3 != -1)):
        #     t = Html[title1 + Length: title3]
        # elif((title1 != -1)):
        t = Html[title1 + Length: title2]
        if(title1 != -1):
            # print(t)
            Movielink.append(t)
        index = title1 + KeyLenth
    return Movielink

def Make_Dict(MovieName, Movielink):
    TextList = []
    MovieNum = 0
    Text = {'name': 0,
            'link': 0}
    if(len(MovieName) == len(Movielink)):
        MovieNum = len(MovieName)

    while (MovieNum):
        # tname = MovieName[len(MovieName) - MovieNum]
        # tlink = Movielink[len(Movielink) - MovieNum]
        # Text['name'] = [tname]
        # Text['link'] = [tlink]
        TextList.append(small_Dict(MovieName, Movielink, MovieNum))
        MovieNum = MovieNum-1

    return TextList

def small_Dict(MovieName, Movielink, num):
    Text = {'name': 0,
            'link': 0}
    tname = MovieName[len(MovieName) - num]
    tlink = Movielink[len(Movielink) - num]
    Text['name'] = [tname]
    Text['link'] = [tlink]
    return Text



# def test():
#     t = "0"
#     testlist =[]
#     while(t != "3"):
#         testlist.append(t)
#         if(t == "0"):
#             t = "1"
#         elif(t == "1"):
#             t = "2"
#         elif(t == "2"):
#             t = "3"
#
#     return testlist

def main():

    douban = Get_Content_From_Url(url, headers)

    # print(Analysis_Content(douban))
    # print(Analysis_Movie_Link(douban))
    print(Make_Dict(Analysis_Content(douban), Analysis_Movie_Link(douban)))
    # print(test())

if __name__ == "__main__":
    main()
