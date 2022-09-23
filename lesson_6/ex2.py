import requests

URL2 = 'https://script.googleusercontent.com/macros/echo?user_content_key=18-MLQGTcHyrGVnCCRqEJVIYWZFvfhHIMnvz6IimW_d0QNG088U8d_u_TGX8sza95NImHj3c-K6W3xcva8CKzk_RAPwJsOzim5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnEVvqx-kuTyynDs87B0KIRw4WGwaIu2iLivPlsyF7KQlBh9kMh9BLwwA9c3NkOuRrYa6Ar8Jygf33jRX1nkQX4XDg6I4JxZ6WNz9Jw9Md8uu&lib=MnTjVF8bTE4ny8Yhas7KUsdqK-6lY-9os'

def get_data(url: str):
    response = requests.get(url)
    data = response.json()
    return data

x = get_data(URL2)

for i in x['data']:
    m=i['e_mail']
    f = m.find('@')
    if (f == -1) or (f == 0) or (f == len(m)-1):
        print(m)
