import pyttsx3


engine = pyttsx3.init() # 初始化语音库
rate = engine.getProperty('rate')
engine.setProperty('rate',rate-50)
engine.say