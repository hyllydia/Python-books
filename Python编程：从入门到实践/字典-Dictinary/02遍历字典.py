#coding:utf-8
print("6-5")
river_city={
    'yellow river':'luoyang',
    'changjiang':'shanghai',
    'zhujiang':'guangzhou'
}
for river,city in river_city.items():
    print("The " + river.title() +" runs through "+city.title() +"!")
for river in river_city.keys():
    print(river.title())
for city in river_city.values():
    print(city.title())

print("6-6")
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
survey_list=['jen','allen','blair','Phil','Eric']
for name in favorite_languages.keys():
    if name.lower() in [people.lower() for people in survey_list]:
        print(name.title()+" has been surveyed! Thanks a lot!")
    else:
        print(name.title()+", welcome you to join the survey!")