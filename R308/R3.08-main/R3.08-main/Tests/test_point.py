from R308.src.formes.point import Point

def test_distancecoord():
    p1 = Point (2 ,3)
    assert p1.distancecoord (2 ,3) == 0