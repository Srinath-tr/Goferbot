

hmdir = "F:\python\Lib\site-packages\pocketsphinx\model\hmm\wsj1"
lmd = "F:\python\Lib\site-packages\pocketsphinx\model\lm\wsj\wlist5o.3e-7.vp.tg.lm.DMP"
dictd = "F:\python\Lib\site-packages\pocketsphinx\model\lm\wsj\wlist5o.dic"

def decodeSpeech(hmmd,lmdir,dictp,wavfile):
    
    import pocketsphinx as ps
    from sphinxbase import *

  
    speechRec = ps.Decoder(hmm = hmmd, lm= lmdir, dict = dictd)
    wavFile = file(wavfile,'rb')
    wavFile.seek(44)
    speechRec.decode_raw(wavFile)
    result = speechRec.get_hyp()

    return result[0]

wavfile = "sample.mp3"
recognised = decodeSpeech(hmdir,lmd,dictd,wavfile)
print recognised
