from django.http import HttpResponseForbidden, HttpResponse
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, TextMessage, FollowEvent, UnfollowEvent,
    TextSendMessage, ImageMessage, AudioMessage
)

from linebot import LineBotApi, WebhookHandler
from flask import Flask, request, abort

from linebot.exceptions import InvalidSignatureError



# 各クライアントライブラリのインスタンス作成
line_bot_api = LineBotApi(channel_access_token="kcxKeivITnXdyb0m3ClvzDuadraGuPgON+Dr57DTQpSv+zfFUAGNlMfAUrkVjtghEVrttlF1juP8vxqG/MBX4sJWaVqIbuzCjaYfioEWnl8hCgRQq+RyM0LJYW9YSAkmT2pb1oe1RSjJZg3h+bKLIwdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler(channel_secret="27a35b0567b8ef0633d4bac44e541778")

app = Flask(__name__)

@app.route(“/callback”, methods=[‘POST’])
def callback():
　signature = request.headers[‘X-Line-Signature’] 　body = request.get_data(as_text=True)
　app.logger.info(“Request body: ” + body)

　try:
　　handler.handle(body, signature)
　except InvalidSignatureError:
　　abort(400)

　return ‘OK’

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
　line_bot_api.reply_message(
　　event.reply_token,
　　TextSendMessage(text=event.message.text))

if __name__ == “__main__”:
　app.run()