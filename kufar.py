# #
# # import requests
# # from bs4 import BeautifulSoup
# #
# #
# # url = 'https://www.kufar.by/listings?cat=17010'
# # response = requests.get(url)
# # soup = BeautifulSoup(response.text, 'lxml')
# #
# # # page = soup.find_all('a', class_='kf-FXM-0a457')
# # http = soup.find_all('a', class_='kf-yebg-87537')
# #
# #
# # все объявления
# # for a in range(len(http)):
# #     print (http[a].get('href'))
#
# # for b in range(len(http)):
# #     url2 = http[b].get('href')
# #     response2 = requests.get(url2)
# #     soup2 = BeautifulSoup(response2.text, 'lxml')
# #
# #     title = soup2.find('h1', class_='kf-HslH-f15fa')
# #     city = soup2.find('span', class_='kf-Hyzm-878d8')
# #     information = soup2.find('div', class_='kf-lGkP-b7d81')
# #
# #
# #     print(b, title.text)
# #     print(city.text)
# #     print(information.text)
#
#
# # __________________________________________________________________________________________
#
# import datetime
# import requests
# import json
# from bs4 import BeautifulSoup
#
# def get_date2():
#     start_time = datetime.datetime.now()
#
#     url = "https://www.kufar.by/listings?size=42&sort=lst.d&cur=BYR&cat=17010&rgn=7&cnd=1"
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'lxml')
#     # pages_count = soup.find_all('div')[1092].find_all('a')[2].text #количество страниц
#     data_list = []
#
#     article = soup.find('article')
#     a = article.find_all('a', {'target': '_blank'})
#     for i in range(2): #len(a)
#         link_product = a[i].get('href')
#         photo_link = a[i].find('img').get('data-src')  # link in the photo
#         name_product = a[i].find('img').get('alt')
#         info1 = a[i].find('div').find_next_sibling()
#         # description = info1.find('h3').text
#         info2 = info1.find('div').find_next_sibling()
#         price = info2.find('div').find('span').text
#         location = info2.find('div').find_next_sibling().find('span').text
#         print ("information sasha")
#         try:
#             for item in range(43):
#
#                 url2 = link_product
#                 response2 = requests.get(url2)
#                 soup2 = BeautifulSoup(response2.text, 'lxml')
#
#                 title = soup2.find('div', "kf-pVgp-b9098").text
#                 description = soup2.find_all('div')[171].find('div').text
#                 factory = soup2.find_all('div')[151].find('a').text
#                 model = soup2.find_all('div')[153].find_all('div')[1].text
#                 print("information my")
#
#                 data_list.append({
#                     "title": title,
#                     "factory": factory,
#                     "model": model,
#                     "link_product": link_product,
#                     "photo_link": photo_link,
#                     "name_product": name_product,
#                     # "data_time": data_time,
#                     "description": description,
#                     "price": price,
#                     "location": location})
#         except:
#             pass
#
#
#
#     cur_time = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M")
#     with open(f"data_catalog_phones_{cur_time}.json", "a") as file:
#         json.dump(data_list, file, indent=4, ensure_ascii=False)
#
#     diff_time = datetime.datetime.now() - start_time
#     print(f"Процесс завершился за: {diff_time}")
#
# get_date2()

# ___________________________________________________________________________________

# import datetime
# import requests
# import json
# from bs4 import BeautifulSoup
#
# url = 'https://www.kufar.by/listings?size=42&sort=lst.d&cur=BYR&cat=17010&rgn=7&cnd=1'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')
# article = soup.find('article')
# a = article.find_all('a', {'target': '_blank'})
# print(article)
# print (a)

# ___________________________________________________________________________________

import requests
import json
from datetime import datetime

def get_date2():
    start_time = datetime.now()

    url = f"https://cre-api.kufar.by/ads-search/v1/engine/v1/search/rendered-paginated?size=200&sort=lst.d&cur=BYR&cat=17010&cnd=1&cmp=0"
    response = requests.get(url)
    pages_count = response.json()["pagination"]["pages"][3]["num"]  # количество страниц
    token_second_page=response.json()["pagination"]["pages"][1]["token"] # токен второй станицы

    url2 = f"https://cre-api.kufar.by/ads-search/v1/engine/v1/search/rendered-paginated?size=200&sort=lst.d&cur=BYR&cat=17010&cnd=1&cmp=0&cursor={token_second_page}"
    response2 = requests.get(url2)
    token_page = response2.json()["pagination"]["pages"][0]["token"] # токен первой станицы

    data_list = []
    for page in range(1, 2): # pages_count+1
        url3 = f"https://cre-api.kufar.by/ads-search/v1/engine/v1/search/rendered-paginated?size=200&sort=lst.d&cur=BYR&cat=17010&cnd=1&cmp=0&cursor={token_page}"
        response3 = requests.get(url3)
        data = response3.json()
        try:
            for item in range(200):

                phones_brand = None
                model = None
                memory = None
                ram_memory = None

                name = response3.json()["ads"][item]["subject"]
                http = response3.json()["ads"][item]["ad_link"]
                description = None
                id = response3.json()["ads"][item]["ad_id"]
                user = response3.json()["ads"][item]["account_parameters"][0]["v"]
                price = int(response3.json()["ads"][item]["price_byn"]) / 100
                date_created1 = response3.json()["ads"][item]["list_time"]
                date_created = datetime.strptime(date_created1, "%Y-%m-%dT%H:%M:%SZ")
                photo_list = []
                try:
                    for a in range (20):
                        temp = response3.json()["ads"][item]["ad_parameters"][a]["pl"]
                        if temp == "Город / Район":
                            location = response3.json()["ads"][item]["ad_parameters"][a]["vl"]
                            if location == "Центральный" or "Советский" or "Первомайский" or "Партизанский" or "Заводской" or "Ленинский" or "Октябрьский" or "Московский" or "Фрунзенский":
                                location = "Минск"
                        elif temp == "Город / Район":
                            location = response3.json()["ads"][item]["ad_parameters"][a]["vl"]
                        elif temp=="Производитель":
                            phones_brand = response3.json()["ads"][item]["ad_parameters"][a]["vl"]  # Samsung
                        elif temp == "Модель":
                            model = response3.json()["ads"][item]["ad_parameters"][a]["vl"]  # model
                        elif temp == "Память":
                            memory_parser = response3.json()["ads"][item]["ad_parameters"][a]["vl"]  # 16 ГБ
                            memory = memory_parser.split()
                            for a in range(len(memory)):
                                if memory[a].lower() == "гб":
                                    memory[a] = "GB"
                            memory = ''.join(memory)
                        elif temp == "Оперативная память":
                            ram_memory_parser = response3.json()["ads"][item]["ad_parameters"][a]["vl"]  # 3 ГБ
                            ram_memory = ram_memory_parser.split()
                            for a in range(len(ram_memory)):
                                if ram_memory[a].lower() == "гб":
                                    ram_memory[a] = "GB"
                            ram_memory = ''.join(ram_memory)
                        else: pass
                except: pass
                try:
                    for b in range (20):
                        photo_id = response3.json()["ads"][item]["images"][b]["id"]
                        photo_list.append(f"https://yams.kufar.by/api/v1/kufar-ads/images/{photo_id[:2]}/{photo_id}.jpg?rule=gallery")
                except IndexError: pass


                data_list.append(
                    {
                        "id": id,
                        "http" : http,
                        "equipment": name,
                        "name": user,
                        "description": description,
                        "price": price,
                        #"date_created" : date_created,
                        "phones_brand" : phones_brand,
                        "model" : model,
                        "memory" : memory,
                        "ram_memory" : ram_memory,
                        "locaton": location,
                        "photo" : photo_list
                    })
        except IndexError: pass

        print(f"[INFO] Обработал {page}/{pages_count}")

    cur_time = datetime.now().strftime("%d_%m_%Y_%H_%M")
    with open(f"data_catalog_phones_{cur_time}.json", "a") as file:
        json.dump(data_list, file, indent=4, ensure_ascii=False)

    diff_time = datetime.now() - start_time
    print(f"Процесс завершился за: {diff_time}")

get_date2()