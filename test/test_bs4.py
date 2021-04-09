from bs4 import BeautifulSoup

html = '''
<td class="title black>
    <div class="tit3" data-no="10">
        <a href="/movie/b1/m1/basic.nhn?code=189075" title="자산어보">자산어보</a>
    </div>
</td>
'''

# 1. tag 조회
def ex01():
    bs = BeautifulSoup(html, 'html.parser')
    # print(bs)

    # td 태그 가져오기
    tag_td = bs.td
    # print(tag_td)

    # a 태그 가져오기
    tag_a = bs.a
    # print(tag_a)

    # td 태그 안에 있는 a 태그 가져오기
    tag_a = tag_td.a
    print(tag_a)

    # None 일때
    tag_h1 = bs.td.h1
    print(tag_h1) # h1 태그가 없기 때문에 None이 출력

# 2. attribute로 조회하기
def ex02():
    bs = BeautifulSoup(html, 'html.parser')
    tag_td = bs.find('td', attrs={'class': ['title', 'black']})
    print(tag_td)

    tag_div = bs.find('div', attrs={'class': 'tit3', 'data-no': '10'})
    print(tag_div)


if __name__ == '__main__':
    # ex01()
    ex02()