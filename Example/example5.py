import time

class playtime():


    def __init__(self):
        # 再生中
        time.sleep(5)

class serial():


    def __init__(self, cnt):
        # シリアルポート開いたりうんぬんするから__init__は必要
        self.cnt = cnt
        serial.signal(self)

    def signal(self):
        if cnt == 0:
            signal = "A"
            print(f"{signal}を送りました")
        elif cnt == 1:
            signal = "B"
            print(f"{signal}を送りました")


if __name__ =='__main__':
    for cnt in range(2):
        if cnt == 0:
            x=0
            serial(x)
            playtime()
        elif cnt == 1:
            x=1
            serial(x)
    else:
        print("正常に処理できました")
