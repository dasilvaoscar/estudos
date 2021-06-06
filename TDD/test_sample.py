from Person import Person
import pytest


class Tests:

  def test_one(self):
    x = 'Oscar'
    assert "s" in x

  def test_two(self):
    test_class = Person()
    if hasattr(test_class, "name"):
      assert 'test' in {'test': test_class.name}
    else:
      assert hasattr(test_class, "test")