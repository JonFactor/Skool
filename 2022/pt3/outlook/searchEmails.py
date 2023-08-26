import os 
from pathlib import Path
import re 
import time
a = 0
e = []
items = []
Email = 'python\outlook\Emails'
RawEmail = 'python\outlook\Emails\RawEmails\\'
exactDir = "\\Users\\jonfa\\Documents\\GitHub\\Portfolio\\python\\outlook\\Emails\\RawEmails\\"
keyword = 'jon'#input('please input Search:')
subjects = []
os.chdir(RawEmail)
names = []

direct = os.listdir()
direct2 = []
# get list of emails with keyword
for item in direct:
    os.chdir(exactDir+direct[a])
    direct2 = os.listdir()
    b = 0 
    
    for files in direct2:
        d = []
        try:
            os.chdir(exactDir+direct[a]+'\\'+direct2[b])
            c = open("BODY.txt", 'r')
            for line in c:
                d.append(line)
                

            c.close()
        except NotADirectoryError:
            pass
        finally: 
            b+=1
            h=0
            for g in d:
                if keyword in d[h]:
                    if files not in e:
                        e.append(files)
                    if item not in items:
                        items.append(item)
                    h+=1
    k = 'EMAIL:' + str(e) +'SENDER:'+ str(items)
    
    a += 1

    k = re.sub('[^\u0000-\u007f]', '',  k)


os.chdir('C:\\Users\jonfa\Documents\GitHub\Portfolio\python\outlook\Emails\RESULTS')
f = open('RESULT.txt', 'w+')
f.writelines(k)
f.close
print()