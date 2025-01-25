import json

"""
    -bu dasturning vazifasi users.json faylida nechta enjeneerlar borligini hisoblash va ekranga chiqarish...
"""
try:
    with open('people.json') as f:

        json_data = f.read()
except FileNotFoundError:
    print("xato: 'people.json' fayli topilmadi.")
try:
    users_list = json.loads(json_data)
except json.JSONDecodeError:
    print("xato: Json formatida xato.")
    exit()
try:
    engineer = list(filter(lambda user: user['job'] == 'Engineer', users_list))
except KeyError:
    print("lug'atda mavjud bolmagan kalitga murojat qildingiz.")
except NameError:
    print("name maydoni noto'g'ri turdagi qiymatga ega.")
print(engineer)