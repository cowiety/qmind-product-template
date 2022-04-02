import pandas as pd
import holidays
import datetime

#def getHoliday():
# get current time
now = datetime.datetime.now()
start_time = now - datetime.timedelta(days=1)
end_time = now

# create Series of timestamps ranging between 24 hours ago to the last hour
dates = pd.date_range('{month}/{day}/{year} {hour}:00'
                      .format(day=start_time.day, month=start_time.month, year=start_time.year,
                              hour=start_time.hour-1),
                      '{month}/{day}/{year} {hour}:00'
                      .format(day=end_time.day, month=end_time.month, year=end_time.year, hour=23),
                      freq='H')
# fill Dataframe
df = pd.DataFrame()
df['Time'] = dates

# import Canadian holiday data
can_holidays = holidays.Canada()
# compare each timestamp with those found in can_holidays (if it is a holiday, df.isHoliday = 1, else,
# df.isHoliday = 0)
df['isHoliday'] = df.apply(lambda row: 1 if (row['Time'] in can_holidays) else 0, axis=1)
#df.drop(['Time'], inplace=True, axis=1)
df.to_csv('holiday.csv', index=False, header=False)
#return df
