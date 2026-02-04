from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class LogEntry:
    timestamp: datetime
    level: str
    message: str

def parse_line(line: str) -> LogEntry | None:
    line = line.strip()

    if not line:
        return None
    try:
        timestamp_str = line[:19]
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")

        rest = line[20:]
        level, message = rest.split(" ", 1)

        return LogEntry(timestamp=timestamp, level=level, message=message)

    except(ValueError, IndexError):
        return None