#****************************百度语音自动播放***************************************
from aip import AipSpeech
""" 你的 APPID AK SK """
APP_ID = '14975947'
API_KEY = 'X9f3qewZCohppMHxlunznUbi'
SECRET_KEY = 'LupWgIIFzZ9kTVNZSH5G0guNGZIqqTom'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
Your_expect_input = input("请输入你想让她说的话：")
result = client.synthesis(Your_expect_input, 'zh', 1, {
    'vol': 5,  # 音量
    'spd': 3,  # 语速
    'pit': 9,  # 语调
    'per': 5,  # 0：女 1：男 3：逍遥 4：小萝莉
})
# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('new_voice.mp3', 'wb') as f:
        f.write(result)
