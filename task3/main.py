from display_counters import display_log_counters, display_log_details
from parse_logs import load_logs, parse_log_line, filter_logs_by_level, count_logs_by_level
from pathlib import Path
import sys

def main() -> None:
    path = Path(sys.argv[1].strip()).absolute()
    level_filter = sys.argv[2].strip().upper() if len(sys.argv) > 2 else None

    try:
        raw_logs = load_logs(path)
        logs = [parse_log_line(log) for log in raw_logs]
        log_counts = count_logs_by_level(logs)
        display_log_counters(log_counts)

        if level_filter:
            filtered_logs = filter_logs_by_level(logs=logs, level=level_filter)
            display_log_details(logs=filtered_logs, level=level_filter)
            
    except Exception as err:
        print(err)


if __name__ == '__main__':
    main()