import uiautomator2 as u2
import time


class StockDetLib():
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    def __init__(self):
        pass

    def connect_phone(self, ip, time=3):
        '''
        :param ip: 手机ip
        :param time: toast展示时间
        '''
        self.d = u2.connect(ip)
        self.d.healthcheck()
        self.d.toast.show('start test', time)

    def open_application(self, pkgname):
        self.d.app_start(pkgname)


    def check_introducepage(self, value, startx, starty, endx, endy, duration=0.5):
        '''
        Args:
            value : 元素定位
            startx, starty : 起始位置（小数为百分比，如：0.9 是整个分辨率的百分之90）
            endx, endy ：目标位置

        '''
        while self.d(resourceId=value).exists:
            self.d.swipe(
                float(startx),
                float(starty),
                float(endx),
                float(endy), duration)

    def change_colour(self, value):
        '''
        Args:
            value: 1, 黑色主题; 2, 白色主题; 3, 智能模式
        '''

        self.d(resourceId="com.lphtsccft:id/rb_market").click()
        self.d(resourceId="com.lphtsccft:id/tv_title_bar_radio_left").click()
        self.d(resourceId="com.lphtsccft:id/theme_switcher").click()
        if value == '1':
            self.d.xpath("//android.widget.TextView[contains(@text, '黑色主题')]").click()
        elif value == '2':
            self.d.xpath("//android.widget.TextView[contains(@text, '白色主题')]").click()
        elif value == '3':
            self.d.xpath("//android.widget.TextView[contains(@text, '智能模式')]").click()

    def select_hs(self, value):
        '''

        :param value: 任何沪深类模块名，如：沪深A股， 中小板等
        '''

        self.d.xpath("//android.widget.TextView[@text=%s]" % value).click()

    def select_gg(self, value):
        '''

        :param value: 任何港股类模块名，如：港股通， 红筹股等
        '''

        self.d.xpath("//android.widget.TextView[@text=%s]" % value).click()

    def select_zs(self, value):
        '''

        :param value: 任何全球重要指数类模块名，如：美洲市场， 欧洲市场等
        '''

        self.d.xpath("//android.widget.TextView[@text=%s]" % value).click()

    def select_jj(self, value):
        '''

        :param value: 任何场外基金类模块名，如：股票基金等
        '''

        self.d.xpath("//android.widget.TextView[@text=%s]" % value).click()

    def select_gnqh(self, value):
        '''

        :param value: 任何国内期货类模块名，如：中金所等
        '''

        self.d.xpath("//android.widget.TextView[@text=%s]" % value).click()

    def select_gjqh(self, value):
        '''

        :param value: 任何国际期货类模块名，如：贵金属等
        '''

        self.d.xpath("//android.widget.TextView[@text=%s]" % value).click()

    def select_hl(self, value):
        '''

        :param value: 任何国际汇率类模块名，如：重要外汇等
        '''

        self.d.xpath("//android.widget.TextView[@text=%s]" % value).click()

    def select_stock(self, num=0):
        '''
        Args:
            num : 列表中的具体某个股, 如选择第三个 则num填2
        '''
        self.d(resourceId="com.lphtsccft:id/ranking_stock_name")[int(num)].click()

    def drag_k_line(self, value):
        '''
        Args:
            value : minute_line  :  0
                    fiveDay_line :  5
                    oneDay_line  :  1
                    week_ling    :  7
                    month_line   :  30
        '''
        if value == '0':
            d(resourceId="com.lphtsccft:id/radio_button_1").click()



d = u2.connect('160.6.90.84:7912')
# # d.healthcheck()
# # d.app_start('com.lphtsccft')
d.toast.show('测试开始', 3)
# d.xpath("//android.widget.TextView[contains(@text, '黑色主题')]").click()
#
#
# while d(resourceId='com.lphtsccft:id/introducePageViewPager').exists:
#     print('find it')
#     d.swipe(0.9, 0.5, 0.1, 0.5)
#
#
# # '''case1:黑白版检查'''
# # d(resourceId="com.lphtsccft:id/rb_market").click()
# # d(resourceId="com.lphtsccft:id/tv_title_bar_radio_left").click()
# #
# # #黑白版测试 —— 依次点击黑版/白版/智能版
# # d(resourceId="com.lphtsccft:id/theme_switcher").click()
# # d(resourceId="com.lphtsccft:id/theme_black").click()
# # d(resourceId="com.lphtsccft:id/theme_change_back_img").click()
# #
# # d(resourceId="com.lphtsccft:id/theme_white").click()
# # d(resourceId="com.lphtsccft:id/theme_change_back_img").click()
# #
# #
# # d(resourceId="com.lphtsccft:id/theme_smart").click()
# # d(resourceId="com.lphtsccft:id/theme_change_default_back_img").click()
# #
# #
# # #黑版跳转测试
# # d(resourceId="com.lphtsccft:id/theme_black").click()
# # d(resourceId="com.lphtsccft:id/theme_change_confirm_btn").click()
# # time.sleep(0.5)
# # d.screenshot("black.jpg")
# #
# # #白版跳转测试
# # d(resourceId="com.lphtsccft:id/theme_switcher").click()
# # d(resourceId="com.lphtsccft:id/theme_white").click()
# # d(resourceId="com.lphtsccft:id/theme_change_confirm_btn").click()
# # time.sleep(0.5)
# # d.screenshot("white.jpg")
# #
# # #智能版跳转测试
# # d(resourceId="com.lphtsccft:id/theme_switcher").click()
# # d(resourceId="com.lphtsccft:id/theme_smart").click()
# # d(resourceId="com.lphtsccft:id/theme_change_default_confirm_btn").click()
# # time.sleep(0.5)
# # d.screenshot("other.jpg")
# # d(resourceId="com.lphtsccft:id/title_bar_left").click()
#

print(d(resourceId="com.lphtsccft:id/ranking_stock_name").count)
d(resourceId="com.lphtsccft:id/ranking_stock_name")[3].click()
# '''case2：竖屏分时/五日/周k/月k'''
# time.sleep(2)
# #进入沪深A股个股详情页
# d(resourceId="com.lphtsccft:id/more").click()
# d(resourceId="com.lphtsccft:id/tv_more_index_item").click()
# d(resourceId="com.lphtsccft:id/ranking_stock_name").click()
# d(resourceId="com.lphtsccft:id/radio_button_1").click()
# time.sleep(0.5)
# #分时K线滑动
# d.drag(0.075, 0.5, 0.95, 0.5, 0.7)
#
#
# d(resourceId="com.lphtsccft:id/radio_button_2").click()
# time.sleep(0.5)
# d.drag(0.075, 0.5, 0.95, 0.5, 0.7)
#
#
# d(resourceId="com.lphtsccft:id/radio_button_4").click()
# time.sleep(0.5)
# d.drag(0.075, 0.5, 0.95, 0.5, 0.7)
#
#
# d(resourceId="com.lphtsccft:id/radiobtn_month").click()
# d(text="月K").click()
# time.sleep(0.5)
# d.drag(0.075, 0.5, 0.95, 0.5, 0.7)
#
# '''case3:横屏滑动k线'''
# d(resourceId="com.lphtsccft:id/hq_chartview").click()
# time.sleep(1)
# print(d.info)
# d.drag(0.1, 0.5, 0.90, 0.5, 2)
#
# d(resourceId="com.lphtsccft:id/radio_button_4").click()
# time.sleep(0.5)
# d.drag(0.1, 0.5, 0.90, 0.5, 2)
#
# d(resourceId="com.lphtsccft:id/radio_button_2").click()
# time.sleep(0.5)
# d.drag(0.1, 0.5, 0.90, 0.5, 2)
# time.sleep(1)
#
# d(resourceId="com.lphtsccft:id/radio_button_1", text=u"分时", className="android.widget.RadioButton").click()
# time.sleep(0.5)
# d.drag(0.075, 0.5, 0.95, 0.5, 2)
# d(resourceId="com.lphtsccft:id/hq_land_back").click()
#
# '''case4：竖屏日K1'''
# d(resourceId="com.lphtsccft:id/radio_button_3").click()
# time.sleep(0.5)
# d.drag(0.075, 0.5, 0.95, 0.5, 2)
# time.sleep(1)
# d.screenshot('日K均线初始化状态.jpg')
# d.double_click(0.1, 0.4, 1)
#
# # 均线设置5日
# d(resourceId="com.lphtsccft:id/kline_pop_togglebutton1").click()
# d.screenshot('点击5日均线设置.jpg')
# d(resourceId="com.lphtsccft:id/kline_settings_close_button").click()
#
# #均线设置10日
# time.sleep(0.5)
# d.click(0.1, 0.4)
# d(resourceId="com.lphtsccft:id/kline_pop_togglebutton2").click()
# d.screenshot('点击10日均线设置.jpg')
# d(resourceId="com.lphtsccft:id/kline_settings_close_button").click()
#
# #均线设置20日
# time.sleep(0.5)
# d.click(0.1, 0.4)
# d(resourceId="com.lphtsccft:id/kline_pop_togglebutton3").click()
# d.screenshot('点击20日均线设置.jpg')
# d(resourceId="com.lphtsccft:id/kline_settings_close_button").click()
#
# #均线设置60日
# time.sleep(0.5)
# d.click(0.1, 0.4)
# d(resourceId="com.lphtsccft:id/kline_pop_togglebutton4").click()
# d.screenshot('点击60日均线设置.jpg')
# d(resourceId="com.lphtsccft:id/kline_settings_close_button").click()
#
# #均线设置120日
# time.sleep(0.5)
# d.click(0.1, 0.4)
# d(resourceId="com.lphtsccft:id/kline_pop_togglebutton5").click()
# d.screenshot('点击120日均线设置.jpg')
# d(resourceId="com.lphtsccft:id/kline_settings_close_button").click()
#
# '''case5：竖屏日K2'''
# d(resourceId="com.lphtsccft:id/radio_button_3").click()
# #不复权
# time.sleep(0.5)
# d.click(0.1, 0.4)
# d(resourceId="com.lphtsccft:id/kline_pop_radiobutton_bufuquan").click()
# d(resourceId="com.lphtsccft:id/kline_settings_close_button").click()
# d.screenshot('不复权K线图.jpg')
#
# #前复权
# time.sleep(0.5)
# d.click(0.1, 0.4)
# d(resourceId="com.lphtsccft:id/kline_pop_radiobutton_qianfuquan").click()
# d(resourceId="com.lphtsccft:id/kline_settings_close_button").click()
# d.screenshot('前复权K线图.jpg')
#
# #后复权
# time.sleep(0.5)
# d.click(0.1, 0.4)
# d(resourceId="com.lphtsccft:id/kline_pop_radiobutton_houfuquan").click()
# d(resourceId="com.lphtsccft:id/kline_settings_close_button").click()
# d.screenshot('后复权K线图.jpg')
#
#
# #竖屏 指标操作
# d.click(0.068, 0.655)
#
# eleInfo = d(resourceId="com.lphtsccft:id/indicate_sel_wheel_view").info
# topInfo = d(text=u"选择指标").info
#
# start = int(eleInfo['bounds']['bottom'])
# end = int(topInfo['bounds']['bottom'])
#
# deviceInfo = int(d.info['displayHeight'])
# print(start,deviceInfo)
#
# while True:
#     d.swipe(540,start-50,540,start-150,0.5)
#
#     eles = len(d(text='心理线'))
#
#     if not eles:
#         volCurrentInfo = d(resourceId="com.lphtsccft:id/indicate_current_setting_tv").get_text()
#         print(volCurrentInfo)
#         # volInfo = d(resourceId="com.lphtsccft:id/indicate_detail_use").get_text()
#         # print(volInfo)
#         continue
#
#     else:
#         break
#
#
# realInfo = ''
# volInfo = d(resourceId="com.lphtsccft:id/indicate_detail_use").get_text()
# # assert volInfo==realInfo,'成交量描述错误！！！'
#
# d(resourceId="com.lphtsccft:id/indicate_set_layout").click()
# #go to vol set
#
# for ele in d(resourceId="com.lphtsccft:id/indicate_vol_switch"):
#     print(ele.info)