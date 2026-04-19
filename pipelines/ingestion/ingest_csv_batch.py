for file in glob.glob(file_path):
    print(f"Reading file: {file}")
    df = pd.read_csv(file)
    

def run():
    data = extract_from_source()
    data = basic_cleaning(data)
    save_raw(data)
    log_metadata()
