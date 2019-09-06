print('*********************')
print('BASIC STRING LIST')
print('*********************')
for item in ['vinay', 'tola', 'ivy']:
  print(item)
print('')

print('*********************')
print('BASIC NUMBER LIST')
print('*********************')
for item in [1, 2, 3, 4, 5]:
  print(item)
print('')

print('*********************')
print('BASIC RANGE LIST')
print('*********************')
for item in range(5):
  print(item)
print('')

print('********************************')
print('BASIC SPECIFIED RANGE LIST')
print('********************************')
for item in range(10, 15):
  print(item)
print('')

print('*******************************************')
print('BASIC SPECIFIED RANGE LIST WITH 2-STEPS')
print('*******************************************')
for item in range(10, 15, 2):
  print(item)

print('****************')
print('BASIC TOTAL')
print('****************')
prices = [1, 2, 3, 4, 5]
total = 0
for price in prices:
  total += price
print(f'Total is: {total}')

print('***************')
print('NESTED LOOP')
print('***************')
for x in range(5):
  for y in range(4):
    print(f'({x}, {y})')

print('***********')
print('DRAW F')
print('**********')
allx = [8, 2, 8, 2, 2]
for x_count in allx:
  output = ''
  for x in range(x_count):
    output += 'X'
  print(output)