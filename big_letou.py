import requests
import re

url = 'http://kaijiang.500.com/shtml/dlt/19095.shtml'
resp = requests.get(url)
html_text = resp.content.decode('GBK')

reg = re.compile(r'<span class="span_right">(.+)</span>')
dt = reg.findall(html_text)[0][5:15]
print('开奖日期为：', dt)

reg = re.compile(r'<li class="ball_red">(\d+)</li>')
front_balls = reg.findall(html_text)

reg = re.compile(r'<li class="ball_blue">(\d+)</li>')
back_balls = reg.findall(html_text)
result_nums = ' '.join(front_balls) + ' + ' + ' '.join(back_balls)
print('本期开奖号码为：\033[0;31m%s\033[0m\n' % result_nums)

nums = input("请输入一注号码，号码之间以空格分割\n")
nums = nums.split(' ')

front_nums = nums[:5]
back_nums = nums[5:]


def result_handler(results, num, is_matched):
    if is_matched:
        res = '\033[0;31m%s\033[0m' % num
    else:
        res = '\033[0;32m%s\033[0m' % num
    results.append(res)


results = []
for num in front_nums:
    is_matched = True if num in front_balls else False
    result_handler(results, num, is_matched)
for num in back_nums:
    is_matched = True if num in back_balls else False
    result_handler(results, num, is_matched)

print('\n\033[0;31m红色\033[0m为中奖号码，\033[0;32m绿色\033[0m为非中奖号码，你这注号码的结果为...:')
print(' '.join(results[0:5]) + ' + ' + ' '.join(results[5:]))
