import requests 

def rand_activity():
    bored_url = 'https://www.boredapi.com/api/activity/'

    responce_bored_json = requests.get(bored_url).json()
    responce_bored = requests.get(bored_url)

    if responce_bored.status_code == 200:
        print(responce_bored_json['activity'])
    else:
        print('Page not found')

def activity(type):
    try:
        bored_url = 'https://www.boredapi.com/api/activity?type=' + type
        responce_bored_json = requests.get(bored_url).json()

        return responce_bored_json['activity']
    except:
        return 'Something went wrong. Try again.'
    
def participants(participantss):
    try:
        bored_url = 'https://www.boredapi.com/api/activity?participants=' + participantss
        responce_bored_json = requests.get(bored_url).json()

        return responce_bored_json['activity']
    
    except:
        return 'Something went wrong. Try again.'
    

print(participants('76'))