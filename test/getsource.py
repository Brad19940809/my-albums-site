import http.client

conn = http.client.HTTPConnection("127.0.0.1:8000")


headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'x-requested-with': "XMLHttpRequest",
    'cache-control': "no-cache",
    'postman-token': "19ffa1ae-0303-929b-4e6c-f898f7a8a42f"
    }

conn.request("GET", "/captcha/refresh/", headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))