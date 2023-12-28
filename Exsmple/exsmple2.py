# グローバル変数はclass内で使えるのか
test = "これが表示できたら行けるってこと"
class main():
    def __init__(self):
        print(test)
    def setup(self):
        test = "なんならこうも行けちゃったり"
        print(test)

p=main()
p.setup()