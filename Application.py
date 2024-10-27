import tkinter as tk
import V0_1 as mlm

TextFont = ("Courier", 15)


def Main():

    def Search(search_term):
        symptomList.delete(0, tk.END)
        for item in mlm.symptoms:
            if search_term.lower() in item.lower():
                symptomList.insert(tk.END, item)

    def Diagnose(sympt):
        if not sympt: 
            OutputLabel.config(text = '')
            return None
        print([symptomList.get(x) for x in sympt])
        disease = mlm.Diagnose([symptomList.get(x) for x in sympt], mlm.knn_model)
        OutputLabel.config(text = disease)

    def ClearSelections():
        SelectedText.config(state = 'normal')
        SelectedText.delete("1.0", tk.END)
        symptomList.selection_clear(0, tk.END)

    def SymptSelection(sympt):
        SelectedText.config(state = "normal")
        SelectedText.delete("1.0", tk.END)
        SelectedText.insert(tk.END, ' ; '.join([symptomList.get(x) for x in sympt]))
        SelectedText.config(state = "disabled")

    window = tk.Tk()
    window.geometry("500x750+200+100")
    window.resizable(False, False)
    window.config(bg = "#fa2359")

    searchEntry = tk.Entry(window, 
                           bg = "#bfbfbf", 
                           font = TextFont, 
                           width = 14)
    searchEntry.place(anchor = tk.N, 
                      x = 250, 
                      y = 50)

    searchButton = tk.Button(window, 
                             bg = "#ea2359", 
                             activebackground = "#ea2359", 
                             activeforeground = "black", 
                             text = 'search', 
                             command = lambda: Search(searchEntry.get()), 
                             font = TextFont, 
                             width = 6)
    searchButton.place(anchor = tk.N, 
                       x = 390, 
                       y = 50,
                       height = 26)
    
    symptomList = tk.Listbox(window,
                             activestyle = "underline",
                             bg = "#fa2359",
                             font = TextFont,
                             border = 5, 
                             width = 35,
                             selectmode = "multiple",
                             selectforeground = "black",
                             selectbackground = "#f0bbbb",
                             height = 10)
    symptomList.place(anchor = tk.N,
                      x = 250,
                      y = 100)
    
    for symptom in mlm.symptoms:
        symptomList.insert(tk.END, symptom)

    symptomList.bind("<<ListboxSelect>>", 
                     lambda event: SymptSelection(symptomList.curselection()))

    diagnoseButton = tk.Button(window, 
                             bg = "#ea2359", 
                             activebackground = "#ea2359", 
                             activeforeground = "black", 
                             text = 'diagnose', 
                             command = lambda: Diagnose(symptomList.curselection()), 
                             font = TextFont, 
                             width = 8)
    diagnoseButton.place(anchor = tk.N, 
                       x = 250, 
                       y = 350,
                       height = 26)
    clearButton = tk.Button(window, 
                             bg = "#ea2359", 
                             activebackground = "#ea2359", 
                             activeforeground = "black", 
                             text = 'clear', 
                             command = ClearSelections, 
                             font = TextFont, 
                             width = 5)
    clearButton.place(anchor = tk.N, 
                       x = 400, 
                       y = 350,
                       height = 26)
    
    SelectedFrame = tk.Frame(window, width = 480, height = 200)
    SelectedFrame.place(anchor = tk.N,
                       x = 250,
                       y = 400)
    SelectedText = tk.Text(SelectedFrame, 
                           bg = "#df2359", 
                           width = 50, 
                           height = 10,
                           wrap="word",
                           selectforeground = "black",
                           selectbackground = "#f0bbbb")
    
    OutputLabel = tk.Label(window, font = TextFont,
                           bg = "#fa2359")
    OutputLabel.place(anchor = tk.S, x = 250, y = 700)
    
    
    SelectedText.pack()

    window.mainloop()

Main()