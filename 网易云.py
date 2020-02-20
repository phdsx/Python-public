from tkinter import *
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
 
 
def download():
    url = entry.get()
    new_url = url.replace('/#', '')
 
    header = {
        'Host': 'music.163.com',
        'Referer': 'https://music.163.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
    }
 
    res = requests.get(new_url, headers=header).text
 
    r = BeautifulSoup(res, "html.parser")
    music_dict = {}
    result = r.find('ul', {'class', 'f-hide'}).find_all('a')
    for music in result:
        print(music)
        music_id = music.get('href').strip('/song?id=')
        music_name = music.text
        music_dict[music_id] = music_name
    for song_id in music_dict:
        song_url = "http://music.163.com/song/media/outer/url?id=%s" % song_id
        path = "E:\\python demo\wangyiyunmusic\%s.mp3" % music_dict[song_id]
 
        # 添加数据
        text.insert(END, "正在下载：%s" % music_dict[song_id])
        text.see(END)
        text.update()
 
        urlretrieve(song_url, path)
 
 
root = Tk()
root.title("网易云音乐下载器")
root.geometry("550x400+550+230")
 
label = Label(root, text="歌单URL", font=('宋体', 15))
label.grid()
 
entry = Entry(root, font=('微软雅黑', 20))
entry.grid(row=0, column=1)
 
text = Listbox(root, font=("微软雅黑", 15), width=45, height=10)
text.grid(row=1, columnspan=2)
 
button = Button(root, text="开始下载", font=("微软雅黑", 15), command=download)
button.grid(row=2, column=0, sticky=W)
 
button1 = Button(root, text="退出", font=("微软雅黑", 15), command=root.quit)
button1.grid(row=2, column=1, sticky=E)
 
 
mainloop()
