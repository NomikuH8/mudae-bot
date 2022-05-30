import requests
import datetime
import json
import re

# reagir:
#   PUT channels/<chan-id>/reactions/<emoji>/@me?location=Message

configs = json.loads(open('preferences.json').read())

user = configs['your-username']
mudae_user = configs['mudae-username']
auth = configs['auth']

channel = f'https://discord.com/api/v9/channels/{configs["channel"]}/messages'
req_limit = '?limit=2'

react_start = f'{channel}/'
# in-between goes message id
react_end = f'/reactions/{configs["emoji-reaction"]}/%40me?location=Message'

command = configs['command-to-make']
wishlist = configs['wishlist']


USER_AGENT = "NomikuH8's Mudae bot (0.0.1 - dev)"

headers = { 'User-Agent': USER_AGENT, 'Authorization': auth }

def get_last_messages():
    data = requests.get(channel, headers=headers).json()

    messages = []
    if data[0]['author']['username'] == user:
        i = data[1]
        if i['author']['username'] == mudae_user:
            try:
                desc = i['embeds'][0]['description'].split('\n')
                obj = {
                    'message_id': i['id'],
                    'character': i['embeds'][0]['author']['name'],
                    'series': desc[0],
                    'kakera': int(re.findall(r'\d+', desc[1][2:])[0])
                }
                messages.append(obj)
            except:
                pass

    with open('last_appeared.json', 'w') as file:
        file.write(json.dumps(messages, indent=2))
    with open('last_message_collected.json', 'w') as file:
        file.write(json.dumps(data, indent=2))


def send_message():
    data = requests.post(channel, data={ 'content': command })

def get_messages():
    data = requests.get(channel, headers=headers).json()

    messages = []
    for i in data:
        if i['author']['username'] == mudae_user:
            try:
                desc = i['embeds'][0]['description'].split('\n')
                obj = {
                    'message_id': i['id'],
                    'character': i['embeds'][0]['author']['name'],
                    'series': desc[0],
                    'kakera': int(re.findall(r'\d+', desc[1][2:])[0])
                }
                messages.append(obj)
            except:
                continue
    with open('my.json', 'w') as file:
        file.write(json.dumps(messages, indent=2))
    with open('ayoya.json', 'w') as file:
        file.write(json.dumps(data, indent=2))


def run_once():
    send_message()
    time.sleep(2)
    get_last_messages()

def run():
    print(str(datetime.datetime.now().hour) + str(datetime.datetime.now().minute))

if __name__ == '__main__':
    run()