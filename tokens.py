import requests
import json
import time

#Starting new job to have in response new token and needed time from server
response1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
obj = json.loads(response1.text)

#token key and value in the first server response
tokenKey = "token"

if tokenKey in obj:
    print(f"The '{tokenKey}' key is in the first server response, as expected")
    token = obj[tokenKey]
    print(f"The new job token's value in the first server response is: {token}")
else:
    print(f"There is no '{tokenKey}' key in the first server response: '{obj}'")

#seconds key and value in the first server response
secondsKey = "seconds"

if secondsKey in obj:
    print(f"The '{secondsKey}' key is in the first server response, as expected")
    seconds_needed_for_job = obj[secondsKey]
    print(f"To do the job server need {seconds_needed_for_job} seconds.")
else:
    print(f"There is no '{secondsKey}' key in the first server response: '{obj}'")


#Send second request with the new token to know the current job status
tok = {"token": token}
response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", tok)
obj = json.loads(response2.text)

#status key and value in the 2nd server response
statusKey = "status"

if statusKey in obj:
    print(f"The '{statusKey}' key is in the 2nd server response, as expected")
    if obj[statusKey] == "Job is NOT ready":
        print(f"Actual status key value in the 2nd server response is: '{obj[statusKey]}', as expected")
    else:
        print(f"Unexpected status key value in the 2nd server response: '{obj[statusKey]}'")
else:
    print(f"There is no '{statusKey}' key in the 2nd server response: '{obj}'")


#After waiting needed time to complete job, we send 3rd request with token to know the job result and current job status
time.sleep(seconds_needed_for_job)

response3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", tok)
obj = json.loads(response3.text)

#result key and value in the 3rd server response
resultKey = "result"

if resultKey in obj:
    print(f"The '{resultKey}' key is in the 3rd server response, as expected")
    if obj[resultKey] == "42":
        print(f"Actual job result key value in the 3rd server response is: '{obj[resultKey]}', as expected")
    else:
        print(f"Unexpected job result key value in the 3rd server response: '{obj[resultKey]}'")
else:
    print(f"There is no '{resultKey}' key in the 3rd server response: '{obj}'")

#status key and value in the 3rd server response
if statusKey in obj:
    print(f"The '{statusKey}' key is in the 3rd server response, as expected")
    if obj[statusKey] == "Job is ready":
        print(f"Actual status key value in the 3rd server response is: '{obj[statusKey]}', as expected")
    else:
        print(f"Unexpected status key value in the 3rd server response: '{obj[statusKey]}'")
else:
    print(f"There is no '{statusKey}' key in the 3rd server response: '{obj}'")
