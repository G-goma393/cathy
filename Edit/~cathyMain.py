from ctypes import CDLL
from pathlib import Path
import platform

# 異なるOS間特有の依存関係を排除
print("toggle debug mode: [on] or [off]")
debug_mode = input()# デバックモードのON/OFFの切り替え

os_name = platform.system()
os_info = platform.platform()


if os_name == "Linux":# ubuntu and Rasbian
    CDLL(str(Path("/home/cathy/projectCathy/env2/libonnxruntime.so.1.13.1").resolve(strict=True)))
    open_jtalk_path ="/home/cathy/projectCathy/env2/open_jtalk_dic_utf_8-1.11"

elif os_name == "Windows":

    if os_info =="Windows-10-10.0.22621-SP0":# win11
        CDLL(str(Path("C:/GitHub/projectCathy/env2/main/onnxruntime.dll").resolve(strict=True)))
        open_jtalk_path ="C:/GitHub/projectCathy/env2/main/open_jtalk_dic_utf_8-1.11"

    elif os_info=="Windows-11-10.0.17763-SP0":# win10
        CDLL(str(Path("X:/venv/env/onnxruntime.dll").resolve(strict=True)))
        open_jtalk_path ="X:/venv/env/open_jtalk_dic_utf_7-1.11"

    else:
        print("新しい環境エラー")
        CDLL(str(Path("onnxruntime.dll").resolve(strict=True)))
        os_info = "null"
        open_jtalk_path = "null"

from googletrans import Translator
from voicevox_core import VoicevoxCore
from openai import OpenAI
import whisper
import pyaudio
import wave
import serial

# setupとは別の関数
def cathy_Main():

    if debug_mode == "off":
        lis = listen()# 録音に必要な値を設定
        listen_wav = lis.jene()# 録音した音声ファイルのPathを取得
        dic = char_conver(listen_wav)# 音声ファイルを元に文字起こし
        # dictationの中身がChatGPTへ送られる
        dictation = dic.result()# 文字起こしした結果を代入

    elif debug_mode == "on":
        dictation = {
        "text":"あなたの名前を教えてください", 
        "language":"ja"
        }

    translation = trans(dictation)# dictationの中身をバラして整理して再統合
    language_translation = translation.iflanguage()# いる？

    print("System message : {}へと翻訳 ...".format(language_translation[0]))
    # google_translation()はソースの言語に併せて翻訳を担当するフレンズ
    send_content = translation.google_translation()

    print(f"send_message : {send_content}")
    transmission = send_ai(send_content)
    transletor_transmission = trans(transmission.handler())
    language_translation_two = transletor_transmission.iflanguage()
    print(f"System message : {language_translation_two[0]}へと翻訳 ...")
    # google_translation()はソースの言語に併せて翻訳を担当するフレンズ
    maniscript = transletor_transmission.google_translation()

    # 合成音声を生成するフレンズ
    synthetic = tts(maniscript)
    # 再生時間を取得するフレンズ
    play_time = synthetic.play_time()

    for cnt in range(2):
        if cnt == 0:
            # 再生中M5Stackに信号を送るフレンズ
            runtime_serial(play_time, cnt)
            # 再生するフレンズ
            synthetic.speaker_zunda()
        elif cnt == 1:
            # 再生中M5Stackに信号を送るフレンズ
            runtime_serial(play_time, cnt)
    else:
        print("正常に処理できました")

class listen():
    # 録音とその音声ファイルの生成するフレンズ


    def __init__(self):

    # 録音に必要な情報を辞書型に代入
        self.args={
        "CHUNK":1024,
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
    # 文字起こし

    def __init__(self, path):
        model = whisper.load_model("base")
        self.conver = model.transcribe(path)
        print(self.conver)

    def result(self):
        return self.conver


class trans():
    # 翻訳

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
        client = OpenAI()

        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "you are a cheerful assistant."},
            {"role": "user", "content": content}
        ]
        )

        print(completion.choices[0].message)
        reply_content = completion.choices[0].message.content
        self.reply = {"text":reply_content, "language":"en"}


    def handler(self):
        return self.reply


class tts():
    # text to speech

    def __init__(self,ja_text):
        # 翻訳したテキストをもとに合成音声を生成
        core = VoicevoxCore(open_jtalk_dict_dir=Path(open_jtalk_path))
        speaker_id = 3
        self.output_path = "speechCathy.wav"
        if not core.is_model_loaded(speaker_id):  # モデルが読み込まれていない場合
            core.load_model(speaker_id)  # 指定したidのモデルを読み込む
        wave_bytes = core.tts(ja_text, speaker_id)  # 音声合成を生成
        with open(self.output_path, "wb") as f:
            f.write(wave_bytes)  # ファイルに書き出す


    def play_time(self):
        # 音声の再生時間を取得
        wf = wave.open(self.output_path, 'rb')# 合成音声ファイルを開く
        samplerate = wf.getframerate()
        frame = wf.getnframes()
        play_time = frame / samplerate + 1
        return play_time


    def speaker_zunda(self):
        # 合成音声を再生
        chunk = 1024  # チャンクサイズ
        wf = wave.open(self.output_path, 'rb')# 合成音声ファイルを開く
        p = pyaudio.PyAudio()
        # ストリームを開く
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        # データを読み込んでストリームに書き込む
        data = wf.readframes(chunk)
        while data:
            stream.write(data)
            data = wf.readframes(chunk)
        # ストリームを閉じる
        stream.stop_stream()
        stream.close()
        # PyAudioを終了
        p.terminate()


class runtime_serial():


        def __init__(self, clock, cnt):
            self.cnt = cnt
            self.clock = clock
            runtime_serial.signal(self)
            # time.sleep(clock)
            # print(f"{clock}s経過しました")

            if os_name == "linux":
                ser = serial.Serial('/dev/serial0', 115200, timeout = 1.0)

            elif os_name =="Windows":
                ser ="null"
            
            runtime_serial.signal(self, ser)


        def signal(self):
            ser = serial.Serial('/dev/serial0', 115200, timeout = 1.0)
            if os_name == "Linux":    
                if self.cnt == 0:
                    # 信号をESP32に送信
                    play_signal = "A"
                    ser.write(play_signal.encode())
                elif self.cnt == 1 :
                    print(f"{self.clock}s経過しました")
                    play_signal = "B"
                    ser.write(play_signal.encode())
                    print("再生を終了します")
                    ser.close()
            else:
                if self.cnt == 0:
                    play_signal = "A"
                    print("【デバック】Aシグナルを送信した体。再生を開始します")
                elif self.cnt == 1 :
                    print(f"【デバック】{self.clock}s経過しました")
                    play_signal = "B"
                    print("【デバック】Bシグナルを送信した体。再生を終了します")


cathy_Main()
