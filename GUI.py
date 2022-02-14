import tkinter as tk
from turtle import width
from tfe import twenty_forty_eight

class MainWindow:
    def __init__(self, master):
        self.master = master
        
        self.frame = tk.Frame(self.master, width=200, height=50)
        self.frame.grid(row=0, column=0)
        
        self.tiles = tk.Canvas(self.frame, width=200, height=200)
        self.tiles.grid(row=1, column=0)
        
        self.game = twenty_forty_eight(1)
        #self.assets = self.background_create()
        self.bindings()
        
    def bindings(self):
        self.master.bind('<Left>', lambda event: self.move_event(-3))
        self.master.bind('<Right>', lambda event: self.move_event(-1))
        self.master.bind('<Up>', lambda event: self.move_event(0))
        self.master.bind('<Down>', lambda event: self.move_event(-2))

    def tile_background(self):
        return self.tiles.create_rectangle(40, 40, 0, 0, fill=self.game.colours[4])
    
    def move_event(self, direction):
        self.game.turn(direction)
        self.board_display()
    
    def board_display(self):
        y = 0
        for boardRow in self.game.board:
            x = 0
            for boardCol in boardRow:
                gameNumWid = tk.Label(self.frame, text=f'Game Num : {self.game.ID}')
                gameNumWid.grid(row=0, column=0)
                turnNumWid = tk.Label(self.frame, text=f'Turn Num : {self.game.turnNum}')
                turnNumWid.grid(row=0, column=1)
                
                self.tiles.create_rectangle(30+x*32, 30+y*32, 60+x*32, 60+y*32, fill=self.game.colours[boardCol], width=0)
                self.tiles.grid(row=1, column=0, columnspan=2)
                self.tiles.create_text(45+x*32, 45+y*32, text=str(boardCol))
                self.tiles.grid(row=1, column=0, columnspan=2)

                x += 1
            y += 1
        
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('200x200+400+400')
    window = MainWindow(root)
    window.board_display()
    window.frame.mainloop()