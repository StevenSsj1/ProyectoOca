import tkinter as tk
import random
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
        ar = random.choice(self.question_list)
        question_label = tk.Label(self.parent, text=ar, font=("Arial", 12))
        question_label.pack()

        etiqueta = tk.Label(self.parent, text="¿Es correcta la pregunta?", font=("Arial", 14))
        etiqueta.pack(pady=20)

        boton_frame = tk.Frame(self.parent)
        boton_frame.pack()

        imagen_correcto = Image.open("imagenes/visto.png")
        imagen_correcto = imagen_correcto.resize((50, 50), Image.ANTIALIAS)
        imagen_correcto = ImageTk.PhotoImage(imagen_correcto)
        boton_correcto = tk.Button(boton_frame, image=imagen_correcto, command=self.boton_correcto_click, bd=0)
        boton_correcto.image = imagen_correcto  
        boton_correcto.pack(side="left", padx=10)

        imagen_incorrecto = Image.open("imagenes/equis.png")
        imagen_incorrecto = imagen_incorrecto.resize((50, 50), Image.ANTIALIAS)
        imagen_incorrecto = ImageTk.PhotoImage(imagen_incorrecto)
        boton_incorrecto = tk.Button(boton_frame, image=imagen_incorrecto, command=self.boton_incorrecto_click, bd=0)
        boton_incorrecto.image = imagen_incorrecto 
        boton_incorrecto.pack(side="left", padx=10)

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