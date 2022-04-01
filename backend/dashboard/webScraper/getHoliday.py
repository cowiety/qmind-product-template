import pandas as pd
import holidays
import datetime

def getHoliday():
    # get current time
    now = datetime.datetime.now()
    # create Series of timestamps ranging between 24 hours ago to the last hour
    dates = pd.date_range('{month}/{day}/{year} {hour}:00'\
                          .format(day=datetime.datetime.today().day-1, month=datetime.datetime.today().month, year=(datetime.datetime.today().year), hour=(datetime.datetime.now().hour - 5)),\
                          '{month}/{day}/{year} {hour}:00'\
                          .format(day=datetime.datetime.today().day, month=datetime.datetime.today().month, year=datetime.datetime.today().year, hour=(datetime.datetime.now().hour - 5)),\
                          freq='H')
    # fill Dataframe
    df = pd.DataFrame()
    df['Time'] = dates

    # import Canadian holiday data
    can_holidays = holidays.Canada()
    # compare each timestamp with those found in can_holidays (if it is a holiday, df.isHoliday = 1, else, df.isHoliday = 0)
    df['isHoliday'] = df.apply(lambda row: 1 if(row['Time'] in can_holidays) else 0, axis = 1)
    return df