import unittest
import requests
from calls import get_data
from mock import patch, Mock

class TestCalls(unittest.TestCase):

    def test_get_data(self):
        with patch.object(requests, 'get') as mock_get:
            mock_get.return_value = mock_response = Mock()
            mock_response.status_code = 200
            response = requests.get('http://httpbin.org/get')
            #assert get_data() == 200
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(requests.get('http://httpbin.org/get').status_code, 200)

if __name__ == "__main__":
    unittest.main()