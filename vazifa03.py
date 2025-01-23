import json

try:
    with open('people.json') as f:

        json_data = f.read()
except FileNotFoundError:
    #agar people.json fayli yoq bolsa FileNotFoundError xatosi chiqsa expect ishlaydi.
    print("xato: 'people.json' fayli topilmadi.")
try:
    users_list = json.loads(json_data)
except json.JSONDecodeError:
    #agar JSONDecodeError xatosi chiqsa expect ishlaydi va ekranga json formatida xato degan yozuv chiqadi
    print("xato: Json formatida xato.")
    exit()
try:
    india = list(filter(lambda user: user['country'] == 'India', users_list))
except KeyError:
    #userni [country] sozi xato yozilsa yoki yoq bolsa key eror xatosi kelib chiqadi
    print("lug'atda mavjud bolmagan kalitga murojat qildingiz.")
print(india)