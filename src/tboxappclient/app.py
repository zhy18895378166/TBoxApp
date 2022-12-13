"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from toga.style.pack import CENTER, LEFT, RIGHT

from tboxappclient.login import verify_login



SWITCH_BOX_PDDING_TOP = 700

# 数据显示条目模板
class CreateStatusItem(object):
    def __init__(self, dm_box, item_name):
        self.__dm_box = dm_box
        self.__item_name = item_name

        self.create_item()

    def create_item(self):
        item_box = toga.Box(style=Pack(direction=ROW))
        item_label = toga.Label(self.__item_name, style=Pack(height=25, flex=1))
        item_show_data = toga.TextInput(readonly=True, style=Pack(height=25, flex=1))

        item_box.add(item_label)
        item_box.add(item_show_data)

        self.__dm_box.add(item_box)

# 远程控制条目模板
class CreateControlItem(object):
    def __init__(self, rc_box, item_name):
        self.__rc_box = rc_box
        self.__item_name = item_name

        self.create_item()

    def create_item(self):
        item_box = toga.Box(style=Pack(direction=ROW))
        item_btn = toga.Button(self.__item_name, style=Pack(height=100))

        item_box.add(item_btn)
        self.__rc_box.add(item_box)

# 用户界面控制条目模板
class CreateUserCenterItem(object):
    def __init__(self, uc_box, item_name, onpress_func):
        self.__uc_box = uc_box
        self.__item_name = item_name
        self.__onpress_func = onpress_func
        self.create_item()

    def create_item(self):
        item_box = toga.Box(style=Pack(direction=ROW))
        item_btn = toga.Button(self.__item_name, style=Pack(height=50))

        item_box.add(item_btn)
        item_btn.on_press = self.__onpress_func

        self.__uc_box.add(item_box)



# 登录界面
class LoginInterfce(object):
    def __init__(self):
        self.create_login_face()

    def create_login_face(self):
        un_box = toga.Box(style=Pack(direction=ROW, padding=5))
        pw_box = toga.Box(style=Pack(direction=ROW, padding=5))
        self.box = toga.Box(style=Pack(direction=COLUMN, padding_top=10))

        self.un_input = toga.TextInput(style=Pack(flex=1))
        self.pw_input = toga.PasswordInput(style=Pack(flex=1))

        un_label = toga.Label("用户名", style=Pack(text_align=LEFT, width=100, padding_left=10))
        pw_label = toga.Label("密码", style=Pack(text_align=LEFT, width=100, padding_left=10))

        self.exit_btn = toga.Button("X", style=Pack(width=20, alignment=RIGHT, flex=1, background_color='white'))
        self.login_btn = toga.Button("登录", style=Pack(padding=20, alignment=RIGHT, flex=1, background_color='orange'))



        un_box.add(un_label)
        un_box.add(self.un_input)

        pw_box.add(pw_label)
        pw_box.add(self.pw_input)

        self.box.add(self.exit_btn)
        self.box.add(un_box)
        self.box.add(pw_box)
        self.box.add(self.login_btn)



# 1.用户中心页面
class UserCenterInterfce():
    def __init__(self):
        self.__login_btn_onpress = None


    @property
    def login_btn_onpress(self):
        return self.__login_btn_onpress

    @login_btn_onpress.setter
    def login_btn_onpress(self, on_press):
        self.__login_btn_onpress = on_press
        self.cerate_user_center()
        pass

    def cerate_user_center(self):
        self.box = toga.Box("user_center", style=Pack(direction=COLUMN))
        CreateUserCenterItem(self.box, '登录', self.__login_btn_onpress)

# 2.数据监控界面
class DataMonitorInterfce():
    def __init__(self):
        self.cerate_data_monitor()


    def cerate_data_monitor(self):
        self.box = toga.Box("data_monitor", style=Pack(direction=COLUMN))
        CreateStatusItem(self.box, '平均油耗')
        CreateStatusItem(self.box, '燃油液位')
        CreateStatusItem(self.box, '续航里程')
        CreateStatusItem(self.box, '总行驶里程')



# 3.命令下发界面
class RemoteControlInterfce():
    def __init__(self):
        self.cerate_data_monitor()

    def cerate_data_monitor(self):
        self.box = toga.Box("remote_control", style=Pack(direction=COLUMN))
        CreateControlItem(self.box, '启动车辆')
        CreateControlItem(self.box, '打开空调')
        CreateControlItem(self.box, '打开车窗')


#定义一个静态类，用于app布局管理
class LayoutManager():
    def __init__(self, func_box):
        self.func_box = func_box
        self.func_box_height = 0

    # 计算每个box中widgets中最大的高度
    def calculate_max_hight_in_box(self, box):
        # 1.获取box中所有的child
        child_list = box.children
        print(f"each box in func_box include widgets: {child_list}")

        # 2.获取child_list中每个child的高度
        height_list = []
        for child in child_list:
            h = child.style.height
            height_list.append(h)

        # 3.获取最大高度
        h_max = max(height_list)
        print(h_max)
        return h_max

    # 计算func_box中所有的box高度和(包括padding_top和padding_bottom)
    def calculate_func_box_height(self):
        cur_interface = self.func_box.children
        box_list = cur_interface[0].children
        print(f"func_box include boxes: {box_list}")
        box_height_list = []
        padding_top_bottom_list = []
        for box in box_list:
            # box高度
            box_h = self.calculate_max_hight_in_box(box)
            box_height_list.append(box_h)

            #padding_top和padding_bottom的总和
            padding_t_b = box.style.padding_top + box.style.padding_bottom
            print(f'padding_t_b = {padding_t_b}')
            padding_top_bottom_list.append(padding_t_b)

        # 所有box高度和padding 总高度
        sum = 0
        for i in box_height_list:
            sum += i
        for i in padding_top_bottom_list:
            sum += i

        self.func_box_height = sum



    def get_func_box_height(self):
        self.calculate_func_box_height()
        return self.func_box_height



# App
class TBoxAppClient(toga.App):
    def startup(self):
        # 1.构建APP框架
        self.create_app_framework()

        # 2.创建界面切换按钮
        self.create_switch_buton()

        # 3.实例化界面
        self.instantiate_interfaces()

        # 4.绑定回调函数
        self.set_widget_callback_func()

        # 5.显示初始的界面（可定制）
        self.set_initial_interface()

        # 6.刷新界面
        self.refresh_layouts()




    #构建APP框架
    def create_app_framework(self):
        # 1.布局box
        self.func_box = toga.Box("single_interface", style=Pack(flex=10))
        self.switch_box = toga.Box("contrl_btn_sets", style=Pack(alignment=CENTER, padding=(200, 0, 0, 0)))
        self.top_box = toga.Box("main_box", children=[self.func_box, self.switch_box], style=Pack(direction=COLUMN, alignment=CENTER))

        # 2.放置布局box的窗口
        self.main_window = toga.MainWindow(title="TBox-App-Client", resizeable=False, size=(300,750))
        self.main_window.content = self.top_box

        # 3.创建一个布局管理器
        self.app_layout_manager = LayoutManager(self.func_box)


    # 创建切换按钮，并将按钮添加到对应的box中
    def create_switch_buton(self):
        dm_btn = toga.Button('数据监控', on_press=self.switch_to_dm, style=Pack(flex=1))
        rc_btn = toga.Button('远程控制', on_press=self.switch_to_rc, style=Pack(flex=1))
        uc_btn = toga.Button('我的', on_press=self.switch_to_uc, style=Pack(flex=1))
        self.switch_box.add(dm_btn)
        self.switch_box.add(rc_btn)
        self.switch_box.add(uc_btn)

    # 实例化界面
    def instantiate_interfaces(self):
        # 用户界面
        self.user_center = UserCenterInterfce()
        self.user_center.login_btn_onpress = self.open_login_window

        self.data_monitor = DataMonitorInterfce()
        self.remote_control = RemoteControlInterfce()
        self.login_face = LoginInterfce()

    # 绑定部件的回调函数
    def set_widget_callback_func(self):

        #2.登录界面
        self.login_face.exit_btn.on_press = self.exit_from_login_interface
        self.login_face.login_btn.on_press = self.user_login_verify

        #2.远程控制界面

        #
        pass

    # 设置初始显示界面
    def set_initial_interface(self):
        self.func_box.add(self.user_center.box)
        self.set_current_interface_flag('uc')

    #刷新界面
    def refresh_layouts(self):
        if self.current_interface != 'login':
            func_box_h = self.app_layout_manager.get_func_box_height()
            print(f'func box h= {func_box_h}')
            top = SWITCH_BOX_PDDING_TOP - func_box_h
            print(f"padding_top = {top}")
            self.switch_box.style.update(padding_top=top)

        #显示
        self.top_box.refresh()
        self.top_box.refresh_sublayouts()
        self.main_window.show()

###################################  class TBoxAppClient  callback following   ######################################
    # 切换到数据监控界面(dm <==>data monitor)
    def switch_to_dm(self, widget):
        if self.get_current_interface_flag() != 'dm':
            print("切换到数据监控界面")
            self.interface_switch_manager('dm')


    # 切换到远程控制界面(rc <==>remote control)
    def switch_to_rc(self, widget):
        if self.get_current_interface_flag() != 'rc':
            print("切换到远程控制界面")
            self.interface_switch_manager('rc')


    # 切换到用户中心(uc <==>user center)
    def switch_to_uc(self, widget):
        if self.get_current_interface_flag() != 'uc':
            print("切换到用户中心")
            self.interface_switch_manager('uc')


    # 打开登录窗口
    def open_login_window(self, widget):
        print("打开登录窗口")
        self.interface_switch_manager('login')


    #从登录界面返回到用户中心
    def exit_from_login_interface(self, widget):
        print('退出登录界面，返回到用户中心')
        self.interface_switch_manager('uc')

    # 设置当前界面
    def set_current_interface_flag(self, interface_name_str):
        self.current_interface = interface_name_str

    # 获取当前界面
    def get_current_interface_flag(self):
        return self.current_interface


    #用户界面切换到其他界面
    def switch_from_uc_to_others(self,new):
        # uc ===> login
        if new == 'login':
            self.top_box.remove(self.func_box)
            self.top_box.remove(self.switch_box)

        # uc ===> rc/dm
        elif new == 'rc' or new == 'dm':
            self.func_box.remove(self.user_center.box)

    # 其他界面切换到用户界面
    def switch_from_others_to_uc(self, old):
        # login  ===> uc
        if old == 'login':
            self.top_box.add(self.func_box)
            self.top_box.add(self.switch_box)
            self.func_box.add(self.user_center.box)

        # rc/dm ===> uc
        elif old == 'rc' or old == 'dm':
            self.func_box.add(self.user_center.box)


    # 移除当前界面
    def remove_current_interface(self,new_interface_name):
        old = self.get_current_interface_flag()

        if old == 'dm':
            self.func_box.remove(self.data_monitor.box)
        elif old == 'rc':
            self.func_box.remove(self.remote_control.box)
        elif old == 'uc':
            self.switch_from_uc_to_others(new_interface_name)
        elif old == 'login':
            self.top_box.remove(self.login_face.box)


    # 切换到新界面
    def switch_to_new_interface(self, old_interface_name):
        new = self.get_current_interface_flag()
        if new == 'dm':
            self.func_box.add(self.data_monitor.box)
        elif new == 'rc':
            self.func_box.add(self.remote_control.box)
        elif new == 'uc':
            self.switch_from_others_to_uc(old_interface_name)
        elif new == 'login':
            self.top_box.add(self.login_face.box)


    # 界面切换管理
    def interface_switch_manager(self, new_interface_name):
        old = self.get_current_interface_flag()
        self.remove_current_interface(new_interface_name)
        self.set_current_interface_flag(new_interface_name)
        print(f'switch: {old} ===> {self.get_current_interface_flag()}')
        self.switch_to_new_interface(old)
        self.refresh_layouts()

    # 用户登录验证
    def user_login_verify(self, widget):
        user_name_input = self.login_face.un_input.value
        password_input = self.login_face.pw_input.value
        print(type(user_name_input), user_name_input)
        print(type(password_input), password_input)

        is_success, msg = verify_login(user_name_input, password_input)

        # 根据登录结果做出下一步操作
        if is_success is True:
            # todo 返回用户中心
            print(f'{msg}，登录成功，自动返回到用户中心')
            self.exit_from_login_interface(widget)

            #修改登录按钮状态，并显示
            pass
        else:
            # todo 在界面上提示用户错误原因
            pass





    # 刷新界面切换的box组件
    def refresh_switch_box(self, value):
        self.func_box.style.update(padding=(value, 0, 0, 0))
        self.func_box.refresh()






def main():
    tbox_app = TBoxAppClient()

    return tbox_app
