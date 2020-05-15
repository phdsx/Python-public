# -*- encoding = utf-8 -*-
#   作者   ： phdsx
# 创建时间  ： 2020/5/12 21:08
# 文件名称  ： run.py
# 所属工程  ： Python-learning
# 版本号    ： Ver.
import cloudmusic as cm


def get_play_list(id):
    playlist = []
    musiclist = cm.getPlaylist(id)  # 2323298184
    for i in range(len(musiclist)):
        print(f'第{i + 1}首:', musiclist[i].name)
        playlist.append(musiclist[i].id)
    return playlist

def get_song_info(id):
    song=cm.getMusic(id)
    return song.name
def download(id, level='0'):
    try:
        music = cm.getMusic(id)
        quailty = {'0': "standard", '1': "higher", '2': "exhigh", '3': "lossless"}
        music.download(level=quailty.get(level))
    except:
        print(get_song_info(id),'下载失败')


if __name__ == '__main__':
    listid = str(input('请输入歌单id：'))

    print('0: 标准\n1:较高\n2: 极高\n3: 无损')
    level=str(input('请选择下载质量（0~3）：'))
    for each in get_play_list(listid):
        download(each,level )
