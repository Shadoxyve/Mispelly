import discord
from discord.ext import commands, tasks
from datetime import datetime


class memberjoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        # Channel to send Member Join Welcome Message
            wmssg = self.bot.get_channel(947470937450762320) 
        # Channel to send Member Join Server Log  
            slog = self.bot.get_channel(957672961769361508)
        # Get's user's Server Joined date and Time
            joinat = member.joined_at.strftime("%A, %B %d %Y @ %I:%M %p")
        # Get's user's Account Creation Date and Time
            acrtd = member.created_at.strftime("%A, %B %d %Y @ %I:%M %p")

        # Member Join Welcome Message
            embed = discord.Embed(title= "New Member Joined", description=f"Welcome {member.mention} , Thanks for joining with us today..... We hope that you will be having a great time here!", color = 0x29AB87)
            embed.set_thumbnail(url=member.guild.icon)
            await wmssg.send(embed=embed)
         
        # Member Join Server Log
            embed = discord.Embed(title="New member Joined - Info", description=f"{member.mention} joined the server", color = 0x2FEE62)
            embed.set_thumbnail(url=member.avatar)
            embed.add_field(name = "Name", value=f"{member} ({member.id})", inline = False)
            embed.add_field(name = "Joined at", value=f"{joinat}", inline = False)
            embed.add_field(name = "Account created at", value=f"{acrtd}", inline = False)
            embed.add_field(name = "New Member Count", value=f"{member.guild.member_count} Members")
            await slog.send(embed=embed)


def setup(bot):
    bot.add_cog(memberjoin(bot))




