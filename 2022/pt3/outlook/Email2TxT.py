#importing windows api
import win32com.client
#importing other junk
from pathlib import Path # 4 folders
import os # 4 finding folders
import re # to remove unicode

########################## Pre-Loop #########################

#shortcut to connecting to outlook
Dispatch = win32com.client.Dispatch("Outlook.Application")
#connect to outlook
outlook = Dispatch.GetNamespace("MAPI")
#pulling accounts
accounts= Dispatch.Session.Accounts
#pulling inbox
inbox = outlook.GetDefaultFolder(6)
#pull incomeing mail
incoming = inbox.Items
#make folders
EmailsDir = Path.cwd() / "python"/ "outlook" / "Emails" # setting path
EmailsDir.mkdir(parents=True, exist_ok=True) # settings to allow overwrite and to be in a file

RawEmailsDir = EmailsDir / "RawEmails" # setting path
RawEmailsDir.mkdir(parents=True, exist_ok=True) # settings to allow overwrite and to be in a file
ResultDir = ''

ResultDir = Path.cwd() / "python"/ "outlook" / "Emails" / "RESULTS"
ResultDir.mkdir(parents=True, exist_ok=True)
########################### Loop ################################

for incomin in incoming:  #looping until no more incoming mail
    # setting mail parts to respective name
    RawSender = incomin.Sender
    Rawsubject = incomin.Subject 
    Rawbody = incomin.body
    imagies = incomin.Attachments
    #making varibles writable
    Sender = ""
    for character in str(RawSender):
        if character.isalnum():
            Sender += character
    Sender = Sender[:20]
    subject = ""
    for character in str(Rawsubject):
        if character.isalnum():
            subject += character
    subject = subject[:20]
    body = ""
    for character in str(Rawbody):
        if character.isalnum():
            body += character
    body = body.strip("/n")
    body = re.sub('[^\u0000-\u007f]', '',  body) # removes unicode from body
    # creates new folder for every Sender
    SenderFolderDir = "" # so if statment can run
    if not os.path.exists(SenderFolderDir):
        SenderFolderDir = RawEmailsDir / str(Sender)
        SenderFolderDir.mkdir(parents=True, exist_ok=True)
    # creates new folder for every Subject
    SubjectFolderDir = "" # so if statment can run
    if not os.path.exists(SubjectFolderDir):
        SubjectFolderDir = SenderFolderDir / str(subject)
        SubjectFolderDir.mkdir(parents=True, exist_ok=True)
    #puts txt file of body in folder
    Path(SubjectFolderDir / "BODY.txt").write_text(str(body))
    #puts imagies in folder
    for image in imagies:
        image.SaveAsFile(SubjectFolderDir / str(image))


