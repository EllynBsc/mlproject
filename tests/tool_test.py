
from mlproject.tools import haversine
import pytest

def test_haversing_distance():
    # Le Wagon location
    lat1, lon1 = 48.865070, 2.380009
    #Insert your coordinates from google maps here
    lat2, lon2 = 47.80421, 2.27609
    distance = haversine(lon1, lat1, lon2, lat2)
    assert type(distance) == float
