import utils
from user_base import UserBase

class WalletOrg(UserBase):
    def __init__(self):
        super().__init__(name)
        self.users = []

    def add_user(self, name, pk):
        pass

    def del_user(self, name):
        pass

    def lookup_user(self, name):
        pass

    def check_balance(self, name, blockchain):
        pass

    def self_sign(self):
        pass
