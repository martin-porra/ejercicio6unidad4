import tkinter as tk
from tkinter import Scrollbar, messagebox
from tkinter.constants import N, S, W
from claseprovincia import Provincia
from claseclima import clima

class provincialista(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.lb = tk.Listbox(self, **kwargs)
        scroll = tk.Scrollbar(self, command=self.lb.yview)
        self.lb.config(yscrollcommand=scroll.set)
        self.lb.grid(row=0, column=0, sticky=(N, S))
        scroll.grid(row=0, column=1, sticky=(N, S))

    def insertar(self, provincia, index=tk.END):
        text = '{0}'.format(provincia.getnom())
        self.lb.insert(index, text)

    def borrar(self, index):
        self.lb.delete(index, index)

    def modificar(self, provincia, index):
        self.borrar(index)
        self.insertar(provincia, index)

    def bind_doble_click(self, callback):
        handler = lambda _: callback(self.lb.curselection()[0])
        self.lb.bind("<Double-Button-1>", handler)


class provform(tk.LabelFrame):
    _fields = ("Nombre", "Capital", "Cantidad de habitantes",
               "Cantidad de departamentos/partidos")
    def __init__(self, master, **kwargs):
        super().__init__(master, text="Provincia", padx=10, pady=10, **kwargs)
        self.frame = tk.Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(self._fields)))
        self.frame.grid()

    def crearCampo(self, field):
        position, text = field
        label = tk.Label(self.frame, text=text)
        entry = tk.Entry(self.frame, width=40)
        label.grid(row=position, column=0, pady=(10, 5), sticky=W)
        entry.grid(row=position, column=1, pady=5, sticky=W)
        return entry

    def mostrarEstadoProvinciaEnFormulario(self, provincia):
        values = (provincia.getnom(), provincia.getcapi(),
                  provincia.getcanthabi(), provincia.getcandepa())

        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)

    def crearDesdeFormulario(self):
        values = [e.get() for e in self.entries]
        provincia = None
        try:
            provincia = Provincia(*values)
        except ValueError as e:
            messagebox.showerror("Error de Validación", str(e), parent=self)
        return provincia

    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)


class nuevaprov(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.resizable(0, 0)
        self.title('Nueva provincia')
        self.contacto = None
        self.form = provform(self)
        self.btn_add = tk.Button(self, text="Confirmar", command=self.confirmar)
        self.form.grid(row=0, column=0, padx=10, pady=10)
        self.btn_add.grid(row=1, column=0, pady=10)

    def confirmar(self):
        self.contacto = self.form.crearDesdeFormulario()
        if self.contacto:
            self.destroy()

    def show(self):
        self.grab_set()
        self.wait_window()
        return self.contacto

class actualizarprovf(provform):
    def __init__(self, master, **kwargs):
        self._fields = (
        "Nombre", "Capital", "Cantidad de habitantes", "Cantidad de departamentos/partidos", "Temperatura",
        "Sensación térmica", "Humedad")
        super().__init__(master, **kwargs)

    def mostrarEstadoProvinciaEnFormulario(self, provincia):
        miclima = clima()
        miclima.conectar(provincia.getnom(), provincia.getcapi())
        values = (provincia.getnom(), provincia.getcapi(),
                  provincia.getcanthabi(), provincia.getcandepa(), miclima.temp(),
                  miclima.termica(), miclima.humedad())

        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)


class ProvinciasView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lista de Provincias")
        self.resizable(0, 0)
        self.list = provincialista(self, height=15)
        self.form = actualizarprovf(self)
        self.btn_new = tk.Button(self, text="Agregar provincia")
        self.list.grid(row=0, column=0, padx=10, pady=(15, 10))
        self.form.grid(row=0, column=1, padx=10, pady=10, sticky=(N, S))
        self.btn_new.grid(row=1, column=1, pady=5)
        
    def setControlador(self, ctrl):
        self.btn_new.config(command=ctrl.crear)
        self.list.bind_doble_click(ctrl.seleccionar)
    def detalles(self):
        return self.form.crearDesdeFormulario()
    def verrovform(self, provincia):
        self.form.mostrarEstadoProvinciaEnFormulario(provincia)
    def agregarprov(self, provincia):
        self.list.insertar(provincia)
    def modifica(self, provincia, index):
        self.list.modificar(provincia, index)
    def borrar(self, index):
        self.form.limpiar()
        self.list.borrar(index)
    