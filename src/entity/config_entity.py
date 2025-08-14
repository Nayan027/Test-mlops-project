from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    data_source: str

    root_dir: Path
    local_store: Path