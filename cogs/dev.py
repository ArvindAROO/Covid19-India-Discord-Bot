import discord
from discord.ext import commands
import os

class Dev(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['file', 'f'])
    async def file_command(self, ctx):
        if((ctx.author.id == 554876169363652620) or (ctx.author.id == 723377619420184668) or (ctx.author.id == 718845827413442692) or (ctx.author.id == 404597472103759872) or (ctx.author.id == 771985293011058708)):
            await ctx.send("You have clearance")
            with open('alerts.csv', 'r') as fp:
                await self.client.get_channel(841561036305465344).send(file=discord.File(fp, 'alerts.csv'))
            fp.close()
            with open('mypings.csv', 'r') as fp:
                await self.client.get_channel(841561036305465344).send(file=discord.File(fp, 'mypings.csv'))
            fp.close()
        else:
            await ctx.send("You are not authorised to run this command")

    @commands.command(aliases=['guilds'])
    async def guilds_command(self, ctx):
        if((ctx.author.id == 554876169363652620) or (ctx.author.id == 723377619420184668) or (ctx.author.id == 718845827413442692) or (ctx.author.id == 404597472103759872) or (ctx.author.id == 771985293011058708)):
            await ctx.channel.trigger_typing()
            count = 0
            dat = 'SERVER NAME,SERVER ID\n\n'
            guilds_details = await self.client.fetch_guilds(limit=150).flatten()
            for guild_deets in guilds_details:
                dat += f"{guild_deets.name},{guild_deets.id}\n"
                count += 1
            dat += f"\nCOUNT: {count}"
            with open('guilds.csv', 'w+') as fp:
                fp.write(dat)
            await ctx.send("You have clearance")
            await self.client.get_channel(841561036305465344).send(file=discord.File('guilds.csv'))
            fp.close()
            os.remove('guilds.csv')
        else:
            await ctx.send("You are not authorised for this")

    @commands.command(aliases=['announce'])
    async def announce_command(self, ctx, *, msg: str = ''):
        if((ctx.author.id == 554876169363652620) or (ctx.author.id == 723377619420184668) or (ctx.author.id == 718845827413442692) or (ctx.author.id == 404597472103759872) or (ctx.author.id == 771985293011058708)):
            if(msg == ''):
                await ctx.send("Put a message man")
                return
            fp = open('alerts.csv', 'r')
            ch_list = [line.split(',')[1] for line in list(
                filter(None, fp.read().split('\n')))]
            for ch in ch_list:
                await self.client.get_channel(int(ch)).send(f"**NEW ALERT FROM THE DEVS**\n\n{msg}")
            await ctx.send("Announcement sent")
            fp.close()
        else:
            await ctx.send("You don't have permission to execute this command")



def setup(client):
    client.add_cog(Dev(client))