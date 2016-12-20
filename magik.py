import discord
from discord.ext import commands
class magik:
    """magik brought to roy"""
    
    def __init__(self, bot):
        self.bot = bot
      
  @commands.command(pass_context=True, aliases=['imagemagic', 'imagemagick', 'magic', 'magick'])
  async def magik(self, ctx, url:str=None, url2=None):
    """Apply magik to Image(s)\n .magik image_url or .magik image_url image_url_2"""
    try:
      if url == None and len(ctx.message.attachments) == 0:
        await self.bot.say("Error: Invalid Syntax\n`.magik <image_url> <image_url2>*`\n`* = Optional`")
        return
      elif len(ctx.message.attachments) >= 1:
        url = ctx.message.attachments[0]['url']
      if url == None and url2 == None and len(ctx.message.attachments) == 2:
        url = ctx.message.attachments[0]['url']
        url2 = ctx.message.attachments[1]['url']
      if len(ctx.message.mentions) > 0 and url2 == None:
        user = ctx.message.mentions[0]
        if user.avatar == None:
          await self.bot.say(":no_entry: Mentioned User Has No Avatar")
          return
        x = await self.bot.say("ok, processing")
        avatar = "https://cdn.discordapp.com/avatars/{0}/{1}.jpg".format(user.id, user.avatar)
        rand = str(random.randint(0, 100))
        path = "/root/discord/files/magik_user_{0}.png".format(rand)
        await download(avatar, path)
        if os.path.getsize(path) == 127:
          await self.bot.say(":no_entry: Mentioned User 1's Avatar is Corrupt on Discord Servers!")
          return
        image = wand.image.Image(filename='/root/discord/files/magik_user_{0}.png'.format(rand))
        image.alpha_channel = True
        i = image.clone()
        i.transform(resize='800x800>')
        i.liquid_rescale(width=int(i.width*0.5), height=int(i.height*0.5), delta_x=1, rigidity=0)
        i.liquid_rescale(width=int(i.width*1.5), height=int(i.height*1.5), delta_x=2, rigidity=0)
        i.resize(i.width, i.height)
        i.save(filename='/root/discord/files/nmagik_user_{0}.png'.format(rand))
        await self.bot.send_file(ctx.message.channel, '/root/discord/files/nmagik_user_{0}.png'.format(rand))
        await self.bot.delete_message(x)
        return
      elif url2 != None and len(ctx.message.mentions) > 0:
        user = ctx.message.mentions[0]
        if len(ctx.message.mentions) == 1:
          user2 = ctx.message.mentions[0]
        else:
          user2 = ctx.message.mentions[1]
        if user.avatar == None:
          await self.bot.say(":no_entry: Mentioned User 1 Has No Avatar")
          return
        if user2.avatar == None:
          await self.bot.say(":no_entry: Mentioned User 2 Has No Avatar")
          return
        x = await self.bot.say("ok, processing")
        avatar = "https://cdn.discordapp.com/avatars/{0}/{1}.jpg".format(user.id, user.avatar)
        avatar2 = "https://cdn.discordapp.com/avatars/{0}/{1}.jpg".format(user2.id, user2.avatar)
        rand = str(random.randint(0, 100))
        path = "/root/discord/files/magik_user_{0}.png".format(rand)
        path2 = "/root/discord/files/magik_user2_{0}.png".format(rand)
        await download(avatar, path)
        await download(avatar2, path2)
        if os.path.getsize(path) == 127:
          await self.bot.say(":no_entry: Mentioned User 1's Avatar is Corrupt on Discord Servers!")
          return
        elif os.path.getsize(path2) == 127:
          await self.bot.say(":no_entry: Mentioned User 2's Avatar is Corrupt on Discord Servers!")
          return
        d = '/root/discord/files/nmagik_user_{0}.png'.format(rand)
        d2 = '/root/discord/files/nmagik2_user_{0}.png'.format(rand)
        image = wand.image.Image(filename=path)
        image.alpha_channel = True
        i = image.clone()
        i.transform(resize='800x800>')
        i.liquid_rescale(width=int(i.width*0.5), height=int(i.height*0.5), delta_x=1, rigidity=0)
        i.liquid_rescale(width=int(i.width*1.5), height=int(i.height*1.5), delta_x=2, rigidity=0)
        i.resize(i.width, i.height)
        i.save(filename=d)
        image2 = wand.image.Image(filename=path2)
        image2.alpha_channel = True
        i2 = image2.clone()
        i2.transform(resize='800x800>')
        i2.liquid_rescale(width=int(i.width*0.5), height=int(i.height*0.5), delta_x=1, rigidity=0)
        i2.liquid_rescale(width=int(i.width*1.5), height=int(i.height*1.5), delta_x=2, rigidity=0)
        i2.resize(i.width, i.height)
        i2.save(filename=d2)
        list_im = [d, d2]
        imgs    = [PIL.Image.open(i).convert('RGBA') for i in list_im]
        min_shape = sorted([(np.sum(i.size), i.size) for i in imgs])[0][1]
        imgs_comb = np.hstack((np.asarray(i.resize(min_shape)) for i in imgs))
        imgs_comb = PIL.Image.fromarray(imgs_comb)
        new_p = '/root/discord/files/nmagik_user_url2_{0}.png'.format(rand)
        imgs_comb.save(new_p)
        await self.bot.send_file(ctx.message.channel, new_p, filename='magik_2users.png')
        os.remove(path)
        os.remove(path2)
        os.remove(new_p)
        await self.bot.delete_message(x)
        return
      if isimage(url) == False:
        await self.bot.say("Invalid or Non-Image!")
        return
      rand = str(random.randint(0, 500))
      rand2 = str(random.randint(0, 500))
      if url2 is None:
        x = await self.bot.say("ok, applying magik")
        location = '/root/discord/files/magik_{0}.png'.format(rand)
        await download(url, location)
      elif url2 is not None:
        x = await self.bot.say("ok, applying magik")
        location = '/root/discord/files/magik_{0}.png'.format(rand)
        location2 = '/root/discord/files/magik2_{0}.png'.format(rand2)
        await download(url, location)
        await download(url2, location2)
      exif = {}
      image = wand.image.Image(filename='/root/discord/files/magik_{0}.png'.format(rand))
      exif.update((k[5:], v) for k, v in image.metadata.items() if k.startswith('exif:'))
      if url2 is not None:
        exif2 = {}
        image2 = wand.image.Image(filename='/root/discord/files/magik2_{0}.png'.format(rand2))
        exif2.update((k[5:], v) for k, v in image2.metadata.items()
          if k.startswith('exif:'))
      img = wand.image.Image(filename='/root/discord/files/magik_{0}.png'.format(rand))
      img.alpha_channel = True
      i = img.clone()
      i.alpha_channel = True
      if url2 is not None:
          with wand.image.Image(filename='/root/discord/files/magik2_{0}.png'.format(rand2)) as B:
            B.alpha_channel = True
            B.clone()
            B.transform(resize='800x800>')
            B.liquid_rescale(width=int(B.width*0.5), height=int(B.height*0.5), delta_x=1, rigidity=0)
            B.liquid_rescale(width=int(B.width*1.5), height=int(B.height*1.5), delta_x=2, rigidity=0)
            B.resize(B.width, B.height)
            B.save(filename='/root/discord/files/nmagik2_{0}.png'.format(rand))
            with wand.image.Image(filename='/root/discord/files/magik_{0}.png'.format(rand)) as A:
              A.alpha_channel = True
              A.clone()
              A.transform(resize='800x800>')
              A.liquid_rescale(width=int(A.width*0.5), height=int(A.height*0.5), delta_x=1, rigidity=0)
              A.liquid_rescale(width=int(A.width*1.5), height=int(A.height*1.5), delta_x=2, rigidity=0)
              A.resize(A.width, A.height)
              A.save(filename='/root/discord/files/nmagik1_{0}.png'.format(rand))
          list_im = ['/root/discord/files/nmagik1_{0}.png'.format(rand), '/root/discord/files/nmagik2_{0}.png'.format(rand)]
          imgs    = [PIL.Image.open(i).convert('RGBA') for i in list_im]
          min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
          imgs_comb = np.hstack((np.asarray( i.resize(min_shape)) for i in imgs))
          imgs_comb = PIL.Image.fromarray(imgs_comb)
          new_p = '/root/discord/files/nmagik_{0}.png'.format(rand)
          imgs_comb.save(new_p)
      else:
        i.transform(resize='800x800>')
        i.liquid_rescale(width=int(i.width*0.5), height=int(i.height*0.5), delta_x=1, rigidity=0)
        i.liquid_rescale(width=int(i.width*1.5), height=int(i.height*1.5), delta_x=2, rigidity=0)
        i.resize(i.width, i.height)
        i.save(filename='/root/discord/files/nmagik_{0}.png'.format(rand))
      if len(exif) != 0 and len(str(exif)) <= 2000 and url2 is None:
        await self.bot.say("Exif Data: ```{0}```".format(str(exif)))
      elif url2 is not None and len(exif) != 0 and len(str(exif)) <= 2000 and len(str(exif2)) <= 2000:
          await self.bot.say("Exif Data Image 1: ```{0}```".format(str(exif)))
          await self.bot.say("Exif Data Image 2: ```{0}```".format(str(exif2)))
      elif len(str(exif)) > 2000:
          await self.bot.say("Exif Data too long, truncated")
      else:
          pass
      await self.bot.send_file(ctx.message.channel, '/root/discord/files/nmagik_{0}.png'.format(rand))
      await self.bot.delete_message(x)
      if len(glob.glob("/root/discord/files/magik*")) > 0:
        os.system("rm /root/discord/files/magik*")
      if len(glob.glob("/root/discord/files/nmagik*")) > 0:
        os.system("rm /root/discord/files/nmagik*")
    except Exception as e:
      if type(e).__name__ == "Forbidden":
        await self.bot.say("Sorry, I do not have permission to send files!")
      else:
        await self.bot.say("Invalid or Non-Image!")
      print(e)
 
------------ NEW ------------
 
  @commands.command(pass_context=True, aliases=['imagemagic', 'imagemagick', 'magic', 'magick'])
  async def magik(self, ctx, *urls:str):
    """Apply magik to Image(s)\n .magik image_url or .magik image_url image_url_2"""
    try:
      if len(urls) == 0:
        await self.bot.say(":no_entry: Please input url(s), mention(s) or atachment(s).")
        return
      x = await self.bot.say("ok, processing")
      img_urls = []
      for attachment in ctx.message.attachments:
        img_urls.append(attachment['url'])
      if len(ctx.message.mentions) != 0:
        for mention in ctx.message.mentions:
          img_urls.append(mention.avatar_url)
      for url in urls:
        if url.startswith('<@'):
          continue
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
        i.liquid_rescale(width=int(i.width*0.5), height=int(i.height*0.5), delta_x=1, rigidity=0)
        i.liquid_rescale(width=int(i.width*1.5), height=int(i.height*1.5), delta_x=2, rigidity=0)
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
        for s in exif[x]:
          if len(s) >= 2000:
            continue
          await self.bot.say('**Exif data for image #{0}**\n'.format(str(x))+code.format(s))
      ya.seek(0)
      await self.bot.send_file(ctx.message.channel, ya, filename='magik.png')
      await self.bot.delete_message(x)
    except discord.errors.Forbidden:
      await self.bot.say(":warning: **I do not have permission to send files!**")
    except Exception as e:
      print(e)
      await self.bot.say(e)
      
def setup(bot):
    bot.add_cog(magik(bot))
