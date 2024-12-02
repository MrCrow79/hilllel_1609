from datetime import datetime, UTC
import time



row1 = '2024-11-30 17:55:59'  # UTC
row2 = '24-17-03T5:55:30.255 PM'  # UTC
row3 = '28-02-20 8:55:40.255 -0200'  # TZ = -2 години
row4 = '28-02-20'

# row1_transformed = datetime.fromisoformat(row1)
# print(type(row1_transformed))

row1_transformed = datetime.strptime(row1, '%Y-%m-%d %H:%M:%S')  # приймае строку, поверне class datetime
row2_transformed = datetime.strptime(row2, '%y-%d-%mT%H:%M:%S.%f %p')  # приймае строку, поверне class datetime
row3_transformed = datetime.strptime(row3, '%d-%m-%y %H:%M:%S.%f %z')  # приймае строку, поверне class datetime
row4_transformed = datetime.strptime(row4, '%d-%m-%y')  # приймае строку, поверне class datetime

# print(row3_transformed.tzinfo)
# print(row3_transformed.tzname())
# print(row3_transformed)
# print(datetime.strftime(row3_transformed, '%H:%M:%S'))
# print(row4_transformed)

# print(datetime.now(UTC))
#
# cur_time = datetime.now()
#
# cur_time_with_tz = time.localtime()


print(row3_transformed)


# print(datetime.strftime(row1_transformed, "%d/%m/%Y, %H:%M:%S"))  # приймає class datetime поверне строку в форматі
# print(datetime.strftime(row1_transformed, "%H:%M:%S"))  # приймає class datetime поверне строку в форматі
# print(type(row1_transformed))
# print(row1_transformed.date())
# print(row1_transformed.year)
# print(row1_transformed.month)
# print(row1_transformed.day)
# print(row1_transformed.hour)
# print(row1_transformed.microsecond)
