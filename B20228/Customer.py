'''Customer Class
Write a class Customer that contains a name and an address of a customer.
'''
class Customer:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
    def __str__(self):
        return f'\nCustomer Information \nName: {self.name}\nAddress: {self.address}\n'


if __name__ == '__main__':
    customer1 = Customer('AJAY', 'WAKISO')
    print(customer1)
