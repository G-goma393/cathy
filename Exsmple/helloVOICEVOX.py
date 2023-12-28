from ctypes import CDLL
from pathlib import Path

CDLL(str(Path("C:\GitHub\projectCathy\env2\main\cathy\Edit\onnxruntime.dll").resolve(strict=True)))
#CDLL(str(Path("C:/Users/5155a/OneDrive/ドキュメント/GitHub/python/01.openai/onnxruntime.dll").resolve(strict=True)))
from voicevox_core import VoicevoxCore

core = VoicevoxCore(open_jtalk_dict_dir=Path("C:\GitHub\projectCathy\env2\main\open_jtalk_dic_utf_8-1.11"))
speaker_id = 3
text = "こんにちは、これからチャットGPTとボイスボックスを活用した簡単なチャットボットの動作テストをお見せします。少しコードのお話をしますと、今、範囲選択したところにラズベリーパイで音声認識した結果が入り、それをチャットGPTへデータフォーマットにして送信しています。チャットGPTは日本語ではあまり精度が出せないので、グーグルトランスAPIを使い、会話に機械翻訳を挟んでいます。それでは実演していきましょう。"
if not core.is_model_loaded(speaker_id):  # モデルが読み込まれていない場合
    core.load_model(speaker_id)  # 指定したidのモデルを読み込む
wave_bytes = core.tts(text, speaker_id)  # 音声合成を行う
with open("説明.wav", "wb") as f:
    f.write(wave_bytes)  # ファイルに書き出す