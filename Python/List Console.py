Python 3.13.5 (v3.13.5:6cb20a219a8, Jun 11 2025, 12:23:45) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> #data Collection in Python
>>> #List is ordered and mutable data collection
>>> #ordered -indexing
>>> x = [1,2,5,6,7,9]
>>> x[0]
1
>>> x[-1]
9
>>> x = [1,2,3,[4,5,6,[7,8,9,10]]]
>>> x[3][3][2]
9
>>> #slicing in List
>>> x = [10,20,30,40,50,60,70,80,90,100]
>>> x[0:5]
[10, 20, 30, 40, 50]
>>> x[:5]
[10, 20, 30, 40, 50]
>>> x[6:]
[70, 80, 90, 100]
>>> x[::-1]
[100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
#methods in List
x = [1,2,3,4,5]
#storing value in list
x.append(100)#it will append the value at the end of the List
x
[1, 2, 3, 4, 5, 100]
x.append(90)
x
[1, 2, 3, 4, 5, 100, 90]
x.insert(0,"hey")
x
['hey', 1, 2, 3, 4, 5, 100, 90]
#Updating the List
x[0]="hello"
x
['hello', 1, 2, 3, 4, 5, 100, 90]
#deletion
x
['hello', 1, 2, 3, 4, 5, 100, 90]
x.pop()#it will remove last value
90
x

x
['hello', 1, 2, 3, 4, 5, 100]
x.pop(0)
'hello'
x
[1, 2, 3, 4, 5, 100]
x = [1,5,4,3,2,1,1,1,1,2,2,3,10,-100]
x.remove(2)
x
[1, 5, 4, 3, 1, 1, 1, 1, 2, 2, 3, 10, -100]
del x[0]
x
[5, 4, 3, 1, 1, 1, 1, 2, 2, 3, 10, -100]
x.clear()
x
[]
#list comprehension
x = [i for i in range(2,21,2)]
x
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
x = [10,-100,90,-20,3,4,5,500,0]
min(x)
-100
max(x)
500
sum(x)
492
x
[10, -100, 90, -20, 3, 4, 5, 500, 0]
x.sort()
x
[-100, -20, 0, 3, 4, 5, 10, 90, 500]
x.sort(reverse=True)
x
[500, 90, 10, 5, 4, 3, 0, -20, -100]
x
[500, 90, 10, 5, 4, 3, 0, -20, -100]
len(x)
9
x.index(100)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    x.index(100)
ValueError: 100 is not in list
x.index(0)
6
y = [1,1,1,2,2,2]
y.count(2)
3

for i in range(len(x)):
    print(x[i])

500
90
10
5
4
3
0
-20
-100
for item in x:
    print(item)

500
90
10
5
4
3
0
-20
-100

#Deep copy vs shallow copy
x = [1,2,3,[4,5,6,[7]]]
y= x.copy()
x
[1, 2, 3, [4, 5, 6, [7]]]
y
[1, 2, 3, [4, 5, 6, [7]]]
del x[0]
x
[2, 3, [4, 5, 6, [7]]]
y
[1, 2, 3, [4, 5, 6, [7]]]
del x[2][0]
x
[2, 3, [5, 6, [7]]]
y
[1, 2, 3, [5, 6, [7]]]
from copy import deepcopy
x
[2, 3, [5, 6, [7]]]
y = x.deepcopy()
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    y = x.deepcopy()
AttributeError: 'list' object has no attribute 'deepcopy'

y = deepcopy(x)
x
[2, 3, [5, 6, [7]]]
y
[2, 3, [5, 6, [7]]]
del x[2][1]
x
[2, 3, [5, [7]]]
y
[2, 3, [5, 6, [7]]]
