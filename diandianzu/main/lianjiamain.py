from scrapy import cmdline
from threading import Timer

timer_interval = 3*24*60*60

def run():
    global timer
    # 重复构造定时器
    timer = Timer(timer_interval, run)
    timer.start()
    cmdline.execute('scrapy crawl lianjia'.split())
run()