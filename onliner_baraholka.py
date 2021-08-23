import datetime
import requests
from bs4 import BeautifulSoup
import json
import re

"""
Here was been cat!
Cat say meow!
Meow, meow, meow!
"""

replace = {
  "хуавей" : "Huawei",
  "филипс" : "Philips",
  "смарт" : "Smart",
  "плюс" : "Plus",
  "самсунг" : "Samsung",
  "айфон" : "Iphone",
  "сименс" : "Simens",
  "сони эриксон" : "Sony Ericson",
  "нокиа" : "Nokia",
  "ксяоми" : "Xiaomi",
  "престижио" : "Prestigio",
  "леново" : "Lenovo",
  "икспериа" : "Iksperia",
  "люмиа" : "Lumia",
  "гелакси" : "Gelaxy",
  "хонар" : "Honor",
  "хонор" : "Honor",
  "ксиоми" : "Xiaomi",
  "редми" : "Redmi",
  "ноте" : "Note",
    "гб" : " GB"
}


def get_data():
    start_time = datetime.datetime.now()

    data_list=[]
    url = 'https://baraholka.onliner.by/viewforum.php?f=2&cat=1&sk=up' #page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    page = soup.find("ul", class_='pages-fastnav').find_all("li")[-2].text #количество страниц

    count=0
    for a in range (1, 3): #int(page)+1
        url_page = f'https://baraholka.onliner.by/viewforum.php?f=2&cat=1&sk=up&start={count}'
        response3 = requests.get(url_page)
        soup3 = BeautifulSoup(response3.text, 'lxml')
        number_of_ad  = soup3.find_all("td", class_='frst ph colspan')  # количество объявлений

        if count == 0:
            number = 6
        else: number=5

        for b in range (number, len(number_of_ad)):
            http = soup3.find_all('h2', class_='wraptxt')
            web="https://baraholka.onliner.by/" + http[b].find('a').get('href')

            response2 = requests.get(web)
            soup2 = BeautifulSoup(response2.text, 'lxml')

            name_parser = soup2.find("h1", class_='m-title-i title').text
            name = name_parser.split()

            for k, v in replace.items():
                for a in range(len(name)):
                    if name[a].lower() == k:
                        name[a] = v

            description = (soup2.find_all('div', class_= "content"))[0].get_text(separator=u' ')
            id = soup2.find("td", class_='bd numb').text
            user = soup2.find("a", class_='_name star-notes').text
            try:
                price = soup2.find("li", class_='price-primary').text
            except Exception:
                price = 0
            date_created_find = soup2.find("small", class_="msgpost-date").find_all("span")[0].text
            date_created = str(re.findall(r'^[0-9]{0,2} [а-я]{1,8} [0-9]{4} [0-9]{2}[:][0-9]{2}', date_created_find)).strip('[]')
            try:
                date_updated_find = soup2.find("td", class_='b-ba-subj-up b-ba-subj-upped').text
                date_updated = str(re.findall(r'[0-9]{0,4} [а-я]{0,6} [а-я]{5}', date_updated_find)).strip('[]')
            except AttributeError:
                date_updated = date_created
            location = soup2.find("strong", class_='fast-desc-region').text
            photo_l=[]

            try:
                for c in range(15):
                    photo_l.append((soup2.find_all("img", class_='msgpost-img'))[c].get('src'))
            except IndexError:
                pass

            data_list.append({
                "http" : web,
                "name" : ' '.join(name),
                "description" : description,
                "id" : id,
                "user" : user,
                "price" : price,
                "date_created" : date_created,
                "date_updated" : date_updated,
                "location" : location,
                "photo" : photo_l
                }

)
            print (b)

        count += 50
        print(f"[INFO] Обработал {a}/{page}")
    cur_time = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M")
    with open(f"data_catalog_phones_{cur_time}.json", "a") as file:
        json.dump(data_list, file, indent=4, ensure_ascii=False)

    diff_time = datetime.datetime.now() - start_time
    print(f"Процесс завершился за: {diff_time}")

    # for a in range (len(data_list)):
    #     print (list(data_list.values().count((data_list[a]))))

get_data()


