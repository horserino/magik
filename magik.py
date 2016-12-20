import sys
import os
import re
import asyncio
import traceback
import requests
import aiohttp
import urllib.request
import json
import wand
import PIL
import copy
import PIL.Image
import PIL.ImageFont
import PIL.ImageOps
import PIL.ImageDraw
import random
import discord
import subprocess
import time
import html
import urbandict
import shutil
import magic
import numpy as np
import datetime
import macintoshplus
import linecache
import math
from io import BytesIO
from io import StringIO
from sys import argv, path
from discord.ext import commands
from utils import checks
from discord.message import Message
from discord.user import User
from pyfiglet import figlet_format
from wand.drawing import Drawing
from wand.image import Image
from wand.color import Color
from PIL import ImageDraw
from PIL import Image
from gif import *
from image import *
from subprocess import call

class magik:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True, aliases=['imagemagic', 'imagemagick', 'magic', 'magick'])
    async def magik(self, ctx, *urls:str):
      """Apply magik to Image(s)\n .magik image_url or .magik image_url image_url_2"""
      
      try:
        if len(urls) == 0 and len(ctx.message.attachments) == 0:
          await self.bot.say(":no_entry: Please input url(s), mention(s) or atachment(s).")
          return
        xx = await self.bot.say("ok, processing")
        img_urls = []
        scale = None
        content_msg = ''
        for attachment in ctx.message.attachments:
          img_urls.append(attachment['url'])
        if len(ctx.message.mentions) != 0:
          for mention in ctx.message.mentions:
            img_urls.append(mention.avatar_url)
        for url in urls:
          if url.startswith('<@'):
            continue
          try:
            if str(math.floor(float(url))).isdigit():
              scale = int(math.floor(float(url)))
              content_msg = '`Scale: {0}`\n'.format(scale)
              if scale > 5 and ctx.message.author.id != config['ownerid']:
                scale = 5
                content_msg = '`Scale: {0} (Limit: <= 5)`\n'.format(scale)
              continue
          except:
            pass
          if isimage(url) == False:
            if isgif(url):
              await self.bot.say(":warning: `magik` is for images, pleas use gmagik!")
            else:
              await self.bot.say('Invalid or Non-Image!')
            return
          img_urls.append(url)
        else:
          if len(img_urls) == 0:
            await self.bot.say(":no_entry: Please input url(s), mention(s) or atachment(s).")
            return
        yummy = []
        exif = {}
        count = 0
        for url in img_urls:
          b = await bytes_download(url)
          i = wand.image.Image(file=b, format='png').clone()
          exif.update({count:(k[5:], v) for k, v in i.metadata.items() if k.startswith('exif:')})
          count += 1
          i.transform(resize='800x800>')
          if scale == None:
            i.liquid_rescale(width=int(i.width*0.5), height=int(i.height*0.5), delta_x=1, rigidity=0)
            i.liquid_rescale(width=int(i.width*1.5), height=int(i.height*1.5), delta_x=2, rigidity=0)
          else:
            i.liquid_rescale(width=int(i.width*0.5), height=int(i.height*0.5), delta_x=1, rigidity=0)
            i.liquid_rescale(width=int(i.width*1.5), height=int(i.height*1.5), delta_x=scale, rigidity=0)
          i.resize(i.width, i.height)
          magikd = BytesIO()
          i.save(file=magikd)
          magikd.seek(0)
          yummy.append(magikd)
        if len(yummy) > 1:
          imgs = [PIL.Image.open(i).convert('RGBA') for i in yummy]
          min_shape = sorted([(np.sum(i.size), i.size) for i in imgs])[0][1]
          imgs_comb = np.hstack((np.asarray(i.resize(min_shape)) for i in imgs))
          imgs_comb = PIL.Image.fromarray(imgs_comb)
          ya = BytesIO()
          imgs_comb.save(ya, 'png')
        else:
          ya = yummy[0]
        for x in exif:
          if len(exif[x]) >= 2000:
            continue
          content_msg += '**Exif data for image #{0}**\n'.format(str(x+1))+code.format(exif[x])
        else:
          if len(content_msg) == 0:
            content_msg = None
        ya.seek(0)
        await self.bot.send_file(ctx.message.channel, ya, filename='magik.png', content=content_msg)
        await self.bot.delete_message(xx)
      except discord.errors.Forbidden:
        await self.bot.say(":warning: **I do not have permission to send files!**")
    
def setup(bot):
    bot.add_cog(magik(bot))
