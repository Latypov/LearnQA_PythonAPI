import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
first_response = response.history[0]
second_response = response.history[1]
third_response = response.history[2]

print(first_response.url)
print(second_response.url)
print(third_response.url)
print(response.history)

