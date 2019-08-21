import tkinter, re,os
import random
from tkinter import StringVar
from PIL import Image,ImageTk
from common.entry_display_tool import *
from ui.homepage import *
# from client.clientmanager import ClientManager
from tkinter.messagebox import *


# from MainPage import *

class RegisterPage(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.title("CQ")
        self.resizable(width=False, height=False)  # 窗口大小不可变
        self.geometry('%dx%d+%d+%d' % (550, 500, 650, 200))  # 设置窗口大小 和位置
        self['background'] = '#52AAE5'  # 窗口背景色

        self.username_value = StringVar()
        # self.username.set(r"请输入CQ号")
        self.username_focus_num = 0

        self.password_value = StringVar()
        # self.password.set(r"请输入密码")
        self.password_focus_num = 0

        self.password_again_value = StringVar()
        # self.password_again_value.set(r"请确认密码密码")
        self.password_again_focus_num = 0

        self.check_code_value = StringVar()
        # self.check_code_value.set(r"验证码")
        self.check_code_focus_num = 0

        self.check_code_info = StringVar()
        self.build_check_code()

        # self.img_logo = ImageTk.PhotoImage(Image.open("static/16.ico"))
        # self.iconbitmap(self.img_logo)  # 加窗口图标


        self.img_safety = tkinter.PhotoImage(file="")

        current_path = os.path.abspath(__file__)  #获取当前文件路径
        # father_path = os.path.abspath(os.path.dirname(current_path)+os.path.sep+'.')#获取当前文件父目录
        # config.ini文件路径，获取当前目录的父目录的父目录与config.ini拼接
        # config_file_path=os.path.join(os.path.abspath(os.path.dirname(current_path)+os.path.sep+".."),'config.ini')
        # print('1:',current_path,'2:',father_path,'3:',config_file_path)

        path =os.path.join(os.path.abspath(os.path.dirname(current_path)+os.path.sep+".."),
                                             'static','image','register')
        self.img_refresh = Image.open(os.path.join(path,'refresh.png'))

        self.img_refresh = ImageTk.PhotoImage(self.img_refresh)

        self.create_page()

    def create_page(self):
        self.page = tkinter.Frame(self,bg='#52AAE5')  # 创建Frame
        self.page.pack(expand=True)

        # tkinter.Label(self.page,height=1).grid(row=0, stick='W')
        tkinter.Label(self.page, text="用户注册",bg='#52AAE5',font=("宋体", 20)).grid(row=1, stick='W')
        tkinter.Button(self.page, text="用户登录", bg='#52AAE5',font=("宋体", 10), borderwidth=0, width=4,
                       activebackground="#52AAE5", command=self.login_request) \
            .grid(row=2, column=1, columnspan=2, stick='E')

        tkinter.Label(self.page,bg='#52AAE5').grid(row=2, stick='W')
        tkinter.Label(self.page, text='账户:', font=("宋体", 20),bg='#52AAE5') \
            .grid(row=3, stick='E', pady=10)
        self.username = tkinter.Entry(self.page, textvariable=self.username_value, width=27,
             font=25, fg='#767676', validate='focus', validatecommand=self.user_name_display)
        self.username.insert(10, "请输入CQ号")
        self.username.grid(row=3, column=1, columnspan=2, stick='W')

        tkinter.Label(self.page, text='密码:', font=("宋体", 20),bg='#52AAE5') \
            .grid(row=4, stick='E', pady=10)
        self.password = tkinter.Entry(self.page, textvariable=self.password_value, width=27,
             font=25, fg='#767676', validate='focus', validatecommand=self.password_display)
        self.password.insert(10, "请输入密码")
        self.password.grid(row=4, column=1, columnspan=2, stick='W')

        tkinter.Label(self.page, text='安全级别:', font=("宋体", 20),bg='#52AAE5') \
            .grid(row=5, stick='W', pady=10)
        tkinter.Label(self.page, text='', font=("宋体", 20),bg='#52AAE5') \
            .grid(row=5, column=1, stick='W', pady=10)

        tkinter.Label(self.page, text='确认密码:', font=("宋体", 20),bg='#52AAE5') \
            .grid(row=6, stick='W', pady=10)
        self.password_again = tkinter.Entry(self.page, textvariable=self.password_again_value,
                                            width=27,font=25, fg='#767676', validate='focus',
                                            validatecommand=self.password_again_display)
        self.password_again.insert(10, "请确认密码")
        self.password_again.grid(row=6, column=1, columnspan=2, stick='W')

        tkinter.Label(self.page, text='验证码:', font=("宋体", 20),bg='#52AAE5') \
            .grid(row=7, stick='E', pady=10)
        self.check_code = tkinter.Entry(self.page, textvariable=self.check_code_value, width=12,
                                        font=25, fg='#767676', validate='focus',
                                        validatecommand=self.check_code_display)
        self.check_code.insert(10, "请输入验证码")
        self.check_code.grid(row=7, column=1, stick='W')

        tkinter.Button(self.page, image=self.img_refresh, width=30, borderwidth=0,bg='#52AAE5',height=27,
                       font=("宋体", 11), activebackground="#52AAE5", command=self.refresh) \
            .grid(row=7, column=2, stick='W', pady=10)

        tkinter.Label(self.page, textvariable=self.check_code_info, width=4,
                      bg='#0495B7', font=("宋体", 17)) \
            .grid(row=7, column=2, stick='E', pady=10)

        tkinter.Label(self.page,bg='#52AAE5').grid(row=8, stick='W')
        tkinter.Button(self.page, text='注册', font=("宋体", 20), width=13,bg='#52AAE5',
                       activebackground="#A5CEED",command=self.register_check) \
            .grid(row=8, column=1, columnspan=2, stick='W', pady=10)
        # tkinter.Button(self.page, text='退出', command=self.page.quit).grid(row=7, column=1, stick='E')

    def user_name_display(self):
        # if self.username_focus_num % 2 == 0:
        #     if self.username_value.get() == '请输入CQ号':
        #         self.username.delete(0, "end")
        # else:
        #     if self.username_value.get() == '':
        #         self.username.insert(10, '请输入CQ号')
        default_value = "请输入CQ号"
        entry_display_tool(self.username_focus_num, self.username,
                                self.username_value, default_value)
        self.username_focus_num += 1
        return True

    def password_display(self):

        # if self.password_focus_num % 2 == 0:
        #     self.password['show'] = "*"
        #     if self.password_value.get() == '请输入密码':
        #         self.password.delete(0, "end")
        # else:
        #     if self.password_value.get() == '':
        #         self.password['show'] = ''
        #         self.password.insert(10, '请输入密码')
        default_value = "请输入密码"
        entry_display_tool(self.password_focus_num, self.password,
                                self.password_value, default_value, 1)
        self.password_focus_num += 1
        return True

    def password_again_display(self):
        # if self.password_again_focus_num % 2 == 0:
        #     self.password_again['show'] = "*"
        #     if self.password_again_value.get() == '请确认密码':
        #         self.password_again.delete(0, "end")
        # else:
        #     if self.password_again_value.get() == '':
        #         self.password_again['show'] = ''
        #         self.password_again.insert(10, '请确认密码')
        default_value = "请确认密码"
        entry_display_tool(self.password_again_focus_num, self.password_again,
                                self.password_again_value, default_value,1)
        self.password_again_focus_num += 1
        return True

    def check_code_display(self):
        # if self.check_code_focus_num % 2 == 0:
        #     if self.check_code_value.get() == '请输入验证码':
        #         self.check_code.delete(0, "end")
        # else:
        #     if self.check_code_value.get() == '':
        #         self.check_code.insert(10, '请输入验证码')

        default_value ='请输入验证码'
        entry_display_tool(self.check_code_focus_num,self.check_code,
                                self.check_code_value,default_value)
        self.check_code_focus_num += 1
        return True

    # def entry_display_tool(self,num,entry_name,entry_value,default_value,flag=0):
    #     if num%2==0:
    #         if flag:
    #             entry_name['show']='*'
    #         if entry_value.get()==default_value:
    #             entry_name.delete(0,'end')
    #     else:
    #         if entry_value.get()=='':
    #             if flag:
    #                 entry_name['show']=''
    #             entry_name.insert(10,default_value)
    #     return True


    def register_check(self):

        name = self.username_value.get()
        # print(name,type(name))
        password = self.password_value.get()
        # print(password,type(password))
        password_again = self.password_again_value.get()
        # print(password_again,type(password_again))
        check_code = self.check_code_value.get()
        check_code_info = self.check_code_info.get()
        print(check_code, check_code_info)
        try:
            name = re.fullmatch(r'[a-zA-Z][a-zA-Z0-9]{1,17}', name).group()
            # print(name)
            password = re.fullmatch(r'[a-zA-Z1-9]{1,17}', password).group()
            password_again = re.fullmatch(r'[a-zA-Z1-9]{1,17}', password_again).group()
            print(name, password, password_again)

            if password != password_again:
                print("密码不一致")
                self.build_check_code()
                return "密码不一致"

            else:
                if check_code.lower() != check_code_info.lower():
                    print("验证码错误")
                    self.build_check_code()
                    return "验证码错误"
                else:
                    print("注册成功")
                    return [name, password]
                    # result = ClientManager().register(name, password)
                    # print(result)
        except Exception as e:
            print(e)
            print("用户名或密码不合法")
            self.build_check_code()
            return "用户名或密码不合法"

    def login_result(self,result,user_name='',friend_list=[]):
        if result:
            self.destroy()
            root = HomePage(user_name, friend_list)
            root.mainloop()
        else:
            return


    def login_request(self):

        self.destroy()
        from ui.login import LoginPage
        root = LoginPage()
        root.mainloop()

    def refresh(self):
        self.build_check_code()

    def build_check_code(self):
        code = ''
        for i in range(4):
            num = random.randint(0, 61)
            code_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', "a", 'b', 'c', 'd', 'e', 'f',
                         'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                         'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                         'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            code += code_list[num]

        self.check_code_info.set(code)

# root = RegisterPage()
# root.mainloop()
