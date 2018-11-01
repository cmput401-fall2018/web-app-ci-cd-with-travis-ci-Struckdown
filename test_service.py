from unittest.mock import patch
from service import *


@patch("service.Service.bad_random", return_value=10)
def test_divide():
	x = Service()
	value = x.divide(2)
	assert(value == 5)


def test_abs_plus():
	value = 1
	newValue = abs_plus(value)
	assert (newValue == value+1)

	value = -2
	newValue = abs_plus(value)
	assert (newValue == abs(value)+1)

	value = -1.5
	newValue = abs_plus(value)
	assert (newValue == abs(value)+1)


@patch("service.Service.bad_random", return_value=10)
def test_complicated_function(x):
	value = complicated_function(2)
	assert(value[0] == 4)
	assert(value[1] = 5)

