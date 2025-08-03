import requests

def get_jokes():
    url = 'https://official-joke-api.appspot.com/jokes/random'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        setup = data['setup']
        punchline = data['punchline']

        print("Here's a joke for you!!!")
        print('\n',setup)
        input('....')
        print(punchline,'😂')

    else:
        print("couldn't fetch the joke")

def get_quotes():
    url = "https://zenquotes.io/api/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        quote = data[0]['q']
        author = data[0]['a']
        
        print("Here's a quote for you !!!")
        print('\n',quote)
        print("\t\t\t-By ",author)

    else:
        print("Couldn't fetch a quote at this moment")
   
        