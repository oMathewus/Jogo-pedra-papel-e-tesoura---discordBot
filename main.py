import discord
from discord.ext import commands, tasks

bot = commands.Bot("Seu prefixo")


pedra = "✊"
tesoura = "✌️"
papel = "✋"
@bot.command()
async def ppt(ctx, *, member:discord.Member=None):
    escolha_member = None
    escolha_author = None
    
    if member == None:
        embed = discord.Embed(
            title='Pedra, papel e tesoura',
            color=0x2faed,
            description='Como usar? ``.jogar <usúario>``\n\n📖 Exemplo: ``.jogar @matheus``'
        )
        await ctx.send(embed=embed)
    else:
        jogo = discord.Embed(
            title='Pedra, papel tesoura',
            color = discord.Color.dark_gold(),
            description='Faça sua escolha reagindo a baixo!'
        )      

        jogar = await ctx.author.send(embed=jogo)
        jogo = await member.send(embed=jogo)
        dm = await ctx.send('Olhem a dm de vocês enviei uma coisa..')


        await jogo.add_reaction("✊")
        await jogo.add_reaction("✋")
        await jogo.add_reaction("✌️")

        await jogar.add_reaction("✊")
        await jogar.add_reaction("✋")
        await jogar.add_reaction("✌️")

        await dm.add_reaction("👀")
       
        

    def check(reaction, user):
        return user in [ctx.author, member] and str(reaction.emoji) in [pedra, papel, tesoura]

    while True:
        try:
            reaction, user = await bot.wait_for("reaction_add", timeout=60, check=check)

        except asyncio.TimeoutError:
            await message.delete()
            break

        else:
            if user == member: #verificando as escolhas
                escolha_member = str(reaction.emoji)
            else:
                escolha_author = str(reaction.emoji)

            if escolha_member is not None and escolha_author is not None:
                embed20 = discord.Embed(
                title='Quem ganhou?',
                color= discord.Color.dark_gold(),
                description=f'{ctx.author.mention} jogou: {escolha_author} {member.mention} jogou: {escolha_member}'
            )
                await ctx.send(embed=embed20)
                await dm.delete()
                break



bot.run("Token do seu bot")