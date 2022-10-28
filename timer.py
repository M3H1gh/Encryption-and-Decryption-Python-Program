from datetime import datetime

now = datetime.now()
now_string = now.strftime("%d/%m/%Y %H:%M:%S")

class DateAndTime():

    def extract_day():
        return (int(now_string[0])*10+int(now_string[1]))

    def extract_hour():
        return (int(now_string[11]) * 10 + int(now_string[12]))

    def extract_minute():
        return (int(now_string[14]) * 10 + int(now_string[15]))