import time

def retry_logic_decorator(max_retries):
    def retry_logic(func):
        def wrapper():
            retries = 0
            while retries < max_retries:
                try:
                    func()
                    retries += 1
                    time.sleep(2)
                except Exception as e:
                    print("Error occured: ", e)
            
            if retries == max_retries:
                print("Max retries limit reached. Exiting")
                
        return wrapper
    return retry_logic

@retry_logic_decorator(max_retries=3)
def consume_event():
    print("Consuming Event")            