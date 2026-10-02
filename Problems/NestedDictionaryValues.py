def get_values(dict1):
    result = []

    for value in dict1.values():
        if isinstance(value, dict):
            result.extend(get_values(value))
        else:
            result.append(value)

    return result

data = {
    "a": 1,
    "b": {
        "c": 2,
        "d": {
            "e": 3
        }
    },
    "f": 4
}

print(get_values(data))