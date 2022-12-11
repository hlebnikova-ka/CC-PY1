from random import sample


def get_random_password(n=8) -> str:
    source = '0123456789ABCDEFGHJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    return "".join(sample(source, n))


print(get_random_password())
# answer
