import telebot
import os
import random

TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "🤖 MUGT AI Bot taýýar!\n📊 /signal → analiz al"
    )

@bot.message_handler(commands=['signal'])
def signal(message):
    signals = [
        "📈 TREND: UP\n✅ SIGNAL: BUY\nSebäp: Alujylar güýçli",
        "📉 TREND: DOWN\n❌ SIGNAL: SELL\nSebäp: Satyjylar agdyk",
        "⏸ TREND: RANGE\n⚠️ SIGNAL: WAIT\nSebäp: Net trend ýok"
    ]
    bot.send_message(message.chat.id, random.choice(signals))

bot.polling(none_stop=True)
