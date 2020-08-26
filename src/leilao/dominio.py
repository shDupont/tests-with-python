from src.leilao.excecoes import LanceInvalido


class Usuario:
    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira
    
    def propoe(self, leilao, valor_lance):
        if not self._valor_e_valido(valor_lance):
            raise LanceInvalido('Não pode propor um lance com um valor maior que o valor da carteira')

        lance = Lance(self, valor_lance)
        leilao.propoe(lance)

        self.__carteira -= valor_lance

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def _valor_e_valido(self, valor):
        return valor <= self.__carteira

class Lance:
    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:
    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = 0.00
        self.menor_lance = 0.00

    def propoe(self, lance: Lance):
        if self._lance_e_valido(lance):
            if not self._tem_lances():
                self.menor_lance = lance.valor

            self.maior_lance = lance.valor

            self.__lances.append(lance)



    @property
    def lances(self):
        return self.__lances[:]


    def _tem_lances(self):
        return self.__lances


    def _sao_usuarios_diferentes(self, lance):
        if self.__lances[-1].usuario != lance.usuario:
            return True
        raise LanceInvalido("O mesmo usuario nao pode dar dois lances seguidos.")


    def _valor_maior_que_lance_anterior(self, lance):
        if lance.valor > self.__lances[-1].valor:
            return True
        raise LanceInvalido("O valor do lance deve ser maior que o valor do lance anterior.")


    def _lance_e_valido(self, lance):
        return not self._tem_lances() or (self._sao_usuarios_diferentes(lance) and
        self._valor_maior_que_lance_anterior(lance))
