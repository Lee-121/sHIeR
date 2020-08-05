

# 用类和面向对象的思想，“描述”生活中任意接触到的东西
# 比如动物、小说里面的人物，不做限制，随意发挥），数量为5个

# 定义House类

class House:
    window = "明亮的"
    door = "安全的"
    people = "有人"
    ceiling = "天花板"

    def people(self):
        print("房间里有人吗？")

    def high_wind(self):
        print("要关窗吗？")

    def open_door(self):
        print("谁开的门？")

    def upstairs(self):
        print("楼上噪音好大呀！！！")

    def back_home(self):
        print("要回家了！！！")
me = House()
me.back_home()
me.high_wind()

