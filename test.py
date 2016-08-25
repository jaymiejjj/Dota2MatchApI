from functools import lru_cache

@lru_cache(maxsize=32)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print([fib(n) for n in range(10) ])

newdict= {}

dict1 ={'name':'jaymie','score' : 60}
dict2 = {'name':'xiaohong','score' : 90}
dict3 = {'name':'jaymie','score' : 70}
dict4 = {'name':'jaymie','score' : 65}
dict5 = {'name':'xiaoli','score' : 85}
dict6 = {'name':'xiaohong','score' : 89}


list = [dict1,dict2,dict3,dict4,dict5,dict6]
newdict= {}

for dict in list:
    if dict['name'] in newdict.keys():
        newdict[dict['name']] = newdict[dict['name']]+[dict['score']]
    else:
        newdict[dict['name']] = [dict['score']]

print(newdict)
#fib.cache_clear()
