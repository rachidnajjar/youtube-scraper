'''
Created on 24/12/2018

@author: Rachid
'''
import requests
from bs4 import BeautifulSoup as bs
from pytube import YouTube

# query YouTube for a particular search string
base = "https://www.youtube.com/results?search_query="
qstring = "boddingtons+advert"
r = requests.get(base+qstring)

# extract the html of the search results page using BeautifulSoup
page = r.text
soup=bs(page,'html.parser')

# extract the links to the individual videos
vids = soup.findAll('a',attrs={'class':'yt-uix-tile-link'})

videolist=[]
for v in vids:
    tmp = 'https://www.youtube.com' + v['href']
    videolist.append(tmp)
    print(tmp)

count=0
for item in videolist:
 
    # increment counter:
    count+=1
 
    # initiate the class:
    yt = YouTube(item)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
 
    # have a look at the different formats available:
    #formats = yt.get_videos()
 
    # grab the video:
    #video = yt.get('mp4', '360p')
 
    # set the output file name:
    #yt.set_filename('Video_'+str(count))
 
    # download the video:
    #video.download('./')