import requests

key_value, string_val = input().split()

user_arr = []
user_string = ''
username_string = ''
query_params = ''
count = 0

response = requests.get("https://jsonplaceholder.typicode.com/posts")

json_arr = response.json()

for post in json_arr:
    if string_val in (post[key_value]).split():
        count = count + 1
        user_id = post['userId']
        if user_id not in user_arr:
            user_arr.append(user_id)
            user_string = user_string + str(user_id) + ', '
            query_params = query_params + 'id=' + str(user_id) + '&'

query_params = query_params[:-1]

if count != 0:
    response = requests.get("https://jsonplaceholder.typicode.com/users?" + query_params)
    users = response.json()
    user_string = user_string[:-2]
    for user in users:
        username_string = username_string + user['username'] + ', '
    username_string = username_string[:-2]

print(key_value, "with word '%s': %d" % (string_val, count))
print('User Ids:', user_string)
print('Query params:', query_params)
print('Usernames:', username_string)
