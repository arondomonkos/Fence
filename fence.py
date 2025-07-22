# Fence Visualization Project
# Author: Áron Domonkos
# Year: 2022

import random


data = []
with open('fence.txt', 'r') as file:
    for line in file:
        side, width, color = line.strip().split()
        data.append([int(side), int(width), str(color)])

print('\nFunction 2')
print(f'Total number of lots sold: {len(data)}')

print('\nFunction 3')
even = []
odd = []
for lot in data:
    if lot[0] == 0:
        even.append(lot)
    else:
        odd.append(lot)

if data[-1][0] == 0:
    print('The last lot was sold on the even side.')
    print(f'The house number of the last lot: {len(even) * 2}')
else:
    print('The last lot was sold on the odd side.')
    print(f'The house number of the last lot: {len(odd) * 2 - 1}')

print('\nFunction 4')
matching = []
matching_fences = []

for i in range(len(odd) - 1):
    if odd[i][2] == odd[i + 1][2]:
        matching.append(odd[i])

for lot in matching:
    if lot[2] != '#' and lot[2] != ':':
        matching_fences.append(lot)

fence_index = 0
for lot in odd:
    if lot != matching_fences[0]:
        fence_index += 1
    if lot == matching_fences[0]:
        break

print(f'The fence color matches the neighbor at house number: {fence_index * 2 + 1}')

print('\nFunction 5')
# input_number = int(input('Enter a house number: '))
input_number = 83
house = []
excluded_colors = []
alphabet = [chr(i) for i in range(65, 91)]
available_colors = []

if input_number % 2 == 1:
    house.append(odd[input_number // 2])
    for i in range(len(odd) - 1):
        if house[0] == odd[i]:
            excluded_colors.append([
                odd[i][2],
                odd[i + 1][2],
                odd[i - 1][2]
            ])
else:
    house.append(even[input_number // 2 - 1])
    if house[0] == even[i]:
        excluded_colors.append([
            even[i][2],
            even[i + 1][2],
            even[i - 1][2]
        ])

print(f'Fence color / status: {house[0][2]}')

for color in alphabet:
    if color not in excluded_colors[0]:
        available_colors.append(color)

new_color = random.choice(available_colors)
print(f'A possible painting color: {new_color}')

fence_lengths = []
fence_colors = []
fence_row = []
number_row = []
house_numbers = []

for lot in odd:
    fence_lengths.append(int(lot[1]))
    fence_colors.append(lot[2])
    fence_row.append(lot[2] * lot[1])

for i in range(1, len(odd) * 2 + 1):
    if i % 2 == 1:
        house_numbers.append(i)

for length, number in zip(fence_lengths, house_numbers):
    if number > 100:
        row = str(number) + (length - 3) * ' '
    elif number > 10:
        row = str(number) + (length - 2) * ' '
    else:
        row = str(number) + (length - 1) * ' '
    number_row.append(row)

fence_row_str = ''.join(fence_row)
number_row_str = ''.join(number_row)

with open('streetview.txt', 'w') as file:
    file.write(f'{fence_row_str}\n{number_row_str}')