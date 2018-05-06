from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        '''打开浏览器并且使浏览器停留3秒'''
        self.brower = webdriver.Chrome()
        self.brower.implicitly_wait(3)

    def tearDown(self):
        '''关闭浏览器'''
        self.brower.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        '''打开Django首页，在title中找To-Do字段，最后结束测试'''
        self.brower.get('http://localhost:8000')
        self.assertIn('To-Do',self.brower.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')

