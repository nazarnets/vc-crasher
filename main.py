# forgot to add this but you have to be in the call on your client for it to work

import httpx
import time

nazareth = httpx.Client()
chanid = input(">")
token = ""
auth = {"Authorization": token}
list = ["brazil", "hongkong", "india", "japan", "rotterdam", "singapore"]
while True:
    for reg in list:
        sex = nazareth.patch(f"https://discord.com/api/v9/channels/{chanid}/call", headers=auth, json={"region": reg})
        time.sleep(3)
        if sex.status_code == 429:
            jizz = sex.json()
            sperm = jizz.get("retry_after")
            print(f"{reg} : {sperm}")
            time.sleep(sperm)
        else:
            print(f"{reg} : {sex.status_code}")
