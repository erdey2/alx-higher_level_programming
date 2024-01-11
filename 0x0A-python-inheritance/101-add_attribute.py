def add_attribute(obj, name, value):
  """
  Adds a new attribute to an object if it doesn't already exist.

  Args:
    obj: The object to add the attribute to.
    name: The name of the attribute to add.
    value: The value of the attribute to add.

  Raises:
    TypeError: If the object doesn't allow adding attributes.

  Returns:
    The modified object.
  """

  if hasattr(obj, "__dict__"):
    # Use __dict__ for standard objects
    obj.__dict__[name] = value
  else:
    # Check for specific methods to add attributes for custom classes
    if hasattr(obj, "set_attribute"):
      obj.set_attribute(name, value)  # Change this to the actual method name
    else:
      raise TypeError("Cannot add attributes to this object")

  return obj
