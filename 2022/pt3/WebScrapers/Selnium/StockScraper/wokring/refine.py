import os, json, re, string

CIK = []
RAW = []
for file in os.listdir('D:\CodeShit\\SEC.Gov'):
    CIK.append(file)
    with open('D:\CodeShit\\SEC.Gov\\'+file, 'r') as read:
        RAW.append(json.load(read))

cikData = []
Check = []
cikValue = []
x = 0
y = 0
for contents in RAW: # each cik
    if x >= 5: break
    for content in contents: # each transaction
        if not content in Check: Check.append(content)
    transactionData = []
    for transaction in Check:
        transactionData.append(transaction.split('\n'))

    TransLineData = []
    values2 = []
    for transaction in transactionData:
        values = []
        values3 = []
        for line in transaction:
            # editing
            fixed = line.replace('  ', '').split('>')
            if fixed == [''] or len(fixed) < 2 or len(fixed) > 3 or 'footnote id' in  fixed[0]: 
                fixed = 'None'
            else: 
                if len(fixed) == 3 and fixed[2] == '': fixed.pop()
                if fixed[0][1:] in fixed[-1]: 
                    fixed[-1] = fixed[-1].replace('</'+fixed[0][1:],'')
                fixed[0] = fixed[0][1:]
            if fixed[0] == 'value':
                if fixed[1] == 'Common Stock' or fixed[1] == 'Restricted Stock Unit' or fixed[1] == 'Stock Equivalent Unit' or fixed[1] == 'Stock Equivalent Units' or fixed[1] == 'Unsecured Convertible Note' or fixed[1] == 'Restricted Stock Units':
                    values3.append(values)
                    values = []
                else:
                    values.append(fixed)
                #pull out
        #pull out
        values2.append(values3)
    # pull out
    valuesDic = {
        'cik': CIK[x],
        'values': values2
    }
    print(x - len(RAW))
    x += 1 
    with open(f'D:\CodeShit\\try\FinalValues[{x}].json', 'w') as write2:
        json.dump(valuesDic, write2)
