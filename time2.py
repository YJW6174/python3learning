#! /usr/bin/env python
#coding=utf-8
import time, os, sched 
  
# 第一个参数确定任务的时间，返回从某个特定的时间到现在经历的秒数 
# 第二个参数以某种人为的方式衡量时间 
schedule = sched.scheduler(time.time, time.sleep) 
  
def perform_command(cmd, inc): 
 # 安排inc秒后再次运行自己，即周期运行 
 schedule.enter(inc, 0, perform_command, (cmd, inc)) 
 os.system(cmd) 
   
def timming_exe(cmd, inc = 60): 
 # enter用来安排某事件的发生时间，从现在起第n秒开始启动 
 schedule.enter(1, 0, perform_command, (cmd, inc)) 
 schedule.enter(10, 1, perform_command, (cmd, inc)) 
 schedule.enter(20, 2, perform_command, (cmd, inc)) 
 schedule.enter(30, 3, perform_command, (cmd, inc)) 

 # 持续运行，直到计划时间队列变成空为止 
 schedule.run() 

def console2():
	print ('ok')
print("show time after 10 seconds:") 
timming_exe(console2, 10)