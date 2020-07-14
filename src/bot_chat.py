from instaBot import *
from tqdm import tqdm
import os

'''

    Bot wich replies to your instagram dms

'''

# Log in
myBot = InstagramBot(os.environ.get("INSTA_USR"), os.environ.get("INSTA_PWD"))
myBot.login()

# Accept follow requests
# print("Accepting follows")
# myBot.acceptFollows()

# Calculate the followers list
# myBot.setFollowers()

# Open chat
myBot.chatMenu()

# Print new chats
chats = myBot.getNewChats()
myBot.openChat(chats[-1])
myBot.sendMsg()

# Exit safely
print("Done!!")
print("Enter any key to continue")
input()
myBot.closeBrowser()
