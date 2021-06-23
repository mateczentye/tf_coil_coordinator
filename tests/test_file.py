import pytest
from tf_coil_coordinator import find_points, thick_check, tup_check, surface_area



@pytest.mark.dtype
def test_input_coordinates():
    with pytest.raises(TypeError):
        find_points(1,2,3)

@pytest.mark.dtype
def test_input_thickness():
    with pytest.raises(TypeError):
        find_points((0, 0), (0, 0), "asd")

@pytest.mark.length
def test_tuple_length():
    with pytest.raises(ValueError):
        find_points((0, 0, 0),(0, 0), 0)


@pytest.mark.length
def test_return_tuple():
    answer = find_points((5,-25),(40,0),5)
    assert len(answer) == 10 or len(answer) == 16

@pytest.mark.length
def test_return_coordinate_check():
    answer = find_points((5,-25),(40,0),5)
    for coord in answer:
        assert len(coord) == 2 or len(coord) == 3

@pytest.mark.value
def test_returned_values_for_coordinates():
    answer = find_points((50,0), (100,100), 20)
    assert answer == [
    (50.0, 0.0),
    (92.0, 0.0),
    (97.65685424949238, 2.3431457505076194),
    (100.0, 8.0),
    (100.0, 192.0),
    (97.65685424949238, 197.65685424949237),
    (92.0, 200.0),
    (50.0, 200.0),
    (50.0, 220.0),
    (92.0, 220.0), 
    (111.79898987322333,211.79898987322332),
    (120.0, 192.0),
    (120.0, 8.0),
    (111.79898987322333, -11.79898987322333),
    (92.0, -20.0),
    (50.0, -20.0)
    ]

@pytest.mark.value
def test_check_x_coordinates():
    with pytest.raises(ValueError):
        find_points((50,50), (0,0), 5)