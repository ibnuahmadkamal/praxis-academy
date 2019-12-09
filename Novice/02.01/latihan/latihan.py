obj = [1,2,3]
it = iter(obj)
it

it.__next__()

for i in iter(it):
    print(i)

for i in (it): #sama seperti line 7
    print(i)
print("")

L= [1,2,3,4]
iteration = iter(L)
t = tuple(iteration)
print (t)
print("")

m = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
      'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

for key in m:
    print(key, m[key])
print("")

print(list(map(int, ["1","2","3"])))

def hello_world(k):
    def world(w):
        print(k,w)
    return world
print("")

h = hello_world
x = h("hello")
x = x("world")
print("")

square = lambda x : x*x
print (square(3))
print("")

x =[1,2,3,4,5,6]
from functools import reduce
print(reduce(lambda x,y: x+y,x))

print("")
from functools import partial
def power(base, exp):
     return base ** exp

cube = partial(power, exp=3)
print (cube(5))

print("")
dictionary = ['fox', 'boss', 'orange', 'toes', 'fairy', 'cup','box']
def puralize(words):
    f =[]
    for i in range(len(words)):
        word = words[i]
        if word.endswith('s') or word.endswith('x'):
            word += 'es'
        if word.endswith('y'):
            word = word[:-1] + 'ies'
        else:
            word += 's'
        words[i] = word
        f.append(word)
    print(f[0:3])
    
hasil = dictionary
print(hasil)
puralize(hasil)
##print (end)