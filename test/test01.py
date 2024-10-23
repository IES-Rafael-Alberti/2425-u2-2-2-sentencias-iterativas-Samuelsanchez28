# test_palabra_repetida.py

import pytest
from io import StringIO
from contextlib import redirect_stdout
from palabra_repetida import mostrar_palabra

def test_mostrar_palabra(capsys):
    palabra = "Hola"
    mostrar_palabra(palabra)
    
    # salida
    captured = capsys.readouterr()
    
    #salida esperada
    expected_output = "Hola\n" * 10
    assert captured.out == expected_output
