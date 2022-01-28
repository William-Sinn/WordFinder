import requests
#
# response = requests.get('https://randomfox.ca/floof')
# fox = response.json()
# print(fox['image'])

response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/hey")
word_info = response.json()
if isinstance(word_info, list):
    word_dict = word_info[0]
    print(word_dict['word'])
else:
    print(word_info['title'])
