
numbers = [2, 5, 100, 500, 89, 20, 300]
sum = 0
for number in numbers:
    sum = sum + number
    if sum > 100:
        break
# if finished on break? or list ended?
if sum > 100:
    print(f'sum is over 100: {sum}')
    

numbers = [2, 4, 6, 10, 200, 190, 200, 300]
for number in numbers:
    if number % 2 == 0:
        print(number)
    else:
        break

if number % 2 != 0:
    print('exit on odd number')
else:
    print('successfully completed...')
    

dishes = ['burger', 'ice-cream', 'cracker', 'coffee']
for dish in dishes:
    print(dish)
    for letter in dish: # ['b','u','r','g','e','r']
        print(letter)

matrix = [[10, 22, 36], [-4, 25, 63], [87, 98, 109]]
# print sum of each list
# find biggest number
#matrix[1][2]

biggest = matrix[0][0]
for row in matrix:
    sum = 0
    for col in row:
        sum = sum + col
        if col > biggest:
            biggest = col
    print(f'{row} sum is {sum}')
print(f'the bigegst number is {biggest}')

