# Bot code: NzIwMjA3MDUxMjg0MDIxMjkx.XuCnFQ.ZAibhUYqmEC2l3Ah9sA3djtVPkc
import discord

client = discord.Client()
token = 'NzIwMjA3MDUxMjg0MDIxMjkx.XuCnFQ.ZAibhUYqmEC2l3Ah9sA3djtVPkc'
default_call = '='
authorised = ['GoldenDNA#1938', 'ylq#9769']
num = 16
txt = ''
player = ''
channel = ''


class word:
    def __init__(self, text):
        self.word = text
        self.enter = ""`
        self.ans = ""

    def startswith(self, entered):
        self.enter = str(entered)
        for i in range(len(self.enter)):
            try:
                if self.enter[i] != self.word[i]:
                    return False
            except:
                return False
        return True

    def clearfront(self, entered):
        self.ans = ""
        self.enter = int(entered)
        self.word = list(self.word)
        if len(self.word) >= self.enter + 1:
            for i in range(self.enter):
                self.word.pop(0)
            for i in range(len(self.word)):
                self.ans += self.word[i]
            self.word = self.ans
            return self.word
        else:
            pass

    def clearback(self, entered):
        self.ans = ""
        self.enter = int(entered)
        self.word = list(self.word)
        if len(self.word) >= self.enter + 1:
            for i in range(self.enter):
                self.word.pop(len(self.word) - 1)
            for i in range(len(self.word)):
                self.ans += self.word[i]
            self.word = self.ans
            return self.word
        else:
            pass


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    global txt, num, channel, player
    if message.author.bot:
        return

    if message.content.startswith(str(default_call) + "setchannel "):
        if str(message.author) in authorised:
            txt = word(str(message.content))
            txt.clearfront(13 + len(str(default_call)))
            txt.clearback(1)
            try:
                if not channel == int(txt.word):
                    num = 0
                    player = ''
                    channel = client.get_channel(int(txt.word))
                    await channel.send('```Counting starts here!```')
                    channel = int(txt.word)
                    return
                else:
                    await message.channel.send("```You are already counting at that channel!```")
                    return
            except:
                await message.channel.send("```That channel id does not exist```")
        else:
            await message.channel.send("```You do not have the permission to do that!```")
    elif message.content:
        try:
            txt = word(str(message.content))
            txt = int(txt.word)
            if channel == message.channel.id:
                if player != str(message.author):
                    if txt == num + 1:
                        num += 1
                        player = str(message.author)
                        await message.add_reaction("✅")
                        return
                    else:
                        await message.delete()
                        await message.channel.send("```" + str(message.author) + ", you were supposed to type " + str(num + 1) + "!```")
                        message.delete()
                        return
                else:
                    await message.delete()
                    await message.channel.send("```You cannot be the one counting for the next number, " + str(message.author) + "!```")
                    return
        except ValueError:
            return

client.run(token)
