import utils

class Transaction:
    def __init__(self, payer, pay_to=[]):
        self.payer = payer
        self.pay_to = pay_to
        self.timestamp = utils.get_timestamp()

    def add_payment(self, payee, amount):
        self.pay_to.append((payee, amount))

    def del_payment(self, entry):
        try:
            del self.pay_to[self.pay_to.index(entry)]
        except ValueError:
            pass

    def __str__(self):
        return '%s%s%d' % (self.payer, self.pay_to, self.timestamp)

    def __bytes__(self):
        return bytes(str(self).encode('utf-8'))
