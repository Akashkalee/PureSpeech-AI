from murf import Murf
import sys

log = open("murf_log.txt", "w")
sys.stdout = log
sys.stderr = log

key = "ap2_4ae196e6-b04d-4684-8772-1ca82cd549ce"
try:
    client = Murf(api_key=key)
    print("Client initialized")
    
    print("Checking text_to_speech attributes:", dir(client.text_to_speech))

    # Try to find voices
    # Some SDKs have no list_voices, you just use IDs.
    # But let's check if there is a 'voices' attribute on client
    if hasattr(client, 'voices'):
        print("client.voices:", dir(client.voices))
        try:
            print("client.voices.list():", client.voices.list())
        except Exception as e:
            print("Error listing voices:", e)

    # Try generate with a likely valid voice
    try:
        res = client.text_to_speech.generate(
            format="MP3",
            text="Hello testing",
            voice_id="en-US-natalie", # Standard voice
        )
        print("Generate result type:", type(res))
        print("Generate result:", res)
    except Exception as e:
        print("Error generating:", e)

except Exception as e:
    print("Fatal:", e)

log.close()
