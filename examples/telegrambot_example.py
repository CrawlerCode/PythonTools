from pythontools.telegram import telegrambot

BOT = telegrambot.TelegramBot(token="TOKEN")
BOT.trustUserByID(id="USER-ID")

BOT.start()

# send message
BOT.sendMessage(chat_id="CHAT-ID", text="This is a message!")

# recipe messages
def recipeMessages(message):
    print("message:", message.text)
    message.reply("answer.")

BOT.registerMessageHandler(recipeMessages)

# handle commands
def handleCommand(command):
    print("command: test")

BOT.registerCommand('test', handleCommand)