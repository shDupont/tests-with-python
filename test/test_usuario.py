import pytest
from src.leilao.dominio import *

@pytest.fixture
def vini():
    return Usuario('Vini', 100.0)

@pytest.fixture
def leilao():
    return Leilao('Celular')

def test_deve_subtrair_valor_da_carteira_do_usuario_quando_esse_propor_um_lance(vini, leilao):
    vini.propoe(leilao, 50.00)

    assert vini.carteira == 50.0


def test_deve_permitir_propor_lance_quando_valor_e_menor_que_o_valor_da_carteira(vini, leilao):
    vini.propoe(leilao, 1.00)

    assert vini.carteira == 99.0


def test_deve_permitir_propor_lance_quando_o_valor_e_igual_ao_valor_da_carteira(vini, leilao):
    vini.propoe(leilao, 100.00)
    assert vini.carteira == 0.0


def test_nao_deve_permitir_propor_lance_quando_o_valor_e_maior_ao_valor_da_carteira(vini, leilao):
    with pytest.raises(LanceInvalido):
        vini.propoe(leilao, 200.00)
