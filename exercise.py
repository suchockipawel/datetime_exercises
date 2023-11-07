'''
### Task 1 (Timestamps)
If a shop sold items at the following timestamps
    1. 3499005059 item A
    2. 4899797989 item B
    3. 3499499607 item C
    4. 1005969876 item D
    5. 4000005555 item E
    a. give the corresponding dates in the following format
        1. 25 december, 2022. 11:00:00
        2. 2023/11/02 23:00:00
    b. tell us which item was sold first and last
    
    '''
from datetime import datetime

timestamps = (3499005059, 4899797989, 3499499607, 1005969876, 4000005555)
formatted_dates = []
for timestamp in timestamps:
    formatted_date = datetime.utcfromtimestamp(timestamp).strftime('%d %B, %Y. %H:%M:%S')
    formatted_dates.append(formatted_date)
    print(formatted_dates)


first_sold = formatted_dates[formatted_dates.index(min(formatted_dates))]
print(first_sold)

last_sold = formatted_dates[formatted_dates.index(max(formatted_dates))]
print(last_sold)

'''
If a meetting occurs every 25 minutes between 25 december, 2022. 08:00:00 and 
    25 december, 2022. 20:00:00, give me all the possible meeting date and time in timestamps
'''

from datetime import datetime, timedelta

start_time = datetime(2022, 12, 25, 8, 0, 0)
end_time = datetime(2022, 12, 25, 20, 0, 0)

meeting_interval = timedelta(minutes=25)

meeting_times = []
current_time = start_time

while start_time <= end_time:
    timestamp = int(start_time.timestamp())
    meeting_times.append(start_time.strftime('%d %B, %Y. %H:%M:%S'))
    start_time += meeting_interval

for timestamp in meeting_times:
    print(timestamp)

'''
### Task 2 (time delta)
a. if i make an order for a shirt on 25 december, 2022. 11:00:00 and it will take 
93 hours to get to me, what will be the arrival date and time of the order?
(Please give your arrival date in this format 'Mon Dec 31 17:41:00 2018')
'''


order_time = datetime(2022, 12, 25, 11, 0, 0)
delivery_time = timedelta(hours=93)
arrival_time = order_time + delivery_time

formatted_arrival_time = arrival_time.strftime('%a %b %d %H:%M:%S %Y')
print(formatted_arrival_time)


'''
b. If a meetting occurs every 55 minutes between 25 december, 2022. 08:00:00 and 
    25 december, 2022. 20:00:00, give me all the possible meeting date and time using this format (25 december, 2022. 11:00:00)
'''



start_time = datetime(2022, 12, 25, 8, 0, 0)
end_time = datetime(2022, 12, 25, 20, 0, 0)
meeting_interval = timedelta(minutes=55)

meeting_times = []
current_time = start_time

while current_time <= end_time:
    formatted_time = current_time.strftime('%d %B, %Y. %H:%M:%S')
    meeting_times.append(formatted_time)
    current_time += meeting_interval
for meeting_time in meeting_times:
    print(meeting_time)


'''
### Task 3 (TimeZone)
a. if a movie is meant to premier at 1 december, 2022. 11:00:00 (American time),
    what time can a person in Europe or Africa watch that movie
'''

from datetime import datetime
import pytz

american_time = pytz.timezone('America/New_York')
premier_time = american_time.localize(datetime(2022, 12, 1, 11, 0, 0))


european_time = pytz.timezone('Europe/Berlin')
african_time = pytz.timezone('Africa/Nairobi')

european_premier_time = premier_time.astimezone(european_time)
african_premier_time = premier_time.astimezone(african_time)

print(european_premier_time.strftime('%d %B, %Y. %H:%M:%S'))
print(african_premier_time.strftime('%d %B, %Y. %H:%M:%S'))
