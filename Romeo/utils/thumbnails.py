import os
import re
import textwrap
import random
import aiofiles
import aiohttp
from PIL import (Image, ImageDraw, ImageEnhance, ImageFilter,
                 ImageFont, ImageOps)
from youtubesearchpython.__future__ import VideosSearch

from config import MUSIC_BOT_NAME, YOUTUBE_IMG_URL

themes = ["blue", "red", "pink", "purple"]
colors = ["white", "black", "red", "orange", "yellow", "green", "cyan", "azure", "blue", "violet", "magenta", "pink"]


def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


async def gen_thumb(videoid, user_id):
    try:
        os.remove(f"cache/thumb{videoid}.png")
    except:
        pass
    url = f"https://www.youtube.com/watch?v={videoid}"
    try:
        results = VideosSearch(url, limit=1)
        for result in (await results.next())["result"]:
            try:
                title = result["title"]
                title = re.sub("\W+", " ", title)
                title = title.title()
            except:
                title = "Unsupported Title"
            try:
                duration = result["duration"]
            except:
                duration = "Unknown Mins"
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            try:
                views = result["viewCount"]["short"]
            except:
                views = "Unknown Views"
            try:
                channel = result["channel"]["name"]
            except:
                channel = "Unknown Channel"

        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(
                        f"cache/thumb{videoid}.png", mode="wb"
                    )
                    await f.write(await resp.read())
                    await f.close()

        images = random.choice(themes)
        border = random.choice(colors)
        image1 = Image.open(f"cache/thumb{videoid}.png")
        image2 = Image.open(f"helper/rj/{images}.png")
        image3 = changeImageSize(1280, 720, image1)
        image4 = changeImageSize(1280, 720, image2)
        image5 = image3.convert("RGBA")
        image6 = image4.convert("RGBA")
        Image.alpha_composite(image5, image6).save("cache/temp.png")
        logo = Image.open("cache/temp.png")
        img = ImageOps.expand(logo, border=10, fill=f"{border}")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("helper/rj/font.otf", 55)
        font2 = ImageFont.truetype("helper/rj/font.otf", 35)
        draw.text((20, 555), f"Title: {title[:50]} ...", (255, 255, 255), font=font)
        draw.text((20, 615), f"Duration: {duration}", (255, 255, 255), font=font)
        draw.text((20, 675), f"Views: {views}", (255, 255, 255), font=font)
        draw.text((10, 10), f"RJ•MUSIC", (255, 255, 255), font=font2)
        try:
            os.remove(f"cache/thumb{videoid}.png")
            os.remove(f"cache/temp.png")
        except:
            pass
        img.save(f"cache/{videoid}.png")
        return f"cache/{videoid}.png"
    except Exception:
        return YOUTUBE_IMG_URL
        
        
        
        
async def gen_qthumb(videoid, user_id):
    try:
        os.remove(f"cache/thumb{videoid}.png")
    except:
        pass
    url = f"https://www.youtube.com/watch?v={videoid}"
    try:
        results = VideosSearch(url, limit=1)
        for result in (await results.next())["result"]:
            try:
                title = result["title"]
                title = re.sub("\W+", " ", title)
                title = title.title()
            except:
                title = "Unsupported Title"
            try:
                duration = result["duration"]
            except:
                duration = "Unknown Mins"
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            try:
                views = result["viewCount"]["short"]
            except:
                views = "Unknown Views"
            try:
                channel = result["channel"]["name"]
            except:
                channel = "Unknown Channel"

        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(
                        f"cache/thumb{videoid}.png", mode="wb"
                    )
                    await f.write(await resp.read())
                    await f.close()

        images = random.choice(themes)
        border = random.choice(colors)
        image1 = Image.open(f"cache/thumb{videoid}.png")
        image2 = Image.open(f"helper/rj/{images}.png")
        image3 = changeImageSize(1280, 720, image1)
        image4 = changeImageSize(1280, 720, image2)
        image5 = image3.convert("RGBA")
        image6 = image4.convert("RGBA")
        Image.alpha_composite(image5, image6).save("cache/temp.png")
        logo = Image.open("cache/temp.png")
        img = ImageOps.expand(logo, border=10, fill=f"{border}")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("helper/rj/font.otf", 55)
        font2 = ImageFont.truetype("helper/rj/font.otf", 35)
        draw.text((20, 555), f"Title: {title[:50]} ...", (255, 255, 255), font=font)
        draw.text((20, 615), f"Duration: {duration}", (255, 255, 255), font=font)
        draw.text((20, 675), f"Views: {views}", (255, 255, 255), font=font)
        draw.text((10, 10), f"RJ•MUSIC", (255, 255, 255), font=font2)
        try:
            os.remove(f"cache/thumb{videoid}.png")
            os.remove(f"cache/temp.png")
        except:
            pass
        img.save(f"cache/{videoid}.png")
        return f"cache/{videoid}.png"
    except Exception:
        return YOUTUBE_IMG_URL
