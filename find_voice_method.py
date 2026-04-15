from murf import Murf
try:
    c = Murf(api_key="x")
    mn = [x for x in dir(c) if 'voice' in x.lower()]
    print("Methods with 'voice':", mn)
    
    # Check inside tts
    mn_tts = [x for x in dir(c.text_to_speech) if 'voice' in x.lower()]
    print("TTS methods with 'voice':", mn_tts)
except Exception as e:
    print(e)
