import json


class setup():


    def __init__(self):
        self.bar = input()
        self.foo = "てきすとだお"
        self.hoge = "んごんご"
        self.peke = "ぐふふ"
        print("hello,world")
        setup.main(self)


    def main(self):
        print("class構造のinitでも呼び出し行けるよ")
        setup.json(self)


    def json(self):
        print("方法は[class名].[呼び出したいdef]最後にself")
        dictionary = {
             "foo":self.foo,
             "bar":self.bar,
             "hoge":self.hoge,
             "peke":self.peke
        }

        with open('blank01.json', 'w') as afile: # 第二引数：writableオプションを指定
            json.dump(dictionary, afile)

        with open('blank01.json') as afile:
            print(json.load(afile))

        baikin = "楽シージ"     
        return baikin

if __name__ =='__main__':
    p = setup()
    print(p)
