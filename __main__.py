# __main__ 이 있으면 터미널에서 디렉토리 이름으로 접근 가능

import time
from datetime import datetime
from itertools import count

from bs4 import BeautifulSoup
from selenium import webdriver

from collection import crawler
import pandas as pd




def crawling_pelicana():  # 페이지가 HTML 형식
    results = []

    # 페이지 처음부터 한페이지씩 이동
    for index in count(start=1, step=1):
        url = f"https://pelicana.co.kr/store/stroe_search.html?page={index}&branch_name=&gu=&si="
        html = crawler.crawling(url)

        bs = BeautifulSoup(html, 'html.parser')
        tag_table = bs.find('table', attrs={'class': ['table', 'mt20']})
        tag_tbody = tag_table.find('tbody')
        tags_tr = tag_tbody.findAll('tr')

        # 끝 검출
        if len(tags_tr) == 0:
            print('페이지 끝 - ' +str(index))
            break


        for tag_tr in tags_tr:
            datas = list(tag_tr.strings)  # strings == 개행 단위로 출력
            name = datas[1]  # 지점 이름
            address = datas[3]  # 가게 주소
            # print(name, address)
            sidogugun = address.split(' ')[:2]  # split(' ') -- 띄어쓰기를 기준으로 나눠줌 // 시, 도, 구까지 출력

            t = (name, address) + tuple(sidogugun)
            results.append(t)  # 튜플 형태로 저장
    # print(results)

    # store
    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gugun'])
    table.to_csv('results/pelicana.csv', encoding='utf-8', mode='w', index=True)


def crawing_nene():
    pass


def crawing_kyochon():
    pass


def crawing_goobne():  # 페이지가 JavaScript 일때
    # Chrome 브라우저 시작
    url = "http://goobne.co.kr/store/search_store.jsp"
    wd = webdriver.Chrome("C:\\Users\\rlatj\\Desktop\\AI 융복합\\chromedriver_win32\\chromedriver.exe")

    # 페이지 이동
    wd.get(url)
    time.sleep(3)

    results = []

    for index in count(start=1, step=1):
        # 자바 스크립트 실행
        script = f'store.getList({index})'
        wd.execute_script(script)
        print(f'{datetime.now()}: success for request[{script}]')
        time.sleep(3)

        # 자바스크립트 실행된 HTML(동적으로 랜더링된 HTML) 가져오기
        html = wd.page_source
        # print(html)


        # 파싱하기(bs4)
        bs = BeautifulSoup(html, 'html.parser')
        tag_tbody = bs.find('tbody', attrs={'id': 'store_list'})
        tags_tr = tag_tbody.findAll('tr')

        # 끝 검출
        if tags_tr[0].get('class') is None:
            break

        for tag_tr in tags_tr:
            datas = list(tag_tr.strings)

            name = datas[1]
            address = datas[6]
            # print(datas)
            sidogugun = address.split()[:2]

            t = (name, address) +tuple(sidogugun)
            results.append(t)

    # 브라우저 닫기
    wd.close()

    # store
    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gugun'])
    table.to_csv('results/goobne.csv', encoding='utf-8', mode='w', index=True)


if __name__ == '__main__':
    # crawling_pelicana()
    # crawing_nene()
    # crawing_kyochon()
    crawing_goobne()