from datetime import datetime

from src.constants_enums.datetime_format import DateFormats


class Logger:
    def __init__(self, filename) -> None:
        self.filename = filename

    def add_entry(self, entry):
        now = datetime.now()
        with open(self.filename, 'a') as f:
            f.write(f"{now.strftime(DateFormats.LOGGING_TIME_FORMAT)}: {entry}")


