# -*- coding:utf-8 -*-

# 导入模块
import chinese_administration_division_service as cads

if __name__ == '__main__':
    # 创建类实例
    c = cads.AdministrationDivisionService()

    # `parseCode`测试用例

    # 省级用例
    print(c.parseCode('110000'))
    print(c.parseCode('330000'))
    print(c.parseCode('810000'))

    # 地市用例
    print(c.parseCode('130200'))
    print(c.parseCode('130800'))
    print(c.parseCode('652300'))

    # 区县用例
    print(c.parseCode('130529'))
    print(c.parseCode('130432'))
    print(c.parseCode('110105'))
    print(c.parseCode('130825'))
    print(c.parseCode('810107'))
    print(c.parseCode('710101'))
    print(c.parseCode('540223'))

    # 错误情况 =>

    ## 参数不匹配
    print(c.parseCode(123))
    print(c.parseCode('hello'))
    print(c.parseCode('130825123'))
    print(c.parseCode('1235'))
    print(c.parseCode('12356555'))

    ## 不存在的区划代码
    print(c.parseCode('123456'))
    print(c.parseCode('123123'))

    # `parseString`测试用例

    # 正确用例 =>

    print(c.parseString('北京市'))
    print(c.parseString('广平县'))
    print(c.parseString('日喀则市'))
    print(c.parseString('香港特别行政区'))

    # 错误用例 =>

    print(c.parseString('xxxxxxxxx'))
    print(c.parseString(';;'))

