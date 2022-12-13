from linkkit import linkkit
import time
import json


class Aliyun(object):
    def __init__(self, product_key, dev_name, dev_secret):
        self.lk = linkkit.LinkKit(
            host_name="cn-shanghai",  # 填自己的host_name
            product_key=product_key,  # 填自己的product_key
            device_name=dev_name,  # 填自己的device_name
            device_secret=dev_secret)  # 填自己的device_secret
        self.lk.on_connect = self.on_connect
        self.lk.on_disconnect = self.on_disconnect
        self.lk.on_topic_message = self.on_topic_message
        self.lk.on_subscribe_topic = self.on_subscribe_topic
        self.lk.on_unsubscribe_topic = self.on_unsubscribe_topic
        self.lk.on_publish_topic = self.on_publish_topic


    def on_connect(self, session_flag, rc, userdata):
        print("on_connect:%d,rc:%d,userdata:" % (session_flag, rc))

    def on_disconnect(self, rc, userdata):
        print("on_disconnect:rc:%d,userdata:" % rc)

    def on_topic_message(self, topic, payload, qos, userdata):
        print("on_topic_message:" + topic + " payload:" + str(payload) + " qos:" + str(qos))
        pass

    def on_subscribe_topic(self, mid, granted_qos, userdata):
        print("on_subscribe_topic mid:%d, granted_qos:%s" %
              (mid, str(','.join('%s' % it for it in granted_qos))))
        pass

    def on_unsubscribe_topic(self, mid, userdata):
        print("on_unsubscribe_topic mid:%d" % mid)
        pass

    def on_publish_topic(self, mid, userdata):
        print("on_publish_topic mid:%d" % mid)

    def connect_aliyun_server(self):
        self.lk.connect_async()




def test1():
    product_key = "h1cploYwJdu"
    device_name = "Of13bizMCE6pRIbeAGPh"
    device_secret = "63d791792e887897e239dfc35684516f"
    server = Aliyun(product_key, device_name, device_secret)
    server.connect_aliyun_server()
    while True:
        pass

test1()

#
#
# isOTA_CAN_ConnectAliyun = False
# SendIndex = 0
# FLASH_START_ADDR = 0x08008000   #飞思卡尔单片机内置FLASH起始地址
#
# '''
# 2.打开文件成功后，开始连接阿里云
# 注：这一步之前必须确保文件打开成功，否则无法继续执行
# '''
# lk = None
#
#
#
#     #取消连接阿里云
# def on_disconnect(rc, userdata):
#     print("on_disconnect:rc:%d,userdata:" % rc)
#
#
# def on_subscribe_topic(mid, granted_qos, userdata):#订阅topic
#     print("on_subscribe_topic mid:%d, granted_qos:%s" %
#           (mid, str(','.join('%s' % it for it in granted_qos))))
#     pass
#
# #接收云端的数据
# def on_topic_message(topic, payload, qos, userdata):
#     #设备端的接收到的数据却是b:"123"用了一个切片去处理数据
#     #print("阿里云上传回的数值是:", str(payload))
#     #拿到接收来的数据
#     data=str(payload)[2:-1]
#     print("阿里云上传回的数值是:",data)
#     dataDict=json.loads(data)
#     #print("阿里云上传回的数值是:",type(dataDict))   #切片左闭右开 取头不取尾
#
#
#     HandleData_from_Aliyun(dataDict)
#     pass
#
#
# #处理阿里云传回的数据
# def HandleData_from_Aliyun(datadic):
#     global  SendIndex
#     global  isOTA_CAN_ConnectAliyun
#     if "FeedBackMessage" in datadic:
#         print("FeedBackMessage exit")
#         if datadic["FeedBackMessage"] == "Single block program update success!":
#            print("第一块程序更新成功")
#            print("SendIndex = %d" % SendIndex)
#            if SendIndex < windows_.ProgramBlockNumbers:
#                SendProgramData_byBlock(SendIndex)
#                SendIndex += 1
#                print("发送第 %d 块程序！" % SendIndex)
#
#            if  SendIndex == len(datadic):   #程序数据发送完毕
#                SendIndex = 0
#            pass
#
#         ShowInClient(datadic["FeedBackMessage"])
#     pass
#
#     if "OTA_CAN_ConnectAliyunState" in datadic:
#         print("OTA_CAN_ConnectAliyunState exist")
#         if datadic["OTA_CAN_ConnectAliyunState"] == "OTA-CAN has connected Aliyun!":
#             windows_.Update_OTA_CAN_ConnectState(True)
#             isOTA_CAN_ConnectAliyun = True
#             pass
#         pass
#     pass
#
#
#
#
#
# #终止订阅云端数据
# def on_unsubscribe_topic(mid, userdata):
#     print("on_unsubscribe_topic mid:%d" % mid)
#     pass
# #发布消息的结果，判断是否成功调用发布函数
# def on_publish_topic(mid, userdata):
#     print("on_publish_topic mid:%d" % mid)
#
# def Config_Connect_Parameters(product_key,dev_name,dev_secret):
#     # 设置连接参数，方法为“一机一密”型
#     global lk
#
#
#     # 注册接收到云端数据的方法
#     lk.on_connect = on_connect
#     # 注册取消接收到云端数据的方法
#     lk.on_disconnect = on_disconnect
#     # 注册云端订阅的方法
#     lk.on_subscribe_topic = on_subscribe_topic
#     # 注册当接受到云端发送的数据的时候的方法
#     lk.on_topic_message = on_topic_message
#     # 注册向云端发布数据的时候顺便所调用的方法
#     lk.on_publish_topic = on_publish_topic
#     # 注册取消云端订阅的方法
#     lk.on_unsubscribe_topic = on_unsubscribe_topic
#     pass
#
#
#
# def Init_Client(product_key,dev_name,dev_secret):
#     Config_Connect_Parameters(product_key,dev_name,dev_secret)
#     pass
#
# def Subscribe_Topic():
#     # 订阅主题
#     rc, mid = lk.subscribe_topic(lk.to_full_topic("user/get"))
#     print(lk.to_full_topic("user/set"))
#     #rc, mid = lk.subscribe_topic("/sys/h1cploYwJdu/Of13bizMCE6pRIbeAGPh/thing/service/property/set")
#
#     pass
#
#
# #发送程序片段
# def SendProgramData_byBlock(index):
#     Json_data = generate_Json_struct("FlashStartAddr", str(FLASH_START_ADDR),
#                                      "PrmTotalSize",windows_.ProgramTotalSize,
#                                      "PrmSize",len(windows_.FileData_list[index]),
#                                      "PrmData", str(windows_.FileData_list[index]))
#     if lk.check_state() == lk.LinkKitState.CONNECTED:
#         print("开始发布")
#         rc, mid = lk.publish_topic(lk.to_full_topic("user/update"), Json_data)
#     else:
#         print("未连接阿里云")
#     pass
#
# #发布程序块
# def Publish_Topic_byBlock():
#     global  SendIndex
#     global  FLASH_START_ADDR
#     FLASH_START_ADDR = 0x08008000
#     SendIndex = 0
#
#     SendProgramData_byBlock(SendIndex)
#     ShowInClient("程序发布成功")
#     SendIndex += 1
#     print("发送第 %d 块程序！" % SendIndex)
#
#     pass
#
# #发布单个命令
# def Publish_Single_CMD():
#     Json_data = generate_Json_struct("CMD_Name", "start vehicle",
#                                      "CMD_Index", 666,
#                                      "CMD_Description", "开始启动车辆",
#                                      "CMD_Check", "要进行命令check")
#     if lk.check_state() == lk.LinkKitState.CONNECTED:
#         print("开始发布")
#         rc, mid = lk.publish_topic(lk.to_full_topic("user/update"), Json_data)
#     else:
#         print("未连接阿里云")
#     pass
#
#
#
# #连接阿里云
# def Connected_Aliyun():
#     lk.connect_async()
#
#     time_start = time.time()
#     while  lk.check_state() != lk.LinkKitState.CONNECTED:
#         time.sleep(0.5)
#         if (time.time() - time_start) > 5:  #大于5s退出，并提醒用户连接阿里云失败，检查网络连接
#             #ShowInClient("上位机连接阿里云失败，请检查网络连接")
#             break
#     #如果连接成功，订阅话题
#     if lk.check_state() == lk.LinkKitState.CONNECTED:
#         #windows_.Update_Aliyun_ConnectState(True)
#         Subscribe_Topic()
#     pass
#
# def DisconnectAliyun():
#     lk.disconnect()
#     while lk.check_state() != lk.LinkKitState.DISCONNECTED:
#         time.sleep(0.5)
#     print("断开与阿里云连接成功！")
#     pass
#
# #生成Json数据格式
# def generate_Json_struct(key1,val1,key2,val2,key3,val3,key4,val4):
#     program_package_dict={}
#
#     #填写数据
#     program_package_dict[key1] = val1
#     program_package_dict[key2] = val2
#     program_package_dict[key3] = val3
#     program_package_dict[key4] = val4
#
#     jtext = json.dumps(program_package_dict,ensure_ascii=True)
#     return jtext
#     pass
#