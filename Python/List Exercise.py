#Q1.Adding all values of List
'''
x = [3,4,5,8,9]

print(sum(x))
'''
#Q2.Multiplying the values in the list
'''
x = [1,2,3,4,5]
result = 1
for item in x:
    result *= item
print(result)
'''
#Q3.Find the largest number from the list
#without using max function
'''
x = [1,2,3,4,5,99,-10,0]
large = x[0]
for item in x:
    if item>large:
        large = item
print(large)
'''
