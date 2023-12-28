import json

dictionary ={"test":"やっほ","content":"ー"}

with open('blank01.json', 'w') as file: # 第二引数：writableオプションを指定
  json.dump(dictionary, file)

with open('blank01.json') as file:
	print(json.load(file))