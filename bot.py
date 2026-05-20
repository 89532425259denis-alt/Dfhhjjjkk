import telebot
import urllib.parse

bot = telebot.TeleBot("8492764278:AAFDuKe2e5T6GKI4NvYJorOiameDfpSjDUM")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Отправь описание картинки!")

@bot.message_handler(func=lambda message: True)
def generate(message):
    prompt = urllib.parse.quote(message.text)
    url = f"https://image.pollinations.ai/prompt/{prompt}"
    bot.send_photo(message.chat.id, url, caption="Вот ваше изображение!")
    if __name__ == "__main__":
    bot.infinity_polling()  # <-- Добавьте 4 пробела перед bot.infinity_polling()
