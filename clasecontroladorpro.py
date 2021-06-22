from vistasprov import ProvinciasView, nuevaprov
from clasemanejadorprov import ManejadorProvincias

class controlaprov:
    def __init__(self, repo, vista):
        self.repo = repo
        self.vista = vista
        self.seleccion = -1
        self.provincias = list(repo.obtenerlist())

    def crear(self):
        nuevaProvincia = nuevaprov(self.vista).show()
        if nuevaProvincia:
            provincia = self.repo.agregarprov(nuevaProvincia)
            self.provincias.append(provincia)
            self.vista.agregarprov(provincia)


    def modifica(self):
        if self.seleccion == -1:
            return
        rowid = self.provincias[self.seleccion].rowid
        detallesProvincia = self.vista.detalles()
        detallesProvincia.rowid = rowid
        provincia = self.repo.modifica(detallesProvincia)
        self.provincias[self.seleccion] = provincia
        self.vista.modifica(provincia, self.seleccion)
        self.seleccion = -1


    def seleccionar(self, index):
        self.seleccion = index
        provincia = self.provincias[index]
        self.vista.verrovform(provincia)

    def borrar(self):
        if self.seleccion == -1:
            return
        provincia = self.provincias[self.seleccion]
        self.repo.borrar(provincia)
        self.provincias.pop(self.seleccion)
        self.vista.borrar(self.seleccion)
        self.seleccion = -1

    def grabar(self):
        self.repo.grabar()

    def start(self):
        for c in self.provincias:
            self.vista.agregarprov(c)
        self.vista.mainloop()
