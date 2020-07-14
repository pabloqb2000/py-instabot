from instaBot import *
from tqdm import tqdm
import os

'''

    Unfollow all the people that aren't following you back

'''

# Log in
myBot = InstagramBot(os.environ.get("INSTA_USR"), os.environ.get("INSTA_PWD"))
myBot.login()

# Go to main profile
myBot.goToProfile()
account = myBot.username

# Get follow list
following, followers = myBot.getFollowLists(account)

# Filter people that aren't following you back
fekas = [f for f in following if not f in followers and f != account]

# Unfollow that people
for f in tqdm(fekas, desc="Unfollows:"):
    myBot.unfollow(f)
    sleep(10)

# Exit safely
print("Done!!")
myBot.closeBrowser()
