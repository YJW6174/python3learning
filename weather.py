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
	}]
for obj in data:
	obj['url'] = api + urllib.parse.quote(obj['city'])
	if obj['type'] == 'friends':
		obj['chatobj'] = bot.friends().search(obj['name'])[0]
	elif obj['type'] == 'groups':
		obj['chatobj'] = bot.groups().search(obj['name'])[0]

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
    	tomorrow = '明天:' + tomorrowWeather['temperature'] + ',' + tomorrowWeather['weather']
    	sendMsg = Today + '\n' + tomorrow + '\n' + '不管天气如何,祝你天天好心情~'
    	print (sendMsg)
    	obj['chatobj'].send(sendMsg)

sendWeather(obj)
schedule = sched.scheduler(time.time, time.sleep)

dayseconds = 24 * 60 * 60

def exe(): 
 # enter用来安排某事件的发生时间，从现在起第n秒开始启动  第一个参数,延迟时间,第二个参数 优先级
 schedule.enter(0, 0, sendWeather,data) 
 schedule.enter(dayseconds / 2, 0, sendWeather,data) 
 schedule.enter(dayseconds, 0, sendWeather,data)
 schedule.enter(dayseconds * 1.5, 0, sendWeather,data)
 # 持续运行，直到计划时间队列变成空为止 
 schedule.run() 
exe()   



