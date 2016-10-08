# Douban
简单的一个爬取豆瓣所有电影的爬虫。用的是Beautifulsoup，简单用了浏览器伪装和间隔时间访问 
A simple web crawling of scraping all movies info from Douban.com（120000+ movies） using BeautifulSoup, and  using webbrowser simulation and time gap accessing.
一开始要输入你想保存的绝对路径，然后输入你想爬取得电影类型：比如科幻，喜剧，剧情。等等 
First step: type in your absolute path that you want to store those info, then type what genre you want:eg. comdy（喜剧），scare(惊悚)
然后就开始抓取，可能有warning，忽略它。 
Then it starts
爬取的是封面，电影标题，时间，评分，和豆瓣网址。 
Film cover will be downloaded into a file, and each film's name, launch time, score, and Douban link will be stored in a text file separately.
截图放出来了 
Screenshots are provided.
TO DO
接下去想做的是自动化一类，比如爬取后一个电影后自动在网上搜索BT资源，然后加入百度网盘离线下载到自己网盘里。 
Next I want to do is Automatic batch producing, eg. type in a score s, then it will get all the movie whose score is higher than s, then search in the p2p(bt) network get the resource and copy it into computer.
还有就是把电影信息放进Excel之类 

然后分析提取信息，比如从国家角度看哪些国家盛产高分电影，艺术电影导演经常分布在哪个国家等等。
Finally, analysis.
eg.which country can produce high quality film, art-movie directors are always born in which region?
