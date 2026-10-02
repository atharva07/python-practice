'''
Focus is on functions as first-class citizens.
Key Idea:
1. Avoid changing state
2. Use Pure functions
3. Pass functions as arguments to other functions
'''

# Below is an example of a pure function
def add_tax(price):
    return price * 1.1

price = [100, 200, 300]

# Here we are passing function as an argument
new_prices = list(map(add_tax, price))
print(new_prices)