import unittest
from method_missing import MethodMissing

class MethodMissingTest(unittest.TestCase):
  def test_method_missing_exists(self):
    class TestExistsClass(MethodMissing):
      def __init__(self):
        self.method_missing_called = False

      def method_missing(self, method_name, *args, **kwargs):
        self.method_missing_called = True

    test_obj = TestExistsClass()

    test_obj.nonexistent_method()

    self.assertTrue(test_obj.method_missing_called, 
        'method_missing should be called')

  def test_method_missing_passes_name_through(self):
    class TestNamePassedClass(MethodMissing):
      def __init__(self):
        self.method_missing_name = None

      def method_missing(self, method_name, *args, **kwargs):
        self.method_missing_name = method_name

    test_obj = TestNamePassedClass()

    test_obj.nonexistent_method()

    self.assertEquals('nonexistent_method', test_obj.method_missing_name,
        "'nonexistent_method' should be passed to method_missing")

  def test_method_missing_passes_self_through(self):
    class TestSelfPassedClass(MethodMissing):
      def __init__(self, tester):
        self.tester = tester
        self.self_reference = self

      def method_missing(self, method_name, *args, **kwargs):
        self.tester.assertTrue(isinstance(self, TestSelfPassedClass),
            'self should be of the right class')
        self.tester.assertEquals(self.self_reference, self,
            'self should be passed through')

    test_obj = TestSelfPassedClass(self)
    test_obj.nonexistent_method()

  def test_method_missing_passes_args_through(self):
    class TestArgsPassedClass(MethodMissing):
      def __init__(self):
        self.arg_value1 = None
        self.arg_value2 = None

      def method_missing(self, method_name, *args, **kwargs):
        self.arg_value1 = args[0]
        self.arg_value2 = args[1]

    test_obj = TestArgsPassedClass()
    foo_arg = 'foo'
    bar_arg = 'bar'
    test_obj.nonexistent_method(foo_arg, bar_arg)
    self.assertEquals(foo_arg, test_obj.arg_value1,
        'first positional arg should be passed through')
    self.assertEquals(bar_arg, test_obj.arg_value2,
        'second positional arg should be passed through')

  def test_method_missing_passes_kwargs_through(self):
    pass

if __name__ == '__main__':
  unittest.main()
