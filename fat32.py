from manim import *

class FAT32(Scene):
    def construct(self):
        fat_grid = [Rectangle(width=2, height=1) for _ in range(24)]
        for i in range(24):
            fat_grid[i].add(Text(f"{i:#0{4}x}").scale(0.4).shift(RIGHT*0.6 + DOWN*0.3))
        fat_grid_vgroup = VGroup(*fat_grid)
        fat_grid_vgroup.arrange_in_grid(buff=(0, 0), rows=6, cols=4,)
        fat_grid_label = Tex("FileAllocationTable")
        self.add(fat_grid_label)
        fat_filetable = VGroup(fat_grid_label, fat_grid_vgroup).arrange(DOWN)
        fat_filetable.to_corner(UP + LEFT)
        fat_grid_label.to_corner(LEFT)

        # Initial & reserved clusters
        self.play(FadeIn(fat_grid_vgroup, shift=UP))
        self.play(*[fat_grid[i].animate.set_fill(RED, opacity=0.4) for i in range(2)])

        self.wait(5)

