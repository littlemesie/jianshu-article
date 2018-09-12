# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

headers = {
    'Cookie': '_ga=GA1.2.1323902367.1500108642; read_mode=day; default_font=font2; locale=zh-CN; hibext_instdsigdip=1; _gid=GA1.2.1338869087.1536396682; hibext_instdsigdipv2=1; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1535091055,1535250251,1536396681,1536402519; remember_user_token=W1s1NTE4MzEyXSwiJDJhJDEwJE9LUU9jNC4xcEt2eXlzSExETjJoMWUiLCIxNTM2NDAyODgyLjIzNzI0NjUiXQ%3D%3D--f094ed2dd7e0f0c5e607c7d4e1cf10eb20106695; _m7e_session=0c1949c06fe7289423efa43aebe7fe90; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%225518312%22%2C%22%24device_id%22%3A%2215f7d12b7f1255-0bcafb4b1e1c86-31657c03-1296000-15f7d12b7f2c5c%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22desktop%22%2C%22%24latest_utm_medium%22%3A%22index-collections%22%7D%2C%22first_id%22%3A%2215f7d12b7f1255-0bcafb4b1e1c86-31657c03-1296000-15f7d12b7f2c5c%22%7D; _gat=1; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1536406093',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
def start_request():
    url = 'https://www.jianshu.com/c/NEt52a?order_by=commented_at&page=1'
    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.text,'lxml')
    li_list = soup.find('ul',class_='note-list').find_all('li')
    for li in li_list:
        title = li.find('a',class_='title').text.strip()
        title_id = li.find('a',class_='title')['href'].split('/')[-1]
        article_url = 'https://www.jianshu.com' + li.find('a',class_='title')['href']
        author = li.find('a',class_='nickname').text.strip()
        author_id = li.find('a',class_='nickname')['href'].split('/')[-1]
        author_url = 'https://www.jianshu.com' + li.find('a',class_='nickname')['href']
        comment_num = li.find('div', class_='meta').find_all('a')[1].text.strip()
        comment_url = 'https://www.jianshu.com' + li.find('div', class_='meta').find_all('a')[1]['href']
        like_num = li.find('div', class_='meta').find('span').text.strip()
        print(title,title_id,author,author_id,comment_num,like_num)
        print(article_url,author_url,comment_url)

def article_content(url):
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    read_num = soup.find('span',class_='views-count')
    print(soup)



if __name__ == '__main__':
    start_request()
    # article_content('https://www.jianshu.com/p/e7bb97218946')