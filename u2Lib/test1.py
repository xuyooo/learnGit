#coding:utf-8
import uiautomator2 as ut2
import uiautomator2.ext.htmlreport as htmlreport
import time

def main():
    u = ut2.connect('160.6.72.193:7912')
    print(u.info)
    time.strftime('%Y-%m-%d', time.localtime(time.time()))
    u.app_start('com.lphtsccft')
    # hrp = htmlreport.HTMLReport(u)
    # hrp.patch_click()   #操作一次click就截图
    u(text='跳过').click()
    u(text='行情').click()
    u(text='更多').click()
    u(text='股转').click()
    time.sleep(1)
    print(u(text='创新层'))
    x, y = u(text='创新层').center() #返回元素x y坐标
    retDict = {}
    namelen = len(u(resourceId='com.lphtsccft:id/stock_name'))
    infolen = len(u(resourceId='com.lphtsccft:id/stock_anytext'))
    if namelen == infolen:
        for i in range(int(namelen)):
            stock_name = u(resourceId='com.lphtsccft:id/stock_name')[i].info['text']  #取个股名称
            stock_info = u(resourceId='com.lphtsccft:id/stock_anytext')[i].info['text']  #取个股涨跌幅

            if stock_name not in retDict:  #考虑不在一屏内的问题，用dict组装数据
                retDict[stock_name] = stock_info
    print(len(u(text='基础层')))

    #循环判断想要的值是否出现
    while True:
        u.swipe(x,y,x,y-180,0.5)

        eles = len(u(text='基础层'))

        if not eles:
            continue

        sx,sy = u(text='基础层').center()
        print(sx,sy)
        namelen = len(u(resourceId='com.lphtsccft:id/stock_name'))
        infolen = len(u(resourceId='com.lphtsccft:id/stock_anytext'))
        if namelen == infolen:
            for i in range(int(namelen)):
                stock_name = u(resourceId='com.lphtsccft:id/stock_name')[i].info['text']
                stock_info = u(resourceId='com.lphtsccft:id/stock_anytext')[i].info['text']

                if stock_name not in retDict:
                    retDict[stock_name] = stock_info
        print(retDict)
        u.swipe(sx,sy,sx,y,1) #duration 值不与appium一致
        break
    print(time.strftime('%Y-%m-%d', time.localtime(time.time())))




        # for stock_name in u(resourceId='com.lphtsccft:id/stock_name'):
        #     print(stock_name.info['text'])
        # for stock_info in u(resourceId='com.lphtsccft:id/stock_anytext'):
        #     print(stock_info.info['text'])
    # if u(text='创新层').wait(timeout=3.0):
    #     u(scrollable=True).scroll.to(text='两网及退市')
    # clicked = u(text='创新层').click_exists(timeout=10.0)
    # u(text='基础层').get_text()
    # clicked = u(text='基础层').click_exists(timeout=10.0)
    # u(className='android.widget.TextView',resourceId='com.lphtsccft:id/tv_market_section_header_title').child_by_text('做市转让',allow_scroll_search=True,className='android.widget.TextView').click()

if __name__ == '__main__':
    main()