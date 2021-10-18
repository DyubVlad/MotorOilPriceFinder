import requests


def get_oil_list():
    cookies = {'KFP_DID': '25143242-25d0-6b10-6f64-8c667982098c',
               'CityCookie': 'orl', 'oxxfgh': '469ac60f-e5d0-47e2-bd0f-07b20e917b24#0#1800000#5000#1800000'}
    user_agent = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                'Chrome/89.0.4389.72 Safari/537.36'}
    lenta_session = requests.Session()
    get_to_api = 'https://lenta.com/api/v1/skus/list'
    lenta_url = 'https://lenta.com/catalog/avtotovary/ekspluatacionnye-zhidkosti/masla/'

    start_page = lenta_session.get(lenta_url, headers=user_agent, cookies=cookies, verify=True)
    list_sku = lenta_session.post(get_to_api, headers=user_agent, cookies=cookies, verify=True)
    print()


get_oil_list()
print()