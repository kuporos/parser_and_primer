
import datetime
import requests
import json





def get_date2():
    start_time = datetime.datetime.now()

    url = "https://www.onliner.by/sdapi/catalog.api/search/mobile?order=date:desc&page=1"
    response = requests.get(url)
    pages_count = response.json()["page"]["last"]#количество страниц
    data_list = []
    data_photo = []
    for page in range(1, pages_count+1):
        url = f"https://www.onliner.by/sdapi/catalog.api/search/mobile?order=date:desc&page={page}"
        response = requests.get(url)
        items_count = response.json()["page"]["items"]  # количество объектов на странице
        data = response.json()
        for item in range(items_count):
            name1 = data["products"][item]["full_name"]
            key_catalog = data["products"][item]["key"]
            second = data["products"][item]["second"]["offers_count"]
            if second > 0:
                url = f"https://catalog.onliner.by/sdapi/second.api/product/{key_catalog}/offers?include=product,user_counters,permissions,constraints&v"
                response = requests.get(url)
                date = response.json()
                for a in range(second):
                    name = date["offers"][a]["contact"]["name"]
                    id = date["offers"][a]["id"]
                    phone = date["offers"][a]["contact"]["phones"][0]
                    description = date["offers"][a]["description"]
                    price = date["offers"][a]["price"]["amount"]
                    date_created = date["offers"][a]["created_at"]
                    date_updated = date["offers"][a]["updated_at"]
                    currency = date["offers"][a]["price"]["currency"]  # валюта
                    location = date["offers"][a]["location"]["town"]
                    photo=[]
                    for b in range(0, 20):
                        try:
                            photo.append(date["offers"][a]["photos"][b]["1280x1280"])
                        except IndexError:
                            pass

                    data_list.append(
                        {
                        "id" : id,
                        "equipment": name1,
                        "key_catalog" : key_catalog,
                        "name": name,
                        "phone": phone,
                        "description": description,
                        "price": price,
                        "currency": currency,
                        # "photo" : photo,
                        "date_created" : date_created,
                        "date_updated":date_updated,
                        "locaton" : location,
                        })

                    data_photo.append (
                    {"photo" : photo})


        print(f"[INFO] Обработал {page}/{pages_count}")

    cur_time = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M")
    with open(f"data_catalog_phones_{cur_time}.json", "a") as file:
        json.dump(data_list, file, indent=4, ensure_ascii=False)

    diff_time = datetime.datetime.now() - start_time
    print(f"Процесс завершился за: {diff_time}")

get_date2()
