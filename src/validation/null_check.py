def validate_no_nulls(df, columns):
    for col in columns:
        if df[col].isnull().any():
            raise ValueError(f"Null values found in {col}")
