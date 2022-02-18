import requests
import random
import string
i = int(input('>>>'))
url = 'http://u1597324.plsk.regruhosting.ru/5CyA27iHOStqY40/email.php'
head = {
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding' : 'gzip, deflate',
    'Accept-Language' : 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control' : 'max-age=0',
    'Connection' : 'keep-alive',
    'Content-Length' : '25',
    'Content-Type' : 'application/x-www-form-urlencoded',
    'Cookie' : '_ga=GA1.2.4275064.1635670195; PHPSESSID=05e941ce78e5d38998e54d036cb0274d',
    'Host' : 'u1597324.plsk.regruhosting.ru',
    'Origin' : 'http://u1597324.plsk.regruhosting.ru',
    'Referer' : 'http://u1597324.plsk.regruhosting.ru/5CyA27iHOStqY40/index.php',
    'Upgrade-Insecure-Requests' : '1',
    'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Mobile Safari/537.36',
}


for i in range(i):
    char_set = string.ascii_uppercase + string.digits
    yoyo = ''.join(random.sample(char_set*6, 6))
    char = string.ascii_uppercase + string.digits
    yoy = ''.join(random.sample(char*9, 6))
    data = {
    'text' : yoyo,
    'password' : yoy,
    'go': '',
}
    r = requests.post(url=url , data=data , headers=head).status_code
    print(i)