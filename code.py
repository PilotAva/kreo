import requests

def get_quote_of_the_day():
    url = "https://favqs.com/api/qotd"
    response = requests.get(url)
    data = response.json()
    if "quote" in data:
        return data["quote"]["body"]
    return "Цитата дня недоступна."

while True:
    user_input = input("Введите 'цитата' для получения цитаты дня или 'выход' для завершения: ")

    if user_input == "выход":
        break
    elif user_input == "цитата":
        quote = get_quote_of_the_day()
        print("Цитата дня:")
        print(quote)
    else:
        print("Неверная команда. Пожалуйста, введите 'цитата' или 'выход'.")
