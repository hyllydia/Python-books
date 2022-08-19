#coding:utf-8
print("8-6")
def city_country(city,country):
    return (city+', '+country)
if __name__=="__main__":
    luoyang=city_country('luoyang','China')
    print(luoyang)

print("8-7")
def make_album(singer,album_name,num=0):
    album={'singer':singer,'album_name':album_name}
    if num:
        album['num']=num
    return album
if __name__=="__main__":
    album1 = make_album('Jay','Fantancy')
    print(album1)
    album2 = make_album('Jay','Yehuimei',10)
    print(album2)

print('8-8')
while True:
    print("Please input info for this album:")
    print("(If you wanna to quit ,please input quit!)")
    singer_name=input("Enter the singer_name:")
    if singer_name=='quit':
        break
    album_name=input("Enter the album_name:")
    if album_name=='quit':
        break
    def make_album(singer_name,album_name):
        album = {'singer':singer_name,'album_name':album_name}
        return album
    if __name__ =="__main__":
        album_info = make_album(singer_name,album_name)
        print(album_info)