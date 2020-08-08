from aip import AipSpeech
APP_ID = '21862234'
API_KEY = 'pgGF0FGflQtGopuOQX9yXauE'
SECRET_KEY = '8TfOu3Zo09GCEXgAGk8UvlQqY2v8oC7W'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


path = 'voices/myvoices.wav'
def listen():
    with open(path,'rb') as fp:
        voices = fp.read()
    try:
        result = client.asr(voices, 'wav', 16000, {'dev_pid':1537,})
        print(result)
        result_text = result['result'][0]
        print("your said", result_text)
        return result_text
    except KeyError:
        print("KeyError")
if __name__ == '__main__':
    print(client)
    listen()