import json
"""
    -bu dasturning vazifasi users.json faylida nechta 20 yoshdan kichiklar borligini hisoblash...
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
    age = list(filter(lambda user: user['age'] < 20, users_list))
except KeyError:
    print("lug'atda mavjud bolmagan kalitga murojat qildingiz.")
except TypeError:
    print("age maydoni noto'g'ri turdagi qiymatga ega.")
print(age)