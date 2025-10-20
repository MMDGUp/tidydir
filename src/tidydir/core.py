import os
import shutil
from pathlib import Path
from typing import Dict, List

CATEGORIES: Dict[str, List[str]] = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".md"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".webm"],
    "Audio": [".mp3", ".wav", ".flac", ".ogg"],
    "Code": [".py", ".js", ".ts", ".html", ".css", ".json"],
}

def get_category(ext: str) -> str:
    ext = ext.lower()
    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category
    return "Other"

def organize_directory(path: str, dry_run: bool = False, verbose: bool = False) -> None:
    target = Path(path)
    if not target.is_dir():
        raise ValueError(f"'{path}' is not a directory")

    for item in target.iterdir():
        if item.is_file():
            ext = item.suffix
            category = get_category(ext)
            dest_dir = target / category

            if not dry_run:
                dest_dir.mkdir(exist_ok=True)
                new_path = dest_dir / item.name

                # Обработка дубликатов
                counter = 1
                while new_path.exists():
                    name, suffix = item.stem, item.suffix
                    new_path = dest_dir / f"{name}({counter}){suffix}"
                    counter += 1

                shutil.move(str(item), str(new_path))
                if verbose:
                    print(f"MOVED: {item} → {new_path}")
            else:
                if verbose:
                    print(f"DRY-RUN: {item} → {dest_dir / item.name}")