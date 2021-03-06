from unittest import TestCase
from leilao.dominio import Usuario, Lance, Leilao


class TestAvaliador(TestCase):

    def setUp(self):
        self.gui = Usuario("Gui")
        self.yuri = Usuario("Yuri")
        self.lance_do_yuri = Lance(self.yuri, 100.0)
        self.lance_do_gui = Lance(self.gui, 150.0)
        self.leilao = Leilao("Celular")

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        self.leilao.propoe(self.lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_maior_e_menor_lance_quando_leilao_tiver_apenas_um_lance(self):
        self.leilao.propoe(self.lance_do_gui)

        menor_valor_esperado = 150.0
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_decrescente(self):
        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(self.lance_do_yuri)
        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_o_leilao_tiver_tres_lances(self):
        self.vini = Usuario("Vini")
        self.lance_do_vini = Lance(self.vini, 200.0)
        self.leilao.propoe(self.lance_do_vini)
        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(self.lance_do_yuri)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
