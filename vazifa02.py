import json
"""
    -bu dasturning vazifasi users.json faylida nechta erkaklar borligini hisoblash...
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

count_of_males=0

for user in users_list:
    
    if user['gender']=='Male':
        count_of_males+=1
print(f"erkaklar soni:{count_of_males}\n")