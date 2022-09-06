# створіть функцію для перевірки, що за замовчуванням число не менше 0 та не
# більше 100 (потрібно, щоб верхня та нижня межа могли налаштовуватися)
i = 5
v = 7
n = 0
#
def check_numb():
    assert i <=v, 'меньше v'
    assert i >=n, 'не больше чем n'
check_numb()


# створіть функцію для перевірки, що отриманий аргумент є числом (інт)

def check_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# створіть функцію, що отримує урл та віддає json, отриманий через цей урл
# (валідувати не потрібно, ми поки що працюємо з даними, вважаючи,
# що вони валідні)
#
import requests
def get_data(url:str=None):
    response = requests.get(URL)
    data = response.json()
    return data

# створити функцію, яка приймає стрічку, і має її повернути, враховуючи , що ця
# стрічка має бути довжиною не більше 150 символів (може регулюватися через
# передачу аргумента функції), а якщо отримана стрічка буде довшою за 150
# символів, то стрічка має бути обрізана до 150 символів, причому останні
# три символи мають бути ... (трьома крапками)

st = ('dfijiheriuhguierhgjerhgigsdfsdfsdfsddfsdfsdfhirghierhguierdsnfjksdfjkhsdkjfhsdjkfhsdjkfhsjkfhjsdkhfjksdhfhguierhguierhguierhguierhgfjkdfngjkdngjkdfhgjkdfhgjkdhgjkdfhgjksdhgjksd')
def check_len (a=st):
    if len(a) >=150:
        a = a[:147]
    print(a , "...")
check_len(st)

def write_file(file_name='photo.txt', text_data='default text data'):
    with open(file_name, 'a+') as f:
        f.write(text_data + '\n')
write_file()

# Далее на 3 TASK я поплыл, не понимаю ка это прописывать......
# створити функцію, котра приймає урл (та опційний параметр bd булевого формату
# для завдання 4), і очікує там словник з ключами, описаними в завданні 1
# в функції перевіряється, що якщо в учня бали від 90 до 100, учень має
# винагороди, його вік від 9 до 18 років, то формуємо стрічку типу

