import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("18651170"))
API_HASH = getenv("5e9a549d86d92149142464049d4d70d7")
# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")
# Add Owner Username without @ 
OWNER_USERNAME = getenv("OWNER_USERNAME", "Mr_DaNiSh_kHaN21")
# Get Your bot username
BOT_USERNAME = getenv("BOT_USERNAME", "RYTHMUSIK_BOT)
# Don't Add style font 
BOT_NAME = getenv("BOT_NAME", " Rʸ͢͢͢THM🆇BOT")
#get Your Assistant User name
ASSUSERNAME = getenv("ASSUSERNAME", "RYTHMASSISTANT01)
EVALOP = list(map(int, getenv("EVALOP", "6195725562").split()))
# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://DanishDBINN:DanishDBINN@cluster0.pf7pm0f.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "10000"))

# Duration Limit for downloading Songs in MP3 or MP4 format from bot
SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "18000")
)  # Remember to give value in Minutes

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1001981325108)

# Get this value from  on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "5392794822"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/sanju9636/LOFI_MUSIC",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/RYTHM_UPDATE")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/RYTHM_DISCUSSION")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# Time after which you're assistant account will leave chats automatically.
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400000")
)  # Remember to give value in Seconds


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "250"))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Ge@STRINGSEASO_NBOT2 session from @STRINGSEASO_NBOT
STRING1 = getenv("STRING_SESSION", "BQEcmCIAs1OaV5Xazih-A4lOSAx7i6Oi8K903v3wlVgfFrerrYl6UwNrLI_oSXTjRTmYNaSX4PaFysWzYKoUCCZGPrx3SNcGvqHgeh5l4RRLvyI4cXXIL3-3KX3iXGdFeilXIvqavIC-BY6cdwRt7Wi8fyAd4YXlWtmlluJWeFvsLSf-GgcyI3pBn1_lVFsMPBQUb_LvKS_HpYwW3tiOdYwvH6ZIWBIT9Z51xnAIUOgB2dvV0tuUkeOjDgIgO1YmrqxwLaraeDqg0iprhhnxjTHqYH72iRVvN9eOwEkekaSqxDs4khDRZ3bLLiLgwFCg2x30YRRyOkh1hkrH5BhWcM1-wiZpSgAAAAEqTznMAA")
STRING2 = getenv("STRING_SESSION2", "AQAls2MAUkoQxAAydsncdTm0sLy4lu6d1cIAkSYaTwfKalv2X6AsLFPkOMKcYvEU4Pl0ZNqFIIqkvBllYqj8y9CQv1vgSY-2SQXQZYhknPomrxynmfbHJrHrjvzk11eF79yGIkwUIwNJtiOgJE2OUVGBGBb2WUsJpkpZTtY5CRory0S0g8anGICpCz7z9m870qyhJrkOek21CHNmtsG74-Am4M_77MzlVH6M5Un4hkx9kOZ47ft5Yy7OvD6JieGiq2VYzSYMF4Zb9qX7bwuOLJTZLechSKgmGrFziFToshnnrFcGnP-K0i1dJMg9n4QYCPwWlVlP7G-HrXv0tgWkd4kvV8E0EgAAAAFDDakGAA")
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
    "START_IMG_URL", "https://graph.org/file/4565ffe46f5043f95e2a2.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/dec61e858d57c14343455.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/40a68bb3c5d30e2298685.jpg"
STATS_IMG_URL = "https://graph.org/file/136c57e473c33a0c62152.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/d2081243af7c1d7578b7b.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/d2081243af7c1d7578b7b.jpg"
STREAM_IMG_URL = "https://graph.org/file/829d73d62e52f5d945f2e.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/982b01ba53c3d69b0d0ce.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/d2081243af7c1d7578b7b.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/61024698bfc926e95d57a.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/61024698bfc926e95d57a.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/61024698bfc926e95d57a.jpg"


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
