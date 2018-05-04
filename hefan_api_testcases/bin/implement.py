from hefan_api_testcases.test_caes.test_api_userlogin import Test_api_case
from hefan_api_testcases.conf.set_up import report
import unittest,HTMLTestRuner

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test_api_case('test_case'))
    with open(report(),'wb') as fp:
        runner = HTMLTestRuner.HTMLTestRunner(
            stream=fp,
            title='测试报告',
            description='测试结果:'
        )
        runner.run(suite)



