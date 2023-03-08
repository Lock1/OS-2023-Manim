from manim import *

class FAT32(Scene):
    def construct(self):
        fat_grid = Rectangle(width=8, height=12, grid_xstep=2, grid_ystep=1)
        fat_grid = Rectangle(width=3, height=4, grid_xstep=2, grid_ystep=1)
        fat_grid_label = Tex("FileAllocationTable")
        self.add(fat_grid_label)
        fat_filetable = VGroup(fat_grid_label, fat_grid).arrange(DOWN)
        fat_filetable.to_corner(UP + LEFT)
        self.play(Create(fat_grid))
        self.wait(5)

