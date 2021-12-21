import requests
from bs4 import BeautifulSoup
from proxies import getProxy, renew


def get_news_Tradingview():
    proxy = getProxy()
    proxyDict  = {
        "http": proxy
    }
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    r = requests.get("https://vn.tradingview.com/ideas/?sort=recent", headers=headers, proxies=proxyDict)
    soup = BeautifulSoup(r.text, 'html.parser')

    myDivs = soup.findAll("div", class_="js-userlink-popup-anchor")
    list = []
    for item in myDivs:
        new = {}
        new["title"] = item.find_next("div", class_="tv-widget-idea__title-row").text
        new["code"] = item.find_next("div", class_="tv-widget-idea__symbol-info").a.text
        new["link"] = "https://vn.tradingview.com" + item.find_next("div", class_="tv-widget-idea__title-row").a.get("href")
        new["description"] = item.find_next("p", class_="tv-widget-idea__description-row").text
        new["image"] = "https://s3.tradingview.com/7/7ptIOwYi_big.png"
        list.append(new)
    renew(proxy)
    return list