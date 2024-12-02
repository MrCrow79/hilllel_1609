import time
from datetime import datetime, UTC
import pytz


client_time = '2024-12-02 18:09:10.226311'
server_time = '2024-12-02 18:09:10.226311+00:00'

client_time_dt = datetime.strptime(client_time, '%Y-%m-%d %H:%M:%S.%f')
server_time_dt = datetime.strptime(server_time, '%Y-%m-%d %H:%M:%S.%f%z')


local_tz = time.localtime().tm_zone  #  дістатии локальну timezone
client_time_dt2 = pytz.timezone(local_tz).localize(client_time_dt)  # вказати локальну timezone

print(client_time_dt)
print(server_time_dt)
# print(client_time_dt2.tzinfo)

diff_between_times = server_time_dt - client_time_dt2
print(type(diff_between_times))
print(diff_between_times.seconds)

