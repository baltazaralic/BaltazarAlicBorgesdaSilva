#Guilherme Gonzaga Silva 11621EMT021 
#prog17.py

import datetime
import pytz

#1)
# d = datetime.date(2021, 3, 15)
# print(d)
# tday = datetime.date.today()
# print(tday) #2021-03-15
# print(tday.year()) #2021 
# print(tday.weekday()) #0, mostra dia da semana sendo 0 segunda

#2)
# tday = datetime.date.today()
# datetime.timedelta(days=7)
# tdelta = datetime.timedelta(days=7)
# print(tday + tdelta)
# date2 = date1 + timedelta
# timedelta = date1 + date2

#3)
# tday = datetime.date.today()
# bday = datetime.date(2021, 7, 23)
# till_bday = bday - tday
# print(till_bday.days) #faltam 130 dias

#4)
# t = datetime.time(9, 30, 45, 100000)
# dt = datetime.time(2021, 3, 15, 16, 33, 20, 100000)
# tdelta = datetime.timedelta(hour=12)
# print(t.hour)
# print(dt+tdelta)

#5)
# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# dt_utcnow = datetime.datetime.utcnow()
# print(dt_today)
# print(dt_now)
# print(dt_utcnow)

#6)
# dt = datetime.datetime(2021, 3, 15, 16, 33, 20, tzinfo=pytz.UTC)
# print(dt)
# dt_now = datetime.datetime.now(tz=pytz.UTC)
# print(dt_now)
# dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# print(dt_utcnow)
# dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
# print(dt_mtn)
# dt_mtn = datetime.datetime.now()
# mtn_tz = pytz.timezone('US/Mountain')
# dt_mtn = mtn_tz.localize(dt_mtn)
# # print(dt_mtn)
# dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
# # print(dt_east)
# print(dt_mtn.strftime('%B %d, %Y'))
# dt_str = 'March 15, 2021'
# dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
# print(dt)
# strftime - Datetime to String
# strptime - String to Datetime