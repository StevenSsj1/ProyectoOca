import tkinter as tk
import random
from newWindow import NewScreen

class QuestionEntry(tk.Frame):
    
    def __init__(self, parent, question_number):
        tk.Frame.__init__(self, parent)
        self.question_number = question_number

        self.label = tk.Label(self, text=f"Ingrese la pregunta número {question_number}:")
        self.label.grid(row=0, column=0)

        self.entry = tk.Entry(self)
        self.entry.grid(row=1, column=0)
        
        self.respuesta = self.entry.get()
        
    def get_answer(self):
        self.respuesta = self.entry.get()

class App(tk.Frame):
    
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.parent.title("Preguntas")
        self.create_question_entries()
        self.parent.bind("<MouseWheel>", self.on_mousewheel)  # Detectar desplazamiento

        button = tk.Button(self.parent, text="Enviar", command=self.open_new_window)
        button.pack(padx=40)

    def open_new_window(self):
        self.question_list = self.get_questions()
        self.parent.destroy()  # Cerrar la ventana de preguntas
        return self.question_list

    def get_questions(self):
        question_list = []
        for question_entry in self.question_entries:
            question_entry.get_answer()
            if question_entry.respuesta != "":
                question_list.append(question_entry.respuesta)
        return question_list

    def createScrollbar(self):
        self.scrollable_frame = tk.Frame(self.parent)
        self.scrollable_frame.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(self.scrollable_frame)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.configure(highlightthickness=0)
        self.scrollbar = tk.Scrollbar(self.scrollable_frame, command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind("<Configure>", lambda event: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.inner_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")
    
    def create_question_entries(self):
        self.createScrollbar()
        self.question_entries = []
        for i, question_number in enumerate(range(1, 13)):
            question_entry = QuestionEntry(self.inner_frame, question_number)
            question_entry.grid(row=i, column=0, padx=3.5, pady=8)
            self.question_entries.append(question_entry)
    
    def on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        
if __name__ == "__main__":
    ROOT = tk.Tk()
    ROOT.geometry("350x490")
    APP = App(parent=ROOT)
    APP.mainloop()
