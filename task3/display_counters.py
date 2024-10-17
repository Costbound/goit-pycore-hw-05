def display_log_counters(counters: dict) -> None:
    print('\n')
    print(f'{'Log Level':<20} | {'Quantity':<10}')
    print(f'{'-' * 20} | {'-' * 10}')
    for level, count in counters.items():
        print(f'{level:<20} | {count:<10}')
    print('\n')

def display_log_details(logs:list, level: str) -> None:
    print(f'Log details for level \'{level}\':')
    for log in logs:
        print(f'{log['date']} - {log['message']}')