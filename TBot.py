import requests
import schedule
import telebot

CLIENT_ID = 'JzAg-FLKmFuL_qat7Sh_Pg'
SECRET_KEY = 'hT-OW3KP3xQoshUO1TEHwWlel4-zzg'
TG_TOKEN = '1647121721:AAFhxL_KmXXxbGqV2nVHbMdA7os8KN_N_XU'
TG_CHANNEL = '1001586199616'
bot = telebot.TeleBot(TG_TOKEN)
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)
data = {
    'grant_type': 'password',
    'username': 'Hamsterr123',
    'password': 'cfhx8sza5kbkjswa'
}
headers = {'User-Agent': 'MyAPI/0.0.1'}
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)
TOKEN = res.json()['access_token']
headers = {**headers, **{'Authorization': f'bearer {TOKEN}'}}
requests.get('https://oauth.reddit.com/api/v1/me', headers=headers).json()

list = []
def send_telegram(text: str):
    token = "1647121721:AAFhxL_KmXXxbGqV2nVHbMdA7os8KN_N_XU"
    url = "https://api.telegram.org/bot"
    channel_id = "@RedditMemesChannel"
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
         "chat_id": channel_id,
         "text": text
          })

    if r.status_code != 200:
        raise Exception("post_text error")


def get_memes():
    #f = open('1.txt', 'a', encoding='utf-8')
    res = requests.get('https://oauth.reddit.com/r/memes/new',
                       headers=headers)
    for post in res.json()['data']['children'][:1]:
        a = post['data']['url_overridden_by_dest']
        if a not in list:
            list.append(a)
            send_telegram(a)
        else:
            continue
        #f.write(post['data']['url_overridden_by_dest'] + '\n')
    #f.close()
    # title = post['kind'] + '_' + post['data']['id']




#get_memes()
schedule.every(1).minutes.do(get_memes)
while True:
    schedule.run_pending()
