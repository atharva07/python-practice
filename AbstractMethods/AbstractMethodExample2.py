from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing Paypal payment of ${amount}")

class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing UPI payment of ${amount}")

payment = CreditCardPayment()
payment.process_payment(100)