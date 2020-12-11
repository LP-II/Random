import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.title("To Do list")

def tilføj_opg():
    opg = tekstfelt_opg.get()
    if opg != "":
        liste_opg.insert(tkinter.END, opg)
        tekstfelt_opg.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Advarsel!", message="Du skal tilføje en opgave")

def slet_opg():
    try:
        opg_index = liste_opg.curselection()[0]
        liste_opg.delete(opg_index)
    except:
        tkinter.messagebox.showwarning(title="Advarsel!", message="Du skal vælge en opgave at slette")

frame = tkinter.Frame(root)
frame.pack()


liste_opg = tkinter.Listbox(frame, height=15, width=50)
liste_opg.pack(side=tkinter.LEFT)

scrollbar_opg = tkinter.Scrollbar(frame)
scrollbar_opg.pack(side=tkinter.RIGHT, fill=tkinter.Y)

liste_opg.config(yscrollcommand=scrollbar_opg.set)
scrollbar_opg.config(command=liste_opg.yview)

tekstfelt_opg = tkinter.Entry(root, width=50)
tekstfelt_opg.pack()

knap_tilføj_opg = tkinter.Button(root, text="Tilføj opgave", width=48, command=tilføj_opg)
knap_tilføj_opg.pack()

knap_slet_opg = tkinter.Button(root, text="Slet opgave", width=48, command=slet_opg)
knap_slet_opg.pack()

root.mainloop()