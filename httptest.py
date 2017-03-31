#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'yuanjunwen'

from urllib import request
import json,time,os,sched,datetime
from wxpy import *
cityName = '上海'
url = 'http://api.map.baidu.com/telematics/v3/weather?location=%E5%8D%97%E4%BA%AC&output=json&ak=EDb6761c5b033eaa0cd169651f54c3d2'

#res = request.urlopen('http://api.map.baidu.com/telematics/v3/weather?location=%E5%8D%97%E4%BA%AC&output=json&ak=FK9mkfdQsloEngodbFl4FeY3').read()
#
bot = Bot(True)
my_friend1 = bot.friends().search('潘童怡')[0]
my_friend2 = bot.friends().search('Lynn颖儿')[0]
my_friend3 = bot.groups().search('forever-rejected')[0]
my_friend4 = bot.groups().search('袁氏家族')[0]

def sendWeather(now):
    with request.urlopen(url) as f:
    	print (now)
    	res = f.read().decode('utf-8')
    	res = json.loads(res)
    	error = res['error']
    	result = res['results']
    	cold = result[0]['index'][0]['zs'] #较冷
    	#for
    	todayWeather = result[0]['weather_data'][0] #
    	todayWeatherTem = todayWeather['temperature'] # 16 ~ 6℃"
    	todayWeatherRain = todayWeather['weather'];    

    	tomorrowWeather = result[0]['weather_data'][1] #    
    

    	Today = '今天:' + cold + ',' + todayWeatherTem + ',' + todayWeatherRain + ''
    	tomorrow = '明天:' + tomorrowWeather['temperature'] + ',' + tomorrowWeather['weather'][0]
    	sendMsg = Today + '\n' + tomorrow + '\n' + 
    	print (sendMsg)


    	my_friend1.send(sendMsg)
    	my_friend2.send(sendMsg)
    	my_friend3.send(sendMsg)
    	my_friend4.send(sendMsg)


# sendWeather()

# while True:
# 	os.system(sendWeather)
# 	time.sleep(10)

# schedule = sched.scheduler(time.time, time.sleep) 
# def exe(): 
#  # enter用来安排某事件的发生时间，从现在起第n秒开始启动  第一个参数,延迟时间,第二个参数 优先级
#  schedule.enter(0, 0, sendWeather) 
#  schedule.enter(10, 0, sendWeather) 
#  schedule.enter(20, 0, sendWeather) 
#  schedule.enter(30, 0, sendWeather) 
#  # 持续运行，直到计划时间队列变成空为止 
#  schedule.run() 
# exe()   
# 
# 
# 
# 
	# if error:
	# 	print('error||' + error)
	# else:
	#    print()
	#print('Data:', f.read().decode('utf-8'))
	#print (res.status)
	#
	#
	#
	#
	#
def timerFunc(schedule_Timer):
	flag = 0
	while True:
		now = datetime.datetime.now()
		if now == schedule_Timer:
			print ('=========')
			sendWeather(now)
			flag = 1
		else:
			if flag == 1:
				schedule_Timer = schedule_Timer + datetime.timedelta(hours=8)
				flag = 0
schedule_Timer = datetime.datetime(2017,3,31,23,30,50);
timerFunc(schedule_Timer)