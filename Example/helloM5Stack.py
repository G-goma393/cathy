# シリアル通信で数字を送るプログラムで周期を持つ
# 周期のタイミングは変数play_timeに入れる
# play_time分過ぎたら違う数字を送る
# 一方向通信のみ
import serial
import time

play_time = "A"
cnt = 0
# シリアルポートをオープンにする
ser = serial.Serial('/dev/serial0', 115200, timeout = 1.0)

ser.write(play_time.encode())
time.sleep(10)
print("10s経過しました")
play_time = "B"
ser.write(play_time.encode())
ser.close()
