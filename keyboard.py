from manim import *

# Warning: Most of the time in this manim file, im too lazy for writing proper py code for it
#     i just {hotkey duplicate} all the time in vscode, i prefer focus on iterating animation faster
#     so yes, these code is hot garbage


class Keyboard(Scene):
    def construct(self):
        keyboard_svg = SVGMobject("img/basic_kb")
        self.play(FadeIn(keyboard_svg))
        self.wait(5)
        # FileAllocationTable
        # fat_grid_index = []
        # fat_grid = [Rectangle(width=2, height=1).add_background_rectangle() for _ in range(24)]
        # for i in range(24):
        #     fat_grid_index.append(Tex(f"{i:#0{4}x}").scale(0.4).shift(RIGHT*0.72 + DOWN*0.35))
        #     fat_grid[i].add(fat_grid_index[i])
        # fat_grid_vgroup = VGroup(*fat_grid)
        # fat_grid_vgroup.arrange_in_grid(buff=(0, 0), rows=6, cols=4)
        # fat_grid_label = Tex("FileAllocationTable - Logical View")
        # self.add(fat_grid_label)
        # fat_filetable = VGroup(fat_grid_label, fat_grid_vgroup).arrange(DOWN)
        # fat_filetable.to_corner(UP + LEFT)
        # fat_grid_label.to_corner(LEFT)

        # # Legend
        # fat_legend = [Rectangle(BLACK, width=3, height=1).add_background_rectangle() for _ in range(3)]
        # fat_legend[0].add(Text("Reserved").scale(0.6))
        # fat_legend[1].add(Text("Folder").scale(0.6))
        # fat_legend[2].add(Text("File").scale(0.6))
        # fat_legend[0].background_rectangle.set_fill(RED, opacity=0.4)
        # fat_legend[1].background_rectangle.set_fill(BLUE, opacity=0.4)
        # fat_legend[2].background_rectangle.set_fill(GREEN, opacity=0.4)
        # fat_legend_vgroup = VGroup(*fat_legend)
        # fat_legend_vgroup.arrange_in_grid(buff=(0, 0.3), rows=3, cols=1)
        # fat_legend_vgroup.to_corner(RIGHT).shift(LEFT*1)


        # # Animation - SB #1 - Initial Animation & Reserved clusters
        # self.play(FadeIn(fat_grid_vgroup, shift=UP))
        # self.play(
        #     *[fat_grid[i].background_rectangle.animate.set_fill(RED, opacity=0.4) for i in range(2)],
        #     FadeIn(fat_legend[0], shift=UP),
        # )
        # self.wait(2)


        # # Animation - SB #2 - Reserved clusters value
        # fat_cl0_label = Text("CLUSTER_0_VALUE").scale(0.28).move_to(fat_grid[0])
        # fat_cl1_label = Text("CLUSTER_1_VALUE").scale(0.28).move_to(fat_grid[1])
        # fat_grid[0].add(fat_cl0_label)
        # fat_grid[1].add(fat_cl1_label)
        # self.play(FadeIn(fat_cl0_label), FadeIn(fat_cl1_label))
        # self.wait(2)


        # # Animation - SB #2 - Folder clusters
        # self.play(
        #     fat_grid[2].background_rectangle.animate.set_fill(BLUE, opacity=0.4),
        #     fat_grid[4].background_rectangle.animate.set_fill(BLUE, opacity=0.4),
        #     fat_grid[8].background_rectangle.animate.set_fill(BLUE, opacity=0.4),
        #     fat_grid[10].background_rectangle.animate.set_fill(BLUE, opacity=0.4),
        #     FadeIn(fat_legend[1], shift=UP),
        # )
        # self.wait(2)


        # # Animation - SB #2 - Folder label
        # root_label = Text("root").scale(0.5).move_to(fat_grid[2])
        # fat_grid[2].add(root_label)
        # folder1_label = Text("folder1").scale(0.5).move_to(fat_grid[4])
        # fat_grid[4].add(folder1_label)
        # folder2_label = Text("folder2").scale(0.5).move_to(fat_grid[8])
        # fat_grid[8].add(folder2_label)
        # nested1_label = Text("nestedf1").scale(0.5).move_to(fat_grid[10])
        # fat_grid[10].add(nested1_label)
        # self.play(
        #     FadeIn(root_label), FadeIn(folder1_label),
        #     FadeIn(folder2_label), FadeIn(nested1_label),
        # )
        # self.wait(2)


        # # Animation - SB #2 - File clusters
        # files_grid = [
        #     (3, "kano-0"),
        #     (6, "kano-1"),
        #     (9, "daijoubu-0"),
        #     (11, "kano-2"),
        #     (12, "daijoubu-1"),
        #     (13, "daijoubu-2"),
        #     (18, "frag-0"),
        #     (21, "nbuna-0"),
        # ]
        # self.play(
        #     *[fat_grid[i].background_rectangle.animate.set_fill(GREEN, opacity=0.4) for i, _ in files_grid], 
        #     FadeIn(fat_legend[2], shift=UP),
        # )
        # self.wait(2)


        # # Animation - SB #2 - File names
        # files_label = [Text(fname).scale(0.5).move_to(fat_grid[i]) for i, fname in files_grid]
        # self.play(*[FadeIn(label) for label in files_label])
        # self.wait(2)


        # # Animation - SB #5 - File arrow
        # file_arrow_style = {
        #     "color"        : YELLOW,
        #     "stroke_width" : 3,
        #     "tip_length"   : 0.2,
        # }
        # file_arrows_1 = [
        #     Arrow(start=fat_grid[3].get_center(), end=fat_grid[6].get_center(), **file_arrow_style).scale(0.6),
        #     Arrow(start=fat_grid[6].get_center(), end=fat_grid[11].get_center(), **file_arrow_style).scale(0.6),
        # ]
        # self.play(*[Create(arrow) for arrow in file_arrows_1])
        # self.wait(1)

        # # Second file arrow
        # file_arrows_2 = [
        #     Arrow(start=fat_grid[9].get_center(), end=fat_grid[12].get_center(), **file_arrow_style).scale(0.6),
        #     Arrow(start=fat_grid[12].get_center(), end=fat_grid[13].get_center(), color=YELLOW, 
        #           stroke_width=6, tip_length=0.7).scale(0.25, scale_tips=True),
        # ]
        # self.play(*[Create(arrow) for arrow in file_arrows_2])
        # self.wait(2)


        # # Animation - Remove arrows
        # self.play(*[FadeOut(arrow) for arrow in file_arrows_1 + file_arrows_2])
        # self.wait(1)


        # # Animation - SB #4 - Peek physical, kano
        # # .add_background_rectangle(opacity=0.5,buff=0.1)
        # physical_file_label = [
        #     Tex("0x0000 0006").move_to(files_label[0]).scale(0.6),
        #     Tex("0x0000 000B").move_to(files_label[1]).scale(0.6),
        #     Tex("End of File").move_to(files_label[3]).scale(0.6),
        # ]
        # self.play(Transform(files_label[0], physical_file_label[0]))
        # self.play(Create(file_arrows_1[0]))
        # self.wait(1)
        # outline_box1 = SurroundingRectangle(physical_file_label[0], color=YELLOW, buff=SMALL_BUFF)
        # outline_box2 = SurroundingRectangle(fat_grid_index[6], color=YELLOW, buff=SMALL_BUFF)
        # self.play(Create(outline_box1), Create(outline_box2))
        # self.wait(2)

        # self.play(Uncreate(outline_box1), Uncreate(outline_box2))
        # self.wait(1)

        # self.play(Transform(files_label[1], physical_file_label[1]))
        # self.play(Create(file_arrows_1[1]))
        # self.wait(1)
        # outline_box1 = SurroundingRectangle(physical_file_label[1], color=YELLOW, buff=SMALL_BUFF)
        # outline_box2 = SurroundingRectangle(fat_grid_index[0xB], color=YELLOW, buff=SMALL_BUFF)
        # self.play(Create(outline_box1), Create(outline_box2))
        # self.wait(2)

        # self.play(Uncreate(outline_box1), Uncreate(outline_box2))
        # self.wait(1)

        # self.play(Transform(files_label[3], physical_file_label[2]))
        # self.wait(1)

        # temp_label = Tex("0x0FFF FFFF").move_to(files_label[3]).scale(0.5)
        # self.play(Transform(files_label[3], temp_label))
        # self.wait(2)
        # # Just realize transform also change the text object, whatever


        # # Animation - Revert all physical peek
        # temp_label = [
        #     Text("kano-0").move_to(files_label[0]).scale(0.5),
        #     Text("kano-1").move_to(files_label[1]).scale(0.5),
        #     Text("kano-2").move_to(files_label[3]).scale(0.5),
        # ]
        # self.play(
        #     Transform(files_label[0], temp_label[0]),
        #     Transform(files_label[1], temp_label[1]),
        #     Transform(files_label[3], temp_label[2]),
        #     FadeOut(file_arrows_1[0]),
        #     FadeOut(file_arrows_1[1]),
        # )
        # self.wait(3)


        # # Animation - SB #8 - Directory arrow & DirectoryTable
        # folder_arrow_style = {
        #     "color"        : RED,
        #     "stroke_width" : 3,
        #     "tip_length"   : 0.2,
        # }
        # root_arrows = [
        #     Arrow(start=fat_grid[4].get_center(), end=fat_grid[2].get_center(), **folder_arrow_style).scale(0.9),
        #     Arrow(start=fat_grid[8].get_center(), end=fat_grid[2].get_center(), **folder_arrow_style).scale(0.9),
        #     Arrow(start=fat_grid[0x15].get_center(), end=fat_grid[2].get_center(), **folder_arrow_style),
        #     Arrow(start=fat_grid[3].get_center(), end=fat_grid[2].get_center(), **folder_arrow_style).scale(0.6),
        # ]
        # self.play(*[Create(arrow) for arrow in root_arrows])
        # self.wait(1)


        # # Animation - SB #8 - Actual directory table
        # root_dirtable = [
        #     ["0x2", "root", "special"],
        #     ["0x4", "folder1", "subdir"],
        #     ["0x8", "folder2", "subdir"],
        #     ["0x3", "kano", "file"],
        #     ["0x15", "nbuna", "file"],
        # ]
        # root_table_label = [Text(text) for text in ["Cluster", "Name", "Attribute"]]
        # root_table = Table(
        #     root_dirtable, 
        #     col_labels=root_table_label,
        #     include_outer_lines=True
        # ).scale(0.4).set_row_colors(BLACK)
        # root_table.add_to_back(root_table.get_highlighted_cell((1, 1), color=GOLD_A))
        # root_table.add_to_back(root_table.get_highlighted_cell((1, 2), color=GOLD_A))
        # root_table.add_to_back(root_table.get_highlighted_cell((1, 3), color=GOLD_A))

        # root_dir_label = Tex("DirectoryTable - Root (cluster 0x02)").scale(0.7)
        # root_scene_table = VGroup(root_dir_label, root_table).arrange(DOWN)
        # root_scene_table.move_to(fat_legend[0])

        # self.play(*[FadeOut(mobj, shift=UP) for mobj in fat_legend], FadeIn(root_scene_table, shift=UP))
        # self.wait(2)


        # # Animation - Destroy all red arrows
        # self.play(*[FadeOut(arrow) for arrow in root_arrows])


        # # Animation - Point directory table to clusters FAT
        # root_arrows = [
        #     Arrow(start=root_table.get_cell((3, 1)).get_center(), end=fat_grid[4].get_center(), **folder_arrow_style).scale(0.9),
        #     Arrow(start=root_table.get_cell((4, 1)).get_center(), end=fat_grid[8].get_center(), **folder_arrow_style).scale(0.9),
        #     Arrow(start=root_table.get_cell((5, 1)).get_center(), end=fat_grid[3].get_center(), **folder_arrow_style).scale(0.9),
        #     Arrow(start=root_table.get_cell((6, 1)).get_center(), end=fat_grid[0x15].get_center(), **folder_arrow_style).scale(0.9),
        # ]
        # self.play(*[Create(arrow) for arrow in root_arrows])
        # self.wait(3)

        # # Animation - Destroy all dir table red arrows
        # self.play(*[FadeOut(arrow) for arrow in root_arrows])
        # self.wait(2)

        # # Animation - Revert back to legend
        # self.play(*[FadeIn(legend, shift=UP) for legend in fat_legend], FadeOut(root_scene_table, shift=UP))
        # self.wait(1)

        # # FIXME : Theres some, wacky transition for transforms for SB "Physical View"
        # # Its seems Transform() between Tex and Text is bit buggy
        # # Oh nvm, it seems Transform() direct reference does not trigger all parent.add() instantly
        # # Animation - Physical view
        # self.play(Transform(fat_grid_label, Tex("FileAllocationTable - Physical View").move_to(fat_grid_label)))
        # self.wait(1)
        # self.play(
        #     Transform(fat_cl0_label, Tex("0FFF FFF0").move_to(fat_cl0_label).scale(0.6)),
        #     Transform(fat_cl1_label, Tex("0FFF FFFF").move_to(fat_cl1_label).scale(0.6)),
        # )

        # self.wait(2)
        # self.play(
        #     Transform(files_label[0], Tex("0000 0006").move_to(files_label[0]).scale(0.6)),
        #     Transform(files_label[1], Tex("0000 000B").move_to(files_label[1]).scale(0.6)),
        #     Transform(files_label[2], Tex("0000 000C").move_to(files_label[2]).scale(0.6)),
        #     Transform(files_label[3], Tex("End of File").move_to(files_label[3]).scale(0.6)),
        #     Transform(files_label[4], Tex("0000 000D").move_to(files_label[4]).scale(0.6)),
        #     Transform(files_label[5], Tex("End of File").move_to(files_label[5]).scale(0.6)),
        #     Transform(files_label[6], Tex("End of File").move_to(files_label[6]).scale(0.6)),
        #     Transform(files_label[7], Tex("End of File").move_to(files_label[7]).scale(0.6)),
        # )
        
        # self.wait(2)
        # self.play(
        #     Transform(files_label[3], Tex("0FFF FFFF").move_to(files_label[3]).scale(0.6)),
        #     Transform(files_label[5], Tex("0FFF FFFF").move_to(files_label[5]).scale(0.6)),
        #     Transform(files_label[6], Tex("0FFF FFFF").move_to(files_label[6]).scale(0.6)),
        #     Transform(files_label[7], Tex("0FFF FFFF").move_to(files_label[7]).scale(0.6)),
        # )

        # # Animation - Folder 
        # self.wait(2)
        # self.play(
        #     Transform(root_label, Tex("End of File").move_to(root_label).scale(0.6)),
        #     Transform(folder1_label, Tex("End of File").move_to(folder1_label).scale(0.6)),
        #     Transform(folder2_label, Tex("End of File").move_to(folder2_label).scale(0.6)),
        #     Transform(nested1_label, Tex("End of File").move_to(nested1_label).scale(0.6)),
        # )

        # self.wait(2)
        # self.play(
        #     Transform(root_label, Tex("0FFF FFFF").move_to(root_label).scale(0.6)),
        #     Transform(folder1_label, Tex("0FFF FFFF").move_to(folder1_label).scale(0.6)),
        #     Transform(folder2_label, Tex("0FFF FFFF").move_to(folder2_label).scale(0.6)),
        #     Transform(nested1_label, Tex("0FFF FFFF").move_to(nested1_label).scale(0.6)),
        # )

        # # Animation - Empty spaces
        # self.wait(2)
        # empty_spaces = [
        #     0x05,
        #     0x07,
        #     0x0E,
        #     0x0F,
        #     0x10,
        #     0x11,
        #     0x13,
        #     0x14,
        #     0x16,
        #     0x17,
        # ]
        # empty_label = [Text("Empty").scale(0.5).move_to(fat_grid[i]) for i in empty_spaces]
        # self.play(*[FadeIn(label) for label in empty_label])

        # self.wait(2)
        # self.play(*[Transform(label, Tex("0000 0000").move_to(label.get_center()).scale(0.6)) for label in empty_label])

        # # Animation - Last wait
        # self.wait(5)

        # # Animation - Destroy everything
        # self.play(*[FadeOut(obj) for obj in self.mobjects])

