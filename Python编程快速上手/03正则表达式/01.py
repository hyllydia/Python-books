#coding:utf-8
import re
def find():
    html = '''<div id="songs-list">
        <h2 class="title">经典老歌</h2>
        <p class="introduction">
            经典老歌列表
        </p>
        <ul id="list" class="list-group">
            <li data-view="2">一路上有你</li>
            <li data-view="7">
                <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
            </li>
            <li data-view="4" class="active">
                <a href="/3.mp3" singer="齐秦">往事随风</a>
            </li>
            <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
            <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
            <li data-view="5">
                <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
            </li>
        </ul>
    </div>'''
    print('*')
    # regex=re.compile(r'<a.*?singer="(.*?)">(.*?)</a>')
    # result1=regex.search(html)
    # print(result1.group(1),result1.group(2))
    # result2=regex.findall(html)
    # print(result2)

    #不使用compile()函数
    patten='<a.*?singer="(.*?)">(.*?)</a>'
    res1=re.search(patten,html)
    print(res1.group(1),res1.group(2))
    res2=re.findall(patten,html)
    print(res2)


if __name__=="__main__":
    find()