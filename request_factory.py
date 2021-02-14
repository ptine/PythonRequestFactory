from lxml.html import fromstring
import requests
from bs4 import BeautifulSoup
from random import randint
from fake_useragent import UserAgent


class RequestFactory():
    
    def get_proxies(self):
        url = 'https://free-proxy-list.net/'
        response = requests.get(url)
        parser = fromstring(response.text)
        proxies = []

        parser = fromstring(response.text)
        
        for td in parser.xpath('//tbody/tr')[:5]:

            ip_address = td.xpath('.//td[1]/text()')[0]
            port = td.xpath('.//td[2]/text()')[0]

            proxy = ":".join([ip_address, port])
            print(proxy)

            proxies.append(proxy)

        return proxies

    def get_requests_proxy_params(self):
        
        proxies = self.get_proxies()
        index = randint(0, len(proxies) -1)
        proxy =  proxies[index]

        proxy_params={"http": proxy}

        return proxy_params

    def get_fake_user_agent(self):
        ua = UserAgent()
        ua.update()
        
        return ua.random

    def get_request(self):
        proxy_params = self.get_requests_proxy_params()
        print(proxy_params)

        fake_headers = {'User-Agent': self.get_fake_user_agent()}
        print(fake_headers)

        r = requests.Session()
        r.headers = fake_headers
        r.verify = False
        r.proxies = proxy_params
        
        return r

if __name__ == '__main__':    
    request = RequestFactory().get_request()
    response = request.get("https://www.google.it")
    
    print(response.status_code)
    print(response.json)