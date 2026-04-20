def raw_orders_key(run_date: str) -> str:
    return f"raw/orders/run_date={run_date}/data.parquet"


def processed_features_key(run_date: str) -> str:
    return f"processed/features/run_date={run_date}/data.parquet"
