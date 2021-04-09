from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

from collection import crawler


def ex01():
    request = Request("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")
    response = urlopen(request)
    html = response.read().decode('cp949')
    # print(html)

    bs = BeautifulSoup(html, 'html.parser')
    # divs = bs.find('div', attrs={'class': 'tit3'}) # div 태그에 class tit3인 것을 한개 찾는다
    divs = bs.findAll('div', attrs={'class': 'tit3'})  # div 태그에 class tit3인 것을 모두 찾는다
    # print(divs)

    for index, div in enumerate(divs):
        # print(div.a) # div.a -- div태그 안에 있는 a 태그를 가져온다
        # print(index+1, div.a.text) # div 안에 있는 a 태그의 text를 가져온다
        print(index + 1, div.a.text, div.a['href'], sep=': ')  # ++ url 추가 출력


def ex02():
    html = crawler.crawling(url="https://movie.naver.com/movie/sdb/rank/rmovie.nhn",
                            encoding='cp949')
    # print(html)

    bs = BeautifulSoup(html, 'html.parser')
    # divs = bs.find('div', attrs={'class': 'tit3'}) # div 태그에 class tit3인 것을 한개 찾는다
    divs = bs.findAll('div', attrs={'class': 'tit3'})  # div 태그에 class tit3인 것을 모두 찾는다
    # print(divs)

    for index, div in enumerate(divs):
        # print(div.a) # div.a -- div태그 안에 있는 a 태그를 가져온다
        # print(index+1, div.a.text) # div 안에 있는 a 태그의 text를 가져온다
        print(index + 1, div.a.text, div.a['href'], sep=': ')  # ++ url 추가 출력


if __name__ =='__main__':
    # ex01()
    ex02()