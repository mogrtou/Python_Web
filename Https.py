import HttpsLib



def main():
    Https = HttpsLib.Request_Socket("movie.douban.com", 443, "GET",
                                    "GET /top250 HTTP/1.1", "Host: movie.douban.com",
                                    "User-Agent:Mozilla/5.0(Macintosh;Intel Mac 0sX10.15;rv:123.0)Gecko/2010010")


    Https.connect_server()

    Https.request_data()

if __name__ == "__main__":
    main()