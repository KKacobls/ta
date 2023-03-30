CHATGPT_API_KEY = ''
DISCORDBOT_TOKEN = ''
# 導入Discord.py模組
import discord
from discord.ext import commands
import openai

def gpt(prompt):#本段由bing產生而成
    
    # Set up the OpenAI API client
    openai.api_key = CHATGPT_API_KEY 

    # Set up the model and prompt
    model_engine = "text-davinci-003"
    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response = completion.choices[0].text
    return response
def main():#channel_id=要傳送的頻道
    # client是跟discord連接，intents是要求機器人的權限
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents = intents)
    # 調用event函式庫
    @client.event
    # 當機器人完成啟動
    async def on_ready():
        print(f"目前登入身份 --> {client.user}")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        # 處理輸入文字
        content = message.content
        author = message.author.name
        gulid = message.guild.id #伺服器名稱
        channel_id = message.channel.id
        #message.channel.name 頻道名稱
        content = content.replace('！','!')#把全形改半形 很多手機預設一開始是全形
        if content.startswith('!chatgpt'):#檢測訊息有!chatgpt開頭的
            await message.channel.send(gpt(content.replace('!chatgpt ','')))#把!chatgpt 取代為空 把完整問題丟給chatgpt
        if message.channel.name=='chatgpt':#頻道名稱為chatgpt
            await message.channel.send(gpt(content))
    client.run(DISCORDBOT_TOKEN)
if __name__=='__main__':
    if CHATGPT_API_KEY and DISCORDBOT_TOKEN:#檢測DISCORDBOT_TOKEN和CHATGPT_API_KEY是否為空
        main()
    else:
        print('請修改程式第一行 接上你的token以及apikey')
        print('discordtoken網址','https://discord.com/developers')
        print('chatgptapikey','https://platform.openai.com/account/api-keys')