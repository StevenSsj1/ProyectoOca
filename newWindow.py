import tkinter as tk
from PIL import Image, ImageTk

class NewScreen(tk.Frame):
    def __init__(self, parent, question_list):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.question_list = question_list
        self.init_ui()

    def init_ui(self):
        self.parent.title("EVALUACIÓN DE PREGUNTAS")
        #for question in self.question_list:f"Pregunta: {question_list[0]}"
        question_label = tk.Label(self.parent, text="prueba", font=("Arial", 12))
        question_label.pack()

        etiqueta = tk.Label(self.parent, text="¿Es correcta la pregunta?", font=("Arial", 14))
        etiqueta.pack(pady=20)

        boton_frame = tk.Frame(self.parent)
        boton_frame.pack()

        boton_frame.pack(anchor="center", pady=20)

    def boton_correcto_click(self):
        print("Respuesta correcta")

    def boton_incorrecto_click(self):
        print("Respuesta incorrecta")

if __name__ == "_main_":
    ROOT = tk.Tk()
    question_list = ["Pregunta 1","Pregunta 2","Pregunta 3"]  
    new_window = NewScreen(ROOT, question_list)
    new_window.pack()
    ROOT.mainloop()