import requests
import bs4

def get_oil_page(page):
    cookies = {'KFP_DID': '25143242-25d0-6b10-6f64-8c667982098c',
               'CityCookie': 'orl', 'oxxfgh': '469ac60f-e5d0-47e2-bd0f-07b20e917b24#0#1800000#5000#1800000'}
    user_agent = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                'Chrome/89.0.4389.72 Safari/537.36'}
    lenta_session = requests.Session()
    lenta_url = 'https://lenta.com/catalog/avtotovary/ekspluatacionnye-zhidkosti/masla/' + page
    oil_page = lenta_session.get(lenta_url, headers=user_agent, verify=True)
    print()


def pars_oil_info():
    get_oil_page()


print()
