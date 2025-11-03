"""
Sources:
- Google sheet: https://docs.google.com/spreadsheets/d/1cIoBHAvvuScHrAUnwjGvd-2AxfgsLamWCtx-5x7YYGo/edit?gid=1820067966#gid=1820067966 Credit for the work goes to: https://www.reddit.com/user/orthling/ (mainly for )
- Image URL from https://cardcreator.daggerheart.com 
- Void content: https://www.daggerheart.com/thevoid/
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import json

def extract_domains():
    df = extract_csv_from_google_sheet("2134884751")
    df["URL"] = df.apply(lambda row: "https://cardcreator.daggerheart.com/assets/icons/domain-" + row.Domain.lower()+ ".png", axis=1)
    return df

def extract_classes():
    df = extract_csv_from_google_sheet("1511012738")
    try:
        domain_columns = df["Domains"].str.split(",", expand=True)
        domain_columns.columns = [f"Domain_{i+1}" for i in range(domain_columns.shape[1])]
        df_final = pd.concat([df.drop(columns=["Domains"]),domain_columns],axis=1)
        return df_final
    except:
        return df

def extract_subclasses():
    df = extract_csv_from_google_sheet("1481888499")
    try:
        df = add_artist_and_image_url(df)
        return df
    except:
        return df

def extract_ancestries():
    df = extract_csv_from_google_sheet("1060648534")
    df = add_artist_and_image_url(df)
    return df

def extract_communities():
    df = extract_csv_from_google_sheet("1340074982")
    df = add_artist_and_image_url(df)
    return df

def extract_abilities():
    df = extract_csv_from_google_sheet("1537633946")
    df = add_artist_and_image_url(df)
    return df

def extract_adversaries():
    df = extract_csv_from_google_sheet("542498522")
    try:
        dmg_columns = df["Damage"].str.split(expand=True)
        dmg_columns.columns = ["Damage Dice","Damage Type"]
        df_final = pd.concat([df.drop(columns=["Damage"]),dmg_columns],axis=1)
        return df_final
    except:
        return df

def extract_environments():
    df = extract_csv_from_google_sheet("1962091769")

def extract_armor():
    df = extract_csv_from_google_sheet("1548796884")
    try:
        thr_columns = df["Thresholds"].str.split("/",expand=True)
        thr_columns.columns = ["Lower Threshold","Higher Threshold"]
        df_final = pd.concat([df.drop(columns=["Thresholds"]),thr_columns],axis=1)
        return df_final
    except:
        return df

def extract_consumables():
    df = extract_csv_from_google_sheet("572165442")

def extract_items():
    df = extract_csv_from_google_sheet("1489254262")

def extract_weapons():
    df = extract_csv_from_google_sheet("1483598350")
    df["Damage"].replace({"phy":"","mag":""},regex=True, inplace=True)
    return df

def extract_wheelchairs():
    df = extract_csv_from_google_sheet("826247254")
    try:
        dmg_columns = df["Damage"].str.split(expand=True)
        dmg_columns.columns = ["Damage Dice","Damage Type"]
        df_final = pd.concat([df.drop(columns=["Damage"]),dmg_columns],axis=1)
        return df_final
    except:
        return df

def extract_csv_from_google_sheet(gid):
    sheet_id = "1cIoBHAvvuScHrAUnwjGvd-2AxfgsLamWCtx-5x7YYGo"
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}")   
    return df

def get_void_content():
    url = "https://www.daggerheart.com/thevoid/"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/115.0 Safari/537.36"
        )
    }
    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    hrefs = []
    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"].strip()
        if "wp-content" in href:
            hrefs.append(href)
    content = [href.split("/")[-1].split("-v")[0] for href in hrefs]
    version = [href.split("/")[-1].split("-v")[1].split("-")[0] for href in hrefs]
    data = {"Content Type":content, "Version":version,"URL":hrefs}
    df = pd.DataFrame(data=data)
    return df

def add_artist_and_image_url(df):
    URL, Artist = [], []
    response = requests.get("https://cardcreator.daggerheart.com/api/templates")
    json_string = response.text
    data = json.loads(json_string)
    if "Ability" in df.columns:
        for _, row in df.iterrows():
            URL.append(f"https://pub-cdae2c597d234591b04eed47a98f233c.r2.dev/v1/card-header-images/domains/{row['Domain'].lower()}/{row['Ability'].lower().replace(' ','-')}.webp")
            for entry in data["domain"]:
                if entry["name"].lower().replace("’","'") == row["Ability"].lower().replace("’","'"):
                    Artist.append(entry["artist"])
    if "Subclass" in df.columns:
        for _, row in df.iterrows():
            URL.append(f"https://pub-cdae2c597d234591b04eed47a98f233c.r2.dev/v1/card-header-images/subclass/{row['Subclass'].lower().replace(' ','-')}.webp")
            for entry in data["subclass"]:
                if entry["name"] == row["Subclass"]:
                    Artist.append(entry["artist"])
    if "Ancestry" in df.columns:
        for _, row in df.iterrows():
            URL.append(f"https://pub-cdae2c597d234591b04eed47a98f233c.r2.dev/v1/card-header-images/ancestry/{row['Ancestry'].lower().replace(' ','-')}.webp")
            for entry in data["ancestry"]:
                if entry["name"] == row["Ancestry"]:
                    Artist.append(entry["artist"])
    if "Community" in df.columns:
        for _, row in df.iterrows():
            URL.append(f"https://pub-cdae2c597d234591b04eed47a98f233c.r2.dev/v1/card-header-images/community/{row['Community'].lower().replace(' ','-')}.webp")
            for entry in data["community"]:
                if entry["name"] == row["Community"]:
                    Artist.append(entry["artist"])
    try:
        df["Artist"] = Artist
    except:
        pass
    df["URL"] = URL
    return df