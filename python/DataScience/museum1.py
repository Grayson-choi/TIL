import pandas as pd
MuseumData = pd.read_csv("https://raw.githubusercontent.com/Grayson-choi/Data/master/Dataset/museum1.csv")

University = MuseumData["시설명"].str.contains('대학교')

MuseumData["분류"] = University
MuseumData.loc[(MuseumData["분류"]==True), "분류"] = "대학"
MuseumData.loc[(MuseumData["분류"]==False), "분류"] = "일반"

MuseumData