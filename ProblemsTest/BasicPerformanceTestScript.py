import requests
import threading
import time

success = 0
failure = 0

def hit_api():
    global success, failure

    try:
        start = time.time()

        response = requests.get("https://example.com/api/data")

        end = time.time()
        print(f"Response time: {end - start} seconds")

        if response.status_code == 200:
            success += 1
        else:
            failure += 1

    except Exception as e:
        failure += 1

threads = []

for i in range(200):
    thread = threading.thread(target=hit_api)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Total Success: {success}")
print(f"Total Failure: {failure}")