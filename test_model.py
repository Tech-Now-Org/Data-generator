
from dotenv import get_key
from data_generator.model import Model

api_key = get_key('.env', 'GOOGLE_API_KEY')

data_generator = Model(api_key)

data = data_generator.generate([2,10], ['typical windows,linux and mac-os shell commands in words', 'commands'])

f = open('demofile.txt', 'a')
f.write(str(data))