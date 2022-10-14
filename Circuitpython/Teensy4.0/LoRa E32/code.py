# coding=utf-8
'''
attach boot.py file before running this code
otherwise, ebyteE32 won't save E32config.json file
'''

import board
from loraE32 import ebyteE32


e32 = ebyteE32(board.D2, board.D3, board.D4, Port='U2', Address=0x0001, Channel=0x04, debug=True)

e32.start()

print(e32.config)
print(e32.getConfig())
print(e32.getVersion())
