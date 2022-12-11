from random import randint


def get_unique_list_numbers() -> list[int]:
    random_num = [randint(-10, 10) for _ in range(15)]
    uni_num = set(random_num)
    while len(uni_num) < 15:
        uni_num = list(uni_num)
        uni_num.append(randint(-10, 10))
        uni_num = set(uni_num)
    return list(uni_num)


list_unique_numbers = get_unique_list_numbers()
print(get_unique_list_numbers())
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
# answer
