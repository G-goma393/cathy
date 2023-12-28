class main():
    def __init__(self, data):
        if data == 2:
          self.args = {"text":"寝たい","text2":"だめ"}
        else:
          self.args2 = {'text': '', 'segments': [], 'language': 'en'}
    def run(self):
        return self.args2
    
p = main(1)
s = p.run()
print(s)