import re

def html_search(text):
    """
    Search html url and print it.
    """
    urlRegex = re.compile(r'https?://.*\.html')
    urls = urlRegex.findall(text)
    print("\n".join(urls))
    return urls

html_search("""
    http://www.city.hadano.kanagawa.jp/
http://www.city.hadano.kanagawa.jp/www/genre/1000000000001/index.html
http://www.city.hadano.kanagawa.jp/www/genre/1000000000400/index.html
http://www.city.hadano.kanagawa.jp/www/contents/1484877722560/index.html
http://www.city.hadano.kanagawa.jp/www/contents/1001000000657/index.html
http://www.city.hadano.kanagawa.jp/www/contents/1001000004501/index.html
http://www.city.hadano.kanagawa.jp/www/contents/1001000003530/index.html
http://www.city.hadano.kanagawa.jp/www/contents/1001000003744/index.html
http://www.city.hadano.kanagawa.jp/www/contents/1484873131127/index.html
http://www.city.hadano.kanagawa.jp/www/contents/1001000001816/index.html
http://www.city.hadano.kanagawa.jp/www/contents/1001000004382/index.html
http://www.city.hadano.kanagawa.jp/www/contents/1001000000040/index.html
http://www.city.hadano.kanagawa.jp/www/genre/1000000000152/index.html
http://www.city.hadano.kanagawa.jp/www/contents/1001000001837/index.html
http://www.city.hadano.kanagawa.jp/www/contents/1001000004219/index.html
http://www.city.hadano.kanagawa.jp/www/contents/1001000001801/index.html
http://www.city.hadano.kanagawa.jp/www/contents/1001000000501/index.html
http://www.city.hadano.kanagawa.jp/www/contents/1001000000896/index.html
http://www.city.hadano.kanagawa.jp/www/contents/1001000002297/index.html
http://www.city.hadano.kanagawa.jp/www/contents/1001000002123/index.html
http://www.city.hadano.kanagawa.jp/www/contents/1001000004209/index.html
http://www.city.hadano.kanagawa.jp/www/contents/1001000001306/index.html
http://www.city.hadano.kanagawa.jp/www/genre/1000000000118/index.html
http://www.city.hadano.kanagawa.jp/www/genre/1482370873522/index.html
http://www.city.hadano.kanagawa.jp/www/contents/1001000002683/index.html
http://www.city.hadano.kanagawa.jp/www/genre/1000000000611/index.html
http://www.city.hadano.kanagawa.jp/www/contents/1001000004513/index.html
http://www.city.hadano.kanagawa.jp/www/contents/1001000002964/index.html
http://www.city.hadano.kanagawa.jp/www/contents/1001000003428/index.html
http://www.city.hadano.kanagawa.jp/www/contents/1001000000144/index.html
http://www.city.hadano.kanagawa.jp/www/contents/1001000000827/index.html
http://www.city.hadano.kanagawa.jp/www/genre/1000000000364/index.html
http://www.city.hadano.kanagawa.jp/www/contents/1001000003324/index.html
http://www.city.hadano.kanagawa.jp/www/contents/1001000000866/index.html
http://www.city.hadano.kanagawa.jp/www/contents/1001000000852/index.html
http://www.city.hadano.kanagawa.jp/www/contents/1001000003135/index.html
http://www.city.hadano.kanagawa.jp/www/contents/1001000002860/index.html
http://www.city.hadano.kanagawa.jp/www/contents/1001000003577/index.html
http://www.city.hadano.kanagawa.jp/www/contents/1001000002591/index.html
http://www.city.hadano.kanagawa.jp/www/genre/1000000000213/index.html
    """)
