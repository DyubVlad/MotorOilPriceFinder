import requests


def get_oil_list():
    # Api запрос, возвращающий пагинированный по 30 элементов список моторных масел в продаже Metro-CC
    api_request_to_get_list_oils = 'https://api.metro-cc.ru/api/v1/C98BB1B547ECCC17D8AEBEC7116D6/77/products' \
                             '?category_id[0]=412465&paginate=30&order=name_asc&page=1&price_min=79&price_max' \
                             '=5359&attributes[0][attribute_id]=1132&attributes[0][values_id][0]=8535&attributes[0]' \
                             '[values_id][1]=8536&attributes[0][values_id][2]=8543'
    api_req = requests.get(api_request_to_get_list_oils).json()
    print()


get_oil_list()
print()
