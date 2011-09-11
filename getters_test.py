import unittest
from getters import with_getters_for

class GettersTest(unittest.TestCase):
  def test_with_getters_for(self):
    class MyClass(object):
      def __init__(self, foo, bar):
        self.foo = foo
        self.bar = bar
    with_getters_for(MyClass, 'foo', 'bar')
    
    foo = 'foo_var'
    bar = 'bar_var'

    clazz = MyClass(foo, bar)
    self.assertEquals(foo, clazz.get_foo(), "Should have a getter for foo")
    self.assertEquals(bar, clazz.get_bar(), "Should have a getter for bar")

if __name__ == '__main__':
  unittest.main()
