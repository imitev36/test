import infinigpt
import openai

# Set up the OpenAI API client
openai.api_key = ""

# create the bot and connect to the server
personality = "an AI that can assume any personality, named SadJokerGPT"  #you can put anything here.  A character, person, personality type, object, concept, emoji, etc
channels = ["#channel", "#channel"]
nickname = "SadJokerGPT"
#password = "PASSWORD" #comment out if unregistered
server = "irc.serrver.eu"


#check if there is a password
try:
    infinigpt = infinigpt.ircGPT(personality, channels, nickname, server, password)
except:
    infinigpt = infinigpt.ircGPT(personality, channels, nickname, server)
    
infinigpt.start()
