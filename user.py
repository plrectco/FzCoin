from user_base import UserBase

class User(UserBase):
    def __init__(self, name):
        super().__init__(name)
        self.sk = None
        self.certs = []

        self.last_checked_balance = None
        self.pending_transactions = []
        self.completed_transactions = []

    def register_wallet():
        pass

    def pay_to():
        pass

    def check_balance():
        pass

    def query_transaction_status():
        pass
