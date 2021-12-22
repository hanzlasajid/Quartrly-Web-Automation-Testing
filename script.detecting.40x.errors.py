import requests

try:
    response = requests.get('https://wonder46.mycartzy.com', allow_redirects=False)
    #print(resp.raise_for_status())
    print(response)
    if response.raise_for_status() == '<response[200]>':
        print("Server Working as expected") #Line not accessed, typecase problem
    #return print (resp.)
    #if resp.raise_for_status()= 'None'->print('Server responding')
    
except requests.exceptions.HTTPError as serverMessage:
    print(serverMessage)

#Error template
    #response = requests.get(url)
#if not response:
    #handle error here
#else:
    #handle normal response