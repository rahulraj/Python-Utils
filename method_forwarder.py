"""
A module containing a MethodForwarder mixin that forwards messages to
other objects when the needed method is missing.
"""
from method_missing import MethodMissing

class MethodForwarder(MethodMissing):
  """
  Inherit from this class to use the forwarding functionality. Don't forget
  to call super.__init__ or self.forwardees won't be initialized.

  Use add_forwardee to add forwardees. This class does the rest.
  """
  def __init__(self):
    """
    Initializes self.forwardees. Call this using super.
    """
    super(MethodForwarder, self).__init__()
    self.forwardees = []

  def add_forwardee(self, forwardee):
    """
    Adds a forwardee. Note that order matters; forwardees will be checked
    in the order in which they were added.

    Args:
      forwardee the object to which to forward messages.
    """
    self.forwardees.append(forwardee)

  def method_missing(self, method_name, *args, **kwargs):
    """
    Implementation of method_missing, called when this class does not
    understand a message, as self inherits from MethodMissing. Searches
    the forwardees, and forwards the method to the first one found.

    Args:
      method_name the name of the method that was called.
      *args positional args for that method.
      **kwargs keyword args for that method.

    Returns:
      The return value that the forwardee returned after accepting the
      message and arguments.

    Raises:
      NotImplementedError if no object responds to the method. super will
      be called; by default this goes to MethodMissing which raises the error.
    """
    for forwardee in self.forwardees:
      if hasattr(forwardee, method_name):
        return getattr(forwardee, method_name)(forwardee, *args, **kwargs)

    return super(MethodForwarder, self).method_missing(*args, **kwargs)
