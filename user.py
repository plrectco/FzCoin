from user_base import UserBase
from blockchain import Blockchain

class User(UserBase):
    def __init__(self, name):
        super().__init__(name)

        self.wallets = {}
        '''
        wallet_org:
            name
            sk
            pk
            cert
            balance
            pending_transactions
            completed_transactions
        '''

        self.blockchain = Blockchain(None)

    def listen_broadcast(self, blockchain):
        if not isinstance(blockchain, Blockchain):
            return
        if not utils.verify_blockchain(blockchain):
            return

        if self.blockchain = len(blockchain) > len(self.blockchain):
            self.blockchain = blockchain


    def register_wallet():
        pass

    def pay_to():
        pass

    def check_balance():
        pass

    def query_transaction_status():
        pass
