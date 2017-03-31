# from wxpy import *
# # 初始化机器人，扫码登陆
# bot = Bot()
# reject = bot.groups().search('forever-rejected')[0]
# reject.send('大家好,我是机器人1');
# reject.send('大家好,我是机器人2');
# reject.send('大家好,我是机器人3');
# reject.send('大家好,我是机器人4');
# reject.send('大家好,我是机器人5');

import requests
r = requests.get('https://api.github.com/user', auth=('user', 'pass')
	print(r.status_code);