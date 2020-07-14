from instaBot import *
import os

'''
    
    Log in with the given account
    print the list of people that aren't following the given user back
    (the given account should already be following the user)

'''
USER = "cristiano_ronaldo"

# Log in
myBot = InstagramBot(os.environ.get("INSTA_USR"), os.environ.get("INSTA_PWD"))
myBot.login()

# Print list
myBot.checkFollowersOf(USER)

# Exit safely
print("\n\nDone!!")
myBot.closeBrowser()
input()