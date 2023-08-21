import datetime
import hashlib
from binascii import unhexlify, hexlify
import time


class Block:
    def __init__(self, prev_hash, index, sender, accepter, amount):
        self.next = None
        self.__data = {
            "prev_hash": prev_hash,
            "index": index,
            "sender": sender,
            "accepter": accepter,
            "amount": amount,
            "hash": "",
            "time": datetime.datetime.now().time()
        }

        self.__data["hash"] = self.mine()

    def get_data(self):
        return self.__data
    
    def mine(self):
        start = time.time()

        mine_hash = hexlify(hashlib.sha256(unhexlify(self.get_data()["prev_hash"])).digest()).decode("utf8")
        while mine_hash[:5] != "00000":
            mine_hash = hexlify(hashlib.sha256(unhexlify(mine_hash)).digest()).decode("utf-8")
        
        finish = time.time() - start
        print("Hash was mined in", finish, "sec.")
        print("-----------------------------")

        return mine_hash


    def append(self, index,  sender, accepter, amount):
        n = self
        while n.next:
            n = n.next
        prev_hash = n.get_data()["hash"]
        
        end = Block(prev_hash, index, sender, accepter, amount)
        n.next = end

def show_blockchain(block):
    node = block
    print(node.get_data())
    print("-----------------------------")
    while node.next:
        node = node.next
        print(node.get_data())
        print("-----------------------------")

genesis = Block("000000", 0, "None", "None", 0)

show_blockchain(genesis)

