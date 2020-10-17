import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):

    '''
    test instance to check the behavior of the news class
    '''
    def setUp(self):

        '''
        This method runs before every test
        '''
        self.news1 = News("New York Times", "Trump is a genius", "I don't have DNA, I have USA", "https://trump.com", "https://trump.com", "12th October 2020" )

    def test_instance(self):
        self.assertTrue(isinstance(self.news1,News))

if __name__ == '__main__':
    unittest.main()
    
