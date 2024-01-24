import tkinter as tk

from tkinter import ttk 

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.canvas_width = 800
        self.canvas_height = 600
        self.root.configure(bg = 'black')
        self.canvas = tk.Canvas(self, root, width = self.canvas_width, height=self.canvas_height, bg= 'white', bd = 3, relief = tk.SUNKEN)
        self.canvas.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
        self.setup_navbar()
        self.setup_tools()
        self.setup_events()
        self.prev_x = None
        self.prev_y = None
    
    def setup_navbar(self):
        self.navbar = tk.Menu(self.root) 
        self.root.config(menu = self.navbar)

        self.file_menu = tk.Menu(self.navbar, tearoff=False)
        self.navbar.add_cascade(label = 'File', menu = self.file_menu)
        self.file_menu.add_command(label = 'Save Snapshot', command = self.take_snapshot)
        self.file_menu.add_separator()
        self.file_menu.add_command(label = 'Exit', command = self.root.quit)

        self.edit_menu = tk.Menu(self.navbar, tearoff= False)
        self.navbar.add_cascade(Label = 'Edit', menu = self.edit_menu)
        self.edit_menu.add_command(label = 'Undo', command = self.undo)

    def setup_tools(self):
        self.selected_tool = 'pen'
        self.colors = ['black', 'red', 'green', 'blue', 'yellow', 'orange', 'purple', 'white' ]
        self.selected_color = self.colors[0]
        self.brush_sizes = [2, 4, 6, 8]
        self.selected_size = self.brush_sizes[0]
        self.pen_types = ['line', 'round', 'square', 'arrow', 'diamond']
        self.selected_pen_type = self.pen_types[0]

        self.tool_frame = ttk.LabelFrame(self.root, text='Tools')
        self.tool_frame.pack(side= tk.RIGHT, padx = 5, fill = tk.Y)

        self.pen_button = ttk.Button(self.tool_frame, text = 'Pen', command=self.select_pen_tool)
        self.pen_button.pack(side=tk.TOP, padx = 5, pady = 5)

        self.eraser_button = ttk.Button(self.tool_frame, text = 'Eraser', command=self.select_eraser_tool)
        self.eraser_button.pack(side = tk.TOP, padx = 5, pady = 5)

        self.brush_size_label = ttk.Label(self.tool_frame, text = 'Brush size')
        self.brush_size_label.pack(side=tk.TOP, padx = 5, pady = 5)

        self.brush_size_combobox = ttk.Combobox(self.tool_frame, values = self.brush_sizes, state = 'readonly')
        self.brush_size_combobox.current(0)
        self.brush_size_combobox.pack(side = tk.TOP, padx = 5, pady = 5)
        self.brush_size_combobox.bind('<<ComboboxSelected>>', lambda event: self.select_size(int(self.brush_size_combobox.get())))
        
        self.color_label = ttk.Label(self.tool_frame, text = 'Color:')
        self.color_label.pack(side=tk.TOP, padx = 5, pady = 5)

        self.color_combobox = ttk.Combobox(self.tool_frame, values = self.colors, state = 'readonly')
        self.color_combobox.current(0)
        self.color_combobox.pack(side = tk.TOP, padx = 5, pady = 5)
        self.color_combobox.bind('<<ComboboxSelected>>', lambda event: self.selected_color(self.select_combobox.get()))

        self.pen_type_label = ttk.Label(self.tool_frame, text = 'Pen Type')
        self.pen_type_label.pack(side = tk.TOP, padx = 5, pady = 5)

        self.pen_type_combobox = ttk.Combobox(self.tool_frame, values = self.pen_types, state = 'readonly')
        self.pen_type_combobox.current(0)
        self.pen_type_combobox.pack(side = tk.TOP, padx = 5, pady = 5)
        self.pen_type_combobox.bind('<<BomboboxSelected>>', lambda event: self.selected_pen_type(self.pen_type_combobox.get()))

        self.clear_button = ttk.Button(self.tool_frame, text = 'Clear Canvas', command = self.clear_canvas)
        self.clear_button.pack(side = tk.TOP, padx = 5, pady = 5)

        self.circle_button = ttk.Button(self.shape_frame, text = 'Circle', command=self.draw_circle)
        self.circle_button.pack(side = tk.TOP, padx = 5, pady = 5)

        self.rectangle_button = ttk.Button(self.shape_frame, text = 'Rectangle', command = self.draw_rectangle)
        self.rectangle_button.pack(side = tk.TOP, padx = 5, pady = 5)
        