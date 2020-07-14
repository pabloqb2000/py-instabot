# py-instabot
Bot for instagram I made using selenium library for firefox
## Important note
This bot has been built for a personal proyect, instagram has it's own politics on the use you can do of their website, I do not take any responsabilities on the use you might do of this code, allways beware of the norms you should be following and keep in mind that Instagram could ban your account if you make a bad use of their services.
## Contents
Inside the src/ folder you can find two libraries, EmailSender and InstaBot.</br>
You can also find some examples on how to unfollow people that aren't following you back and how to print on screen the people that don't follow back a certain user.</br>
## OS
This proyect was built in ubuntu, but it could easily be modified to work in other operating systems.
## Notes
You need to have installed some libraries in order to run this code, this libraries are:
- <b>tqdm</b>: python library for showing nice progress bars, it can easily be installed with the terminal by using pip install
- <b>selenium</b>: python library for using some webdrivers, it can also be installed with pip
- <b>geckodriver</b>: mozillas driver for firefox
## Set up your account
For this proyect I have set one enviroment variable for the username of my account and another one for it's password, you should do the same in order to use this the same way, save a "INSTA_USR" variable for the username and a "INSTA_PWD" variable for the password.</br>
Another option is to replace the parts were it says:</br>
```python
os.environ.get("INSTA_USR")
os.environ.get("INSTA_PWD")
```
with your username and password respectively
