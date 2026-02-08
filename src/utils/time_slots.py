from datetime import datetime, timedelta


def generate_meal_times(wake_time: str, sleep_time: str):
    """
    Generates 5 meal times between wake and sleep.
    """
    fmt = "%H:%M"

    start = datetime.strptime(wake_time, fmt)
    end = datetime.strptime(sleep_time, fmt)

    if end <= start:
        end += timedelta(days=1)

    interval = (end - start) / 5

    times = [
        (start + interval * i).strftime(fmt)
        for i in range(5)
    ]

    return {
        "Breakfast": times[0],
        "Morning Snack": times[1],
        "Lunch": times[2],
        "Afternoon Snack": times[3],
        "Dinner": times[4],
    }
