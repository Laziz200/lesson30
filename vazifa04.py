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
    age = list(filter(lambda user: user['age'] < 20, users_list))
except KeyError:
    #userni [country] sozi xato yozilsa yoki yoq bolsa key eror xatosi kelib chiqadi
    print("lug'atda mavjud bolmagan kalitga murojat qildingiz.")
except TypeError:
    #agar agening qiymati notogri turdagi qiymatga ega yoki shunga oxshash tyupe erorlar chiqsa ishlaydi bu except.
    print("age maydoni noto'g'ri turdagi qiymatga ega.")
print(age)