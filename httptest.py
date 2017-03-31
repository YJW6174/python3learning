#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'yuanjunwen'

import urllib
from urllib import request
import json,time,os,sched,datetime
from wxpy import *

bot = Bot(True)

api = 'http://api.map.baidu.com/telematics/v3/weather?output=json&ak=EDb6761c5b033eaa0cd169651f54c3d2&location='
data = [{
	"name": 'Lynn颖儿',
	"city": '南京',
	"type": 'friends'
	},
	{
	"name": '袁氏家族',
	"city": '南通',
	"type": 'groups'
	},
	{
	"name": 'forever-rejected',
	"city": '上海',
	"type": "groups"
	}]
for obj in data:
	obj['url'] = api + urllib.parse.quote(obj['city'])
	if obj['type'] == 'friends':
		obj['chatobj'] = bot.friends().search(obj['name'])[0]
	elif obj['type'] == 'groups':
		obj['chatobj'] = bot.groups().search(obj['name'])[0]
#res = request.urlopen('http://api.map.baidu.com/telematics/v3/weather?location=%E5%8D%97%E4%BA%AC&output=json&ak=FK9mkfdQsloEngodbFl4FeY3').read()
#
#
#sendWeather();

def sendWeather(obj):
    with request.urlopen(obj['url']) as f:
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
    	sendMsg = Today + '\n' + tomorrow + '\n' + '挣扎吧,在血和暗的深渊里'
    	print (sendMsg)
    	obj['chatobj'].send(sendMsg)


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
			for obj in data:
				sendWeather(obj)
			flag = 1
		else:
			if flag == 1:
				schedule_Timer = schedule_Timer + datetime.timedelta(hours=9)
				flag = 0
schedule_Timer = datetime.datetime(2017,4,1,0,28,0);
timerFunc(schedule_Timer)