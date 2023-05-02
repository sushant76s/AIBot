# api_key (TestBot2)
import telebot
from flask import Flask, request
from neuralintents import GenericAssistant
import os
from dotenv import load_dotenv
import requests

from dbOperations import insertUserInfo, checkUserInfo, deleteUserInfo, getUserInfo
from lang import Language
from langTranslation import translateLang, translateLangDefault, keyword_req
from features import Features
from AI_Model.aibotmodel import ai_response


load_dotenv()
TOKEN = os.getenv("API_KEY")
bot = telebot.TeleBot(token=TOKEN)
api = TOKEN

url = "http://127.0.0.1:5000/aibot"

# bot.remove_webhook()
# For removeing the webhook so that it can work on local

help_text = open('help.txt', 'r').read()

# General Functions
@bot.message_handler(commands=['help']) # help command handler
def send_welcome(message):
    bot.send_message(message.chat.id, help_text)

@bot.message_handler(commands=['start']) # start command handler
def start_function(message):
    chat_id = message.chat.id
    firstname = message.chat.first_name
    lastname = message.chat.last_name
    username = message.chat.username
    
    # Checking if the user is already exists in the database or not
    check_user = checkUserInfo(chat_id)
    if check_user is not None:
        bot.reply_to(message, 'Hello, Welcome!\nType /help to get the help!')
    else:
        try:
            insertUserInfo(chat_id, username, firstname, lastname)
            bot.reply_to(message, 'Seems like you are new user type /help to get started.\nThanks!')
        except:
            bot.reply_to(message, 'Something went wrong!')



@bot.message_handler(commands=['hi'])
def deleteUserData(message):
    bot.send_message(message.chat.id, "This is simple text.")


@bot.message_handler(commands=['delete_my_data'])
def deleteUserData(message):
    bot.send_message(message.chat.id, "Are you sure want to delete your data?\n /YES_deletemydata or /NO_keepmydata")

@bot.message_handler(commands=['YES_deletemydata'])
def deleteData(message):
    chat_id = message.chat.id
    try:
        deleteUserInfo(chat_id)
        bot.send_message(message.chat.id, "Your Data has been Deleted!")
    except:
        bot.send_message(message.chat.id, "Something went wrong! try again.")

@bot.message_handler(commands=['NO_keepmydata'])
def keepData(message):
    bot.send_message(message.chat.id, "Okay sure.")


@bot.message_handler(commands=['train'])
def keepData(message):
    bot.send_message(message.chat.id, f"Here is the url click and go to the page to feed some data that you want. {url}")



# Language Translation Part
@bot.message_handler(func=keyword_req)
def send(message):
    t = message.text.split()
    if Language.isPresentLang(t[1].lower()):
        request = message.text.split(' ', 2)
        translated_text = translateLang(request[1].lower(), request[2])
        bot.send_message(message.chat.id, translated_text)
    else:
        request = message.text.split(' ', 1)
        translated_text = translateLangDefault(request[1])
        bot.send_message(message.chat.id, translated_text)


# Fucntion to create media url using its file id
def image_url(file_id):
    api_id = api
    r = requests.post(f'https://api.telegram.org/bot{api_id}/getFile?file_id={file_id}')
    response = r.json()
    filePath = response['result']['file_path']
    img_url = f'https://api.telegram.org/file/bot{api_id}/{filePath}'
    return img_url



flag0 = 20
flag1 = 40
def eSingalFlag():
    global flag0
    flag0 = flag0/2
    print("Printing from the extracted text flag function!")
    print(flag0)

def improveImage():
    global flag1
    flag1 = flag1/2
    print("Printing from the improve image flag function!")
    print(flag1)

mappings = {
    'extract_image_text': eSingalFlag,
    'convert_image_to_grayscale': improveImage
}
assistant = GenericAssistant('C:/Users/Sushant/Downloads/Python_8/Project/AIBot/AI_Model/intents.json', intent_methods=mappings, model_name="aibot_model")
assistant.load_model("C:/Users/Sushant/Downloads/Python_8/Project/AIBot/AI_Model/aibot_model")

def ai_response(input_msg):
    return assistant.request(input_msg)


# Photo handler for performing the image operations
@bot.message_handler(content_types=['photo'])
def test_on_image(message):
    photo_caption = message.caption
    fileId = message.photo[2].file_id
    final_image_url = image_url(fileId)
    global flag0
    global flag1
    try:
        ai_response(photo_caption)
        if(flag0 == 10):
            print("Extract the text")
            etext = Features.extract(final_image_url)
            bot.send_message(message.chat.id, etext)
            flag0 = flag0*2
        elif(flag1 == 20):
            Features.improve_image(final_image_url)
            grayscale_image = open("C:/Users/Sushant/Downloads/Python_8/Project/AIBot/result-image.jpg", "rb")
            print("Improve the image flag")
            bot.send_photo(message.chat.id, grayscale_image)
            flag1 = flag1*2
        else:
            bot.send_message(message.chat.id, "Something went wrong! Please try again.")
    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, "Please add a caption in image for the particular task!")



# Reply to messages and make conversation (AI part)
@bot.message_handler(func=lambda m: True)
def repeat(message):
    temp = message.text
    try:
        msg_res = ai_response(temp)
        bot.send_message(message.chat.id, msg_res)
    except:
        bot.send_message(message.chat.id, "Something went wrong with the ai model.")



if __name__ == "__main__":
    bot.infinity_polling()


