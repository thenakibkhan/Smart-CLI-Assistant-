from datetime import datetime

def show_time_and_date():
    now = datetime.now()
    print("Current date",now.strftime("%d-%m-%Y"))
    print("Current time",now.strftime("%H-%M-%S %p"))


