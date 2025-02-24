import requests

base = "http://127.0.0.1:5000/"
# postreq = requests.post(base + 'ai', json={"question": "hello ai", "answer": "hi"})
# print(postreq.json())
getreq2 = requests.put(base + 'ai', json={"question": "hello ai"})
print(getreq2.json())
