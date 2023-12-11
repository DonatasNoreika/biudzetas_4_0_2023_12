import tkinter as tk


class PagrindinisLangas:
    def __init__(self, master):
        self.master = master
        self.master.title("Biudžetas")
        self.master.geometry("420x400")
        self.master.config(padx=20, pady=20)
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text="Įvesti pajamas")
        self.button2 = tk.Button(self.frame, text="Įvesti išlaidas")
        self.button1.pack()
        self.button2.pack()
        self.frame.pack()


def main():
    langas = tk.Tk()
    app = PagrindinisLangas(langas)
    langas.mainloop()


if __name__ == "__main__":
    main()
