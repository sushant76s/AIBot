import mysql.connector
import os
from dotenv import load_dotenv


load_dotenv()
sql_pass = os.getenv("PASSWORD")

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = sql_pass,
	database = "aibotdb"
)

mycursor = mydb.cursor()

def insertUserInfo(chat_id, u_name, f_name, l_name):
	sql = "INSERT INTO userinfo (chat_id, username, first_name, last_name) VALUES (%s, %s, %s, %s)"
	val = (chat_id, u_name, f_name, l_name)
	mycursor.execute(sql, val)
	mydb.commit()
	return


def checkUserInfo(chatid):
    sql = f'SELECT chat_id FROM userinfo WHERE chat_id = {chatid};'
    mycursor.execute(sql)
    result = mycursor.fetchone()
    return result


def deleteUserInfo(chatid):
    sql = f'DELETE FROM userinfo WHERE chat_id = {chatid};'
    mycursor.execute(sql)
    mydb.commit()
    return


def getUserInfo(chatid):
    sql = f'SELECT first_name FROM userinfo WHERE chat_id = {chatid};'
    mycursor.execute(sql)
    name = mycursor.fetchone()
    return name

# Inserting the intents data to train the  model
def insertIntentsData(tag, patterns, responses, json_formate):
	sql = "INSERT INTO intents_data (tag, patterns, responses, json_formate) VALUES (%s, %s, %s, %s)"
	val = (tag, patterns, responses, json_formate)
	mycursor.execute(sql, val)
	mydb.commit()
	return