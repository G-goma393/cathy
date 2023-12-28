class main():
    def __init__(self):
        self.data = {
            "text":"エナドリ飲みたい",
            "old":18
        }
    def calc(self):
        print(self.data["text"])

p = main()
print(p)
q = p.calc()