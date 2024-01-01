import configparser
config = configparser.ConfigParser()
config.read('C:/GitHub/projectCathy/env2/main/config.ini')
config.read("/home/cathy/projectCathy/env2/config.ini")
config.read("X:/venv/env/config.ini")
api_key = config['DEFAULT']['OPENAI_API_KEY']
print(api_key)