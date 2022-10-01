from pytube import YouTube
from PIL import Image
import requests
from io import BytesIO

class Video:
    
    def __init__(self, video_link):
        self.link = video_link
        self.setVideoObject()
        self.getTitle()
        self.getThumbnailUrl()
        self.getThumbnail()
        self.getDuration()
        self.getFileSize()
        
    def getDetails(self):
        print(self.title)
        print(self.filesize)
        print(self.duration)
        self.displayThumbnail()

    def setVideoObject(self):
        self.video = YouTube(self.link)

    def getTitle(self):
        self.title=self.video.title

    def getThumbnailUrl(self):
        self.thumbnail_url = self.video.thumbnail_url
        
    def getThumbnail(self):    
        response = requests.get(self.thumbnail_url)
        self.thumbnail = Image.open(BytesIO(response.content))
    
    def displayThumbnail(self):  
        self.thumbnail.show()
        
    def getFileSize(self):
        filesize_in_bits = self.video.streams.get_highest_resolution().filesize
        if filesize_in_bits//1000000 >= 1000:
            self.filesize = f"{filesize_in_bits/1000000000}" + " GB"
        else:
            self.filesize = f"{filesize_in_bits/1000000}" + " MB"

    def getDuration(self):
        duration = self.video.length
        hours=0
        minutes=0
        seconds=0
        if duration // 3600 > 0:
            hours = duration // 3600
            duration -= hours*3600
        if duration // 60:
            minutes = duration // 60
            duration -= minutes*60
        if duration > 0 :
            seconds = duration 
            duration -= seconds
        self.duration = {"hours":hours,"minutes":minutes,"seconds":seconds}
        


link = "https://www.youtube.com/watch?v=aQB22y4liXA&list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ&index=18"
video = Video(link)
video.getDetails()
