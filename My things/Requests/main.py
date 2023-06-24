import requests

r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
print(r.status_code)
print(r.encoding)
print(r.headers['content-type'])
print(r.text)
print(r.json())