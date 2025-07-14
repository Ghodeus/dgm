import pytest
from sengen.sengen_link import Link

def test_link_area():
    link = Link(length=5.0, width=2.0)
    assert link.area() == pytest.approx(10.0)
    with pytest.raises(AssertionError):
        Link(length=-1, width=2)