from unittest import TestCase
from designTwitter import Twitter

class TestTwitter(TestCase):
    def setUp(self):
        self.obj = Twitter()

    def test_get_followers(self):
        message= "It's not working!"
        self.assertTrue(self.obj.get_followers(),message)


        # self.fail()

    # def test_get_user_home_timeline(self):
    #     self.fail()
    #
    # def test_get_targt_user_timeline(self):
    #     self.fail()
    #
    # def test_search(self):
    #     self.fail()

    def tearDowm(self):
        pass