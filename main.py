from gingerit.gingerit import GingerIt
import telebot
import openai

openai.api_key = "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"
bot = telebot.TeleBot("5808780702:AAGEXekTInSQnjSda7aMBCrZMZZD5p8ZP-A")
@bot.message_handler(commands=['start'])
def start_message(message):
     bot.send_message(message.chat.id, text="Hello, " + message.chat.first_name)
@bot.message_handler(content_types=['text'])
def message(message):
    parser = GingerIt()
    result = parser.parse(message.text)
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "user", "content": f"{message.text}"}
    ]
    )
    bot.send_message(message.chat.id, str(result['text'] + '\n' + result['result']))
    bot.send_message(message.chat.id, "Answer: " + str(completion.choices[0].message.content))

bot.infinity_polling()

