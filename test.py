dict = {'xiaoming':95,
        'xiaoli':88,
        'xiaohua':79,
        'xiaohei':48,
        'xiaodong':95,
        'xiaobai':88
        }

#list2 = sorted(dict.items, key=lambda x : x[1])
#print(list2)

list = zip(dict.values(),dict.keys())


list1 = sorted(zip(dict.values(),dict.keys()),reverse=True)
print(list1)



