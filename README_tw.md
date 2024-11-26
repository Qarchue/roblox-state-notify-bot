# [roblox-state-notify-bot]([https://www.github.com/Qarchue/roblox-state-notify-bot](https://github.com/Qarchue/roblox-state-notify-bot))

<p align="center">
    <a href="https://github.com/Qarchue/roblox-state-notify-bot/blob/master/LICENSE"><img src="https://img.shields.io/github/license/qarchue/roblox-state-notify-bot"></a>
    <a href="https://github.com/Qarchue/roblox-state-notify-bot"><img src="https://img.shields.io/github/repo-size/Qarchue/roblox-state-notify-bot"></a>
    <a href="https://github.com/Qarchue/roblox-state-notify-bot"><img src="https://img.shields.io/github/languages/top/Qarchue/roblox-state-notify-bot"></a>
    <a href="https://github.com/Qarchue/roblox-state-notify-bot/stargazers"><img src="https://img.shields.io/github/stars/Qarchue/roblox-state-notify-bot?style=socia"></a>
    <a href="https://discord.gg/w5CeZh3rNu"><img src="https://img.shields.io/discord/905865794683015208?style=flat-square&logo=Discord&logoColor=white&label=support&color=5865F2"></a>
</p>

[English](https://github.com/Qarchue/roblox-state-notify-bot/blob/main/README.md) | **中文**

> 歡迎將本專案所有或部分程式碼放入你自己的機器人中。

有些玩家上線時不會通知朋友，導致常常錯過一起遊玩的機會。為了解決這個問題，我使用 **Python 3** 開發了一個工具來監視他們的狀態變化，並即時發送通知。

這是一個簡單的小專案，可以監控指定玩家的狀態變化，並通過 Discord 通知您。您還可以使用 Cookie 來查詢更詳細的資訊，例如玩家加入或離開某個遊戲。

該機器人還支援多語言設置，用戶可以根據自己的需求選擇不同的語言接收通知，只需更改或新增 `language` 資料夾內的 JSON 檔案即可自訂語言內容。

_本文檔將引導您完成創建 Discord 機器人及使用其功能。_


###### 使用chatGPT輔助撰寫

---
# 支持的平台

| 作業系統|支持|經過測試|
| ------------- | ------- | ------- |
| Windows 11    |✅|✅|
| Windows 10    |✅|✅|
| Other Windows |❓| ❌|
| Linux         |❓| ❌|
| MacOS         |❓| ❌|

目前沒有對window以外的電腦做過測試，因為我沒有電腦，也不會用其他的方法測試
## 特徵

- [x] 當玩家上線、下線、加入或離開遊戲時，透過 Discord 通知。
- [x] 支援 Cookie 驗證，用於查詢玩家是否加入或離開某個遊戲。
- [x] 可自訂語言，支持多語言通知。
- [x] 可動態管理訂閱的玩家，透過簡單指令來增加或移除訂閱。

---

## 指令功能

| **指令名稱**   | **功能描述**                     |
|----------------|---------------------------------|
| `/sublist`     | 查看目前訂閱的玩家列表，顯示所有您訂閱的 Roblox 玩家。         |
| `/sub`         | 訂閱或取消訂閱特定玩家。可一次訂閱或取消多個玩家，使用空白隔開玩家名稱或 ID。若已經訂閱的玩家再次輸入，則會取消訂閱。         |
| `/setting`     | 更改語言設置或更新 Cookie。可選擇更改語言或提供新的 Cookie，如果都不填則顯示當前設定。     |

---

## 預設語言

目前 `language` 資料夾中包含以下三個預設語言檔案，供管理者直接使用或根據需求進行修改：

| **語言代碼** | **語言名稱**   |
|--------------|----------------|
| `zh-tw`      | 繁體中文       |
| `en-us`      | 英文           |
| `lzh`      | 文言文           |

預設語言設定為 `zh-TW`，若使用者沒有自訂語言，則會使用此預設語言。

機器人的預設語言設定為 `zh-TW`，此設定將應用於所有未自訂語言的用戶。管理者可以在 `configuration/settings.json` 中更改預設語言。

## JSON 設定說明

以下是需要建立的 JSON 檔案與其內容範例：

### 1. `settings.json`
**位置**：`configuration/settings.json`  
此檔案用於設定機器人的 Token 和預設語言。  
範例內容：
```json
{
    "TOKEN": "你的 Discord Bot Token",
    "Default_language": "zh-tw"
}
```
- `TOKEN`：填入您在 Discord 開發者平台取得的 Bot Token。
- `Default_language`：填入您希望的預設語言檔名稱（如 zh-TW）。

---

## 安裝依賴

確保已安裝 Python 3.8 或更新版本，然後執行以下命令來安裝依賴：

```sh
pip install -r requirements.txt
```

`requirements.txt` 檔案中包含了運行此機器人所需的所有 Python 套件。

---

## 啟動機器人

執行以下指令來啟動機器人：

```sh
python bot.py
```

---

## 注意事項

### 1. Roblox Cookie
提供有效的 `.ROBLOSECURITY` Cookie 可啟用進階功能來查詢玩家的遊戲狀態。如果玩家允許查詢，機器人會顯示詳細的遊戲資訊，否則只會顯示玩家的狀態變化。

### 2. Discord 權限
確保機器人擁有以下基本權限：
- 發送訊息
- 嵌入訊息
- 使用應用程式指令

### 3. 語言設定
機器人支援多語言通知。預設語言決定機器人的指令名稱和說明，但每個使用者可以單獨設定自己的通知語言。這樣，當機器人通知該使用者時，將使用其設定的語言。管理者也可以透過修改 `language` 資料夾中的 JSON 檔案來新增或更改語言。

---

## 貢獻

本專案的靈感與部分程式片段來自於 https://github.com/jackssrt/robloxnotif/blob/master/README.md?plain=1

由 Qarchue 偷偷在上課時間撰寫完成

---

## 授權

此專案採用 MIT 授權，詳情請參閱 LICENSE 檔案。

---
