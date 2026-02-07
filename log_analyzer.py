from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class LogEntry:
    timestamp: datetime
    level: str
    message: str

def parse_line(line: str) -> LogEntry | None:
    """
    Parse a log line into a LogEntry
    Return None if the line is empty or malformed
    
    :return: Description
    """
    line = line.strip()

    if not line:
        return None
    try:
        # Extract timestamp (first 19 characters)
        timestamp_str = line[:19]
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        # Extracting level and message which are the remaining parts. Level is the next world and message is any strings that comes next
        rest = line[20:]
        level, message = rest.split(" ", 1)

        return LogEntry(timestamp=timestamp, level=level, message=message)

    except(ValueError, IndexError):
        return None
    
def read_line(path: str) -> list[str]:
    """
    Read all lines from a log file
    """
    with open(path, "r", encoding="utf-8") as f:
        return f.readlines()
    
def parse_file(path:str) -> LogEntry:
    entries: list[LogEntry] = []
    skipped = 0

    lines = read_line(path)
    for line in lines:
        if parse_line(line)==None:
            skipped+1
        else:
            entries.append(parse_line(line))
    return entries, skipped

from collections import Counter

def count_levels(entries: list[LogEntry]) -> dict[str, int]:
    """
    Count log entries by severity level
    
    :return: Description
    """
    levels = (entry.level for entry in entries)

    return dict(Counter(levels))