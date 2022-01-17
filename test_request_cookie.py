import requests


class TestReqCookie:

    def test_req_cookie(self):

        expectedCookie = {'HomeWork': 'hw_value'}

        response = requests.post("https://playground.learnqa.ru/api/homework_cookie")

        statusCode = response.status_code
        assert statusCode == 200, f"Unexpected Status code in response = '{statusCode}"
        print(statusCode)

        cookie = dict(response.cookies)
        assert cookie == expectedCookie, f"Unexpected cookie in response: '{cookie}'"
        print(f"Cookie in response: '{cookie}', as expected")

    # Use: 'python -m pytest -s test_request_cookie.py -k "test_req_cookie"' string to run test it terminal