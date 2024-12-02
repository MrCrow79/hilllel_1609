from datetime import datetime, timedelta

today = datetime.now()
print(today.date())

seven_days_ago = today - timedelta(seconds=7 * 24 * 60 * 60)  # 7 днів
print(seven_days_ago.date())


def get_diff_between_2_days(time_A: datetime, time_B: datetime):
    return (time_B - time_A).seconds


time_a = datetime.now()
time_b = time_a + timedelta(seconds=32)

assert get_diff_between_2_days(time_a, time_b) < 35
