from instaBot import *
import os

# Print the 'fekas' list of this account (people that arent following you back)
# Bot must be following this account
USER = "cristiano_ronaldo"

myBot = InstagramBot(os.environ.get("INSTA_USR"), os.environ.get("INSTA_PWD"))
myBot.login()

myBot.checkFollowersOf(USER)

print("\n\n\n")
