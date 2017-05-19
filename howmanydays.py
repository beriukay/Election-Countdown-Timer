#!/usr/bin/python
import datetime
import time
import sys

election = datetime.datetime(2020, 11, 3, 0, 0, 0)

while True:
    today = datetime.datetime.now()
    freedom = election - today
    freedom -= datetime.timedelta(microseconds=freedom.microseconds)
    print freedom,
    time.sleep(1)
    print("\r"),
    sys.stdout.flush()

