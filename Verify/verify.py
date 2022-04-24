import discord
from discord.ext import commands
from datetime import datetime

class verify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def verify(self, ctx):

    # Channel to send Verification Log
        slog = self.bot.get_channel(957672961769361508)
    # Get's user's Server Joined date and Time
        joinat = ctx.author.joined_at.strftime("%A, %B %d %Y @ %I:%M %p")
    # Get's verfication started time
        tnow = datetime.utcnow()
        vfat = tnow.strftime("%A, %B %d %Y @ %I:%M %p")
    # Get the role to add after verification
        mrole = discord.utils.get(ctx.author.guild.roles, id = 947491244882419782)
    # Check's if the user is alread verified
        if mrole in ctx.author.roles:
            embed = discord.Embed(title= "Action Denied", description = "You are already verified in this server!" , color = 0xFF0000)
            await ctx.send(embed=embed)
    # Restricts the command to certain channel
        if ctx.channel.id == 947495082561503293:
        # Send a welcome message
            embed = discord.Embed(title= "Welcome to Sizzly Network" , description = "Thanks for joining with us today, Make sure to read <#947470601038213180>....... Have a great day!", color = 0xB549FC)
            await ctx.author.send(embed=embed)
        # Adds the role to the user
            await ctx.author.add_roles(mrole)

        # Verification Logger 
            embed = discord.Embed(title = "Member has passed the verification", color = 0x43EC5A)
            embed.set_thumbnail(url=ctx.author.avatar)
            embed.add_field(name = "Name", value=f"{ctx.author} ({ctx.author.id})", inline = False)
            embed.add_field(name = "Joined at", value=f"{joinat}")
            embed.add_field(name = "Verified at", value=f"{vfat}")
            await slog.send(embed=embed)
        
    @verify.error
    async def verify_error(self, ctx: commands.Context, error: commands.CommandError):    
    #Returns error message when the user direct message is not open
       await ctx.send(f"{ctx.author.mention}, Make sure to open your direct messages to proceed with verification process.")

def setup(bot):
    bot.add_cog(verify(bot))