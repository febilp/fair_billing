import sys
import re
from datetime import datetime

def parse_log(file_path):
    sessions = {}
    start_time = None
    end_time = None

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            pattern = r'(.)\1{2,}'
            has_value = re.search(pattern, parts[1])
            if len(parts) != 4 and len(parts) > 2 and not has_value:
                try:
                    timestamp = datetime.strptime(parts[0], '%H:%M:%S')
                except ValueError:
                    continue

                username = parts[1]
                action = parts[2]

                if action == 'Start':
                    start_time = timestamp
                    if username not in sessions:
                        sessions[username] = []
                    sessions[username].append((start_time, None))
                elif action == 'End':
                    end_time = timestamp
                    if username in sessions:
                        for session in sessions[username]:
                            if session[1] is None:
                                session = (session[0], end_time)
                                break

    return sessions

def calculate_duration(sessions):
    results = {}

    for username, session_list in sessions.items():
        num_sessions = len(session_list)
        total_duration = 0

        for start_time, end_time in session_list:
            if end_time is None:
                end_time = datetime.strptime('23:59:59', '%H:%M:%S')
            duration = (end_time - start_time).total_seconds()
            total_duration += duration

        results[username] = (num_sessions, int(total_duration))

    return results

def process_log(file_path):
    sessions = parse_log(file_path)
    results = calculate_duration(sessions)
    return results

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    response = process_log(file_path)
    print(response)
