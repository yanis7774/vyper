from pathlib import Path
from typing import Sequence


def get_interface_file_path(base_paths: Sequence, import_path: str) -> Path:
    relative_path = Path(import_path)
    for path in base_paths:
        file_path = path.joinpath(relative_path)
        suffix = next((i for i in ('.vy', '.json') if file_path.with_suffix(i).exists()), None)
        if suffix:
            return file_path.with_suffix(suffix)
    raise FileNotFoundError(f" Cannot locate interface '{import_path}{{.vy,.json}}'")
