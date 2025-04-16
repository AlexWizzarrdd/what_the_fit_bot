from core.wb_search import search
import requests

response = search('black dress')
json_dict = response.json()
print(response.status_code)

# import requests

# # URL запроса
# url = "https://search.wb.ru/exactmatch/ru/common/v9/search"
# # Параметры запроса, представленные в виде словаря.
# params = {
#     "ab_testing": "false",
#     "appType": "1",
#     "curr": "rub",
#     "dest": "-1255987",
#     "hide_dtype": "13",
#     "lang": "ru",
#     "page": "1",
#     "query": "свитер серый женский",  # автоматически преобразуется в percent-encoding
#     "resultset": "catalog",
#     "sort": "popular",
#     "spp": "30",
#     "suppressSpellcheck": "false"
# }

# try:
#     # Выполнение GET-запроса
#     response = requests.get(url, params=params)
    
#     # Проверка статуса ответа
#     response.raise_for_status()  # выбрасывает исключение для кодов ответа 4xx/5xx
    
#     # Преобразование ответа из формата JSON в объект Python (например, словарь)
#     data = response.json()
    
#     # Вывод полученных данных
#     print("Полученные данные:")
#     print(data)

# except requests.exceptions.RequestException as e:
#     print("Ошибка при выполнении запроса:", e)

