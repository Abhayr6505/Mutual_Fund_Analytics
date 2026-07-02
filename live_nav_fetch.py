import requests
import pandas as pd
import os

schemes = {
    "119551": "SBI_Bluechip",
    "120503": "ICICI_Bluechip",
    "118632": "Nippon_Large_Cap",
    "119092": "Axis_Bluechip",
    "120841": "Kotak_Bluechip"
}

os.makedirs("data/raw", exist_ok=True)

for code, name in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    nav = pd.DataFrame(data["data"])

    file_name = f"data/raw/{name}.csv"

    nav.to_csv(file_name, index=False)

    print("="*60)
    print("Scheme :", data["meta"]["scheme_name"])
    print("AMC    :", data["meta"]["fund_house"])
    print("Records:", len(nav))
    print("Saved :", file_name)
    