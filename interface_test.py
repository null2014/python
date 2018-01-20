# -*- coding: utf-8 -*-
import requests
import unittest
#查询发布会接口
url = ''
r = requests.get(url,params={'eid':'1'})
result = r.json()


#断言返回值
assert result['status'] == 200
assert result['message'] == "success"
assert result['data']['name'] == "xx发布会"
assert result['data']['address'] == "深圳多丽科技楼"
assert result['data']['start_time'] == "2018-01-18"

class GetEventListTest(unittest.TestCase):
    '''查询发布会接口测试'''

    def setUp(self):
        self.url = ""

    def test_get_event_null(self):
        '''发布会ID为空'''
    r = requests.get(self.url,params={'eid':''})
    result = r.json()
    self.assertEqual(result['status'],10021)
    self.assertEqual(result['message'],"parameter error")

    def test_get_event_error(self):
        '''发布id不存在'''
        r = requests.get(self.url,params={'eid':''})
        result = r.json()
        self.assertEqual(result['status'],10022)
        self.assertEqual(result['message'],"parameter error")


        def test_get_event_success(self):
            '''发布id为1，查询成功'''
            r = requests.get(self.url,params={'eid':'1'})
            result = r.json()
            self.assertEqual(result['status'],200)
            self.assertEqual(result['message'],"success")
            self.assertEqual(result['data']['name'],"发布成功")
            self.assertEqual(result['data']['address'] == "深圳多丽科技楼")
            self.assertEqual(result['data']['start_time'] == "2018-01-18")


if __name__ == '__main__':
    unittest.main()



