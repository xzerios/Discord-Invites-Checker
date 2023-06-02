import threading, time, requests
proxy = {'http': 'http://user:pass@host:port','https': 'http://user:pass@host:port'} # Replace user:pass@host:port with your proxy.
threads = int(input("How many threads would you like to use? "))

def checkInvites(invite):
    try:
        r = requests.get(f'https://discord.com/api/v9/invites/{invite}', proxies=proxy)
        if r.status_code == 200:
            print(f'Valid Invite: {invite}')
            with open('valids.txt', 'a') as f:
                f.write(f'{invite}\n')
            print("Server Name: " + r.json()["guild"]["name"])
        else:
            print(f'Invalid Invite: {invite}')
    except:
        print('Error')

with open('invites.txt', 'r') as f:
    invites = f.read().splitlines()
for invite in invites:
    while threading.active_count() > threads:
        time.sleep(0.1)
    threading.Thread(target=checkInvites, args=(invite,)).start()
while threading.active_count() > 1:
    time.sleep(0.1)
print('Done')