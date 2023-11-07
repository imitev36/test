import infinigpt
import openai

# Set up the OpenAI API client
openai.api_key = "open ai key"

# create the bot and connect to the server
personality = "an AI that can assume any personality, named SadJokerGPT"  #you can put anything here.  A character, person, personality type, object, concept, emoji, etc
channel = "#channel"
nickname = "BotName"
#password = "PASSWORD" #comment out if unregistered
server = "irc.server.eu"


#check if there is a password
try:
    infinigpt = infinigpt.ircGPT(personality, channel, nickname, server, password)
except:
    infinigpt = infinigpt.ircGPT(personality, channel, nickname, server)
    
infinigpt.start()
