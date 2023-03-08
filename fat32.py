from manim import *

class FAT32(Scene):
    def construct(self):
        # fat_grid = Rectangle(width=8, height=12, grid_xstep=2, grid_ystep=1)
        fat_grid = [Rectangle(width=2, height=1) for i in range(24)]
        fat_grid_vgroup = VGroup(*fat_grid)
        fat_grid_vgroup.arrange_in_grid(
            buff=(0, 0),
            rows=6,
            cols=4,
        )
        fat_grid_label = Tex("FileAllocationTable")
        self.add(fat_grid_label)
        fat_filetable = VGroup(fat_grid_label, fat_grid_vgroup).arrange(DOWN)
        fat_filetable.to_corner(UP + LEFT)
        fat_grid_label.to_corner(LEFT)


        self.play(FadeIn(fat_grid_vgroup, shift=DOWN))
        self.play(
            fat_grid[0].animate.set_fill(RED, opacity=0.5),
            fat_grid[1].animate.set_fill(RED, opacity=0.5),
        )

        self.wait(5)

