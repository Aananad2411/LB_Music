import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "23457265"))
API_HASH = getenv("API_HASH", "7a5b7db2d61e9a691677053fe05fd0db)

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", 7348933075:AAEUkbS9-AliXqcPvlEnsekj-oO0lGrCDNw)

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI",mongodb+srv://Jinwoosung:nope24112908@cluster0.df7pz43.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0 )

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 180))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1002158046607)

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "7348188604"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/Learningbots79/LB_Music", # dont Change this otherwise u get error 🧧
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/+H929Q7LdsV4xN2M1")
SUPPORT_CHAT = getenv("SUPPORT_GROUP", "https://t.me/+H929Q7LdsV4xN2M1")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", cd6b1fc089cd4db3a97e8ce93cb746bd)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", ce9b560fe9a64e63b571e2f65b393ced)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", BQGbOlcAtESCNba5DAp1gN9leI_4iy_0sqmiIWOBqgRN_Xg-EJnUl1V-kWST2iEDz7iqLQZ3jOaogws7H2xvzsj7l8iwOl_kBHXkds5jFQw_pFgLQIfdb1gQ5BxAnf8EpM0acSmba8Y9yqv68BV8ykr5T6MTucsL92hPozWuYub8ZkPSJ6I_040XZ5dF0ITRhXt9n3IiFnVaG-4tQ5UVHX6zrWVBn1KTnp1iL6uB5cJ4_kQAlEN-WqP-oAB8TCMw16D0IuxYa0qCrP-afUMPNzCXlVjjtHoeByYv0KF8g6JnixWk66ftMjIXt6EySGFxp9tYwI-ugXmBlyKL2aK1CkscPaWQkAAAAAG8F264AA)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/69a4d370fb382e5808ace.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/69a4d370fb382e5808ace.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/4b6f642a52233b29413c6.jpg"
STATS_IMG_URL = "https://graph.org/file/4b6f642a52233b29413c6.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/4b6f642a52233b29413c6.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/4b6f642a52233b29413c6.jpg"
STREAM_IMG_URL = "https://graph.org/file/4b6f642a52233b29413c6.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/4b6f642a52233b29413c6.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/4b6f642a52233b29413c6.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/4b6f642a52233b29413c6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/4b6f642a52233b29413c6.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/4b6f642a52233b29413c6.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
