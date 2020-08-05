"""
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。
TongLao类里面有2个方法，
see_people方法，需要传入一个name参数，
如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“呸，贱人”，
如果传入“丁春秋”，打印“叛徒！我杀了你”

fight_zms方法（天山折梅手），
调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。
需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。

"""


#定义Tonglao类
class Tonglao:
    def __init__(self,tl_hp,tl_power):
        self.tl_hp = tl_hp
        self.tl_power = tl_power

    # 定义see_people方法
    def see_people(self,name):
        if name == "WYZ":
            print("师弟")
        elif name == "李秋水":
            print("呸，贱人")
        elif name == "丁春秋":
            print("叛徒！我杀了你")

"""
fight_zms方法（天山折梅手），
调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。
需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
"""

    #  定义fight_zms方法（天山折梅手）
    def fight_zms(self,zms_hp,zms_power,my_hp,my_power):
        self.zms_hp = self.tl_hp / 2
        self.zms_power = self.tl_power * 10
        #传入敌人参数
        self.my_hp = my_hp
        self.my_power = my_power
        # 进行一回合对打
        # 童姥的血量 = 童姥用折梅手技能的血量 - 你的力量
        self.zms_hp = self.zms_hp - my_power
        # 你的剩余血量 = 你的血量 - 童姥用折梅手技能的力量
        self.your_hp = my_hp - self.zms_power
        # 打完比较血量，血多胜
        if self.zms_hp < self.my_hp:
            print("天山童姥胜出")
        else:
            print("我赢了")

# 实例化童姥，传童姥血量和武力值
result = Tonglao(800,300)
# 调用see_people 参数是丁春秋
result.see_people("丁春秋")
result.fight_zms(500,500,500,500)






