from json import JSONDecodeError

import requests

#Requests/responses for POST, GET, PUT, DELETE requests type without parameters
#1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.
print("Start #1")
resp200 = 200

respGet = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
actualStatusCodeForGet = respGet.status_code
if actualStatusCodeForGet == resp200:
    print(f"The response for GET request is '{actualStatusCodeForGet}', as expected")
else:
    print(f"Unexpected response for GET request - '{actualStatusCodeForGet}'")

respPost = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type")
actualStatusCodeForPost = respPost.status_code
if actualStatusCodeForPost == resp200:
    print(f"The response for POST request is '{actualStatusCodeForPost}', as expected")
else:
    print(f"Unexpected response for POST request - '{actualStatusCodeForPost}'")

respPut = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type")
actualStatusCodeForPut = respPut.status_code
if actualStatusCodeForPut == resp200:
    print(f"The response for PUT request is '{actualStatusCodeForPut}', as expected")
else:
    print(f"Unexpected response for PUT request - '{actualStatusCodeForPut}'")

respDelete = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type")
actualStatusCodeForDelete = respDelete.status_code
if actualStatusCodeForDelete == resp200:
    print(f"The response for DELETE request is '{actualStatusCodeForDelete}', as expected")
else:
    print(f"Unexpected response for DELETE request - '{actualStatusCodeForDelete}'")



#2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.
print("Start #2")
try:
    respHead = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
    print(f"The response for HEAD request is: '{respHead.status_code}'")
except AttributeError:
    print("The 'requests' module has no attribute 'HEAD'")

try:
    respPlease = requests.please("https://playground.learnqa.ru/ajax/api/compare_query_type")
    print(f"The response for 'PLEASE' request is: '{respPlease.status_code}'")
except AttributeError:
    print("The 'requests' module has no attribute 'PLEASE'")



#3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.
print("Start #3")
successResp = {'success': '!'}
payload = {"method": "GET"}

respGet = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params = payload)
getRespJson = respGet.json()
if getRespJson == successResp:
    print(f"The response for GET request with GET param is '{getRespJson}', as expected")
else:
    print(f"Unexpected response for GET request with GET param - '{getRespJson}'")

payload = {"method": "POST"}
respPost = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data = payload)
postRespJson = respPost.json()
if postRespJson == successResp:
    print(f"The response for POST request with POST param is '{postRespJson}', as expected")
else:
    print(f"Unexpected response for POST request with POST param - '{postRespJson}'")

payload = {"method": "PUT"}
respPut = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data = payload)
putRespJson = respPut.json()
if putRespJson == successResp:
    print(f"The response for PUT request with PUT param is '{putRespJson}', as expected")
else:
    print(f"Unexpected response for PUT request with PUT param - '{putRespJson}'")

payload = {"method": "DELETE"}
respDelete = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data = payload)
deleteRespJson = respDelete.json()
if deleteRespJson == successResp:
    print(f"The response for DELETE request with DELETE param is '{deleteRespJson}', as expected")
else:
    print(f"Unexpected response for DELETE request with DELETE param - '{deleteRespJson}'")



#4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.
# Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее.
#И так для всех типов запроса. Найти такое сочетание, когда реальный тип запроса не совпадает со значением
# параметра, но сервер отвечает так, словно все ок. Или же наоборот, когда типы совпадают, но сервер считает, что это не так.
print("Start #4")

request_types = ["POST", "GET", "PUT", "DELETE"]
success = '{"success":"!"}'
wrongMethod = "Wrong method provided"
#response = ""
#method = ""
#type = ""

def findRightResponse(response, method, type):
    print(f"...Run the '{method} request method with '{type}' param/data")
    if type == method and response == success:
        print(f"The response for '{method}' request with an equal '{type}' param is '{response}', as expected")
    elif type == method and response == wrongMethod:
        print(f"The '{response}'response for '{method}' request with an equal '{type}' param/data is wrong response")
    elif type != method and response == success:
        print(f"The '{response}'response for '{method}' request with not equal '{type}' param/data is wrong response")
    elif type != method and response == wrongMethod:
        print(f"The response for '{method}' request with not equal '{type}' param is '{response}', as expected")
    else:
        print(f"Unexpected '{response}' response for '{method}' request with '{type}' param/data")

for type in request_types:
    payload = {"method": type}
    respGet = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payload)
    findRightResponse(respGet.text, "GET", type)

    respPost = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
    findRightResponse(respPost.text, "POST", type)

    respPut = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
    findRightResponse(respPut.text, "PUT", type)

    respDelete = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
    findRightResponse(respDelete.text, "DELETE", type)


