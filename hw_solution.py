
# answer 8
x = int(input("Please enter 1st number:"))
y = int(input("Please enter 2nd number:"))

if x > y:
    print(f'{x} is bigger')
elif x == 0:
    print('euaql')
else:
    print(f'{y} is bigger')

# answer 9
x = int(input("Please enter 1st number:"))
y = int(input("Please enter 2nd number:"))
z = int(input("Please enter 2nd number:"))

if x > y > z or x > z > y:
    print(f'{x} is the biggest')
elif y > z:
    print(f'{y} is the biggest')
else:
    print(f'{z} is biggest')

# answer 10
formula = input("Enter calculation i.e. 3 + 4 = 7:")
listFormula = formula.split() # ['3', '+', '4', '=', '7']
x = int(listFormula[0]) # 3
y = int(listFormula[2]) # 4
z = int(listFormula[4]) # 7
opr = listFormula[1]
if opr == '+':
    res = x + y == z
elif opr == '-':
    res = x - y == z
elif opr == '*':
    res = x * y == z
elif opr == '/':
    res = x / y == z
print(f'the forumla was {res}')



