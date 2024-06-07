import threading
import queue
import requests

q=queue.Queue()

with open('proxy_list.txt',"r") as f:
    proxies = f.read().split("\n")
    for proxy in proxies:
        q.put(proxy)

def check_proxy():
    global q
    while not q.empty():
        proxy = q.get()
        try:
            response = requests.get('https://httpbin.org/ip', proxies={"http": proxy, "https": proxy}, timeout=5)
        except:
            continue

        if response.status_code == 200:
            print(proxy)

for _ in range(10):
    t = threading.Thread(target=check_proxy)
    t.start()
