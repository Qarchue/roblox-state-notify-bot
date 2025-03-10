import json
import os
import sys


import requests
import numpy as np

import asyncio
import discord
from typing import Optional
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice
import aiohttp

update_data = False
update_data_lock = asyncio.Lock()

# 取得目前腳本的絕對路徑
current_script_path = os.path.abspath(__file__)
# 取得目前腳本所在的目錄
current_script_dir = os.path.dirname(current_script_path)
# 取得父目錄
parent_dir = os.path.dirname(current_script_dir)

#print("目前腳本的絕對路徑:", current_script_path)
#print("目前腳本所在的目錄:", current_script_dir)

with open(current_script_dir+'\\configuration\\settings.json',mode='r',encoding='utf8') as jSettings:
    settings = json.load(jSettings)

folder_path = current_script_dir + '\\language'

language_list = {}
language_dict = {}
languages = []

#print(os.listdir(folder_path))
if settings['Default_language']+'.json' in os.listdir(folder_path):
    with open (folder_path+"\\"+settings['Default_language']+'.json', mode='r', encoding='utf-8') as dl:
        dl = json.load(dl)

    key = next(iter(dl))
    Default_language = dl[key]
    language_dict["Default"] = key

    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)

            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

                if set(data).issubset(set(language_list)):

                    print(Default_language['error']['language_repeat'])
                    input(Default_language['error']['error_exit'])
                    sys.exit()

                else:
                    language_list.update(data)
                    key = next(iter(data))
                    language_dict[filename[:-5]] = key
                    languages.append([key,filename[:-5]])

else:   
    print("can't find Default_language")



#print(language_list)
#print(language_dict)
#print(languages)
#print(language_dict)

notify_list = {}



def language_convert(lang):
        return language_list[language_dict[lang]]


update_data = True


intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "!!!", intents = intents)


async def discord_error(dcid,errortype):
    dcuser = bot.get_user(int(dcid))

    sub_file = open(current_script_dir + '\\subscribers\\discord_user.json', mode='r', encoding='utf8')
    subscribers = json.load(sub_file)
    sub_file.close()

    try:
        language = language_convert(subscribers[dcuser.name]['language'])
    except KeyError:
            language = Default_language


    language_error = language['error']

    if errortype == "cookie":
        embed=discord.Embed(title=language_error['Invalid_cookie2'], color=0xff0000)
        await dcuser.send(embed=embed)


@bot.event
async def on_ready():
    slash = await bot.tree.sync()
    print(f"Current login identity --> {bot.user}")
    print(f"load {len(slash)} commands")
    asyncio.create_task(main())  # 讓 main() 成為背景任務
    # bot.loop.create_task(main())

    
class RobloxAPI:

    def get_user_id(name):
        try:
            x = requests.post(
                "https://users.roblox.com/v1/usernames/users",
                json={"usernames":[name]},
                cookies={},
            )
        except:
            return None
        
        if not(len(x.json()["data"])):
            return None

        return x.json()["data"][0]["id"]
    
    def get_username(user_id):
        data = requests.get(f"https://users.roblox.com/v1/users/{user_id}").json()
        return data["name"]
  
    def authenticate_cookie(cookie):
        try:
            id = requests.get("https://users.roblox.com/v1/users/authenticated",cookies={".ROBLOSECURITY": cookie}).json()['id']
        except:
            return ""
        else:
            return id

    def get_friends(user_id):
        url = f"https://friends.roblox.com/v1/users/{str(user_id)}/friends"
        response = requests.get(url)
        if response.status_code == 200:
            friends_data = response.json()
            friends_list = [friend['id'] for friend in friends_data['data']]
            return friends_list
        else:
            #print(f"Failed to get friends. Status code: {response.status_code}")
            return []

    def get_usericon(userid):
        try:
            usericon = requests.get(url = f"https://thumbnails.roblox.com/v1/users/avatar-bust?userIds={userid}&size=50x50&format=Png&isCircular=true").json()['data'][0]['imageUrl']
        except:
            return ""
        else:
            return usericon


async def rp():#requests planning
    sub_file = open(current_script_dir + '\\subscribers\\discord_user.json', mode='r', encoding='utf8')
    subscribers = json.load(sub_file)
    sub_file.close()

    
    notify_ts = {}


    for subscriber in subscribers:
        i = subscribers[str(subscriber)]
        if i['cookie'] != "":
            robloxid = RobloxAPI.authenticate_cookie(i['cookie'])
            if robloxid != "":
                totalsub = np.array(i['sub_users'][1]+i['sub_users'][0])
                cdg = np.intersect1d(totalsub, np.array(RobloxAPI.get_friends(i['robloxid'])))

                subscribers[str(subscriber)]['sub_users'][0] = cdg.tolist()
                subscribers[str(subscriber)]['sub_users'][1] = np.setdiff1d(totalsub, cdg).tolist()
                subscribers[str(subscriber)]['robloxid'] = robloxid

                if robloxid in subscribers[str(subscriber)]['sub_users'][1]:
                    subscribers[str(subscriber)]['sub_users'][1].remove(robloxid)
                    
            else:
                subscribers[str(subscriber)]['cookie'] = ""
                subscribers[str(subscriber)]['sub_users'][1] = subscribers[str(subscriber)]['sub_users'][1]+subscribers[str(subscriber)]['sub_users'][0]
                subscribers[str(subscriber)]['sub_users'][0] = []
                await discord_error(subscribers[str(subscriber)]['dcid'], "cookie")
        else:
            subscribers[str(subscriber)]['sub_users'][1] = subscribers[str(subscriber)]['sub_users'][1]+subscribers[str(subscriber)]['sub_users'][0]
            subscribers[str(subscriber)]['sub_users'][0] = []
            subscribers[str(subscriber)]['robloxid'] = ""

    global notify_list
    for subscriber in subscribers:
        i = subscribers[str(subscriber)]
        notify_ts[i['dcid']] = [i['language'],i['sub_users']]
    notify_list.update(notify_ts)



    sub_file = open(current_script_dir + '\\subscribers\\discord_user.json', mode='w+', encoding='utf8')
    json.dump(subscribers, sub_file, ensure_ascii=False, indent=4)
    sub_file.close()

    subscribers_user_list = []
    total_user_list = [[],[]]

    for subscriber in subscribers:
        i = subscribers[str(subscriber)]
        total_user_list[0] += i['sub_users'][0]
        total_user_list[1] += i['sub_users'][1]

    total_user_list[0] = np.array(list(set(total_user_list[0])))#total_user_list[0]是能夠查到的玩家的總表
    total_user_list[1] = np.setdiff1d(total_user_list[1], total_user_list[0])#total_user_list[1]是不能查到的玩家的總表

    for subscriber in subscribers:#玩家要求表
        i = subscribers[str(subscriber)]
        n = [np.intersect1d(total_user_list[0], np.array(RobloxAPI.get_friends(i['robloxid']))),i['cookie'],i['robloxid'],i['dcid']]


        subscribers_user_list.append(n)


    ans = []

    tul = total_user_list

    sul = subscribers_user_list

    #print(tul[0])
    while len(tul[0])!=0:#這段是處理能查到遊戲的部分
        sortr = []

        # 計算重複字元數
        for i in sul:
            sortr.append([np.sum(np.isin(i[0], tul[0])),i[0],i[1],i[2],i[3]])
            #[數量排名,要偵測的玩家列,cookie,使用者robloxid]
                
        sortr = sorted(sortr, key=lambda x: x[0], reverse=True)#已數量排名來排序

        show = np.intersect1d(tul[0], sortr[0][1])#sortr在tul內的

        tul[0] = np.setdiff1d(tul[0], sortr[0][1])#從總表中減去
        
        ans.append([show.tolist(),sortr[0][2],sortr[0][3],sortr[0][4]])#新增至return的串列中


    if tul[1].tolist() != []:
        ans.append([tul[1].tolist(),None,None,None]) #加上查不到遊戲的

    return ans





async def player_presence_processing(f_data,last_data):
    global notify_list

    universeId = f_data['universeId']
    lastuniverseId = last_data['universeId']

    Presence = f_data['userPresenceType']
    lastPresence = last_data['userPresenceType']

    userid = f_data['userid']
    username = RobloxAPI.get_username(userid)
    usericon = RobloxAPI.get_usericon(userid)

    message = []
    message_color_list = {
        "Going_offline":0x7C7C7C,
        "Coming_online":0x00A2FF,
        "Entering_the_game":0x02B757,
        "Entering_studio":0xF68802,
        "Exiting_game":0x00A2FF,
        "Exiting_studio":0x00A2FF
    }

    if Presence == 0:
        if lastPresence == 2:
            message.append('Exiting_game')
        elif lastPresence == 3:
            message.append('Exiting_studio')

        message.append('Going_offline')



    elif Presence == 1:
        if lastPresence == 0:
            message.append('Coming_online')
        elif lastPresence == 1:
            message.append('Entering_the_game')
        elif lastPresence == 2:
            message.append('Exiting_game')
        elif lastPresence == 3:
            message.append('Exiting_studio')


    elif Presence == 2:
        if lastPresence == 0:
            message.append('Coming_online')
        elif lastPresence == 2:
            message.append('Exiting_game')

        message.append('Entering_the_game')

        if universeId:
            gameinfo = requests.get(url = f"https://thumbnails.roblox.com/v1/games/multiget/thumbnails?universeIds={universeId}&size=768x432&format=Png&isCircular=false").json()

            placeid = gameinfo['data'][0]['thumbnails'][0]['targetId']
            imageUrl = gameinfo['data'][0]['thumbnails'][0]['imageUrl']

            x = requests.get(url = f"https://games.roblox.com/v1/games?universeIds={universeId}")
            gamename = x.json()['data'][0]['name']
            gamelink = f"https://www.roblox.com/games/{x.json()['data'][0]['rootPlaceId']}"

    elif Presence == 3:
        if lastPresence == 0:
            message.append('Coming_online')

        elif lastPresence == 2:
            message.append('Exiting_game')

        message.append('Entering_the_studio')


    for subscriber in notify_list:
        i = notify_list[subscriber]
        lang = language_convert(i[0])
        dcuser = bot.get_user(subscriber)

        if userid in i[1][0]:
            for msg in message:
                embed=discord.Embed(title=username+" "+lang['presence'][msg], color=message_color_list[msg])
                embed.set_thumbnail(url = usericon)
                await dcuser.send(embed=embed)
            if universeId:
                embed=discord.Embed(title=gamename, url=gamelink, color=message_color_list['Entering_the_game'])
                embed.set_image(url = imageUrl)
                await dcuser.send(embed=embed)

        elif userid in i[1][1]:
            for msg in message:
                embed=discord.Embed(title=username+" "+lang['presence'][msg], color=message_color_list[msg])
                embed.set_thumbnail(url = usericon)
                await dcuser.send(embed=embed)


@bot.tree.command(name = "sublist", description = Default_language['discord']['sublist']['description'])
async def sublist(interaction: discord.Interaction):


    sub_file = open(current_script_dir + '\\subscribers\\discord_user.json', mode='r', encoding='utf8')
    subscribers = json.load(sub_file)
    sub_file.close()

    dcuser = interaction.user
    channel= interaction.channel

    try:
        language = language_convert(subscribers[dcuser.name]['language'])
    except KeyError:
            language = Default_language

    language_sl = language['discord']['sublist']
    language_error = language['error']


    if dcuser.name not in subscribers:
        subscribers[dcuser.name] = {
            "dcid":dcuser.id,
            "robloxid":"",
            "language":"Default",
            "cookie":"",
            "sub_users":[[],[]]
        }

    await interaction.response.send_message(language_sl['start'][0], ephemeral=True)

    try:
        embed=discord.Embed(title=language_sl['start'][1], color=0x00ff00)
        sl_log = await dcuser.send(embed=embed)

    except discord.Forbidden:
        await interaction.edit_original_response(content=language_error['user_send_error'])
        #await interaction.followup.send("無法向您發送私訊。請確保您的私訊設置允許接收來自服務器成員的消息。", ephemeral=True)
    else:
        await interaction.edit_original_response(content=language_sl['user_send'])

    if subscribers[dcuser.name]['sub_users'] == [[],[]]:
        embed.add_field(name=language_sl['nosub'][0], value=language_sl['nosub'][1], inline=False)
        await sl_log.edit(embed=embed)

    else:
        for i in subscribers[dcuser.name]['sub_users'][0]:
            embed.add_field(name=f" - {RobloxAPI.get_username(i)}", value=f"[{language_sl['profile']}](https://www.roblox.com/users/{i}/profile/)", inline=False)
            await sl_log.edit(embed=embed)
        for i in subscribers[dcuser.name]['sub_users'][1]:
            embed.add_field(name=f" - {RobloxAPI.get_username(i)}", value=f"[{language_sl['profile']}](https://www.roblox.com/users/{i}/profile/)", inline=False)
            await sl_log.edit(embed=embed)




@bot.tree.command(name = "setting", description = Default_language['discord']['settings']['description'])
@app_commands.describe(lang = Default_language['discord']['settings']['language'], cookies = Default_language['discord']['settings']['cookies'])
@app_commands.choices(lang = [Choice(name = i[0], value = i[1]) for i in languages])
async def setting(interaction: discord.Interaction, lang: Optional[str] = None, cookies: Optional[str] = None):

    global update_data
    error_len = 0


    sub_file = open(current_script_dir + '\\subscribers\\discord_user.json', mode='r', encoding='utf8')
    subscribers = json.load(sub_file)
    sub_file.close()
    

    dcuser = interaction.user
    channel= interaction.channel

    try:
        #print(dcuser.name)
        #print(type(dcuser.name))
        language = language_convert(subscribers[dcuser.name]['language'])
    except KeyError:
            language = Default_language


    language_set = language['discord']['settings']
    language_error = language['error']

    if dcuser.name not in subscribers:
        subscribers[dcuser.name] = {
            "dcid":dcuser.id,
            "robloxid":"",
            "language":"Default",
            "cookie":"",
            "sub_users":[[],[]]
        }

    await interaction.response.send_message(language_set['start'][0], ephemeral=True)

    try:
        if not(lang) and not(cookies):
            embed=discord.Embed(title=language_set['settings'][0], color=0x00ff00)
        else:
            embed=discord.Embed(title=language_set['start'][1], color=0x00ff00)
        set_log = await dcuser.send(embed=embed)

    except discord.Forbidden:
        await interaction.edit_original_response(content=language_error['user_send_error'])
        #await interaction.followup.send("無法向您發送私訊。請確保您的私訊設置允許接收來自服務器成員的消息。", ephemeral=True)
    else:
        await interaction.edit_original_response(content=language_set['user_send'])



    if cookies:
        robloxid = RobloxAPI.authenticate_cookie(cookies)
        if robloxid == "":
            cookies = None
            cookiemsg = language_error['Invalid_cookie']
            error_len += 1

        else:
            if subscribers[dcuser.name]['cookie'] == "":
                cookiemsg = language_set['cookie_update'][0]

            else:
                cookiemsg = language_set['cookie_update'][1]

            subscribers[dcuser.name]['cookie'] = cookies

        embed.add_field(name=cookiemsg, value="", inline=False)
    


    if lang:
        subscribers[dcuser.name]['language'] = lang
        embed.add_field(name=language_set['lang_update'], value="", inline=False)



    if not(lang) and not(cookies):
        embed.add_field(name=f"{language_set['settings'][1]}:\n    {language_dict[subscribers[dcuser.name]['language']]}", value="", inline=False)
    else:
        embed.title = language_set['set_finish']


    await set_log.edit(embed=embed)

    sub_file = open(current_script_dir + '\\subscribers\\discord_user.json', mode='w+', encoding='utf8')
    json.dump(subscribers, sub_file, ensure_ascii=False, indent=4)
    sub_file.close()

    update_data = True



@bot.tree.command(name = "sub", description = Default_language['discord']['sub']['description'])
@app_commands.describe(user = Default_language['discord']['sub']['user'], cookies = Default_language['discord']['sub']['cookies'])
async def sub(interaction: discord.Interaction, user: str, cookies: Optional[str] = None):

    

    global update_data
    error_len = 0


    sub_file = open(current_script_dir + '\\subscribers\\discord_user.json', mode='r', encoding='utf8')
    subscribers = json.load(sub_file)
    sub_file.close()
    
    dcuser = interaction.user
    channel= interaction.channel
    looking_player=list(user.split(" "))


    try:
        language = language_convert(subscribers[dcuser.name]['language'])
    except KeyError:
            language = Default_language

    language_sub = language['discord']['sub']
    language_error = language['error']
    if dcuser.name not in subscribers:

        subscribers[dcuser.name] = {
            "dcid":dcuser.id,
            "robloxid":"",
            "language":"Default",
            "cookie":"",
            "sub_users":[[],[]]
        }


    await interaction.response.send_message(language_sub['start'][0], ephemeral=True)

    try:
        embed=discord.Embed(title=language_sub['start'][1], color=0x00ff00)
        sub_log = await dcuser.send(embed=embed)

    except discord.Forbidden:
        await interaction.edit_original_response(content=language_error['user_send_error'])
        #await interaction.followup.send("無法向您發送私訊。請確保您的私訊設置允許接收來自服務器成員的消息。", ephemeral=True)

    else:
        await interaction.edit_original_response(content=language_sub['user_send'])


    if cookies:
        robloxid = RobloxAPI.authenticate_cookie(cookies)

        if robloxid != "":
            subscribers[dcuser.name]['robloxid'] = robloxid
            if subscribers[dcuser.name]['cookie'] == "":
                cookiemsg = language_sub['cookie_update'][0]

            else:
                cookiemsg = language_sub['cookie_update'][1]

            subscribers[dcuser.name]['cookie'] = cookies


        else:
            cookies = None
            cookiemsg = language_error['Invalid_cookie']
            error_len += 1

        embed.add_field(name=cookiemsg, value="", inline=False)
        robloxid = subscribers[dcuser.name]['robloxid']

    else:
        robloxid = subscribers[dcuser.name]['robloxid']



    for i in looking_player:
        userid = RobloxAPI.get_user_id(i)
        usericon = RobloxAPI.get_usericon(userid)

        if userid:

            if userid != robloxid:

                if userid in subscribers[dcuser.name]['sub_users'][0]:
                    subscribers[dcuser.name]['sub_users'][0].remove(userid)
                    embed.add_field(name=f"{language_sub['sub_remove']}:{i}", value=f"[{language_sub['profile']}](https://www.roblox.com/users/{userid}/profile/)", inline=False)


                elif userid in subscribers[dcuser.name]['sub_users'][1]:
                    subscribers[dcuser.name]['sub_users'][1].remove(userid)
                    embed.add_field(name=f"{language_sub['sub_remove']}:{i}", value=f"[{language_sub['profile']}](https://www.roblox.com/users/{userid}/profile/)", inline=False)


                else:
                    subscribers[dcuser.name]['sub_users'][1].append(userid)
                    embed.add_field(name=f"{language_sub['sub_add']}:{i}", value=f"[{language_sub['profile']}](https://www.roblox.com/users/{userid}/profile/)", inline=False)

            else:
                embed.add_field(name=language_error['playerisyourself'] % i, value=" - " + i, inline=False)

        else:
            embed.add_field(name=f"{language_error['playernotfound']}{i}", value=" - " + i, inline=False)
            error_len += 1

        await sub_log.edit(embed=embed)

    embed.title = language_sub['sub_finish']
    await sub_log.edit(embed=embed)


    total_len = len(subscribers[dcuser.name]['sub_users'][0]) + len(subscribers[dcuser.name]['sub_users'][1])


    if total_len == 0:
        embed=discord.Embed(title=language_sub['sub_success'][0] + language_sub['sub_success'][1], color=0x00ff00)

    else:
        embed=discord.Embed(title=language_sub['sub_success'][0] + (language_sub['sub_success'][2] % total_len), color=0x00ff00)

    if error_len > 0:
        embed.add_field(name=f"{error_len}{language_error['error_len'][0]}", value=language_error['error_len'][1], inline=False)
    await dcuser.send(embed=embed)


    sub_file = open(current_script_dir + '\\subscribers\\discord_user.json', mode='w+', encoding='utf8')
    json.dump(subscribers, sub_file, ensure_ascii=False, indent=4)
    sub_file.close()

    update_data = True

async def set_update_data(value):
    async with update_data_lock:
        global update_data
        update_data = value

async def fetch_roblox_presence(ids, cookie):
    """ 使用 aiohttp 發送請求，避免同步阻塞 """
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(
                "https://presence.roblox.com/v1/presence/users",
                json={"userIds": ids},
                cookies={".ROBLOSECURITY": cookie} if cookie else {}
            ) as resp:
                return await resp.json()
        except aiohttp.ClientError as e:
            print(f"請求錯誤: {e}")
            return None

async def main():
    global update_data
    await bot.wait_until_ready()  # 確保機器人已準備就緒
    while True:

        await asyncio.sleep(5)  # 避免無窮迴圈卡死 CPU

        column = 0
        if update_data:
            x = await rp()
            last_data = [[] for _ in range(len(x))]
            requests_data = x.copy()
            print(Default_language['data_update'])
            await set_update_data(False)  # 用 set_update_data 來修改變數
        
        for i in requests_data:
            await asyncio.sleep(5)

            ids = i[0]
            cookie = i[1]
            robloxid = i[2]
            dcid = i[3]
            _data = await fetch_roblox_presence(ids, cookie)

            if _data is None:
                await set_update_data(True)
                await asyncio.sleep(10)
                break

            try:
                f_data = [{
                    "userid": item['userId'],
                    "userPresenceType": item['userPresenceType'],
                    "universeId": item['universeId']
                } for item in _data['userPresences']]
            except KeyError as e:
                print(f"解析資料時出錯: {e}")
                await set_update_data(True)
                await asyncio.sleep(10)
                break

            for a in range(len(f_data)):
                if len(last_data[column]) != 0:
                    if f_data[a]['userPresenceType'] != last_data[column][a]['userPresenceType']:
                        print(Default_language['presence_change'])
                        await player_presence_processing(f_data[a], last_data[column][a])

            last_data[column] = f_data.copy()
            column += 1

        

bot.run(settings['TOKEN'])

