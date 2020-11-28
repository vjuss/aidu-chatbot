from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer #new
import re

app = Flask(__name__)


data = open('redditrelations.txt').read() #new

conversations = data.strip().split("\n")

chatbot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
#"chatterbot.storage.MongoDatabaseAdapter"
#"chatterbot.storage.SQLStorageAdapter"

trainer = ListTrainer(chatbot)  #new
trainer.train(conversations)#new


#trainer = ChatterBotCorpusTrainer(nightmare_bot)
#trainer.train("chatterbot.corpus.nightmares")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))

@app.route("/about/")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run()
