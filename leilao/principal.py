from src.leilao.dominio import Usuario, Lance, Leilao

gui = Usuario("Gui")
yuri = Usuario("Yuri")

lance_do_yuri = Lance(yuri, 100.0)
lance_do_gui = Lance(gui, 100.0)
leilao.lances.appernd(lance_do_yuri)
for lance in leilao.lances:
    print("O usuário {lance.usuario.nome} deu um lance de {lance.valor}")
