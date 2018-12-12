import utils


class Blockchain:
    def __init__(self, block):
        self.block = block

    def check_balance(self, name):
        if lookup_pk(name) is None:
            raise ValueError('Name %s Not exists.' % name)

        balance = 0.
        block = self.block

        while isinstance(block, Block):
            balance += block.check_block_balance(name)
            block = block.prev_block

        return balance

    def __len__(self):
        block = self.block

        while isinstance(block, Block):
            block = block.prev_block
            len += 1
        return len

    def __str__(self):
        num_transactions = len(self.block)
        output_total = 0.    # TODO
        height = len(self)

        init_entry, signature = self.block.entries[0]
        _, miner, miner_reward, timestamp = entry

        size = utils.get_size(self)

        return 'Number Of Transactions:\t%d\n' % num_transactions + \
                'Output Total:\t%f\n' % output_total + \
                'Height:\t%d\n' % height + \
                'Timestamp:\t%f\n' % timestamp + \
                'Miner:\t%s\n' % miner.decode('utf-8') + \
                'Miner Reward:\t%f\n' % miner_reward + \
                'Miner Signature:\t%s\n' % signature.decode('utf-8') + \
                'Nounce:\t%d\n' % self.block.nounce + \
                'Hash:\t%s\n' % self.block.hash.decode('utf-8') + \
                'Previous Block Hash:\t%s\n' % self.block.prev_hash.decode('utf-8') + \
                'Merkle Root:\t%s\n' % self.block.merkle_root.decode('utf-8')
