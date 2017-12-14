import pymongo

# client=pymongo.MongoClient('localhost:27017')
# db=client['zhengshen']
# collection=db['info']
# counts=len([info for info in collection.find()])
# print(counts)
from gevent import monkey
import re
import requests
import gevent,time
monkey.patch_all()
def test(url):
    print('get:%s' %url)
    req=requests.get(url)

start_time=time.time()
gevent.joinall([gevent.spawn(test,'http://tingshen.court.gov.cn/live/1689812'),
                gevent.spawn(test,'http://tingshen.court.gov.cn/live/1667543'),
                gevent.spawn(test,'http://tingshen.court.gov.cn/live/1670720')])

print('花费：',time.time()-start_time)
start_time2=time.time()
urls=['http://tingshen.court.gov.cn/live/1689812',
     'http://tingshen.court.gov.cn/live/1667543',
     'http://tingshen.court.gov.cn/live/1670720']
for url in urls:
    print('get:',url)
    req=requests.get(url)
print('第二次花费：',time.time()-start_time2)
import threading
import queue
all_url=queue.Queue()

def url_get():
    all_url.put(url for url in urls)

def thread(number):
    if all_url.qsize()>=number:
        t=threading.Thread(target=url_get,args=(all_url.get(),))
        t.setDaemon(True)
        t.start()
        t.join()

def main():
    m = time.time()
    number=3
    thread(number)
    print('第三次：',time.time()-m)



main()