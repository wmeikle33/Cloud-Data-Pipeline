import requests
import json
import logging
import os
from datetime import datetime

API_URL =
API_KEY = os.environ.get("API_KEY") # Safe way to handle keys
DESTINATION_FILE = "ingested_events.json"

def extract_from_source(start_date, end_date):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    params = {
        "start": start_date,
        "end": end_date,
        "page": 1
    }
    
    all_events = []
    
    while True:
        response = requests.get(API_URL, headers=headers, params=params)
        response.raise_for_status()
        
        data = response.json()
        events = data.get("events", [])
        
        if not events:
            break
            
        all_events.extend(events)
        
        if params['page'] >= data.get("total_pages", 1):
            break
        params['page'] += 1
        
    return all_events

def basic_cleaning():

def save_raw():
     with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def run():
    data = extract_from_source()
    data = basic_cleaning(data)
    save_raw(data)
    log_metadata()
