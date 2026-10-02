class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
print(MathUtils.add(5, 3))

'''
| Feature                   | Instance Method   | Class Method    | Static Method                    |
| ------------------------- | ----------------- | --------------- | -------------------------------- |
| Decorator                 | None              | `@classmethod`  | `@staticmethod`                  |
| First Parameter           | `self`            | `cls`           | None                             |
| Access Instance Variables | ✅                 | ❌               | ❌                                |
| Access Class Variables    | ✅                 | ✅               | ❌ (unless explicitly referenced) |
| Modify Instance State     | ✅                 | ❌               | ❌                                |
| Modify Class State        | ✅ (through class) | ✅               | ❌                                |
| Called On                 | Object            | Class or Object | Class or Object                  |
'''