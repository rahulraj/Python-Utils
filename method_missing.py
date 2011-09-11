"""
Module that defines a mixin to allow users to write classes that support
the method_missing method, similar to what Ruby has.

To use, inherit from MethodMissing, and override method_missing. It will
be called when the descendant object is sent a message it does not understand.

Note that Python does not have a way to differentiate between methods and
field access; I generally avoid this by using getter methods when fields need
to be accessed from outside the class.
"""
import functools

class MethodMissing(object):
  """
  The class to inherit from to use method_missing
  """
  def __getattr__(self, attribute_name):
    """
    Python 'magic method' that is called when normal attribute lookup fails
    
    Args:
      attribute_name the name of the attribute that didn't exist.

    Returns:
      Partially applied version self.method_missing on the assumption that it 
      will be immediately called with the remaining arguments. The partial
      application allows the method name to pass through.
    """
    return functools.partial(self.method_missing, attribute_name)

  def method_missing(self, method_name, *args, **kwargs):
    """
    The method to call when a message is sent to self that it does not have
    a method for; should be implemented by subclasses

    Args:
      method_name the method that the user tried to call
      *args positional arguments for the method.
      **kwargs keyword arguments for the method.
    """
    raise NotImplementedError
