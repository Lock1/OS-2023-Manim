from manim import *

# Warning: Most of the time in this manim file, im too lazy for writing proper py code for it
#     i just {hotkey duplicate} all the time in vscode, i prefer focus on iterating animation faster
#     so yes, these code is hot garbage


class CRUD(Scene):
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

        self.add(fat_grid_vgroup, *fat_grid, *files_label)
        
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
        request_table.shift(DOWN*1.9)
        self.play(FadeIn(request_label, shift=UP), FadeIn(request_table, shift=UP))
        self.wait(2)

        folder_arrow_style = {
            "color"        : RED,
            "stroke_width" : 3,
            "tip_length"   : 0.2,
        }
        parent_cl_arrow = Arrow(
            start=request_table.get_cell((4, 1)).get_center() + LEFT*1.3, 
            end=fat_grid[2].get_center(), **folder_arrow_style
        ).scale(0.8)
        self.play(Create(parent_cl_arrow))
        self.wait(1)

        # Animation - Show root DirectoryTable
        root_dirtable = [
            ["0x2", "root", "0"],
            ["0x4", "folder1", "0"],
            ["0x8", "folder2", "0"],
            ["0x3", "kano", "5123"],
            ["0x15", "nbuna", "1337"],
        ]
        root_table_label = [Text(text) for text in ["Cluster", "Name", "Filesize"]]
        root_table = Table(
            root_dirtable, 
            col_labels=root_table_label,
            include_outer_lines=True
        ).scale(0.34).set_row_colors(BLACK)
        root_table.add_to_back(root_table.get_highlighted_cell((1, 1), color=GOLD_A))
        root_table.add_to_back(root_table.get_highlighted_cell((1, 2), color=GOLD_A))
        root_table.add_to_back(root_table.get_highlighted_cell((1, 3), color=GOLD_A))

        root_dir_label   = Tex("DirectoryTable - Root (cluster 0x02)").scale(0.5)
        root_scene_table = VGroup(root_dir_label, root_table).arrange(DOWN, buff=SMALL_BUFF)
        root_scene_table.move_to(request_table).shift(DOWN*3.25)

        # Arrow first
        parent_dirtable_arrow = Arrow(
            start=fat_grid[2].get_center(),
            end=root_table.get_cell((1, 1)).get_center(), **folder_arrow_style
        ).scale(0.6)
        self.play(Create(parent_dirtable_arrow))
        self.wait(1)

        self.play(FadeIn(root_scene_table, shift=UP))
        self.wait(2)

        # Animation - Surrounding rectangle for iteration
        sr_iterator = SurroundingRectangle(root_table.get_rows()[1])
        sr_iterator.generate_target()
        self.play(FadeOut(parent_dirtable_arrow), FadeOut(parent_cl_arrow))
        self.play(Create(sr_iterator))
        self.wait(2)

        sr_iterator.target.move_to(root_table.get_rows()[2])
        self.play(MoveToTarget(sr_iterator))
        self.wait(1)

        sr_iterator.target.move_to(root_table.get_rows()[3])
        self.play(MoveToTarget(sr_iterator))
        self.wait(1)
        
        sr_iterator.target.move_to(root_table.get_rows()[4])
        self.play(MoveToTarget(sr_iterator))
        self.wait(1)

        # Animation - Highlight name and remove iterator
        highlight_name         = root_table.get_highlighted_cell((5, 2), color=GREEN)
        highlight_request_name = request_table.get_highlighted_cell((2, 1), color=GREEN)
        highlight_request_ext  = request_table.get_highlighted_cell((3, 1), color=GREEN)
        self.play(
            FadeIn(highlight_name), 
            FadeIn(highlight_request_name), 
            FadeIn(highlight_request_ext), 
            FadeOut(sr_iterator),
        )
        self.wait(2)


        # Animation - Highlight file size & buffer
        self.play(
            FadeOut(highlight_name), 
            FadeOut(highlight_request_name), 
            FadeOut(highlight_request_ext),
        )
        highlight_filesize         = root_table.get_highlighted_cell((5, 3), color=GREEN)
        highlight_request_buf_size = request_table.get_highlighted_cell((5, 1), color=GREEN)
        
        self.wait(1)
        self.play(
            FadeIn(highlight_filesize),
            FadeIn(highlight_request_buf_size),
        )
        self.wait(2)

        self.play(
            FadeOut(highlight_filesize),
            FadeOut(highlight_request_buf_size),
        )
        self.wait(2)

        # Animation - Arrow into first cluster
        file_arrow_style = {
            "color"        : YELLOW,
            "stroke_width" : 3,
            "tip_length"   : 0.2,
        }
        first_cl_arrow = Arrow(
            start=root_table.get_cell((5, 1)).get_center() + LEFT*0.4 + DOWN*0.1,
            end=fat_grid[3].get_center(),
            **file_arrow_style,
        )
        self.play(Create(first_cl_arrow))
        self.wait(1)

        # Animation - Read cluster
        read_text = Text("read_clusters(uint8buf + CLUSTER_SIZE*0, 0x03, 1);", t2c={"uint8buf": ORANGE}).scale(0.3)
        read_text.add_background_rectangle(YELLOW, stroke_width=1, stroke_opacity=1.0, buff=MED_SMALL_BUFF)
        read_text.background_rectangle.set_fill(BLACK, opacity=1.0)
        read_text.move_to(first_cl_arrow.get_center())

        buf_arrow_style = {
            "color"        : ORANGE,
            "stroke_width" : 3,
            "tip_length"   : 0.2,
        }
        buf_arrow = Arrow(
            start=request_table.get_cell((1, 1)).get_center() + LEFT*2,
            end=read_text.get_center() + LEFT*0.8,
            **buf_arrow_style,
        )
        self.play(FadeIn(read_text))
        self.wait(1)
        self.play(Create(buf_arrow))
        self.wait(2)
        self.play(FadeOut(buf_arrow))
        self.wait(1)

        # Animation - Reading second pointer
        self.play(Transform(files_label[0], Tex("0000 0006").scale(0.6).move_to(files_label[0])))
        self.play(FadeOut(read_text), FadeOut(first_cl_arrow))
        self.wait(1)
        cl_arrow = Arrow(
            start=fat_grid[3].get_center(),
            end=fat_grid[6].get_center(),
            **file_arrow_style,
        )
        self.play(Create(cl_arrow))
        read_text = Text("read_clusters(uint8buf + CLUSTER_SIZE*1, 0x06, 1);", t2c={"uint8buf": ORANGE, "*1": RED, "0x06": RED}).scale(0.3)
        read_text.add_background_rectangle(YELLOW, stroke_width=1, stroke_opacity=1.0, buff=SMALL_BUFF)
        read_text.background_rectangle.set_fill(BLACK, opacity=1.0)
        read_text.move_to(cl_arrow.get_center())
        self.play(FadeIn(read_text))
        self.wait(2)

        # Animation - Reading third pointer
        self.play(Transform(files_label[1], Tex("0000 000B").scale(0.6).move_to(files_label[1])))
        self.play(FadeOut(read_text), FadeOut(cl_arrow))
        self.wait(1)
        cl_arrow = Arrow(
            start=fat_grid[6].get_center(),
            end=fat_grid[0xB].get_center(),
            **file_arrow_style,
        )
        self.play(Create(cl_arrow))
        read_text = Text("read_clusters(uint8buf + CLUSTER_SIZE*2, 0x0B, 1);", t2c={"uint8buf": ORANGE, "*2": RED, "0x0B": RED}).scale(0.3)
        read_text.add_background_rectangle(YELLOW, stroke_width=1, stroke_opacity=1.0, buff=SMALL_BUFF)
        read_text.background_rectangle.set_fill(BLACK, opacity=1.0)
        read_text.move_to(cl_arrow.get_center())
        self.play(FadeIn(read_text))
        self.wait(2)

        # Animation - EOF read
        self.play(Transform(files_label[3], Tex("End of File").scale(0.6).move_to(files_label[3])))
        self.play(FadeOut(read_text), FadeOut(cl_arrow))
        self.wait(2)

        arrow_request = Arrow(
            start=fat_grid[0xb].get_center(),
            end=request_label.get_center() + DOWN*0.2,
            **file_arrow_style,
        )
        self.play(Create(arrow_request))
        self.wait(1)
        checkmark = Text("✓", color=GREEN)
        checkmark.move_to(request_label).shift(RIGHT)
        self.play(Write(checkmark))
        self.wait(3)

        # Animation - Remove right side
        self.play(
            FadeOut(arrow_request),
            FadeOut(request_label, shift=UP),
            FadeOut(checkmark, shift=UP),
            FadeOut(request_table, shift=UP),
            FadeOut(root_scene_table, shift=UP),
        )




        # Animation - Last wait
        self.wait(5)

        # Animation - Destroy everything
        self.play(*[FadeOut(obj) for obj in self.mobjects])

