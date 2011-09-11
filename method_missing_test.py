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
      def __init__(self, assertEquals):
        self.assertEquals = assertEquals
        self.self_reference = self

      def method_missing(self, method_name, *args, **kwargs):
        self.assertEquals(self.self_reference, self,
            'self should be passed through')

    test_obj = TestSelfPassedClass(self.assertEquals)
    test_obj.nonexistent_method()

  def test_method_missing_passes_args_through(self):
    pass

if __name__ == '__main__':
  unittest.main()
