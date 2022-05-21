from datetime import datetime
from pathlib import Path


def write(message: str, style="info"):
    date = f"{datetime.now().day}{datetime.now().month}{datetime.now().year}"
    path = Path(Path.cwd(), "firmware", f"log-{date}.log")
    with open(path, "a+") as log:
        log.write(
            f"[{datetime.now()}]"
            f"\t{style}\t{message}\n")
