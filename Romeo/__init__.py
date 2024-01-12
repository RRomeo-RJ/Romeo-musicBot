from Romeo.core.bot import RomeoBot
from Romeo.core.dir import dirr
from Romeo.core.git import git
from Romeo.core.userbot import Userbot
from Romeo.misc import dbb, heroku
from Romeo.logging import LOGGER

git()


dirr()

dbb()

heroku()

# Clients
app = RomeoBot()

userbot = Userbot()


from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
