# [roblox-state-notify-bot]([https://www.github.com/Qarchue/roblox-state-notify-bot](https://github.com/Qarchue/roblox-state-notify-bot))

<p align="center">
    <a href="https://github.com/Qarchue/roblox-state-notify-bot/blob/master/LICENSE"><img src="https://img.shields.io/github/license/qarchue/roblox-state-notify-bot"></a>
    <a href="https://github.com/Qarchue/roblox-state-notify-bot"><img src="https://img.shields.io/github/repo-size/Qarchue/roblox-state-notify-bot"></a>
    <a href="https://github.com/Qarchue/roblox-state-notify-bot"><img src="https://img.shields.io/github/languages/top/Qarchue/roblox-state-notify-bot"></a>
    <a href="https://github.com/Qarchue/roblox-state-notify-bot/stargazers"><img src="https://img.shields.io/github/stars/Qarchue/roblox-state-notify-bot?style=socia"></a>
    <a href="https://discord.gg/w5CeZh3rNu"><img src="https://img.shields.io/discord/905865794683015208?style=flat-square&logo=Discord&logoColor=white&label=support&color=5865F2"></a>
</p>


> 歡迎將本專案所有或部分程式碼放入你自己的機器人中。

## 簡介

有些玩家上線時不會通知朋友，導致常常錯過一起遊玩的機會。為了解決這個問題，我使用 **Python 3** 開發了一個工具來監視他們的狀態變化，並即時發送通知。

這是一個簡單的小專案，可以監控指定玩家的狀態變化，並通過 Discord 通知您。您還可以設定 Cookie 來查詢更詳細的資訊，例如玩家加入或離開某個遊戲。

該機器人還支援多語言設置，用戶可以根據自己的需求選擇不同的語言接收通知，只需使用指令功能即可切換 `language` 資料夾內已存在的語言。

_本文檔將引導您完成創建 Discord 機器人及使用其功能。_

---





## 展示

![](https://raw.githubusercontent.com/Qarchue/images/master/rpc/說明圖.png)

---





## 支持的平台

|**作業系統**|**支持**|**經過測試**|
|-|:-:|:-:|
|Windows 11|✅|✅|
|Windows 10|✅|✅|
|Linux|❓|❌|
|MacOS|❓|❌|
|Other|❓|❌|

因為時間問題，目前沒有對windows以外的電腦做過測試。

---





## 功能

- [x] 當玩家上線、下線、加入或離開遊戲時，透過 Discord 通知。
- [x] 可動態管理訂閱的玩家，透過簡單指令來增加或移除訂閱。
- [x] 支援 Cookie，用於查詢更詳細的玩家資料。
- [x] 可自訂通知語言，支持不同語言通知。

---





## 使用教學

### 網頁端

需要在此步驟創建機器人並取得 Bot token

<details><summary>>>> 點此查看完整內容 <<<</summary>

1. 到 [Discord Developer](https://discord.com/developers/applications "Discord Developer") 登入 Discord 帳號

![](https://raw.githubusercontent.com/Qarchue/images/master/discord_bot/discord_1.png)

2. 點選「New Application」建立應用，輸入想要的名稱後按「Create」

![](https://raw.githubusercontent.com/Qarchue/images/master/discord_bot/discord_2.png)

3. 在 Bot 頁面，按「Reset Token」來取得機器人的 Token

![](https://raw.githubusercontent.com/Qarchue/images/master/discord_bot/discord_3.png)

4. 第3步驟做完之後在下面將「Presence Intent」「Server Members Intent」「Message Content Intent」的開關打開

![](https://raw.githubusercontent.com/Qarchue/images/master/discord_bot/discord_4.png)

5. 在 OAuth2/URL Generator，分別勾選「bot」「applications.commands」「Send Messages」

![](https://raw.githubusercontent.com/Qarchue/images/master/discord_bot/discord_5.png)

6. 開啟最底下產生的 URL 將機器人邀請至自己的伺服器

![](https://raw.githubusercontent.com/Qarchue/images/master/discord_bot/discord_6.png)

</details>

### 電腦端
1. 下載最新版本的 [Python](https://www.python.org/downloads/)。

2. 從 GitHub 下載此程式檔並解壓縮成資料夾。

3. 在程式資料夾內開啟命令提示字元並安裝依賴 `python3 -m pip install -r requirements.txt`

4. 更改設定，在設定檔中放入剛剛在網頁端取得的 Token 請參考 [設定](#設定)

5. 完成，您可以參考 [指令](#指令) 或是 [語言](#語言) 來使用機器人了

6. 如果您需要查詢好友加入的遊戲，可以參考 [cookies](#cookies) 來設定

---




## 指令

|**指令名稱**|**功能描述**|**範例**|
|-|-|-|
|`/sub`|訂閱特定玩家。<br>若指定的玩家已在訂閱列表內，則刪除該玩家。|`/sub crooked`<br>`/sub Roblox Qarchue`|
|`/setting`|更改設定。<br>若不指定，則顯示當前設定。|`/setting`<br>`/setting lang: zh_tw`<br>`/setting cookies: _\|WARNING:-DO-NOT...`|
|`/sublist`|查看目前訂閱的玩家。|`/sublist`|

|**指令名稱**|**功能描述**|**範例**|
|-|-|-|
|`/sub`|訂閱特定玩家。<br>若指定的玩家已在訂閱列表內，則刪除該玩家。|`/sub crooked`<br>`/sub Roblox Qarchue`|
|`/sublist`|查看目前訂閱的玩家。|`/sublist`|
---





## 設定

以文字編輯器開啟 `configuration` 資料夾內的 `settings.json` 來更改設定   
預設應該長這樣：
```json
{
    "TOKEN": "Discord Bot Token",
    "Default_language": "zh_tw"
}
```
`TOKEN`：填入您在 Discord 開發者平台取得的 Bot Token。  
`Default_language`：預設語言檔名稱。

### 編輯完設定檔後記得儲存

範例:
```json
{
    "TOKEN": "MTI1NDI1NzMwMTA3ODDzNzYwMA.GBxoCb.p6FqVPGvAYznZy6s1N0xKLWMGu5uHEpESvcuBI",
    "Default_language": "en_us"
}
```

---





## 語言

目前 `language` 資料夾中包含以下三個語言檔案，供直接使用或根據需求進行修改：

|**檔案名稱**|**語言名稱**|
|-|-|
|`en_us.json`|英文|
|`zh_tw.json`|繁體中文|
|`lzh.json`|文言文|

在設定中，預設語言為 `zh_tw` ，如果使用者沒有使用 `/settings` 指令來更改語言，則會使用預設語言

預設語言也決定了指令的說明語言，如果您將預設語言設定為 `en_us` 那指令說明將會變為英文

你也可以將預設語言設定為自己增加的語言，只需把 `zh_tw` 改成語言的檔案名


### 增加語言
<details><summary>>>> 點此查看如何增加語言 <<<</summary>

1. 新增一個json檔案，檔案名稱自訂，例如: `test_lang.json`

2. 複製以下格式並貼在json檔內。

3. 將 `(語言名稱)` 更改為想要在程式內顯示的名稱，例如: `測試語言` ，這個名稱不能與現有的語言名稱重複

4. 依照個人需求更改 `""` 內的文字(不要改到 `""` 內只有英文的)

```json
{   
    "(語言名稱)": {
        "title": "roblox玩家狀態檢測機器人",
        "data_update": "資料已更新",
        "presence_change": "檢測到用戶狀態改變",
        "discord": {
            "sub": {
                "1": "---------------指令---------------",
                "description": "訂閱某人的roblox狀態",
                "user": "輸入使用者名稱",
                "cookies": "輸入cookies",
                "2": "---------------訊息---------------",
                "profile": "個人檔案",
                "user_send": "已向您發送私訊。",
                "sub_add": "成功新增使用者",
                "sub_remove": "成功刪除使用者",
                "sub_finish": "更改完成。",
                "3": "---------------list---------------",
                "start": ["開始執行", "正在進行操作"],
                "cookie_update": ["cookie新增成功", "cookie更新成功"],
                "sub_success": ["已完成，", "目前無追蹤任何玩家。", "正在追蹤%s個人的狀態。"]
            },
            "settings": {
                "1": "---------------指令---------------",
                "description": "更改設定",
                "language": "輸入要更改成的語言",
                "cookies": "輸入cookies",
                "2": "---------------訊息---------------",
                "user_send": "已向您發送私訊。",
                "lang_update": "語言更改成功。",
                "set_finish": "設定完成。",
                "3": "---------------list---------------",
                "start": ["開始執行", "正在修改設定"],
                "cookie_update": ["cookie新增成功。", "cookie更新成功。"],
                "settings": ["設定檔", "語言", "cookie"]
            },
            "sublist": {
                "1": "---------------指令---------------",
                "description": "顯示訂閱用戶列表",
                "2": "---------------訊息---------------",
                "profile": "個人檔案",
                "user_send": "已向您發送私訊。",
                "3": "---------------list---------------",
                "start": ["開始執行", "訂閱使用者名單"],
                "cookie_update": ["cookie新增成功", "cookie更新成功"],
                "nosub": ["這裡空空如也", "你沒訂閱玩家"]
            },
            "notify": {
                "gameinfo": "遊戲資訊",
                "gamename": "遊戲名稱",
                "profile": "個人檔案"
            }
        },
        "error": {
            "1": "---------------指令---------------",
            "Invalid_cookie": "cookie錯誤!",
            "language_repeat": "語言名稱重複!",
            "playernotfound": "無法找到使用者",
            "playerisyourself": "使用者 %s 是你自己",
            "Invalid_cookie2": "cookie過期，請使用/settings指令更新",
            "user_send_error": "無法向您發送私訊。請確保您的私訊設置允許接收來自服務器成員的消息。",
            "2": "---------------cmd---------------",
            "error_exit": "按下任意按鍵離開...",
            "3": "---------------list---------------",
            "error_len": ["則錯誤", "請修正這些錯誤"]
        },
        "presence": {
            "Going_offline": "下線了",
            "Coming_online": "上線了",
            "Entering_the_game": "進入了遊戲",
            "Entering_studio": "進入了studio",
            "Exiting_game": "離開了遊戲",
            "Exiting_studio": "離開了stuio"
        }
    }
}
```

</details>

---





## cookies

`cookies` 能夠用來以特定身份查詢，簡單來說，如果A玩家正在玩一個名為 Doors 的遊戲，且在 roblox 中設定為只有好友才能加入遊戲，那麼就只有與A為好友的玩家能夠知道A在玩的遊戲是 Doors ， `cookies` 就像是一個身份證，如果有設定 `cookies` ，那麼程式就可以使用設定的 `cookies` 這個身份來查詢，便能查到好友正在遊玩的遊戲。

如何取得自己的 `cookies`
<details><summary>>>> 點此查看完整內容 <<<</summary>

1. 用瀏覽器到任意一個 [roblox 頁面](https://www.roblox.com/home)

2. 按下鍵盤上的 「F12」 進入檢查

![](https://raw.githubusercontent.com/Qarchue/images/master/get_cookies/cookies_1.png)

3. 在上方選擇 「Application」 (開發者選項)

![](https://raw.githubusercontent.com/Qarchue/images/master/get_cookies/cookies_2.png)

4. 在左邊找到 「Cookies」 點開，並點下面的網址

![](https://raw.githubusercontent.com/Qarchue/images/master/get_cookies/cookies_3.png)

5. 在中間找到 「Name」 為 .ROB 開頭的，並複製其 「Value」 中的值(_/|WARING...)，這就是你帳號的 `cookies`

![](https://raw.githubusercontent.com/Qarchue/images/master/get_cookies/cookies_4.png)

</details>

取得之後使用 `/settings` 指令設定 `cookies` 就完成了~

---





## 專案資料夾結構

```
roblox-state-notify-bot/
    ├── configuration/     
    │   └── settings.json      = 設定檔，機器人相關設定都在此檔案
    ├── language/          = 語言資料夾
    │   ├── en_us.json         = 英文
    │   ├── lzh.json           = 文言文
    │   └── zh_tw.json         = 繁體中文
    ├── subscribers/       =
    │   └── discord_user.json  = 存放使用者資料的json文件
    ├── bot.py             = 機器人程式檔
    └── requests.txt       = 依賴，首次啟動前請先安裝依賴
```

---





## 貢獻

本專案的靈感與部分程式片段來自於 https://github.com/jackssrt/robloxnotif/blob/master/README.md?plain=1

由 Qarchue 偷偷在上課時間撰寫完成

---





## 授權

此專案採用 MIT 授權，詳情請參閱 LICENSE 檔案。
