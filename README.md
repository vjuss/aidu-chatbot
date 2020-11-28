# Aidu_chatbot
An experimental chatbot built with Flask and Chatterbot. Partly based on https://github.com/chamkank/flask-chatterbot.

Aidu is trained on relationship advice that is scraped with Reddit API. You can use your own .txt file, where the first line is an example question from the user, second line an answer from the chatbot, third line a new question or reply from the user etc.:

Hi chatbot, do you have advice for me?
Chatbots always have some advice.
Great! Can I ask about my friend?

Local setup:

1. Create a virtual Python environment and run pip install -r requirements.txt.
2. Run python app.py.
3. Test your app at http://localhost:5000/.
