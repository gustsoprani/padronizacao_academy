import pytest
from src.main import somar, dividir

def test_somar():
    assert somar(2, 2) == 4

def test_dividir():
    assert dividir(10, 2) == 5
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)