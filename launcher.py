import infinigpt
import openai

# Set up the OpenAI API client
openai.api_key = "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"

# create the bot and connect to the server
personality = "an AI that can assume any personality, named SadJokerGPT"  #you can put anything here.  A character, person, personality type, object, concept, emoji, etc
channels = ["#ideal", "#Haskovo"]
nickname = "SadJokerGPT"
#password = "PASSWORD" #comment out if unregistered
server = "irc.freeunibg.eu"


#check if there is a password
try:
    infinigpt = infinigpt.ircGPT(personality, channels, nickname, server, password)
except:
    infinigpt = infinigpt.ircGPT(personality, channels, nickname, server)
    
infinigpt.start()
