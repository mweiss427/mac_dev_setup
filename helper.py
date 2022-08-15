import os
import time


def daysSinceLastUpdated(path):
    now = time.time()
    # Both the variables would contain time
    # elapsed since EPOCH in float
    time_last_changed = os.path.getmtime(path)

    # Get the difference between now and when the time was last modified.
    elapsed_time = now - time_last_changed

    # Converting the time in seconds to a timestamp for printing
    days = 0
    if elapsed_time >= 86400:
        days = int(elapsed_time / 86400)

    return days
