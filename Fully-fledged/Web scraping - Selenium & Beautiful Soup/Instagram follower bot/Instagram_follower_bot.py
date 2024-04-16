from dotenv import load_dotenv
from instagram_bot_class import FollowerBot
import os

# Bot only imitates clicking the "follow" button, so as not to get my ig account blocked by 'bottish' behaviour

load_dotenv()

LOGIN = os.environ.get('LOGIN')
PASSWORD = os.environ.get('PASSWORD')
ACCOUNT_TO_FOLLOW = input("Type the instagram nickname of the "
                          "account the followers of which you would like to follow: ")

bot = FollowerBot()
bot.login(LOGIN, PASSWORD)
bot.find_profile(ACCOUNT_TO_FOLLOW)
bot.follow_followers()

