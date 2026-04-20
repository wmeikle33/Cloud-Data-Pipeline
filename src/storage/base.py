from __future__ import annotations

from abc import ABC, abstractmethod
import pandas as pd


class StorageClient(ABC):
    @abstractmethod
    def read_csv(self, uri: str) -> pd.DataFrame:
        pass

    @abstractmethod
    def write_parquet(self, df: pd.DataFrame, uri: str) -> None:
        pass

    @abstractmethod
    def exists(self, uri: str) -> bool:
        pass
