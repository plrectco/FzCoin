import utils
import crypto

class WalletOrg:
    def __init__(self):
        self.name = None # 8 byte
        self.sk = None
        self.cert = None

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
