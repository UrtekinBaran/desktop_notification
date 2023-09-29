from plyer import notification
import time
from datetime import datetime


def show_notification(title, message, timeout):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message_indicator = f"{current_time}\n{message}"
    notification.notify(
        title=title,
        message=message_indicator,
        timeout=timeout
    )


def main():
    show_notification("PYTHON TİME", "Go and start studying python at the table", 5)
    time.sleep(10)


main()
