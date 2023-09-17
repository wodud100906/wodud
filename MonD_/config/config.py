import json

def config(value):
    with open("config.json", 'r', encoding='utf-8 sig') as file:
        data = json.load(file)
        guild = data['MonD']['guild']
        role = data['MonD']['role']
        token = data['MonD']['token']

        if value == "guild":
            return int(guild)
        elif value == "role":
            return int(role)
        elif value == "token":
            return token