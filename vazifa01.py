import json

try:
    with open('people.json','r') as f:

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
count_of_females=0

for user in users_list:
    #if sharti genderdagi femalelarni topsa count_of_femalesga 1 qoshib boradi 
    if user['gender'] == "Female":
        count_of_females += 1

print(f"ayollar soni:{count_of_females}\n")#jami ayollar sonini chiqaradi