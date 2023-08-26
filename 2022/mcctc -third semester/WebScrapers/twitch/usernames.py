### imports
import random, json
### open words
words = []
usernames = []
with open("WebScrapers\\twitch\words.txt", "r") as f:
    for line in f:
        words.append(line.replace('\n', ''))
    f.close()
### combine words
for word in words:
        bigWord = word + words[random.randint(0, len(words) - 1)]
        if not bigWord in usernames:
            usernames.append(bigWord)
        else:
            pass
### randomize usernames
newusers = []
for username in usernames:
    newuser = []
    ## upper lower
    for char in username:
        if random.randint(0, 4) == 1:
            char = char.upper()
        else:
            char = char.lower()
        newuser.append(char)
    newnewuser = ''
    for char in newuser:
        newnewuser += char
    ## numbers
    if random.randint(0, 8) == 1:
        newnewuser += str(random.randrange(20, 99))
    elif random.randint(0, 8) >= 4:
        newnewuser += str(random.randrange(1, 20))
    else:
        pass
    newusers.append(newnewuser)
### passwords
passwords = []
for u in usernames:
    password = random.randrange(10000000000000000000000, 10000000000000000000000000)
    passwords.append(int(password))
import makeacct