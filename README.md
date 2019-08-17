# big-letou
对大乐透彩票  

requests模块获取大乐透开奖网站的html文本：  
```.env
url = 'http://kaijiang.500.com/shtml/dlt/19095.shtml'
resp = requests.get(url)
html_text = resp.content.decode('GBK')
```
注意在浏览器的console里获取网站的charset，自行对resp.content解码，有些网站没有在html head里返回
编码，resp.text的结果里可能会有乱码：  
```.env
> document.characterSet
< "GBK"
```  
观察html的构成，前区的5个号码在class="ball_red"的li标签里，
后区的2个号码在class="ball_blue"的li标签里，这里通过正则分别获取前区
和后区号码的列表即可：  
```.env
reg = re.compile(r'<li class="ball_blue">(\d+)</li>')
back_balls = reg.findall(html_text)
result_nums = ' '.join(front_balls) + ' + ' + ' '.join(back_balls)
print('本期开奖号码为：\033[0;31m%s\033[0m' % result_nums)
```
最后让用户输入一注号码，跟开奖结果进行比较，输出结果：  
```.env
def result_handler(results, num, is_matched):
    if is_matched:
        res = '\033[0;31m%s\033[0m' % num
    else:
        res = '\033[0;32m%s\033[0m' % num
    results.append(res)
```