from redbot.core import commands, cog_manager
import random, discord, json

class RandomNoa(commands.Cog):
    """Sends a random Noa card from the official D4DJ Groovy Mix game."""

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def randomnoa(self, ctx):
        cm = cog_manager.CogManager()
        ipath = str(await cm.install_path())
        cards = json.load(open(ipath + "/randomnoa/cards.json", "r"))
        noachoice = 8

        if noachoice == 1:
            embed=discord.Embed(title="Random Noa generated!", description="Card Name: Uniform \n Rarity: 1⭐ \n Untrained or Trained: None \n ", color=await ctx.embed_color())
            embed.set_image(url=cards[noachoice-1])
            await ctx.send(embed=embed)

        elif noachoice == 2:
            embed=discord.Embed(title="Random Noa generated!", description="Card Name: DJ-LIVE! \n Rarity: 2⭐\n Untrained or Trained: None \n ", color=await ctx.embed_color())
            embed.set_image(url=cards[noachoice-1])
            await ctx.send(embed=embed)

        elif noachoice == 3:
            embed=discord.Embed(title="Random Noa generated!", description="Card Name: DJ-MIX! \n Rarity: 2⭐\n Untrained or Trained: None \n ", color=await ctx.embed_color())
            embed.set_image(url=cards[noachoice-1])
            await ctx.send(embed=embed)

        elif noachoice == 4:
            embed=discord.Embed(title="Random Noa generated!", description="Card Name: CuteBringer \n Rarity: 3⭐\n Untrained or Trained: Untrained \n ", color=await ctx.embed_color())
            embed.set_image(url=cards[noachoice-1])
            await ctx.send(embed=embed)
        
        elif noachoice == 5:
            embed=discord.Embed(title="Random Noa generated!", description="Card Name: CuteBringer \n Rarity: 3⭐\n Untrained or Trained: Trained \n ", color=await ctx.embed_color())
            embed.set_image(url=cards[noachoice-1])
            await ctx.send(embed=embed)

        elif noachoice == 6:
            embed=discord.Embed(title="Random Noa generated!", description="Card Name: CuteBringer \n Rarity: 3⭐\n Untrained or Trained: Trained \n ", color=await ctx.embed_color())
            embed.set_image(url=cards[noachoice-1])
            await ctx.send(embed=embed)

        elif noachoice == 7:
            embed=discord.Embed(title="Random Noa generated!", description="Card Name: CuteBringer \n Rarity: 3⭐\n Untrained or Trained: Trained \n ", color=await ctx.embed_color())
            embed.set_image(url=cards[noachoice-1])
            await ctx.send(embed=embed)

        elif noachoice == 8:
            embed=discord.Embed(title="Random Noa generated!", description="Card Name: Melty Smile \n Rarity: 3⭐\n Untrained or Trained: Untrained \n ", color=await ctx.embed_color())
            embed.set_image(url=cards[noachoice-1])
            await ctx.send(embed=embed)

        else:
            embed=discord.Embed(title="Is that.... a prank?", description="Card Name: Pingu Hitting Those Moves \n Rarity: 20⭐ \n Untrained or Trained: Trained (obviously?) \n ", color=await ctx.embed_color())
            embed.set_image(url=" https://c.tenor.com/wuyEcsxrvQwAAAAC/club-penguin-ghosthy.gif ")
            await ctx.send(embed=embed)
