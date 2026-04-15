from murf import Murf
client = Murf(api_key="test")
print("Client attributes:", dir(client))
try:
    print("Voices?", dir(client.voices))
except:
    pass
try:
    print("TTS attributes:", dir(client.text_to_speech))
except:
    pass
