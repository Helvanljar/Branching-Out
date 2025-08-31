import json

# Load users from JSON
with open('users.json', 'r') as f:
    users = json.load(f)

# Filter users older than 25
filtered_users = [user for user in users if user['age'] > 25]

print("Users older than 25:")
for user in filtered_users:
    print(user['name'])
