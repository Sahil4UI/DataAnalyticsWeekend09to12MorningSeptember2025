📘 Python 3.13.5 Notes (Shell Format)
>>> 1x = 12
SyntaxError: invalid decimal literal

>>> *x = 12
SyntaxError: starred assignment target must be in a list or tuple

>>> &x%^%^ = 12
SyntaxError: invalid syntax

>>> _x = 12      # ✅ valid

>>> x1 = 20      # ✅ valid

>>> x$ = 12
SyntaxError: invalid syntax


⚡ Rule: Variable name me sirf alphabets, numbers (after first letter) aur _ use hote hain. Special characters allowed nahi hain.

>>>     x = 12
SyntaxError: unexpected indent

>>> x = 12
>>> print(x)
12


⚡ Rule: Extra indentation bina reason ke nahi chalega.

🔹 List Copy Example
>>> x = [1,2,3,4,5]
>>> y = x
>>> x
[1, 2, 3, 4, 5]
>>> y
[1, 2, 3, 4, 5]

>>> x.pop()
5
>>> x
[1, 2, 3, 4]
>>> y
[1, 2, 3, 4]   # same change in y (reference copy)

>>> x = [1,2,3,4]
>>> y = x.copy()
>>> x.pop()
4
>>> x
[1, 2, 3]
>>> y
[1, 2, 3, 4]   # independent copy

🔹 None & 0
>>> z = 0
>>> z
0

>>> z = None
>>> print(z)
None

🔹 Data Types & Operators
>>> x = [1,2,3,4]
>>> type(x)
<class 'list'>

>>> x = 12
>>> y = 9
>>> x + y
21
>>> x - y
3
>>> x * y
108
>>> x / y
1.3333333333333333
>>> x // y
1
>>> 22 / 7
3.142857142857143
>>> 22 // 7
3
>>> 22 % 7
1
>>> 2 ** 4
16
>>> 2 ** 0.5
1.4142135623730951

🔹 math Module
>>> import math

>>> math.remainder(22,7)
1.0

>>> math.pow(3,3)
27.0

>>> math.sqrt(3)
1.7320508075688772

>>> math.lcm(2,3,4)
12

>>> math.gcd(99,72,81)
9

>>> math.factorial(5)
120

>>> math.fabs(-90)
90.0

>>> math.floor(34.25)
34
>>> math.ceil(34.25)
35

>>> math.comb(2,3)
0
>>> math.comb(3,2)
3
>>> math.perm(3,2)
6

>>> math.pi
3.141592653589793
>>> math.tau
6.283185307179586
>>> math.e
2.718281828459045
