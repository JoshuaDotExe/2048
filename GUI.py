import tkinter as tk
from tfe import twenty_forty_eight

class MainWindow:
    def __init__(self, master):
        self.master = master
        
        self.gameTab = tk.Frame(self.master, width=200, height=250, padx=20, pady=0)
        self.gameTab.grid(row=0, column=0)
        
        self.gameInfo = tk.Frame(self.gameTab, width=200, height=50)
        self.gameInfo.grid(row=0, column=0)
        
        self.tiles = tk.Frame(self.gameTab, width=200, height=200)
        self.tiles.grid(row=1, column=0, columnspan=2)
        
        self.game = twenty_forty_eight(1)
        self.assets = self.tile_background()
        self.bindings()
        
    def bindings(self):
        self.master.bind('<Left>', lambda event: self.move_event(-3))
        self.master.bind('<Right>', lambda event: self.move_event(-1))
        self.master.bind('<Up>', lambda event: self.move_event(0))
        self.master.bind('<Down>', lambda event: self.move_event(-2))

    def tile_background(self):
        tile_background_arr = [[tk.Label(self.tiles, padx=10, pady=10, bg="white") for x in range(4)] for y in range(4)]
        return tile_background_arr
        
    
    def move_event(self, direction):
        self.game.turn(direction)
        self.board_display()
    
    def board_display(self):
        y = 0
        for boardRow in self.game.board:
            x = 0
            for boardCol in boardRow:
                self.assets[y][x].config(text=boardCol, bg=self.game.colours[boardCol], width=1)
                self.assets[y][x].grid(row=y, column=x)
                #self.tiles.create_rectangle(30+x*32, 30+y*32, 60+x*32, 60+y*32, fill=self.game.colours[boardCol], width=0)
                #self.tiles.grid(row=1, column=0, columnspan=2)
                #self.tiles.create_text(45+x*32, 45+y*32, text=str(boardCol))
                #self.tiles.grid(row=1, column=0, columnspan=2)

                x += 1
            y += 1
        gameNumWid = tk.Label(self.gameInfo, text=f'Game Num : {self.game.ID}')
        gameNumWid.grid(row=0, column=0)
        turnNumWid = tk.Label(self.gameInfo, text=f'Turn Num : {self.game.turnNum}')
        turnNumWid.grid(row=0, column=1)
        
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('200x200+400+400')
    window = MainWindow(root)
    window.board_display()
    window.gameTab.mainloop()