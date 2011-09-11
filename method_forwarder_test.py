import unittest
from method_forwarder import MethodForwarder
from mock import Mock

class MethodForwarderTest(unittest.TestCase):

  def setUp(self):
    self.mock_forwardee = Mock()

  def test_method_forwarding(self):
    class TestMethodForwarder(MethodForwarder):
      def __init__(self):
        super(TestMethodForwarder, self).__init__()

    self.mock_forwardee.foo_method.return_value = 'a return value'

    test_obj = TestMethodForwarder()
    test_obj.add_forwardee(self.mock_forwardee)

    result = test_obj.foo_method()
    self.assertEquals('a return value', result,
        'method should be forwarded')

  def test_method_forwarding_with_arguments(self):
    class TestMethodForwarderWithArgs(MethodForwarder):
      def __init__(self):
        super(TestMethodForwarderWithArgs, self).__init__()

    def mock_forwardee_method(self, *args, **kwargs):
      return (args[0], kwargs['number'])
    self.mock_forwardee.foo_method = mock_forwardee_method

    test_obj = TestMethodForwarderWithArgs()
    test_obj.add_forwardee(self.mock_forwardee)

    result = test_obj.foo_method('foo', number=5)
    self.assertEquals(('foo', 5), result,
        'arguments should be passed through')

if __name__ == '__main__':
  unittest.main()
