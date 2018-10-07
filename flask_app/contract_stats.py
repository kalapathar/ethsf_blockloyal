import json
import web3
# from web3.auto.infura import w3
# from web3 import web3

from web3 import Web3
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
# w3.eth.defaultAccount = w3.eth.accounts[0]
UMPT_JSON = json.load(open('./truffle/build/contracts/UnitedMileagePlusToken.json'))
# Address field should be the checksum address at which the ERC20 contract was deployed
umpt = w3.eth.contract(address='0x2c1726335D4B6dFCA91929083328b87CDBCf7232', abi=UMPT_JSON['abi'])

def getUmptContractStats() :
    print ('name:', umpt.functions.name().call())
    print ('symbol:', umpt.functions.symbol().call())
    print (umpt.functions.decimals().call())
    print ('totalSupply:', umpt.functions.totalSupply().call())
    # print ('Balance:', umpt.functions.balanceOf('0xD1220A0cf47c7B9Be7A2E6BA89F429762e7b9aDb').call())

getUmptContractStats()

