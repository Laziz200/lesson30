import json
"""
    -bu dasturning vazifasi users.json faylida nechta hindistonliklar borligini hisoblash...
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
    india = list(filter(lambda user: user['country'] == 'India', users_list))
except KeyError:
    print("lug'atda mavjud bolmagan kalitga murojat qildingiz.")
print(india)