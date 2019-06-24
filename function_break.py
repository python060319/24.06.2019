
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
    
        
