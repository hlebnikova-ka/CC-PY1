from pprint import pprint
dict_ = []
n = 16

for value_a in range(n):
    value_b = {'bin': bin(value_a), 'dec': value_a, 'hex': hex(value_a), 'oct': oct(value_a)}
    dict_.append(value_b)

pprint(dict_)
# answer
