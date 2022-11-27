list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_number, max_element_index = 0, 0
for key, value in enumerate(list_numbers):
    if value >= max_number:
        max_number = value
        max_element_index = key

list_numbers[max_element_index], list_numbers[-1] = list_numbers[-1], max_number

print(list_numbers)
# Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
