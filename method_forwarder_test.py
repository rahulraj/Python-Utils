import unittest
from method_forwarder import MethodForwarder
from mock import Mock

class MethodForwarderTest(unittest.TestCase):
  def test_method_forwarding(self):
    class TestMethodForwarder(MethodForwarder):
      def __init__(self):
        super(TestMethodForwarder, self).__init__()

    mock_forwardee = Mock()
    mock_forwardee.foo_method.return_value = 'a return value'

    test_obj = TestMethodForwarder()
    test_obj.add_forwardee(mock_forwardee)

    result = test_obj.foo_method()
    self.assertEquals('a return value', result,
        'method should be forwarded')

if __name__ == '__main__':
  unittest.main()
