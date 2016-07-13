#-*- coding: UTF-8 -*-   
import sys
import time
import urllib
import urllib2
import random
import requests
from bs4 import BeautifulSoup
import os
hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
{'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
{'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}]

def get_film(path,genre):
    page_num=0
    try_times = 0
    try:
        os.mkdir(path+'/'+genre)    
    except(OSError), ose:
        print "Here Already has a Dict"
    try:
        os.mkdir(path+'/'+genre+'pic')
    except(OSError), ex:
        print "Here is a Dict too"
    while(1):
        movie_list=[]
    	url="https://movie.douban.com/tag/"+genre+"?start="+str(page_num*20)+"&type=T"
    	time.sleep(random.uniform(1, 5))
    	try:
            req = urllib2.Request(url, headers=hds[page_num%len(hds)])
            source_code = urllib2.urlopen(req).read()
            plain_text=str(source_code)   
        except (urllib2.HTTPError, urllib2.URLError), e:
            print e
            continue
        soup = BeautifulSoup(plain_text)
        list_soup=soup.find('div',{'class':['']})
        try_times+=1
        if list_soup==None and try_times<120:
           continue
        elif list_soup==None or len(list_soup)<=1:
           break
        for movie_info in list_soup.findAll('table',''):
            movie_title=movie_info.find('a','').contents[0].strip().rstrip('/').strip().replace('/','').encode('utf-8')
            movie_score=movie_info.find('span',{'class':'rating_nums'})
            if movie_score==None:
                movie_score="0.0"
            elif movie_score.string==None:
                movie_score="0.0"
            else:
                movie_score=movie_score.string
            movie_description=movie_info.find('p').string
            if movie_description==None:
                movie_description="No description"
            desc_list = movie_description.split('/')
            date=desc_list[0].encode('utf-8')
            movie_url=movie_info.find('a',{'class':['']}).get('href')
            image_url=movie_info.find('img').get('src')
            movie_list.append([movie_title,movie_score,date,movie_url,image_url])
        page_num+=1

        for i in range(len(movie_list)):
            #try:
             #   os.mkdir(path+'/'+movie_list[i][0])
            #except:
            #    print "Already Store"
            #    continue
            if not os.path.exists(path+'/'+genre+"/%s.txt"%movie_list[i][0]):
                f=file(path+'/'+genre+"/%s.txt"%movie_list[i][0],"w+")
                for j in range(4):
                    f.write(movie_list[i][j]+'\n')
                f.close()
            if movie_list[i][4]=="https://img3.doubanio.com/f/shire/afee3c96d502c5afca2219d69e57cdaea0f756a4/pics/movie-default-medium.gif":
                continue
            else:
                time.sleep(random.uniform(1, 2))                           
                if not os.path.exists(path+'/'+genre+'pic'+"/%s.jpg"%movie_list[i][0]):                    
                    urllib.urlretrieve(movie_list[i][4],path+'/'+genre+'pic'+"/%s.jpg" % movie_list[i][0])             
        
        print 'Downloading Information From Page %d' % page_num
    return
path=raw_input("Please Enter Your Absolute Store Path:")
print "想要的电影类型请看：https://movie.douban.com/tag/"
genre=raw_input("What genre you want?(Eg.科幻 只能输一个)")
get_film(path,genre)
