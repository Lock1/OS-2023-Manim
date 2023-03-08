from manim import *

# Warning: Most of the time in this manim file, im too lazy for writing proper py code for it
#     i just {hotkey duplicate} all the time in vscode, i prefer focus on iterating animation faster
#     so yes, these code is hot garbage


class FAT32(Scene):
    def construct(self):
        # FileAllocationTable
        fat_grid_index = []
        fat_grid = [Rectangle(width=2, height=1).add_background_rectangle() for _ in range(24)]
        for i in range(24):
            fat_grid_index.append(Text(f"{i:#0{4}x}").scale(0.3).shift(RIGHT*0.68 + DOWN*0.35))
            fat_grid[i].add(fat_grid_index[i])
        fat_grid_vgroup = VGroup(*fat_grid)
        fat_grid_vgroup.arrange_in_grid(buff=(0, 0), rows=6, cols=4)
        fat_grid_label = Tex("FileAllocationTable - Logical View")
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

        # Animation - SB #1 - Initial Animation & Reserved clusters
        self.play(FadeIn(fat_grid_vgroup, shift=UP))
        self.play(
            *[fat_grid[i].background_rectangle.animate.set_fill(RED, opacity=0.4) for i in range(2)],
            FadeIn(fat_legend[0], shift=UP),
        )
        self.wait(2)

        # Animation - SB #2 - Reserved clusters value
        fat_cl0_label = Text("CLUSTER_0_VALUE").scale(0.25).move_to(fat_grid[0])
        fat_cl1_label = Text("CLUSTER_1_VALUE").scale(0.25).move_to(fat_grid[1])
        fat_grid[0].add(fat_cl0_label)
        fat_grid[1].add(fat_cl1_label)
        self.play(FadeIn(fat_cl0_label), FadeIn(fat_cl1_label))
        self.wait(2)

        # Animation - SB #2 - Folder clusters
        self.play(
            fat_grid[2].background_rectangle.animate.set_fill(BLUE, opacity=0.4),
            fat_grid[4].background_rectangle.animate.set_fill(BLUE, opacity=0.4),
            fat_grid[8].background_rectangle.animate.set_fill(BLUE, opacity=0.4),
            fat_grid[10].background_rectangle.animate.set_fill(BLUE, opacity=0.4),
            FadeIn(fat_legend[1], shift=UP),
        )
        self.wait(2)

        # Animation - SB #2 - Folder label
        root_label = Text("root").scale(0.5).move_to(fat_grid[2])
        fat_grid[2].add(root_label)
        folder1_label = Text("folder1").scale(0.5).move_to(fat_grid[4])
        fat_grid[4].add(folder1_label)
        folder2_label = Text("folder2").scale(0.5).move_to(fat_grid[8])
        fat_grid[8].add(folder2_label)
        nested1_label = Text("nestedf1").scale(0.5).move_to(fat_grid[10])
        fat_grid[10].add(nested1_label)
        self.play(
            FadeIn(root_label), FadeIn(folder1_label),
            FadeIn(folder2_label), FadeIn(nested1_label),
        )
        self.wait(2)

        # Animation - SB #2 - File clusters
        files_grid = [
            (3, "kano-0"),
            (6, "kano-1"),
            (9, "daijoubu-0"),
            (11, "kano-2"),
            (12, "daijoubu-1"),
            (13, "daijoubu-2"),
            (18, "frag-0"),
            (21, "nbuna-0"),
        ]
        self.play(
            *[fat_grid[i].background_rectangle.animate.set_fill(GREEN, opacity=0.4) for i, _ in files_grid], 
            FadeIn(fat_legend[2], shift=UP),
        )
        self.wait(2)

        # Animation - SB #2 - File names
        files_label = [Text(fname).scale(0.5).move_to(fat_grid[i]) for i, fname in files_grid]
        self.play(*[FadeIn(label) for label in files_label])
        self.wait(2)

        # Animation - SB #5 - File arrow
        file_arrow_style = {
            "color"        : YELLOW,
            "stroke_width" : 3,
            "tip_length"   : 0.2,
        }
        file_arrows_1 = [
            Arrow(start=fat_grid[3].get_center(), end=fat_grid[6].get_center(), **file_arrow_style).scale(0.6),
            Arrow(start=fat_grid[6].get_center(), end=fat_grid[11].get_center(), **file_arrow_style).scale(0.6),
        ]
        self.play(*[Create(arrow) for arrow in file_arrows_1])
        self.wait(1)

        # Second file arrow
        file_arrows_2 = [
            Arrow(start=fat_grid[9].get_center(), end=fat_grid[12].get_center(), **file_arrow_style).scale(0.6),
            Arrow(start=fat_grid[12].get_center(), end=fat_grid[13].get_center(), color=YELLOW, 
                  stroke_width=6, tip_length=0.7).scale(0.25, scale_tips=True),
        ]
        self.play(*[Create(arrow) for arrow in file_arrows_2])
        self.wait(2)

        # Animation - Remove arrows
        self.play(*[FadeOut(arrow) for arrow in file_arrows_1 + file_arrows_2])
        self.wait(1)

        # Animation - SB #4 - Peek physical, kano
        # .add_background_rectangle(opacity=0.5,buff=0.1)
        physical_file_label = [
            Text("0x0000 0006").move_to(files_label[0]).scale(0.4),
            Text("0x0000 000b").move_to(files_label[1]).scale(0.4),
            Text("End of File").move_to(files_label[3]).scale(0.4),
        ]
        self.play(Transform(files_label[0], physical_file_label[0]))
        self.play(Create(file_arrows_1[0]))
        self.wait(1)
        outline_box1 = SurroundingRectangle(physical_file_label[0], color=YELLOW, buff=SMALL_BUFF)
        outline_box2 = SurroundingRectangle(fat_grid_index[6], color=YELLOW, buff=SMALL_BUFF)
        self.play(Create(outline_box1), Create(outline_box2))
        self.wait(2)

        self.play(Uncreate(outline_box1), Uncreate(outline_box2))
        self.wait(1)

        self.play(Transform(files_label[1], physical_file_label[1]))
        self.play(Create(file_arrows_1[1]))
        self.wait(1)
        outline_box1 = SurroundingRectangle(physical_file_label[1], color=YELLOW, buff=SMALL_BUFF)
        outline_box2 = SurroundingRectangle(fat_grid_index[0xB], color=YELLOW, buff=SMALL_BUFF)
        self.play(Create(outline_box1), Create(outline_box2))
        self.wait(2)

        self.play(Uncreate(outline_box1), Uncreate(outline_box2))
        self.wait(1)

        self.play(Transform(files_label[3], physical_file_label[2]))
        self.wait(1)

        temp_label = Text("0x0FFF FFFF").move_to(files_label[3]).scale(0.4)
        self.play(Transform(files_label[3], temp_label))
        # Just realize transform also change the text object, whatever

        self.wait(5)

