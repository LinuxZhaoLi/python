import win32com.client

speaker = win32com.client.Dispatch('SAPI.SpVoice')
speaker.Speak("我是语音助手，小灵")
