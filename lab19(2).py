import shelve

students_heights = {
    'Іванов': 170,
    'Петренко': 165,
    'Сидоренко': 180,
    'Коваленко': 175,
    'Дмитренко': 160,
    'Шевченко': 190,
    'Кравченко': 185,
    'Мельник': 175,
    'Поліщук': 178,
    'Ткаченко': 172,
    'Кравець': 168,
    'Романенко': 182,
    'Гончаренко': 177,
    'Захарченко': 170,
    'Заболотний': 173,
    'Козак': 180,
    'Лисенко': 165,
    'Тарасенко': 169
}

Q = int(input("Введіть значення Q (зріст для фільтрації): "))

filtered_students = {name: height for name, height in students_heights.items() if height > Q}

with shelve.open('hi.dat') as db:
    db['filtered_students'] = filtered_students
print("Дані учнів із зростом більше за", Q, "записані у файл hi.dat")

with shelve.open('hi.dat') as db:
    filtered_students = db['filtered_students']

print("Учні із зростом більше за Q:")
for name, height in filtered_students.items():
    print(f"{name}: {height} см")
