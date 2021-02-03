# 全局变量 收集所有学员信息
info = []

# 打印登陆界面
def print_info():
    print('请选择如下功能-----------------')
    print('1:添加学员')
    print('2:删除学员')
    print('3:修改学员信息')
    print('4:查询学员信息')
    print('5:显示所有学员信息')
    print('6:退出系统')

# 添加
def add_info():
    new_id = int(input('输入学号：'))
    global info
    # 是否与列表里的学员重复
    for i in info:
        if new_id == i['id']:
            print('已有此id')
            return
    new_name = input('输入姓名：')
    new_sex = input('输入性别：')
    k = {}
    k['id'] = new_id
    k['name'] = new_name
    k['sex'] = new_sex
    info.append(k)
    print('添加成功')

# 删除
def del_info():
    del_id = int(input('输入要删除的学号：'))
    global info
    # 列表里是否有此学员
    for i in info:
        if del_id == i['id']:
            info.remove(i)
            print('已删除此id')
            return
    else:
        print('没有此id')

# 修改
def xiu_info():
    xiu_id = int(input('输入要修改的学号：'))
    global info
    # 列表是否有此id
    for i in info:
        if xiu_id == i['id']:
            info.remove(i)
            new_id = int(input('输入修改后的id：'))
            new_name = input('输入修改后的姓名：')
            new_sex = input('输入修改后的性别：')
            k = {}
            k['id'] = new_id
            k['name'] = new_name
            k['sex'] = new_sex
            info.append(k)
            print('已修改此id')
            return
    else:
        print('没有此id')

# 查看
def cha_info():
    cha_id = int(input('输入要查看学员的id：'))
    # 列表是否有此id
    for i in info:
        if cha_id == i['id']:
            print('该学员的信息：')
            print(f"id是{i['id']}，姓名是{i['name']}，性别是{i['sex']}。")
            return
    else:
        print('没有此id')

# 显示
def xian_info():
    print('id\t姓名\t性别')
    for i in info:
        print(f"{i['id']}\t{i['name']}\t{i['sex']}")

# 选择功能序号，完成对应功能
while True:
    print_info()
    number = int(input('请输入功能序号：'))
    if number == 1:
        # print('添加')
        add_info()
    elif number == 2:
        # print('删除')
        del_info()
    elif number == 3:
        # print('修改')
        xiu_info()
    elif number == 4:
        # print('查询')
        cha_info()
    elif number == 5:
        # print('显示')
        xian_info()
    elif number == 6:
        n = input('是否退出？yes or no')
        if n == 'yes':
            break
    else:
        print('还没有该功能')