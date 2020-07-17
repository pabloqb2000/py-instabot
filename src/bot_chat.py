from instaBot import *
from tqdm import tqdm
import os
from BotAnswers import *

'''

    Bot wich replies to your instagram dms

'''

# Log in
myBot = InstagramBot(os.environ.get("INSTA_USR"), os.environ.get("INSTA_PWD"))
myBot.login()

# Create reactor
reactor = Reactor(myBot, os.environ.get("INSTA_ADMIN"))

# Accept follow requests
# print("Accepting follows")
# myBot.acceptFollows()

# Main loop
while True:
    # Wait for new messages
    while not myBot.hasNewChats():
        sleep(5)

    # Calculate the followers list
    myBot.setFollowers()

    # Open chat
    myBot.chatMenu()

    # Get new chats
    chats = myBot.getNewChats()
    if len(chats) > 0:
        account = chats[-1]
        myBot.openChat(account)

        # Read messages
        msgs = myBot.read_msgs()
        last_msg = msgs[-1]

        # Answer the msg
        reactor.process(last_msg, account)

    # Go back to the profile
    myBot.goToProfile()

# Exit safely
print("Done!!")
print("Enter any key to continue")
raw_input() # use input() for python3
myBot.closeBrowser()
