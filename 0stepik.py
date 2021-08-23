
# №1

minuts_all= 480
hour = 0
minutes = 0

if minuts_all % 60 == 0:
    hour=minuts_all // 60
else:
    hour = minuts_all // 60
    minutes = minuts_all - (hour*60)

print (hour)
print (minutes)