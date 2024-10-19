import tkinter as tk
from tkinter import ttk

solution  = "jkshgvalz"

root = tk.Tk()
root.title("Hello World")

def if_clicked():
    print("Hallo")

root.geometry("600x600")

#Zeigt Frage an

label_question = ttk.Label(master=root, text="Question", font= "Calibri 24")
label_question.pack()

#Button um Loesung anzeigen zu lassen


button_solution = ttk.Button(master = root, text = "Solution", command=if_clicked)
button_solution.pack(side= "right")


#Zeigt die Loesungen an

label_answer = ttk.Label(master=root, text= solution)
label_answer.pack(expand=True)

anwser_frame = ttk.Frame(master=root)


anwser_frame.pack(side="bottom", pady= 60)



# Verschiedene Antwortmoeglichkeiten, jenachdem wie gut er die Frage beantwortet hat

button_answer_1 = ttk.Button(master= anwser_frame, text="Nochmal")
button_answer_1.pack(side="left")


button_answer_2 = ttk.Button(master=anwser_frame, text="Schwer")
button_answer_2.pack(side="left")

button_answer_3 = ttk.Button(master= anwser_frame, text="Normal")
button_answer_3.pack(side="left")

button_answer_4 = ttk.Button(master= anwser_frame, text="Einfach")
button_answer_4.pack(side="left")


root.mainloop()