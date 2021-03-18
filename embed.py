import discord
import datetime
import time
import asyncio
import os
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
    print("봇이 성공적으로 실행되었습니다.")
    game = discord.Streaming(name="BC ClaN 문의", url='https://www.twitch.tv/bc-clan')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("/색깔"):
        await message.channel.send('`빨강` `주황` `노랑` `초록` `파랑` `보라` `분홍` `검정` `민트` `하늘` `갈색` `회색` `남색`')

    if message.content.startswith("/임베드"):
        if message.content[5:7] == '빨강':
            selcolor = 0xFF0000
        if message.content[5:7] == '주황':
            selcolor = 0xFF8C00
        if message.content[5:7] == '노랑':
            selcolor = 0xFFDC37
        if message.content[5:7] == '초록':
            selcolor = 0x00FC08
        if message.content[5:7] == '파랑':
            selcolor = 0x006AFF
        if message.content[5:7] == '보라':
            selcolor = 0x9932CC
        if message.content[5:7] == '분홍':
            selcolor = 0xFF00FF
        if message.content[5:7] == '검정':
            selcolor = 0x000000
        if message.content[5:7] == '민트':
            selcolor = 0x00FFDD
        if message.content[5:7] == '하늘':
            selcolor = 0x3CFBFF
        if message.content[5:7] == '갈색':
            selcolor = 0x8B4F1D
        if message.content[5:7] == '회색':
            selcolor = 0x828282
        if message.content[5:7] == '남색':
            selcolor = 0x3700FF

        value = message.content[8:]
        embed = discord.Embed(color=selcolor)
        embed.add_field(name="\u200b", value=value, inline=False)
        embed.set_author(name="BC ClaN", icon_url=message.author.avatar_url)

        await message.channel.send(embed=embed)
        await message.delete()

    if message.content.startswith("/경고"):
        n = message.content[4:5]
        men = message.author
        user = message.content[6:28]
        reason = message.content[28:]
        
        embed = discord.Embed(color=0xFF0000)
        embed.add_field(name="\u200b", value=f"+ 디스코드아이디: {user}\n+ 제재 사유 : {reason}\n+ 처리 사항 : 경고 {n}회\n+ 해제 날짜 : 영구\n+ 처리자 : {men}", inline=False)
        embed.set_author(name="BC ClaN & TeaM [PUBG] 제재")
        await client.get_channel(693420511463604225).send(embed=embed)

    if message.content.startswith("/밴"):
        men = message.author
        user = message.content[3:25]
        reason = message.content[25:]
        
        embed = discord.Embed(color=0xFF0000)
        embed.add_field(name="\u200b", value=f"+ 디스코드아이디: {user}\n+ 제재 사유 : {reason}\n+ 처리 사항 : 밴\n+ 해제 날짜 : 영구\n+ 처리자 : {men}", inline=False)
        embed.set_author(name="BC ClaN & TeaM [PUBG] 제재")
        await client.get_channel(693420511463604225).send(embed=embed)

    if message.content == '/내정보':
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        await message.channel.send(f"{message.author.mention}의 가입일 : {date.year}년/{date.month}월/{date.day}일/{date.hour}시/{date.minute}분/{date.second}초")
        await message.channel.send(f"```# {user}\n* 닉네임 :{user.display_name}\n{user.name}의 이름 : {user.name} \n아이디 : {user.id} \n닉네임 : {user.display_name}```")
        await message.channel.send(message.author.avatar_url)

    if message.content.startswith("/청소"):
        number = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)
        time.sleep(1)
        embed = discord.Embed(color=0x9932CC)
        embed.add_field(name="\u200b", value=f"{number}개의 메시지가 삭제되었습니다.", inline=False)
        embed.set_author(name="BC ClaN 메시지 삭제")

        await message.channel.send(embed=embed)
        time.sleep(10)

    if message.content.startswith("/공지등록"):
        msg = message.content[6:]
        embed = discord.Embed(color=0x9932CC)
        embed.add_field(name="\u200b", value=msg, inline=False)
        embed.set_author(name="BC ClaN & TeaM [PUBG] 공지사항")
        embed.set_footer(text="공지사항 숙지 부탁드립니다.")

        await client.get_channel(703584991753273354).send(embed=embed)

    if message.content.startswith("/채널생성"):
        cc = message.content[5:]
        channel = await message.guild.create_text_channel(f"{message.author}")

    if message.content.startswith("/클랜가입"):
        embed = discord.Embed(color=0x9932CC)
        embed.add_field(name="\u200b", value=f"클랜 가입을 하시려면 아래 설문지를 작성하셔야 합니다.", inline=False)
        embed.set_author(name="BC ClaN & TeaM 가입 신청")
        embed.set_footer(text="질문은 3초뒤에 나타납니다.")
        await message.channel.send(embed=embed)
        time.sleep(2)
        embed = discord.Embed(color=0x9932CC)
        embed.add_field(name="\u200b", value=f"```지원 플랫폼 [ KaKao / Steam ] : \n배그 닉네임 : \n디스코드이름#태그 : \n본인이 속해 있던 팀 또는 클랜 : \n인게임 닉변 여부 : \n짧은 각오 : ```", inline=False)
        embed.set_author(name="BC ClaN & TeaM 가입하기")
        time.sleep(10)
        await message.channel.send(embed=embed)

    if '지원 플랫폼 [ KaKao / Steam ] : KaKao' in message.content:
        if message.channel.id == 815538292379353119:
            member = message.author
            embed = discord.Embed(color=0x9932CC)
            embed.add_field(name="\u200b", value=f"클랜 가입 단계가 얼마 남지 않았어요!\nDiscord : https://discord.gg/ZwGAM8F /n KaKaoTalk : https://open.kakao.com/o/gThPJV9b 비밀번호 : BCCLAN\n접속 부탁드립니다.", inline=False)
            embed.set_author(name="BC ClaN & TeaM 가입 신청 ")
            embed.set_footer(text="아래 링크 접속 부탁드립니다.")
            await message.channel.send(embed=embed)
            guild = client.get_guild(693311983629369346)
            role = guild.get_role(815190273898184714)
            role2 = guild.get_role(705540156274507787)
            await message.author.add_roles(role)
            await message.author.remove_roles(role2)
            await message.delete()
    if '지원 플랫폼 [ KaKao / Steam ] : 카카오' in message.content:
        if message.channel.id == 815538292379353119:
            member = message.author
            embed = discord.Embed(color=0x9932CC)
            embed.add_field(name="\u200b", value=f"클랜 가입 단계가 얼마 남지 않았어요!\nDiscord : https://discord.gg/ZwGAM8F /n KaKaoTalk : https://open.kakao.com/o/gThPJV9b 비밀번호 : BCCLAN\n접속 부탁드립니다.", inline=False)
            embed.set_author(name="BC ClaN & TeaM 가입 신청 ")
            embed.set_footer(text="아래 링크 접속 부탁드립니다.")
            await message.channel.send(embed=embed)
            guild = client.get_guild(693311983629369346)
            role = guild.get_role(815190273898184714)
            role2 = guild.get_role(705540156274507787)
            await message.author.add_roles(role)
            await message.author.remove_roles(role2)
            await message.delete()

    if '지원 플랫폼 [ KaKao / Steam ] : Steam' in message.content:
        if message.channel.id == 815538292379353119:
            member = message.author
            embed = discord.Embed(color=0x9932CC)
            embed.add_field(name="\u200b", value=f"클랜 가입 단계가 얼마 남지 않았어요!\nDiscord : https://discord.gg/ZwGAM8F/nKaKaoTalk : https://open.kakao.com/o/gThPJV9b 비밀번호 : BCCLAN\n접속 부탁드립니다.", inline=False)
            embed.set_author(name="BC ClaN & TeaM 가입 신청 ")
            embed.set_footer(text="아래 링크 접속 부탁드립니다.")
            await message.channel.send(embed=embed)
            guild = client.get_guild(693311983629369346)
            role = guild.get_role(815190058825941004)
            role2 = guild.get_role(705540156274507787)
            await message.author.add_roles(role)
            await message.author.remove_roles(role2)
                
    if '지원 플랫폼 [ KaKao / Steam ] : 둘다' in message.content:
        if message.channel.id == 815538292379353119:
            member = message.author
            embed = discord.Embed(color=0x9932CC)
            embed.add_field(name="\u200b", value=f"클랜 가입 단계가 얼마 남지 않았어요!\nDiscord : https://discord.gg/ZwGAM8F/nKaKaoTalk : https://open.kakao.com/o/gThPJV9b 비밀번호 : BCCLAN\n접속 부탁드립니다.", inline=False)
            embed.set_author(name="BC ClaN & TeaM 가입 신청 ")
            embed.set_footer(text="아래 링크 접속 부탁드립니다.")
            await message.channel.send(embed=embed)
            guild = client.get_guild(693311983629369346)
            role = guild.get_role(815190058825941004)
            role2 = guild.get_role(705540156274507787)
            role3 = guild.get_role(815190273898184714)
            await message.author.add_roles(role)
            await message.author.add_roles(role3)
            await message.author.remove_roles(role2)

    if '지원 플랫폼 [ KaKao / Steam ]' in message.content:
        if message.channel.id == 815538292379353119:
            member = message.author
            message = message.content[0:]
            embed = discord.Embed(color=0x9932CC)
            embed.add_field(name="\u200b", value=f"```{message}```\n{member.mention}", inline=False)
            embed.set_author(name="BC ClaN & TeaM 가입 신청 ")
            embed.set_footer(text=f"{member.mention}님이 작성하셨습니다.")
            await client.get_channel(815949635625418762).send(embed=embed)
            
       
access_token = os.environ['BOT_TOKEN']
client.run(access_token)
