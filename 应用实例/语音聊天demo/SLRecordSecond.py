import wave
from pyaudio import PyAudio, paInt16
import time

framerate = 16000# 采样率
num_samples = 2000 # 采样点
channels = 1# 声道
sampwidth = 2 # 采样宽度
FILEPATH = 'voices/myvoices.wav'
# 保存文件
def save_wave_file(filePath, data):
    wf = wave.open(filePath, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)
    wf.writeframes(b''.join(data))
    wf.close()

# 录音
def my_record():
    pa = PyAudio()
    stream = pa.open(format = paInt16,channels = channels,
                     rate=framerate, input = True, frames_per_buffer  = num_samples)
    my_buf = []
    t = time.time()
    print("开始录音")
    while time.time() < t + 10:
        string_audio_data = stream.read(num_samples)
        my_buf.append(string_audio_data)
    print("录音结束")
    save_wave_file(FILEPATH,my_buf)
    stream.close()


if __name__ == "__main__":
    my_record()

