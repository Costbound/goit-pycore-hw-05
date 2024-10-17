import re
from collections import Counter

log_regexp = re.compile(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(\w+)\s+(.+)$")

def load_logs(path: str) -> list:
    try:
        with open(path, mode="r", encoding='utf-8') as fh:
            logs = fh.readlines()
        return logs
    except FileNotFoundError as err:
        print(err)
    

def parse_log_line(log: str) -> dict:
    log = log.strip()
    match = re.match(log_regexp, log)
    if match:
        date, level, message = match.groups()
    else:
        raise ValueError('[ERROR] Invalid log format!')
    
    return {
        "date": date,
        "level": level,
        "message": message
    }
    
def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_logs = [log for log in logs if log['level'] == level]
    return filtered_logs
    
def count_logs_by_level(logs: list) -> dict:
    levels = [log['level'] for log in logs]
    counts = Counter(levels)
    return dict(counts)
