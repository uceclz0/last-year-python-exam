import pytest
from simplemaths.simplemaths import SimpleMaths as sm

class TestSimpleMaths():
    def test_constructor(self):
    	x = sm(5)
    	assert x.number == 5

    def test_negative_constructor(self):
    	with pytest.raises(TypeError):
    		x = sm(5.5)

    def test_square_factorial(self):
    	x = sm(5)
    	y = x.square()
    	assert y == 25

    	y = x._factorial(5)
    	assert y == 120

    def test_power(self):
    	x = sm(5)
    	y = x.power(3)
    	assert y == 125

    def test_odd_or_even(self):
    	x = sm(5)
    	y = x.odd_or_even()
    	assert y == 'Odd'
    	x = sm(6)
    	y = x.odd_or_even()
    	assert y == 'Even'

    def test_square_root(self):
    	x = sm(9)
    	y = x.square_root()
    	assert y == 3

