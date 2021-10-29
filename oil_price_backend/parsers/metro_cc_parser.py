import requests


def get_oil_list_from_metro():
    # Api запрос, возвращающий пагинированный по 30 элементов список моторных масел в продаже Metro-CC
    api_request_to_get_list_oils = 'https://api.metro-cc.ru/api/v1/C98BB1B547ECCC17D8AEBEC7116D6/10/products?' \
                                   'category_id[0]=412465&paginate=30&order=name_asc&' \
                                   'attributes%5B0%5D%5Battribute_id%5D=1132&attributes%5B0%5D%5B' \
                                   'values_id%5D%5B0%5D=38804&attributes%5B0%5D%5B' \
                                   'values_id%5D%5B1%5D=38798&attributes%5B0%5D%5Bvalues_id%5D%5B2%5D=47132'
    oil_list = []
    page_num = 1
    params = {'page': page_num}
    api_response = requests.get(api_request_to_get_list_oils, params=params).json()
    if api_response:
        # Получаем ответы от API metro-cc и записываем данные: название, цена, ссылка на странице магазина
        while api_response['data']['next_page_url']:
            for good in api_response['data']['data']:
                oil_list.append([good['name'], good['prices']['offline']['price'], good['url']])
            api_response = requests.get(api_response['data']['next_page_url']).json()
        return oil_list
    else:
        return 'возникла ошибка, попробуйте повторить попытку позже'


list = get_oil_list_from_metro()
print()
