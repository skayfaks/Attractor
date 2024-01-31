import requests
import fake_headers


def requester(url: str):
    headers = fake_headers.Headers().generate()
    for retry in range(5):
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return response
            else:
                raise Exception("Неудачный запрос, код ответа: {}".format(response.status_code))
        except Exception as e:
            print("Произошла ошибка: ", e)
            continue
    raise Exception("Не удалось выполнить запрос после 5 попыток")
