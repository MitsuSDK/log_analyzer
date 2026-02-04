from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class LogEntry:
    timestamp: datetime
    level: str
    message: str

