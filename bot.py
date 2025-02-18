import discord
from discord import Intents

intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Online")

client.run("MTM0MTM4NzQ0Mzc5ODE0NzE3Mg.GGviXe.6hQZ5YPDRHo3SxRvttff1tD3694KIG0PYsaFsU")



import discord
from discord.ext import commands

# 봇 토큰 입력
TOKEN = 'MTM0MTM4NzQ0Mzc5ODE0NzE3Mg.GGviXe.6hQZ5YPDRHo3SxRvttff1tD3694KIG0PYsaFsU'

intents = discord.Intents.default()
intents.message_content = True

# 봇의 접두어 설정
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

# !공지 명령어 구현
@bot.command()
async def 공지(ctx, 시간, 주최자, 훈련종류, *, 기타):
    # 공지가 들어갈 채널 이름
    channel_name = '╠⚾﹕훈련일정'
    
    # 채널 찾기
    channel = discord.utils.get(ctx.guild.text_channels, name=channel_name)
    
    if channel:
        # 임베드 메시지 생성
        embed = discord.Embed(
            title="LG TWINS 훈련 공지", 
            description="LG 트윈스 훈련,가급적 참여부탁드립니다.",
            color=discord.Color.red()  # 임베드 색상 설정
        )
        embed.add_field(name="시간", value=시간, inline=False)
        embed.add_field(name="주최자", value=주최자, inline=False)
        embed.add_field(name="훈련종류", value=훈련종류, inline=False)
        embed.add_field(name="기타", value=기타, inline=False)
        
        # 임베드를 채널에 전송
        await channel.send(embed=embed)
        
        # @선수단ㆍPlayer 역할을 찾고, 언급
        role = discord.utils.get(ctx.guild.roles, name="선수단ㆍPlayer")
        if role:
            await channel.send(f"{role.mention}")  # 역할 언급
        
        await ctx.send(f"공지사항이 {channel.mention}에 전송되었습니다.")
    else:
        await ctx.send(f"{channel_name} 채널을 찾을 수 없습니다.")

# 봇 실행
bot.run(TOKEN)
