import tf_coil_coordinator
import pytest
from paramak import ExtrudeMixedShape
from tf_coil_coordinator import find_points, surface_area, volume

@pytest.mark.value
def test_surface_area():
    paramak_area = ExtrudeMixedShape(
        points = find_points((50, 0), (100, 100), 20, line_type=True),
        distance=10,).area
    package_area = surface_area((50, 0),(100, 100), 20, 10)
    assert pytest.approx(package_area) == paramak_area

def test_volume():
    paramak_vol = ExtrudeMixedShape(
        points = find_points((50, 0), (100, 100), 20, line_type=True),
        distance=10,).volume
    package_vol = volume((50, 0),(100, 100), 20, 10)
    assert pytest.approx(package_vol) == paramak_vol