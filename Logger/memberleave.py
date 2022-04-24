import discord
from discord.ext import commands, tasks
from datetime import datetime, date


class memberleave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        # Channel to send Member Leave Message
            wmssg = self.bot.get_channel(947470937450762320) 
        # Channel to send Member Leave Server Log  
            slog = self.bot.get_channel(957672961769361508)
        # Get's user's Server Joined date and Time
            joinat = member.joined_at.strftime("%A, %B %d %Y @ %I:%M %p")
        # Get's user's Server left date and Time
            leftat = tnow.strftime("%A, %B %d %Y @ %I:%M %p")
        # Get's user's Account Creation Date and Time
            acrtd = member.created_at.strftime("%A, %B %d %Y @ %I:%M %p")

        # Member Leave  Message
            embed = discord.Embed(title= "Member Left the Server", description=f"{member.mention} has left the server , Hope they will join us again and wish them to have a good day! ", color = 0xFA207F)
            embed.set_thumbnail(url=member.guild.icon)
            await wmssg.send(embed=embed)
    
        # Member Leave Server Log
            embed = discord.Embed(title="Member Left - Info", description=f"{member.mention} left the server", color = 0xFB0839)
            embed.set_thumbnail(url=member.avatar)
            embed.add_field(name = "Name", value = f"{member} ({member.id})", inline = False)
            embed.add_field(name = "Joined at", value= f"{joinat}", inline = False)
            embed.add_field(name = "Left at", value = f"{leftat}", inline = False)
            embed.add_field(name = "Account created at", value = f"{acrtd}", inline = False)
            embed.add_field(name = "New Member Count", value= f"{member.guild.member_count} Members")

            await slog.send(embed=embed)


def setup(bot):
    bot.add_cog(memberleave(bot))