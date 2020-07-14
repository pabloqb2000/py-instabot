from instaBot import *
from tqdm import tqdm
import os

# Unfollow all the people that aren't following you back

myBot = InstagramBot(os.environ.get("INSTA_USR"), os.environ.get("INSTA_PWD"))
myBot.login()

myBot.goToProfile()
account = myBot.username

following, followers = myBot.getFollowLists(account)

fekas = [f for f in following if not f in followers and f != account]

for f in tqdm(fekas, desc="Unfollows:"):
    myBot.unfollow(f)
    sleep(10)

print("Done!!")

myBot.closeBrowser()
