from typing import Any, Literal
import customtkinter as ctk # type: ignore
import tkinter as tk


class CTkPanedWindow(ctk.CTkFrame):
    def __init__(self, master: tk.Tk, orient: Literal['horizontal', 'vertical']=tk.HORIZONTAL, **kwargs: Any):
        super().__init__(master, **kwargs) # type: ignore
        
        self.paned_window = tk.PanedWindow(self, orient=orient, bd=0, sashwidth=6)
        self.paned_window.pack(fill=tk.BOTH, expand=True)
        
        self._apply_theme()

    def _apply_theme(self):
        """Applies the current CTk theme colors to the PanedWindow."""
        theme: dict[str, dict[str, str]] = ctk.ThemeManager.theme # type: ignore
        fg_color = theme["CTkFrame"]["fg_color"]
        
        # Handle tuple colors
        if isinstance(fg_color, (list, tuple)):
            fg_color = fg_color[0] if ctk.get_appearance_mode() == "light" else fg_color[1]
        
        self.paned_window.config(bg=fg_color)

    def add(self, child: tk.Widget, **kwargs: Any) -> None: 
        self.paned_window.add(child, **kwargs) # type: ignore

    def remove(self, child: tk.Widget):
        self.paned_window.remove(child) # type: ignore
    
    def sash_coord(self, index: int) -> tuple[int, int]:
        return self.paned_window.sash_coord(index) # type: ignore
    
    def sash_place(self, index: int, x: int, y: int):
        self.paned_window.sash_place(index, x, y) # type: ignore  


class App(ctk.CTk):
    def __init__(self):
        super().__init__() # type: ignore
        self.geometry("300x300")
        self.title("CustomTkinter")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.paned_window = CTkPanedWindow(
            self, orient="horizontal", #sashwidth=10, sashrelief="ridge"
        )
        self.paned_window.grid(row=0, column=0, padx=0, pady=0, sticky="nsew") # type: ignore

        frame1 = ctk.CTkFrame(self.paned_window)
        frame2 = ctk.CTkFrame(self.paned_window)
        self.paned_window.add(frame1) # type: ignore
        self.paned_window.add(frame2) # type: ignore
        
        label1 = ctk.CTkLabel(frame1, text="Frame 1")
        label1.grid(row=0, column=0, padx=10, pady=10) # type: ignore
        label2 = ctk.CTkLabel(frame2, text="Frame 2")
        label2.grid(row=0, column=0, padx=10, pady=10) # type: ignore

if __name__ == "__main__":
    app = App()
    app.mainloop() # type: ignore
