import pickle

def common_divisors(a, b):
    divisors_a = {i for i in range(1, a + 1) if a % i == 0}
    divisors_b = {i for i in range(1, b + 1) if b % i == 0}
    common = divisors_a.intersection(divisors_b)
    return common

common_divs = common_divisors(450, 290)

with open('common_divisors.bin', 'wb') as file:
    pickle.dump(common_divs, file)
print("Спільні дільники чисел 450 і 290 записані у файл common_divisors.bin")

with open('common_divisors.bin', 'rb') as file:
    common_divs = pickle.load(file)

print("Спільні дільники чисел 450 і 290:", common_divs)
