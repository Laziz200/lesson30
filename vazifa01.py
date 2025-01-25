import json

"""
    -bu dasturning vazifasi users.json faylida nechta ayollar borligini hisoblash...
"""
try:
    with open('people.json','r') as f:

        json_data = f.read()
except FileNotFoundError:
    
    print("xato: 'people.json' fayli topilmadi.")
try:
    users_list = json.loads(json_data)
except json.JSONDecodeError:

    print("xato: Json formatida xato.")
    exit()
count_of_females=0

for user in users_list:
    
    if user['gender'] == "Female":
        count_of_females += 1

print(f"ayollar soni:{count_of_females}\n")