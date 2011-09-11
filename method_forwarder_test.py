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

  def test_method_forwarding_with_multiple_forwardees(self):
    class TestMethodForwarderWithMultipleForwardees(MethodForwarder):
      def __init__(self):
        super(TestMethodForwarderWithMultipleForwardees, self).__init__()
    
    first_forwardee = Mock(['foo_method'])
    second_forwardee = Mock(['bar_method'])

    test_obj = TestMethodForwarderWithMultipleForwardees()
    test_obj.add_forwardee(first_forwardee)
    test_obj.add_forwardee(second_forwardee)

    first_forwardee.foo_method.return_value = 'foo'
    second_forwardee.bar_method.return_value = 'bar'

    first_result = test_obj.foo_method()
    second_result = test_obj.bar_method()

    self.assertEquals('foo', first_result, 'should forward to first_forwardee')
    self.assertEquals('bar', second_result, 
      "should forward to second_forwardee as first_forwardee doesn't respond")

  def test_method_forwarding_when_method_missing_from_all_forwardees(self):
    class TestForwardingMethodMissing(MethodForwarder):
      def __init__(self):
        super(TestForwardingMethodMissing, self).__init__()

    first_forwardee = Mock(['foo_method'])
    test_obj = TestForwardingMethodMissing()
    test_obj.add_forwardee(first_forwardee)
    self.assertRaises(NotImplementedError, test_obj.bar_method)
    

if __name__ == '__main__':
  unittest.main()
