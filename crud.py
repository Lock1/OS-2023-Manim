from ctypes import alignment
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
            fat_grid_index.append(Tex(f"{i:#0{4}x}").scale(0.4).shift(RIGHT*0.72 + DOWN*0.35))
            fat_grid[i].add(fat_grid_index[i])
        fat_grid_vgroup = VGroup(*fat_grid)
        fat_grid_vgroup.arrange_in_grid(buff=(0, 0), rows=6, cols=4)
        fat_grid_label = Tex("FileAllocationTable - Logical View")
        fat_filetable = VGroup(fat_grid_label, fat_grid_vgroup).arrange(DOWN)
        fat_filetable.to_corner(UP + LEFT)
        fat_grid_label.to_corner(LEFT)

        # Animation - Set base scene, continuing previous FAT32
        self.add(fat_grid_label)
        # Reserved
        fat_grid[0].background_rectangle.set_fill(RED, opacity=0.4)
        fat_grid[1].background_rectangle.set_fill(RED, opacity=0.4)
        fat_cl0_label = Text("CLUSTER_0_VALUE").scale(0.28).move_to(fat_grid[0])
        fat_cl1_label = Text("CLUSTER_1_VALUE").scale(0.28).move_to(fat_grid[1])
        fat_grid[0].add(fat_cl0_label)
        fat_grid[1].add(fat_cl1_label)

        # Folder
        fat_grid[2].background_rectangle.set_fill(BLUE, opacity=0.4)
        fat_grid[4].background_rectangle.set_fill(BLUE, opacity=0.4)
        fat_grid[8].background_rectangle.set_fill(BLUE, opacity=0.4)
        fat_grid[10].background_rectangle.set_fill(BLUE, opacity=0.4)
        root_label = Text("root").scale(0.5).move_to(fat_grid[2])
        fat_grid[2].add(root_label)
        folder1_label = Text("folder1").scale(0.5).move_to(fat_grid[4])
        fat_grid[4].add(folder1_label)
        folder2_label = Text("folder2").scale(0.5).move_to(fat_grid[8])
        fat_grid[8].add(folder2_label)
        nested1_label = Text("nestedf1").scale(0.5).move_to(fat_grid[10])
        fat_grid[10].add(nested1_label)

        # File
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
        files_label = [Text(fname).scale(0.5).move_to(fat_grid[i]) for i, fname in files_grid]
        for i, (fatidx, _) in enumerate(files_grid):
            fat_grid[fatidx].background_rectangle.set_fill(GREEN, opacity=0.4)
            fat_grid[fatidx].add(files_label[i])

        self.add(fat_grid_vgroup, *fat_grid)
        
        # Animation - Read request
        request_label = Tex("Read")
        request_label.to_corner(RIGHT + UP).shift(LEFT*2)
        
        driver_request = [
            ["buf: <Pointer>"],
            ["name: kano"],
            ["ext: <None>"],
            ["parent_cluster_number: 0x02"],
            ["buffer_size: 10000"],
        ]
        request_table = Table(driver_request, include_outer_lines=True, arrange_in_grid_config={"cell_alignment": LEFT}).scale(0.4)
        request_table.move_to(request_label)
        request_table.shift(DOWN*2)
        self.play(FadeIn(request_label, shift=UP), FadeIn(request_table, shift=UP))

        


        # Animation - Last wait
        self.wait(5)

        # Animation - Destroy everything
        self.play(*[FadeOut(obj) for obj in self.mobjects])

