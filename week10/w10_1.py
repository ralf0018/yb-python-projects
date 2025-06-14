import datetime
 
def log_event(event_type, user_id, message):
    """Logs an event to a file with timestamp, event type, user ID, and message."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] [{event_type}] User: {user_id} - {message}\n"
    log_file_name = "./week10/event_log.txt"
    write_file(log_file_name, log_message)

def write_file(file_name, message):
    with open(file_name, "a") as file:
        file.write(message)
        
if __name__ == "__main__":
    log_event("TEST", "user123", "This is an test.")