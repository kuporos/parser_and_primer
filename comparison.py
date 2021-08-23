

#сравнение процентов и привязка

onliner = ["firstten", "second", "tenn", "nine"]
by = "ten"


import difflib

procent = 0
name_onliner = None
for a in range (len(onliner)):
  matcher = difflib.SequenceMatcher(None, by.lower(), onliner[a].lower())
  if matcher.ratio() > procent:
    procent = matcher.ratio()
    name_onliner = onliner[a].lower()
print (procent * 100, name_onliner)
# Если нет то в others

#___________________________________
#Kufar

onliner = ["Смартфон HONOR 10X Lite DNN-LX9 4GB/128GB (полночный черный)", "second", "tenn", "nine"]
by = "Смартфон HONOR 10X Lite"

phones_brand = "Honor"
model = "10X Lite"
memory = "128GB"
ram_memory = "4GB"
compare = phones_brand +" "+ model +" "+  memory +" "+ ram_memory

import difflib

procent = 0
name_onliner = None

procent_compare = 0
name_onliner_compare = None

for a in range (len(onliner)):
  matcher = difflib.SequenceMatcher(None, by.lower(), onliner[a].lower())
  matcher_compare = difflib.SequenceMatcher(None, compare.lower(), onliner[a].lower())
  if matcher.ratio() > procent:
    procent = matcher.ratio()
    name_onliner = onliner[a].lower()
  if matcher_compare.ratio() > procent_compare:
    procent_compare = matcher_compare.ratio()
    name_onliner_compare = onliner[a].lower()

# print (procent * 100, name_onliner)
# print(procent_compare * 100, name_onliner_compare)

if procent > procent_compare:
  print ("1", procent * 100, name_onliner)
else:
  print("2", procent_compare * 100, name_onliner_compare)

# Если нет то в others



# def similarity(s1, s2):
#   normalized1 = s1.lower()
#   normalized2 = s2.lower()
#   matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
#   return matcher.ratio()
# print(similarity(onliner[0], by[0])*100 , "%")

# trying = []
# import json
# with open ("data_catalog_phones_24_07_2021_19_18.json", "r") as kat:
#   with open ("data_catalog_phones_23_07_2021_20_03.json", "r") as by:
#     k_file = json.load(kat)
#     b_file = json.load(by)
#     print(len(b_file))
#     print(len(k_file))
#
#     for k in range (len(k_file)):
#       count = 0
#       by = None
#       kat = None
#       for b in range (len(b_file)):
#
#         procent = (similarity(k_file[k]["name"], b_file[b]["name"])*100)
#         if procent>count and procent>80:
#           count = procent
#           by = b_file[b]["name"]
#           kat = k_file[k]["name"]
#         trying.append([count , kat , by])
#         print ([count , kat , by])
# print (trying)

replace = {
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



# black_list = ["TNK", "spawn11", "kavchik", "volc_478", "klim0987", "ANJEI2009"
#               "serge2008", "serg19752909", "HTClover", "valery40", "MisterX2008",
#               "worobei", "JiаYu", "BelVik", "asdy", "Ivan33371", "2254013",
#               "minsk_apple_by", "whitecrow", "Evgeniy1", "gsm-store.shop.by",
#               "Kinght_rider", "Evgen-181082", "Swordfish1979", "Quartor",
#               "178353А", "2030278", "vadim1981", "Evsey", "2700898", "pr1td",
#               "2412929", "Vash_3G_ModeM", "apolones", "USBEL", "life375257763467",
#               "1503459", "Puertorico", "планшет", "iriska_28", "Euro5n",
#               "Baobab", "d-i.Mel", "vitali2006v", "whisler"]
#
# black_last = {
#   "TNK" : "6",
#   "vitali2006v" : "3",
#   "d-i.Mel" : "5",
#   "Baobab" : "3",
#   "Euro5n" : "5",
#   "whisler" : "7",
#   "iriska_28" : "3",
#   "планшет" : "3",
#   "Puertorico" : "5",
#   "2412929" : "4",
#   "1503459" : "15",
#   "life375257763467" : "4",
#   "USBEL" : "5",
#   "Vash_3G_ModeM" : "10",
#   "apolones" : "3",
#   "Evsey" : "4",
#   "2700898" : "3",
#   "vadim1981" : "4",
#   "pr1td" : "3",
#   "Quartor" : "4",
#   "Swordfish1979" : "3",
#   "178353А" : "3",
#   "2030278" : "3",
#   "Evgen-181082" : "3",
#   "gsm-store.shop.by" : "10",
#   "Kinght_rider" : "5",
#   "kavchik" : "3",
#   "klim0987": "3",
#   "volc_478" : "3",
#   "ANJEI2009" : "3",
#   "serge2008" : "5",
#   "minsk_apple_by" : "3",
#   "Evgeniy1" : "3",
#   "Ivan33371" : "4",
#   "spawn11": "5",
#   "2254013" : "3",
#   "serg19752909" : "3",
#   "HTClover" : "11",
#   "valery40": "3",
#   "MisterX2008" : "6",
#   "worobei" : "3",
#   "JiаYu" : "4",
#   "BelVik" : "4",
#   "asdy" : "9",
#   "whitecrow" : "6"
#
# }
#
#
#
# data2 = []
# # data2 = {"1": 34}
# for a in range (0, len (data)):
#   count = data.count(data[a])
#   # data2 [data[a]] = count
#   data2 = {data[a] : count}
#   print (data2)
