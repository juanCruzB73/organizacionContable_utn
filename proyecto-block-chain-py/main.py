from hashlib import sha256
import json
import time
import flask from Flask,request
import request

class Block:
    def __init__(self,index,transactions,timestamp,previus_hash):
        self.index=index
        self.transactions=transactions
        self.timestamp=timestamp
        self.previus_hash=previus_hash
        self.unconfirmed_transactions=[]
        self.chain=[]
        self.create_genesis_block()
    def compute_hash(block):
        block_string=json.dumps(block,__dict__,sort_keys=True)
        return sha256(block_string.encode()).haxdigest()
    def add_new_transaction(self,transaction):
        self.unconfirmed_transactions.append(transaction)
    def mine(self):
        if not self.unconfirmed_transactions:
            return False
        last_block=self.last_block()
        new_block=Block(index=last_block.index+1,
                        transactions=self.unconfirmed_transactions,
                        timestamp=time.time(),
                        previus_hash=last_block.hash)
        proof=self.proof_of_work(new_block)
        self.add_block(new_block,proof)
        self.unconfirmed_transactions=[]
        return new_block.index
class Blockchain:
    def __init__(self):
        self.chain=[]
        self.create_genesis_block()
    def create_genesis_block(self):
        genesis_block=Block(0,[],time.time(),"0")
        genesis_block.hash=genesis_block.compute_hash()
        self.chain.append(genesis_block)
    @property
    def last_block(self):
        return self.chain[-1]
    difficulty=2
    def proof_of_work(self,block):
        block.nonce=0
        computed_hash=block.compute_hash()
        while not compute_hash.startswith("0"*Blockchain.difficulty):
            block.nonce+=1
            computed_hash=block.compute_hash()
        return compute_hash
    def add_block(self,proof):
        previus_hash=self.last_block.hash
        if previus_hash != block.previus_hash:
            return False
        if not self.is_valid_proof(block,proof):
            return False
        block.hash=proof
        self.chain.append(block)
        return True
    def is_valid_proof(self,block,block_hash):
        return (block_hash.startswith("0"*Blockchain.difficulty) and block_hash==block.compute_hash())

app=Flask(__name__)
blockchain=Blockchain()

@app.route('/new_transaction',methods=['POST'])
def new_transaction():
    tx_data=request.get_json()
    required_fields=["author","content"]

    for field in required_fields:
        if not tx_data.get(field):
            return "INVALID TRANSACTION DATAI",404
        tx_data["timestamp"]=time.time()
        blockchain.add_new_transaction(tx_data)
        return "SUCCESS",201
@app.route('/mine',methods=['GET'])
def mine_unconfirmed_transaction():
    result=blockchain.mine()
    if not result:
        return "NO TRANSACTION TO MINE"
    return "BLOCK #{} IS MINED".format(result)
@app.route('/pending_tx')
def get_pending_tx():
    return json.dumps(blockchain.unconfirmed_transactions)
peers=set()

@app.route('/register_node',methods=['POST'])
def register_new_peers():
    node_address=request.get_json()['node_address']
    if not node_address:
        return "INVALID DATA",400
    peers.add(node_address)
    return get_chain()
@app.route("/register_with",methods=['POST'])
def register_with_existing_node():
    node_address=request.get_json()['node_address']
    if not node_address:
        return "INVALID DATA",400
    data={"node_address":request.host_url}
    headers={"Content-Type":"application/json"}

    response=request.post(node_address+"/register_node",
                      data=json.dumps(data),headers=headers)
    if response.status_code==200:
        global blockchain
        global peers
        chain_dump=response.json()["chain"]
         blockchain=create_chain_from_dump(chain_dump)
        peers.update(response.json()["peers"])
        return "register successful",200
    else:
        return response.content,response.status_code

def create_chain_from_dump(chain_dump):
    bockchain=Blochain()
    for idx,block_data in enumerate(chain_dump):
        block=Block(block_data["index"],
                    block_data["transactions"],
                    block_data["timestamp"],
                    block_data["previus_hash"])
        proof = block_data["hash"]
        if idx>0:
            added=blockchain.add_block(block,proof)
            if not added:
                raise Exceptionthe ("the chain dumpis tempered")
        else:
            blockchain.chain.append(block)
        return blockchain
