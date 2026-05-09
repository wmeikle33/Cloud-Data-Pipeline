def extract_from_source():

def basic_cleaning():

def run():
    data = extract_from_source()
    data = basic_cleaning(data)
    save_raw(data)
    log_metadata()
