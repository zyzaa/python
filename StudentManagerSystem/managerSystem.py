from Students import *

class ManagerSystem(object):
    def __init__(self):
        # 存储数据
        self.student_list = []

    # 程序入口
    def run(self):
        # 加载数据
        self.load_studer()
        while True:
            # 显示功能菜单
            self.show_menu()
            # 用户输入序号
            number = int(input('请输入功能序号：'))
            # 执行序号的功能
            if number == 1:
                self.add_student()
            elif number == 2:
                self.del_student()
            elif number == 3:
                self.modify_student()
            elif number == 4:
                self.search_student()
            elif number == 5:
                self.show_student()
            elif number == 6:
                self.sava_student()
            elif number == 7:
                return
            else:
                print('功能序号错入，请重新输入')
            
    # 定义功能函数
    # 显示菜单
    @staticmethod
    def show_menu():
        print('请选择如下功能-----------------')
        print('1:添加学员')
        print('2:删除学员')
        print('3:修改学员信息')
        print('4:查询学员信息')
        print('5:显示所有学员信息')
        print('6:保存系统')
        print('7:退出系统')

    # 添加
    def add_student(self):
        add_id = int(input('输入学员的id：'))
        for i in self.student_list:
            if add_id == i.id:
                print('已有此学员的id')
                return
        add_name = input('输入学员的姓名：')
        add_sex = input('输入学员的性别：')
        # 导入学生类，创建学生类对象
        student = Student(add_id, add_name, add_sex)
        # 加入到存储数据列表
        self.student_list.append(student)
        print('添加成功')

    # 删除
    def del_student(self):
        del_id = int(input('输入要删除学员的id：'))
        for i in self.student_list:
            if del_id == i.id:
                self.student_list.remove(i)
                print('删除成功')
                return
        else:
            print('没有此学员的id')

    # 修改
    def modify_student(self):
        mod_id = int(input('输入要修改学员的id：'))
        for i in self.student_list:
            if mod_id == i.id:
                i.id = int(input('输入修改后学员的id：'))
                i.name = input('输入修改后学员的姓名：')
                i.sex = input('输入修改后学员的性别：')
                print('修改完成')
                return
        else:
            print('没有此学员的id')

    # 查询
    def search_student(self):
        sea_id = int(input('输入要查询学员的id：'))
        for i in self.student_list:
            if sea_id == i.id:
                print(f'此学员的id是{i.id}，姓名是{i.name}，性别是{i.sex}。')
                return
        else:
            print('没有此学员的id')
    # 显示
    def show_student(self):
        print('id\t姓名\t性别')
        for i in self.student_list:
            print(f'{i.id}\t{i.name}\t{i.sex}')
    
    # 保存
    def sava_student(self):
        # 1、打开文件
        f = open('student.data', 'w')
        # 2、写入数据
        # __dict__ 转换成 字典
        new_list = [i.__dict__ for i in self.student_list]
        # 文件写入 字符串数据
        f.write(str(new_list))
        # 3、关闭文件
        f.close()
        print('保存完成')

    # 加载数据
    def load_studer(self):
        f = open('student.data')
        red = f.read()
        # 将data字符串转换为列表类型数据
        new_list = eval(red)
        self.student_list = [Student(i['id'], i['name'], i['sex']) for i in new_list]
        f.close()