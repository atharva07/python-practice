from collections import Counter
import json

def get_error_services(file_path):
    error_services = set()

    try:
        with open(file_path, "r") as file:
            logs = json.load(file)

        for log in logs:
            if log.get("level") == "ERROR":
                service = log.get("service")
                if service:
                    error_services.add(service)
        
        return list(error_services)

    except Exception as e:
        print(f"Error processing file: {e}")
        return []
    
def get_messages(file_path):
    messages = []
    try:
        with open(file_path, "r") as file:
            logs = json.load(file)

        for log in logs:
            log_message = log.get("message")
            if log_message:
                messages.append(log_message)

        return messages
    except Exception as e:
        print(f"Error processing file: {e}")
        return []
    
def parse_logs(file_path):
    log_dict = {"INFO": 0, "ERROR": 0, "WARN": 0}

    with open(file_path, "r") as file:
        for line in file:
            for level in log_dict:
                if level in line:
                    log_dict[level] += 1

    return log_dict

def top_errors(file_path):
    errors = []

    with open(file_path, "r") as file:
        for line in file:
            if "ERROR" in line:
                errors.append(line.strip())

    return Counter(errors).most_common(3)

if __name__ == "__main__":
    file_path = "File_Handling/logs.json"   # In Linux: /var/log/app/logs.json
    result = get_error_services(file_path)
    print("Services with ERROR:", result)
    messages_logs = get_messages(file_path)
    print("Logs messages :", messages_logs)
    levels = parse_logs(file_path)
    print("Levels :", levels)