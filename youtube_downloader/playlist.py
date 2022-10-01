from pytube import Playlist as YoutubePlaylist

class Playlist:
    
    def __init__(self, playlist_link):
        self.link = playlist_link
        self.setPlaylist()
        self.getTitle()
        self.getVideoUrls()
        self.getVideoCount()
        self.getTitle()
        
        
    def getDetails(self):
        print(self.title)
        print(self.video_count)
        print(self.video_links)
    
    def getTitle(self):
        self.title=self.playlist.title

    def setPlaylist(self):
        self.playlist = YoutubePlaylist(self.link)
    
    def getVideoUrls(self):
        self.video_links = self.playlist.video_urls
        
    def getVideoCount(self):
        self.video_count = len(self.video_links)

        

link = "https://youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ"
playlist = Playlist(link)
playlist.getDetails()


    