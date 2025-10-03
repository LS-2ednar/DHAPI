"""
This will download all the information available about cards which can be found on this google sheet: https://docs.google.com/spreadsheets/d/1cIoBHAvvuScHrAUnwjGvd-2AxfgsLamWCtx-5x7YYGo/edit?gid=1820067966#gid=1820067966
Credit for the work goes to: https://www.reddit.com/user/orthling/

Image URLS are sourced from: 

"""
import requests
import pandas as pd

def extract_domains():
    df = extract_csv_from_google_sheet("2134884751")
    """
    - Add URL to Image
    - Add Artist
    """

def extract_classes():
    df = extract_csv_from_google_sheet("1511012738")
    """
    - Split Domains to Domain 1 and Domain 2
    """

def extract_subclasses():
    df = extract_csv_from_google_sheet("1481888499")
    """
    - Add URL to Image
    - Add Artist
    """

def extract_ancestries():
    df = extract_csv_from_google_sheet("1060648534")
     """
    - Add URL to Image
    - Add Artist
    """

def extract_communities():
    df = extract_csv_from_google_sheet("1340074982")
    """
    - Add URL to Image
    - Add Artist
    """

def extract_abilities():
    df = extract_csv_from_google_sheet("1537633946")
    """
    - Add URL to Image
    - Add Artist
    """

def extract_adversaries():
    df = extract_csv_from_google_sheet("542498522")
    """
    - Hord HP to be "Empty" if nothing is there
    - Seperate Damage and Damage Type
    """
def extract_environments():
    df = extract_csv_from_google_sheet("1962091769")

def extract_armor():
    df = extract_csv_from_google_sheet("1548796884")
    """
    - Seperate Thresholds to lower Threshold and higher Threshold
    """
def extract_consumables():
    df = extract_csv_from_google_sheet("572165442")

def extract_items():
    df = extract_csv_from_google_sheet("1489254262")

def extract_weapons():
    df = extract_csv_from_google_sheet("1483598350")
    """
    - Damge -> Remove phy / mag
    """
def extract_wheelchairs():
    df = extract_csv_from_google_sheet("826247254")
    """
    - Damage -> Remove phy / mag
    - Seperate Damage and Damage Type
    """

def extract_csv_from_google_sheet(gid):
    sheet_id = "1cIoBHAvvuScHrAUnwjGvd-2AxfgsLamWCtx-5x7YYGo"
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}")   
    print(df)
    return df

def get_artist_and_image_url(card_type,card_name):
    pass

def main():
    pass

extract_domains()