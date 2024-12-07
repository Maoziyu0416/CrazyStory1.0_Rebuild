import sys
from algorithm.main import Game

class UI:
    def input_names(self):
        while True:
            names = []
            names.append(input("请输入主角名："))
            forbidden_names = {"9", "2", "20230609", "20230602", "yqx", "mzy", "YQX", "MZY",
                               "yaoqixuan", "Maoziyu", "Yaoqixuan", "Maoziyu", "YaoQiXuan",
                               "MaoZiYu", "YAOQIXUAN", "MAOZIYU", "姚祁轩", "毛子煜"}

            if names[0] in forbidden_names:
                print("滚")
                sys.exit()

            print("请输入配角名，输入end以结束输入")
            while True:
                name = input()
                if name in forbidden_names:
                    print(f"{name} 被禁止")
                    continue
                if name == "end":
                    if len(names) <= 2:
                        print("人数不足")
                    else:
                        print("选定成功")
                        return names
                names.append(name)

    def output(self, text):
        for line in text:
            print(line)


def main():
    ui = UI()
    names = ui.input_names()
    game = Game(names)
    game.start_game()
    logs = game.end_game()
    ui.output(logs)


if __name__ == "__main__":
    main()
