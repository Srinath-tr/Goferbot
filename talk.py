import sys,os
import pyaudio
import wave
import aiml

hmdir = "G:\python27\Lib\site-packages\pocketsphinx\model\hmm\wsj1"
lmd = "G:\python27\Lib\site-packages\pocketsphinx\model\lm\wsj\wlist5o.3e-7.vp.tg.lm.DMP"
dictd = "G:\python27\Lib\site-packages\pocketsphinx\model\lm\wsj\wlist5o.dic"

def decodeSpeech(hmmd,lmdir,dictp,wavfile):

    import pocketsphinx as ps
    import sphinxbase

    speechRec = ps.Decoder(hmm = hmmd, lm= lmdir, dict = dictp)
    wavFile = file(wavfile,'rb')
    wavFile.seek(44)
    speechRec.decode_raw(wavFile)
    result = speechRec.get_hyp()

    return result[0]

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 4

k = aiml.Kernel()
k.learn("audio2.aiml")

for x in range(10):
    fn = "o"+str(x)+".mp3"
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    print("recording")
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("done recording")
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(fn, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    wavfile = fn
    recognised = decodeSpeech(hmdir,lmd,dictd,wavfile)
    reply = k.respond(recognised)
    cm = 'espeak -s 155 "'+reply+'"'
    os.system(cm)
