def assign_injectables(obj, locals_dict):
  def is_magic_variable(var_name):
    return var_name[0] == '_' and var_name[1] == '_' and \
       var_name[len(var_name) - 1] == '_'and \
       var_name[len(var_name) - 2] == '_'

  def is_injectable(var_name):
    if is_magic_variable(var_name):
      return False
    elif locals_dict[var_name] == obj:
      return False
    return True

  keys = locals_dict.keys()
  injectables = filter(is_injectable, keys)
  for injectable in injectables:
    setattr(obj, injectable, locals_dict[injectable])
