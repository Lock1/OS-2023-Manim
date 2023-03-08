from manim import *

class FAT32(Scene):
    def construct(self):
        # FileAllocationTable
        fat_grid = [Rectangle(width=2, height=1).add_background_rectangle() for _ in range(24)]
        for i in range(24):
            fat_grid[i].add(Text(f"{i:#0{4}x}").scale(0.4).shift(RIGHT*0.6 + DOWN*0.3))
        fat_grid_vgroup = VGroup(*fat_grid)
        fat_grid_vgroup.arrange_in_grid(buff=(0, 0), rows=6, cols=4)
        fat_grid_label = Tex("FileAllocationTable")
        self.add(fat_grid_label)
        fat_filetable = VGroup(fat_grid_label, fat_grid_vgroup).arrange(DOWN)
        fat_filetable.to_corner(UP + LEFT)
        fat_grid_label.to_corner(LEFT)

        # Legend
        fat_legend = [Rectangle(BLACK, width=3, height=1).add_background_rectangle() for _ in range(3)]
        fat_legend[0].add(Text("Reserved").scale(0.6))
        fat_legend[1].add(Text("Folder").scale(0.6))
        fat_legend[2].add(Text("File").scale(0.6))
        fat_legend[0].background_rectangle.set_fill(RED, opacity=0.4)
        fat_legend[1].background_rectangle.set_fill(BLUE, opacity=0.4)
        fat_legend[2].background_rectangle.set_fill(GREEN, opacity=0.4)
        fat_legend_vgroup = VGroup(*fat_legend)
        fat_legend_vgroup.arrange_in_grid(buff=(0, 0.3), rows=3, cols=1)
        fat_legend_vgroup.to_corner(RIGHT).shift(LEFT*1)

        # Animation - Initial & reserved clusters
        self.play(FadeIn(fat_grid_vgroup, shift=UP))
        self.play(*[fat_grid[i].background_rectangle.animate.set_fill(RED, opacity=0.4) for i in range(2)])
        self.play(FadeIn(fat_legend[0], shift=UP))


        # arrow_reserved_1 = Arrow(start=fat_grid[0], end=fat_grid[16], color=GOLD)
        # self.play(Create(arrow_reserved_1))

        self.wait(5)

