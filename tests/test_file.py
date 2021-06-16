import pytest
from tf_coil_coordinator import find_points, thick_check,tup_check

@pytest.mark.dtype
def test_input_coordinates():
    answer = find_points(1,2,3)
    assert answer == "Invalid Input, coordinates must be in a tuple"

@pytest.mark.dtype
def test_input_thickness():
    answer = find_points((0,0),(0,0),"asd")
    assert answer == "Invalid Input, thickness must be an integer or a float"

@pytest.mark.length
def test_tuple_length():
    answer = find_points((0,0,0),(0,0),0)
    assert answer == "Input tuples must be 2 element long - coordinate on XZ plane"

@pytest.mark.length
def test_return_tuple():
    answer = find_points((5,-25),(40,0),5)
    assert len(answer) == 10

@pytest.mark.length
def test_return_coordinate_check():
    answer = find_points((5,-25),(40,0),5)
    for coord in answer:
        assert len(coord) == 2

@pytest.mark.value
def test_returned_values_for_coordinates():
    answer = find_points((5,-25),(40,0),5)
    assert answer == ((5.0, -25.0),
                    (40.0, -25.0),
                    (40.0, 25.0),
                    (5.0, 25.0),
                    (5.0, 30.0),
                    (40.0, 30.0),
                    (45.0, 25.0),
                    (45.0, -25.0),
                    (40.0, -30.0),
                    (5.0, -30.0))