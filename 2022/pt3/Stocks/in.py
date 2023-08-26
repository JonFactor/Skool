import json
### imports ###

inpit = input('Stock Ticker:')
inpit = {'ticker':inpit}
inpit = json.dumps(inpit)
### input ###
with open('BigBoyProj\Stocks\localdata.json', 'w') as op:
    op.write(inpit)
    op.close()
### make txt file ###

import api
### start api code ###