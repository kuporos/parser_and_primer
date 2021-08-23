# import datetime
# import requests
# import json
#
# def get_pages():
#     url = "https://www.onliner.by/sdapi/catalog.api/search/mobile?order=date:desc&page=1"
#     response = requests.get(url)
#     pages_count = response.json()["page"]["last"]  # количество страниц
#     return pages_count
#
# def get_count_items(page):
#     url = f"https://www.onliner.by/sdapi/catalog.api/search/mobile?order=date:desc&page={page}"
#     response = requests.get(url)
#     items_count = response.json()["page"]["items"]  # количество объектов на странице
#     data = response.json()
#     return (items_count, data)
#
# def get_information(data, item):
#     name = data["products"][item]["full_name"]
#     info = data["products"][item]["description"]
#     url_catalog = data["products"][item]["html_url"]
#     id_catalog = data["products"][item]["id"]
#     key_catalog = data["products"][item]["key"]
#     second = data["products"][item]["second"]["offers_count"]
#     return (name, info, url_catalog, id_catalog, key_catalog, second)
#
# def get_data():
#     start_time = datetime.datetime.now()
#     data_list = []
#     for page2 in (range(1, get_pages()+1)): #3pages
#
#         for item2 in (range(get_count_items(page2)[0])): #30
#
#             print(item2)
#             information = get_information(get_count_items(page2)[1], item2)
#             data_list.append(
#                 {
#                     "name": information[0],
#                     "info": information[1],
#                     "url_catalog": information[2],
#                     "id_catalog": information[3],
#                     "key_catalog": information[4],
#                     "second": information[5]
#
#                 }
#             )
#         print(f"[INFO] Обработал {page2}/{get_pages()}")
#
#     cur_time = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M")
#     with open(f"data_catalog_phones_{cur_time}.json", "w") as file:
#         json.dump(data_list, file, indent=4, ensure_ascii=False)
#
#     diff_time = datetime.datetime.now() - start_time
#     print(f"Процесс завершился за: {diff_time}")
#
# get_data()

#___________________________________________________________
#После этой линии!

import datetime
import requests
import django
django.setup()
from django.contrib.auth.models import User
from parsers.models import New_Goods_Onliner, Goods_Photos_Url,Goods_Category


user = User.objects.get(id=1)

def mobile_url():
    url = "https://www.onliner.by/sdapi/catalog.api/search/mobile?order=date:desc&page=1"
    url2 = f"https://www.onliner.by/sdapi/catalog.api/search/mobile?order=date:desc&page="
    return url, url2

def get_pages():
    response = requests.get(mobile_url()[0])
    pages_count = response.json()["page"]["last"]  # количество страниц
    return pages_count

def get_count_items(page):
    url = mobile_url()[1]+{page}
    response = requests.get(url)
    items_count = response.json()["page"]["items"]  # количество объектов на странице
    data = response.json()
    return (items_count, data)

# def get_pages():
#     url = "https://www.onliner.by/sdapi/catalog.api/search/mobile?order=date:desc&page=1"
#     response = requests.get(url)
#     pages_count = response.json()["page"]["last"]  # количество страниц
#     return pages_count
#
# def get_count_items(page):
#     url = f"https://www.onliner.by/sdapi/catalog.api/search/mobile?order=date:desc&page={page}"
#     response = requests.get(url)
#     items_count = response.json()["page"]["items"]  # количество объектов на странице
#     data = response.json()
#     return (items_count, data)

def get_information(data, item):
    name = data["products"][item]["full_name"]
    info = data["products"][item]["description"]
    url_catalog = data["products"][item]["html_url"]
    id_catalog = data["products"][item]["id"]
    key_goods = data["products"][item]["key"]
    image_url = "https:" + data["products"][item]["images"]["header"]
    try:
        min_price = data["products"][item]["prices"]["price_min"]["amount"]
    except TypeError:
        min_price = 0
    try:
        max_price = data["products"][item]["prices"]["price_max"]["amount"]
    except TypeError:
        max_price = 0
    return (name, info, url_catalog, id_catalog, key_goods, image_url, min_price, max_price)

def get_data():
    """
    Эта функция парсит мобильные телефоны с каталога онлайнера и сохраняет данные о них в бд
    """
    start_time = datetime.datetime.now()
    for page in reversed(range(1, get_pages() + 1)):

        for item in reversed(range(get_count_items(page)[0])):
            # information = get_information(get_count_items(page)[1], item)

            name = get_count_items(page)[1]["products"][item]["full_name"]
            info = get_count_items(page)[1]["products"][item]["description"]
            url_catalog = get_count_items(page)[1]["products"][item]["html_url"]
            id_catalog = get_count_items(page)[1]["products"][item]["id"]
            key_goods = get_count_items(page)[1]["products"][item]["key"]
            image_url = "https:" + get_count_items(page)[1]["products"][item]["images"]["header"]
            try:
                min_price = get_count_items(page)[1]["products"][item]["prices"]["price_min"]["amount"]
            except TypeError:
                min_price = 0
            try:
                max_price = get_count_items(page)[1]["products"][item]["prices"]["price_max"]["amount"]
            except TypeError:
                max_price = 0

            # добавление фото с каталога онлайнера в БД
            image_url = Goods_Photos_Url.objects.create(
                image_url=image_url, # information[5],
            )

            New_Goods_Onliner.objects.create(
                name=name, #information[0],
                info=info, #information[1],
                url_catalog=url_catalog, #information[2],
                id_catalog=id_catalog, #information[3],
                key_goods=key_goods, #information[4],
                min_price=min_price, #information[6],
                max_price=max_price, #information[7],
                image_url=image_url, #image_url,
                category=Goods_Category.objects.get(id=1),
                user=user
            )

        print(f"[INFO] Обработал {page}/{get_pages()}")

    diff_time = datetime.datetime.now() - start_time
    print(f"Процесс завершился за: {diff_time}")


def add_data():
    """
    Эта функция добавляет новые модели мобильных телефонов и информацию о них с каталога онлайнера и сохраняет в БД
    """
    start_time = datetime.datetime.now()
    for page in range(1, get_pages() + 1):

        for items in range(get_count_items(page)[0]):
            key_goods_add = get_count_items(page)[1]["products"][items]["key"]
            if New_Goods_Onliner.objects.all().filter(key_goods=key_goods_add):
                break
            else:
                for item in range(get_count_items(page)[0]):
                    information = get_information(get_count_items(page)[1], item)

                    # добавление фото с каталога онлайнера в БД
                    image_url = Goods_Photos_Url.objects.create(
                        image_url=information[5],
                    )

                    New_Goods_Onliner.objects.create(
                        name=information[0],
                        info=information[1],
                        url_catalog=information[2],
                        id_catalog=information[3],
                        key_goods=information[4],
                        min_price=information[6],
                        max_price=information[7],
                        image_url=image_url,
                        category=Goods_Category.objects.get(id=1),
                        user=user
                    )
        print(f"[INFO] Обработал {page}/{get_pages()}")

    diff_time = datetime.datetime.now() - start_time
    print(f"Процесс завершился за: {diff_time}")


def delete_same_data():
    key_goods = New_Goods_Onliner.objects.get()
    New_Goods_Onliner.objects.filter(key_goods=key_goods).delete()
    pass

def update_price():
    """
    Эта функция обновляет цены существующих телефонов в БД
    """
    start_time = datetime.datetime.now()

    for page in range(1, get_pages() + 1):
        for item in range(get_count_items(page)[0]):
            information = get_information(get_count_items(page)[1], item)
            New_Goods_Onliner.objects.filter(key_goods=information[4]).update(min_price=information[6], max_price=information[7])
        print(f"[INFO] Обработал {page}/{get_pages()}")

    diff_time = datetime.datetime.now() - start_time
    print(f"Процесс завершился за: {diff_time}")