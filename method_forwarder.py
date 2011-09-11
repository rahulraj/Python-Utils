from method_missing import MethodMissing

class MethodForwarder(MethodMissing):
  def __init__(self):
    self.forwardees = []

  def add_forwardee(self, forwardee):
    self.forwardees.append(forwardee)

  def method_missing(self, method_name, *args, **kwargs):
    for forwardee in self.forwardees:
      if hasattr(forwardee, method_name):
        return getattr(forwardee, method_name)(forwardee, *args, **kwargs)

    return super(MethodForwarder, self).method_missing(args, kwargs)
