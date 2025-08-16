from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    data_source: str

    root_dir: Path
    local_store: Path


@dataclass
class DataValidationConfig:
    local_data: Path

    all_schema: dict
    
    root_dir: Path
    status_file: str



@dataclass
class TransformationConfig:
    local_data: Path
    root_dir: Path
    
    train_data_path: Path
    test_data_path: Path

    split_ratio: float