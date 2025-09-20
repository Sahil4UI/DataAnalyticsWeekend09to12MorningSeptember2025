Python 3.13.5 (v3.13.5:6cb20a219a8, Jun 11 2025, 12:23:45) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
#Loop=>repetition
#FOR LOOP
for i in range(1,11):
    print(i)

1
2
3
4
5
6
7
8
9
10
for i in range(1,11,1):
    print(i)

1
2
3
4
5
6
7
8
9
10
for i in range(1,11,2):
    print(i)

1
3
5
7
9

for i in range(10,0,-1):
    print(i)

10
9
8
7
6
5
4
3
2
1
for i in reversed(range(10,0,-1)):
    print(i)

1
2
3
4
5
6
7
8
9
10
for i in reversed(range(1,11)):
    print(i)

10
9
8
7
6
5
4
3
2
1
for i in range(1,11):
...     print(2,"X",i,"=",2*i)
... 
2 X 1 = 2
2 X 2 = 4
2 X 3 = 6
2 X 4 = 8
2 X 5 = 10
2 X 6 = 12
2 X 7 = 14
2 X 8 = 16
2 X 9 = 18
2 X 10 = 20
>>> #BREAK - it is used t stop the loop
>>> for i in range(1,10000000000001):
...     if i==5:
...         break
...     print(i)
... 
1
2
3
4
