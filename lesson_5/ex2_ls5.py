# створіть функцію для перевірки, що за замовчуванням число не менше 0 та не
# більше 100 (потрібно, щоб верхня та нижня межа могли налаштовуватися)
from typing import Any
import requests

URL = 'https://script.google.com/macros/s/AKfycbx9eWXOYgFQDuY_Cx8yH7FWCjc74z9Voa9s5sQeeLht4Erp2qc5E183liACyiZhTajF/exec'


def is_number_in_range(number: int, low: int = 0, high: int = 150):
    return number >= low and number <= high


if __name__ == '__main__':
    assert is_number_in_range(60)
    assert is_number_in_range(-5) is False
    assert is_number_in_range(160) is False
    assert is_number_in_range(60, 20, 30) is False


# створіть функцію для перевірки, що отриманий аргумент є числом (інт)


def is_integer(value: Any):
    return type(value) == int


if __name__ == '__main__':
    assert is_integer(2)
    assert is_integer('sdf22') is False
    assert is_integer('22###:') is False
    assert is_integer(2.0) is False
    assert is_integer([]) is False


# створіть функцію, що отримує урл та віддає json, отриманий через цей урл
# (валідувати не потрібно, ми поки що працюємо з даними, вважаючи,
# що вони валідні)


def get_data(url: str = None):
    response = requests.get(url)
    data = response.json()
    return data


# створити функцію, яка приймає стрічку, і має її повернути, враховуючи , що ця
# стрічка має бути довжиною не більше 150 символів (може регулюватися через
# передачу аргумента функції), а якщо отримана стрічка буде довшою за 150
# символів, то стрічка має бути обрізана до 150 символів, причому останні
# три символи мають бути ... (трьома крапками)


def string_cutter(value: str, limit=150):
    if len(value) > limit:
        value = value[:limit - 3] + '...'
    return value


if __name__ == '__main__':
    assert string_cutter('15jkh5') == '15jkh5'
    assert len(string_cutter('15jkh5' * 100, 50)) == 50
    assert string_cutter('15jkh5' * 100, 50)[-3:] == '...'


def write_file(file_name='photo.txt', text_data='default text data'):
    with open(file_name, 'a+') as f:
        f.write(text_data + '\n')


# Далее на 3 TASK я поплыл, не понимаю ка это прописывать......
# створити функцію, котра приймає урл (та опційний параметр bd булевого формату
# для завдання 4), і очікує там словник з ключами, описаними в завданні 1
# в функції перевіряється, що якщо в учня бали від 90 до 100, учень має
# винагороди, його вік від 9 до 18 років, то формуємо стрічку типу

def engine():
    data = get_data(URL)['data']
    for student in data:
        if student['score'] > 90:
            write_file('students.txt', str(student))


engine()
