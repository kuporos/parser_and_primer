
# r'^[0-9]{0,2} [а-я]{1,8} [0-9]{4} '
# date_created = str(re.findall(r'\? be [a-z]{2}', spisok))
# date_created = str(re.findall(r'break\d*', spisok))
#
# import re
# spisok = "fe break lol net  build fe where "
# date = str(re.findall((r'break|repair|broken'), spisok, ))
# print(date)

data_list = {
  "хуавей" : "huawei",
  "филипс" : "philips",
  "смарт" : "smart",
  "плюс" : "plus",
  "самсунг" : "samsung",
  "айфон" : "iphone",
  "сименс" : "simens",
  "сони эриксон" : "sony ericson",
  "нокиа" : "nokia",
  "ксяоми" : "xiaomi",
  "престижио" : "prestigio",
  "леново" : "lenovo",
  "икспериа" : "iksperia",
  "люмиа" : "lumia",
  "гелакси" : "gelaxy",
  "хонар" : "honor",
  "хонор" : "honor"
}

# убрать дубликаты магазинов

delete = []
print (len(data_list))

for k, v in data_list.items():
  count = list(data_list.values()).count(v)
  if count >= 2:
    delete.append(k)

print (delete)

for a in delete:
    data_list.pop(a)

print (len(data_list))








