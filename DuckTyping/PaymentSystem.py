class CreditCard:
    def pay(self, amount):
        print(f"Paid {amount} using credit card")

class UPI:
    def pay(self, amount):
        print(f"Paid {amount} using UPI")

class crypto:
    def pay(self, amount):
        print(f"Paid {amount} using Crypto")

def process_payment(method, amount):
    try:
        method.pay(amount)
    except AttributeError:
        print("Invalid payment method")

process_payment(CreditCard(), 3000)
process_payment(UPI(), 4000)
process_payment("cash", 5000)