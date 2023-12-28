# .wavファイルから再生時間を取得して再生
# serial通信でESP32へ信号を送る
# シリアル通信で数字を送るプログラムで周期を持つ
# 周期のタイミングは変数play_timeに入れる
# play_time分過ぎたら違う数字を送る
# 一方向通信のみ
# class tts行き
from ctypes import CDLL
from pathlib import Path
CDLL(str(Path("/home/cathy/venv/env/onnxruntime-linux-aarch64-1.13.1/lib/libonnxruntime.so").resolve(strict=True)))
from voicevox_core import VoicevoxCore
import pyaudio
import wave
import serial
import time

maniscript = "ぼくの名前はずんだもん、ちんさんを滅ぼして大阪の独立を防ぐことを目的としているずんだ餅の妖精だよ"

# text to speech
class tts():


    def __init__(self,ja_text):
        core = VoicevoxCore(open_jtalk_dict_dir=Path("/home/cathy/venv/env/open_jtalk_dic_utf_8-1.11"))
        speaker_id = 3
        self.output_path = "output.wav"
        if not core.is_model_loaded(speaker_id):  # モデルが読み込まれていない場合
            core.load_model(speaker_id)  # 指定したidのモデルを読み込む
        wave_bytes = core.tts(ja_text, speaker_id)  # 音声合成を生成
        with open(self.output_path, "wb") as f:
            f.write(wave_bytes)  # ファイルに書き出す
    

    def play_time(self):
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
        

        def __init__(self, clock):
            # 信号をESP32に送信
            # シリアルポートをオープンにする
            play_signal = "A"
            ser = serial.Serial('/dev/serial0', 115200, timeout = 1.0)
            ser.write(play_signal.encode())
            time.sleep(clock)
            print(f"{clock}s経過しました")
            play_signal = "B"
            ser.write(play_signal.encode())
            ser.close()


synthetic = tts(maniscript)
play_time = synthetic.play_time()
synthetic.speaker_zunda()
runtime_serial(play_time)
