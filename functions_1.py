
# for
# while
# do-while

# foreach
# - go over each item of a collection

dishes = ['burger', 'ice-cream', 'cracker', 'coffee']
for dish in dishes:
    if dish == 'cracker':
        print(dish)
    else:
        print(dish.upper())

# sum all of the numbers in the list (without sum)
# 1- just sum
# 2- ignore 'bomb'
# 3- sum positive and negative seperately
numbers = [100, -50, 7.8, 'bomb', 55, -30]
sumPos = 0
sumNeg = 0
for number in numbers:
    if number != 'bomb':
        if number > 0:
            sumPos = sumPos + number
        else:
            sumNeg = sumNeg + number
print(f'sum positive = {sumPos}')
print(f'sum negative = {sumNeg}')

