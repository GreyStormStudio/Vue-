k = {0: '有刺', 1: '水生', 2: '喜阳', 3: '药用', 4: '木本', 5: '可食用', 6: '有白色粉末', 7: '叶片针状', 8: '结果实', 9: '黄色花',
     10: '种子有果皮', 11: '种子无果皮', 12: '无茎叶', 13: '无根', 14: '有托叶', 15: '吸引菜粉蝶', 16: '十字形花冠', 17: '缺水环境', 18: '被子植物', 19: '裸子植物',
     20: '藻类植物', 21: '蔷薇科', 22: '十字花科', 23: '仙人掌科', 24: '玫瑰', 25: '荷花', 26: '仙人掌', 27: '水棉', 28: '苹果树', 29: '油菜', 30: '海带', 31: '松树'}

def logout(num, ans):
    for n in num:
        print(k[n], end=' ')
    print('=>', k[ans])

def Solve(rule):
    if len(rule) == 1:
        print('结果为:', k[rule[0]])
        return
    if 10 in rule:
        logout([10], 18)
        rule.remove(10)
        rule.append(18)
        return Solve(rule)
    if 11 in rule:
        logout([11], 19)
        rule.remove(11)
        rule.append(19)
        return Solve(rule)
    if (12 in rule) and (13 in rule):
        logout([12, 13], 20)
        rule.remove(12)
        rule.remove(13)
        rule.append(20)
        return Solve(rule)
    if (18 in rule) and (14 in rule) and (0 in rule):
        logout([18, 14, 0], 24)
        rule.remove(18)
        rule.remove(14)
        rule.remove(0)
        rule.append(24)
        return Solve(rule)
    if (18 in rule) and (1 in rule) and (5 in rule) and (8 in rule):
        logout([18, 1, 5, 8], 25)
        rule.remove(18)
        rule.remove(1)
        rule.remove(5)
        rule.remove(8)
        rule.append(25)
        return Solve(rule)
    if (18 in rule) and (17 in rule) and (0 in rule):
        logout([18, 17, 0], 26)
        rule.remove(18)
        rule.remove(17)
        rule.remove(0)
        rule.append(26)
        return Solve(rule)
    if (20 in rule) and (1 in rule) and (3 in rule):
        logout([20, 1, 3], 27)
        rule.remove(20)
        rule.remove(1)
        rule.remove(3)
        rule.append(27)
        return Solve(rule)
    if (18 in rule) and (14 in rule) and (4 in rule) and (5 in rule) and (8 in rule):
        logout([18, 14, 4, 5, 8], 28)
        rule.remove(18)
        rule.remove(14)
        rule.remove(4)
        rule.remove(5)
        rule.remove(8)
        rule.append(28)
        return Solve(rule)
    if (18 in rule) and (15 in rule) and (16 in rule) and (9 in rule) and (5 in rule) and (8 in rule):
        logout([18, 15, 16, 9, 5, 8], 29)
        rule.remove(18)
        rule.remove(15)
        rule.remove(16)
        rule.remove(9)
        rule.remove(5)
        rule.remove(8)
        rule.append(29)
        return Solve(rule)
    if (20 in rule) and (1 in rule) and (5 in rule):
        logout([20, 1, 5], 30)
        rule.remove(20)
        rule.remove(1)
        rule.remove(5)
        rule.append(30)
        return Solve(rule)
    if (19 in rule) and (4 in rule) and (7 in rule) and (8 in rule):
        logout([19, 4, 7, 8], 31)
        rule.remove(19)
        rule.remove(4)
        rule.remove(7)
        rule.remove(8)
        rule.append(31)
        return Solve(rule)

nums = list(map(int, input("输入数据>>>").split()))
Solve(nums)
