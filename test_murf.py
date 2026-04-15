from murf import Murf
import os

key = "ap2_4ae196e6-b04d-4684-8772-1ca82cd549ce"
client = Murf(api_key=key)

print("Checking voices...")
try:
    # try various locations
    if hasattr(client, 'voices'):
        print("client.voices:", dir(client.voices))
        # try listing
        # vs = client.voices.list()
    if hasattr(client, 'get_voices'):
        print("client.get_voices:", client.get_voices())
    
    # Try text_to_speech
    if hasattr(client.text_to_speech, 'get_voices'):
        print("client.text_to_speech.get_voices:", client.text_to_speech.get_voices())

except Exception as e:
    print("Error checking voices:", e)

print("Checking generate...")
try:
    res = client.text_to_speech.generate(
        format="MP3",
        text="Hello",
        voice_id="en-UK-ryan", # guessing ID
    )
    print("Generate result type:", type(res))
    print("Generate result dir:", dir(res))
except Exception as e:
    print("Error generating:", e)
