import requests


class TestReqHeaders:

    def test_req_header(self):

        expectedHeader = "'x-secret-homework-header': 'Some secret value'"
        expectedKey = 'x-secret-homework-header'
        response = requests.post("https://playground.learnqa.ru/api/homework_header")

        statusCode = response.status_code
        assert statusCode == 200, f"Unexpected Status code in response = '{statusCode}"
        print(statusCode)

        headers = dict(response.headers)

        if expectedKey in headers:
            assert f"'{expectedKey}': '{headers[expectedKey]}'" == expectedHeader, \
                f"Unexpected actual value '{headers[expectedKey]}' of the '{expectedKey}' expected header Key " \
                f"in the actual headers list: '{headers}'"
            print(f"The expected header: '{expectedHeader}' found in the actual headers list: '{headers}'")
        else:
            print(f"There is no '{expectedKey}' expected header Key in the actual headers list '{headers}'")

    # Use: 'python -m pytest -s test_request_headers.py -k "test_req_header"' string to run test it terminal