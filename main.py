import requests
import json

#GET

user_input = input("Enter User ID: ")
get_url = f"https://jsonplaceholder.typicode.com/todos/{user_input}"

response = requests.get(get_url)

print(response.json())

#PUT

to_do_item = {'userId': 2, 'title': 'my to do', 'completed': False}
to_do_item_json = json.dumps(to_do_item)
post_url = "https://jsonplaceholder.typicode.com/todos"

#optional header
headers = {"Content-Type": "application/json"}

post_response = requests.post(post_url, data=to_do_item_json, headers=headers)
#post_response = requests.post(post_url, json=to_do_item, headers=headers)
#post_response = requests.post(post_url, data=to_do_item, headers=headers)
print(post_response.json())

#PUT

to_do_item_15 = {'userId': 2, 'id': 15, 'title': 'put title', 'completed': True}
put_url = "https://jsonplaceholder.typicode.com/todos/15"

put_response = requests.put(put_url, data=to_do_item_15)
print(put_response.json())

#PATCH

to_do_item_15_patch = {'title': 'patch title'}

patch_response = requests.patch(put_url, data=to_do_item_15_patch)
print(patch_response.json())

#DELETE

delete_response = requests.delete(put_url)
print(delete_response)
print(delete_response.json())
