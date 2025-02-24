import requests

base = "http://127.0.0.1:5000/"
# postreq = requests.post(base + 'ai', json={"question": "what are you", "answer": "im just a ai model"})
# print(postreq.json())
getreq2 = requests.post(base + 'ai', json={"question": "hello mate how are you", "answer": "im fine"})
print(getreq2.json())
