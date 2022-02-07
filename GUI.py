import tkinter as tk

board = [[2 for col in range(4)] for row in range(4)]

#for row in range(4):
#    for col in range(4):
#        tk.Label(root, text=f'{board[row][col]}', borderwidth=10).grid(row=row, column=col)

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.gameID = 0
        
        self.frame = tk.Frame(self.master, width = 400, height = 300)
        self.frame.pack()
        
        self.bindings()
        
    def bindings(self):
        self.master.bind('<Left>', lambda event: print('Left'))
        self.master.bind('<Right>', lambda event: print('Right'))
        self.master.bind('<Up>', lambda event: print('Up'))
        self.master.bind('<Down>', lambda event: print('Down'))

if __name__ == "__main__":
    root = tk.Tk()
    window = MainWindow(root)
    window.frame.mainloop()