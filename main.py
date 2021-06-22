from claserepositorio import repositorio
from vistasprov import ProvinciasView
from clasecontroladorpro import controlaprov
from claseobjet import ObjectEncoder

def main():
    conn=ObjectEncoder('datos.json')
    repo=repositorio(conn)
    vista=ProvinciasView()
    ctrl=controlaprov(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.grabar()

if __name__ == "__main__":
    main()