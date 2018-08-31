import uiautomator2 as ut2
#coding:utf-8
import uiautomator2 as ut2
import uiautomator2.ext.htmlreport as htmlreport
import time

def main():
    u = ut2.connect('160.6.72.193:7912')
    print(u.info)
    u.app_start('com.lphtsccft')
    u(text='跳过').click()
    u(text='行情').click()
    u.press('back')
    # u.watcher("ALERT1").when(text="确定").click(text="确定")
    u.jsonrpc.runWatchersOnWindowsChanged(False)





if __name__ == '__main__':
    main()