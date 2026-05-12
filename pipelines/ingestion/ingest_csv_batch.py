def extract_from_source():
    for file in glob.glob(file_path):
        print(f"Reading file: {file}")
        df = pd.read_csv(file)
        
def basic_cleaning():
    nan_count = df.isnull.sum().resetindex()
    duplicate_count = df.duplicated().sum()
    
def run():
    input_path = Path(dir)
    csv_files = list(input_path.glob('*.csv'))
    data = extract_from_source()
    data = basic_cleaning(data)
    save_raw(data)
    log_metadata()
