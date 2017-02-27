
import imaplib,email,imapclient

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)


imapObj.login('rebertjacob@gmail.com','7259692024')
imapObj.select_folder('INBOX', readonly=False)


UIDs= imapObj.search('ALL')
imapObj.delete_messages(UIDs)
imapObj.expunge()
