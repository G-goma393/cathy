import os
from ctypes import CDLL
from pathlib import Path
#CDLL(str(Path("C:/GitHub/Cathy/cathy-master/cathy-master/onnxruntime.dll").resolve(strict=True)))
#CDLL(str(Path("C:/Users/5155a/OneDrive/ドキュメント/GitHub/Cathy/onnxruntime.dll").resolve(strict=True)))
#CDLL(str(Path("/home/cathy/Cathy/onnxruntime-linux-aarch64-1.13.1.tgz").resolve(strict=true)))
CDLL(str(Path("X:/venv/env/cathy-main/onnxruntime.dll").resolve(strict=True)))
from googletrans import Translator
from voicevox_core import VoicevoxCore
import openai
import whisper
import wave
import pyaudio

# グローバル変数
openai.api_key = os.getenv("OPEN_API_KEY")
# 関数呼び出しkeyとコンストラクタ名

class listen():
    # 録音とその音声ファイルの生成


    def __init__(self):
    # 録音に必要な情報を辞書型に代入
        self.args={
        "CHUNK":2**10,
        "FORMAT":pyaudio.paInt16,
        "CHANNELS":1,
        "RATE":44100,
        "record_time":5
        }

    
    def jene(self):
        # .wavを生成してpathを返す
        p = pyaudio.PyAudio()
        stream = p.open(format = self.args["FORMAT"],
                 channels = self.args["CHANNELS"],
                 rate = self.args["RATE"],
                 input = True,
                 frames_per_buffer = self.args["CHUNK"])
        # [保留]変数cntは実行回数に応じて増加
        # output_path = f"./output{cnt}.wav"　
        output_path = "output.wav"
        print("recoding now ...")
        frames = []
        for i in range(0, int(self.args["RATE"] / self.args["CHUNK"] * self.args["record_time"])):
            data = stream.read(self.args["CHUNK"])
            frames.append(data)
        print("Done.")
        stream.stop_stream()
        stream.close()
        p.terminate()
        wf = wave.open(output_path, 'wb')
        wf.setnchannels(self.args["CHANNELS"])
        wf.setsampwidth(p.get_sample_size(self.args["FORMAT"]))
        wf.setframerate(self.args["RATE"])
        wf.writeframes(b''.join(frames))
        wf.close()
        return output_path
    

class char_conver():


    def __init__(self, path):
        model = whisper.load_model("base")
        self.conver = model.transcribe(path)
        print(self.conver)

    def result(self):
        return self.conver


class trans():


    def __init__(self, data):
        # self.dataには文字列を
        self.data=data["text"]
        # dataの言語をstatusに代入
        self.status = data["language"]

    
    def iflanguage(self):
        if self.status == "ja":
            self.language=["ja","en"]
        elif self.status == "en":
            self.language=["en","ja"]
        else:
            print("ERROR--unknown language")
            print("ERROR--treat as japanece")
            self.language = ["ja","en"]
        return self.status


    def google_translation(self):# callback
        translator = Translator()
        translate_content = translator.translate(self.data, src=self.language[0], dest=self.language[1]).text
        return translate_content


class send_ai():


    def __init__(self,content):
        messages = [
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": content},
        ]
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
        )
        self.reply = {"text":response.choices[0].message.content, "language":"en"}


    def handler(self):
        return self.reply


class tts():
    # text to speech


    def __init__(self,data):
        self.args={
        "CHUNK":2**10,
        "FORMAT":pyaudio.paInt16,
        "CHANNELS":1,
        "RATE":44100,
        "record_time":5
        }
        core = VoicevoxCore(open_jtalk_dict_dir=Path("open_jtalk_dic_utf_8-1.11"))
        speaker_id = 3
        self.output_path = "./output.wav"
        if not core.is_model_loaded(speaker_id):  # モデルが読み込まれていない場合
            core.load_model(speaker_id)  # 指定したidのモデルを読み込む
        wave_bytes = core.tts(data, speaker_id)  # 音声合成を行う
        with open(self.output_path, "wb") as f:
            f.write(wave_bytes)  # ファイルに書き出す


    def speaker_zunda(self):
        wf = wave.open(self.output_path, 'rb')
        pa = pyaudio.PyAudio()

        stream = pa.open(format   = pa.get_format_from_width(wf.getsampwidth()),
                         channels = wf.getnchannels(),
                         rate     = wf.getframerate(),
                         output   = True)

        print("Read a file")
        data = wf.readframes(self.args["CHUNK"])

        # 各バッファで再生はFRAME SIZE分だけ行われる
        print("play the flie")
        is_to_go = True
        while is_to_go:
            stream.write(data)
            data = wf.readframes(self.args["CHUNK"])
            is_to_go = len(data) != 0 # dataがゼロになったらフラグをFalseにしてwhileループを抜ける

        stream.close()
        pa.terminate()
    

listen = listen()# 録音に必要な情報を代入
listen_wav = listen.jene()# 録音し生成した音声ファイルのPathを取得
dic = char_conver(listen_wav)# 音声ファイルを元に文字起こし
dictation = dic.result()# 文字起こしした結果を代入
translation = trans(dictation)# 文字起こしした結果から必要な情報だけを抜き取る
language_translation = translation.iflanguage()

print("System message : {}へと翻訳 ...".format(language_translation))
send_content = translation.google_translation()
print(f"send_message : {send_content}")
transmission = send_ai(send_content)
transletor_transmission = trans(transmission.handler())
language_translation_two = transletor_transmission.iflanguage()
print(f"System message : {language_translation_two[1]}へと翻訳 ...")
maniscript = transletor_transmission.google_translation()
synthetic_voice = tts(maniscript)
synthetic_voice.speaker_zunda()
