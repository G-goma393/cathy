# pyaudio & wave & voicevox & serial(?) 動作テスト
# 合成音声の生成から再生まで、再生の前後にシリアル通信
# Raspiの仮想環境前提
from ctypes import CDLL
from pathlib import Path
CDLL(str(Path("C:\GitHub\projectCathy\env2\main\onnxruntime.dll").resolve(strict=True)))
#import time
import pyaudio
from voicevox_core import VoicevoxCore
import wave
import serial


class voicevox():


    def __init__(self):
        self.output_path = "output_test.wav"
        core = VoicevoxCore(open_jtalk_dict_dir=Path("C:\GitHub\projectCathy\env2\main\open_jtalk_dic_utf_8-1.11"))
        speaker_id = 3
        text = "レインボーシックスシージの初見は帰れなのだ。なぜかって？きみは70人いるオペレーターの特性やそのこわざもマップの構造もデフォカメの位置も突き上げ突き下げポジションもプラントする位置も索敵もプリエイムもブリーチングもラペリングも音の聞き方さえ知らないじゃないか、それでいてリコイルコントロールやヘッドラインすら覚えていない。このゲームは覚えることが多すぎる。ヴァロラントやエーペックスを後発にしてる化石ゲームだからオペレーターがいっぱいいる。きみはそんなオペレーターひとりひとりの特性や立ち回りだけでなくマップすら覚えていないじゃないか？それでもこのゲームの高難易度を心地良いと思えるならやるが良い、全てを越えた先で待っている"
        if not core.is_model_loaded(speaker_id):  # モデルが読み込まれていない場合
            core.load_model(speaker_id)  # 指定したidのモデルを読み込む
            wave_bytes = core.tts(text, speaker_id)  # 音声合成を行う
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
        print("再生終わりました")


class runtime_serial():


        def __init__(self, clock, cnt):
            self.cnt = cnt
            self.clock = clock
            #ser = serial.Serial('/dev/serial0', 115200, timeout = 1.0)
            ser = "windows用"
            runtime_serial.signal(self, ser)


        def signal(self, ser):
            if self.cnt == 0:
                # 信号をESP32に送信
                play_signal = "A"
                #ser.write(play_signal.encode())
                print("再生を開始しました")
            elif self.cnt == 1 :
                print(f"{self.clock}s経過しました")
                play_signal = "B"
                #ser.write(play_signal.encode())
                print("再生を終了します")
                #ser.close()


def handler():
    path = voicevox()

    for cnt in range(2):
        foobar = cnt
        if cnt == 0:
            runtime_serial(path.play_time(), foobar)
            path.speaker_zunda()
        elif cnt == 1:
            runtime_serial(path.play_time(), foobar)
    else:
        print("正常に処理完了")

handler()
