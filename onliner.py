import datetime
import requests
import json
import csv


def get_data():
    start_time = datetime.datetime.now()

    url = "https://www.onliner.by/sdapi/catalog.api/search/mobile?order=date:desc&page=1"
    response = requests.get(url)
    pages_count = response.json()["page"]["last"]#количество страниц
    data_list = []
    for page in reversed(range(1, pages_count+1)):
        url = f"https://www.onliner.by/sdapi/catalog.api/search/mobile?order=date:desc&page={page}"

        response = requests.get(url)
        items_count = response.json()["page"]["items"]  # количество объектов на странице
        data = response.json()
        for item in reversed(range(items_count)):
            name = data["products"][item]["full_name"]

            info = data["products"][item]["description"]
            url_catalog = data["products"][item]["html_url"]
            id_catalog = data["products"][item]["id"]
            key_catalog = data["products"][item]["key"]
            second = data["products"][item]["second"]["offers_count"]
            photo = "https:" + data["products"][item]["images"]["header"]

            data_list.append(

                {
                    "name" : name,
                    "info": info,
                    "url_catalog": url_catalog ,
                    "id_catalog": id_catalog ,
                    "key_catalog": key_catalog,
                    "second": second,
                    "photo" : photo
                }
            )
        print(f"[INFO] Обработал {page}/{pages_count}")

    cur_time = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M")
    with open(f"data_catalog_phones_{cur_time}.csv", "a") as file:
        csv.writer(file).writerow(data_list[0].keys())
        for a in data_list:
            csv.writer(file).writerow(a.values())

    diff_time = datetime.datetime.now() - start_time
    print(f"Процесс завершился за: {diff_time}")

get_data()

# _____________________________________________

# catalog=[16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# bd=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# temp=[]
# to_remember = bd[-1]
#
# for a in range (len(catalog)):
#     if to_remember!=catalog[a]:
#         temp.append(catalog[a])
#     else:
#         to_remember=temp[-1]
#         break
#
# for b in reversed(range (len(temp))):
#     bd.append(temp[b])
#
# print(temp)
# print(bd)
# print(catalog)

#______________________________________________________________
#
# def add_data():
#     start_time = datetime.datetime.now()
#     url = "https://www.onliner.by/sdapi/catalog.api/search/mobile?order=date:desc&page=1"
#     response = requests.get(url)
#     pages_count = response.json()["page"]["last"]  # количество страниц
#     data_list = []
#     for page in range(1, pages_count):
#         url = f"https://www.onliner.by/sdapi/catalog.api/search/mobile?order=date:desc&page={page}"
#         response = requests.get(url)
#         items_count = response.json()["page"]["items"]  # количество объектов на странице
#         data = response.json()
#         for item in range(items_count):
#             id_catalog = data["products"][item]["id"]
#             key_catalog = data["products"][item]["key"]
#             if key_catalog==list[-1]:
#                 exit()
#             else:
#                 for item in reversed(range(items_count)):
#                     name = data["products"][item]["full_name"]
#                     info = data["products"][item]["description"]
#                     url_catalog = data["products"][item]["html_url"]
#                     id_catalog = data["products"][item]["id"]
#                     key_catalog = data["products"][item]["key"]
#                     second = data["products"][item]["second"]["offers_count"]
#                     photo = "https:" + data["products"][item]["images"]["header"]
#
#                     data_list.append(
#                         {
#                             "name": name,
#                             "info": info,
#                             "url_catalog": url_catalog,
#                             "id_catalog": id_catalog,
#                             "key_catalog": key_catalog,
#                             "second": second,
#                             "photo": photo
#                         }
#                     )
#                 print(f"[INFO] Обработал {page}/{pages_count}")
#
#                 cur_time = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M")
#                 with open(f"data_catalog_phones_{cur_time}.json", "a") as file:
#                     json.dump(data_list, file, indent=4, ensure_ascii=False)
#
#                 diff_time = datetime.datetime.now() - start_time
#                 print(f"Процесс завершился за: {diff_time}")
#                 remember = data_list[-1]
#                 print(remember)
#
# add_data()()
#
# def update_price():
#     start_time = datetime.datetime.now()
#
#     for item in range(New_Goods_Onliner.objects.count()):
#         url = f"https://catalog.api.onliner.by/products/{New_Goods_Onliner.objects.filter(key_goods).(id=item)}/prices-history"
#         response = requests.get(url)
#         data = response.json()
#         try:
#             min_price_update = data["prices"]["min"]["amount"]
#         except TypeError:
#             min_price_update = 0
#         try:
#             max_price_update = data["products"]["max"]["amount"]
#         except TypeError:
#             max_price_update = 0
#
#         New_Goods_Onliner.objects.all().update(min_price=min_price_update, max_price=max_price_update)
#
#
#     diff_time = datetime.datetime.now() - start_time
#     print(f"Процесс завершился за: {diff_time}")



