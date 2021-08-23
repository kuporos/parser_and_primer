###############################################################
# №1 Square Every Digit

# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
# Note: The function accepts an integer and returns an integer


# def square_digits(num):
#     number=[]
#     num2=list(str(num))
#     for a in num2:
#         number.append(str(int(a)**2))
#
#     return int("".join(number))
#
#
# print(square_digits(15))

###############################################################
# №2 Vowel Count

# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.


# def getCount(sentence):
#
#     vowels = ["a", "e", "i", "u", "o"]
#     count=0
#     for a in vowels:
#         for b in list(sentence):
#             if a==b:
#                 count+=1
#     return count
#
# print(getCount("qwqwqwqwqwaepppppppu"))

###############################################################

s = "aqdf&0#1xyz!22[153(777.777"

nine="ge"
list=[]
number=0

for a in range(len(s)+1):
    try:
        if int(s[a])/2:
            number=f"{number}{s[a]}"
    except:
        list.append(number)
        number=0
print (list)


