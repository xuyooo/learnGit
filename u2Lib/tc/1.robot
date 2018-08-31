*** Settings ***
Library  pylib.StockDetLib

*** Test Cases ***
进入app - tc000001
    connect_phone      160.6.90.84:7912     3
    open_application    com.lphtsccft
    check_introducepage    com.lphtsccft:id/introducePageViewPager    0.9      0.5     0.1     0.5

