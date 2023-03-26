from manim import *

# Warning: Most of the time in this manim file, im too lazy for writing proper py code for it
#     i just {hotkey duplicate} all the time in vscode, i prefer focus on iterating animation faster
#     so yes, these code is hot garbage


class Keyboard(Scene):
    def construct(self):
        file_arrow_style = {
            "color"        : YELLOW,
            "stroke_width" : 3,
            "tip_length"   : 0.2,
        }
        
        # SB #1 - Initial setup
        keyboard_svg       = SVGMobject("img/basic_kb")
        keyboard_svg.scale(0.5)
        keyboard_state_box = Rectangle(width=0.6, height=0.6).set_fill(RED, opacity=0.6).set_stroke(width=0.6)
        keyboard_group     = VGroup(keyboard_state_box, keyboard_svg).arrange(RIGHT).to_corner(RIGHT + DOWN)
        kernel_code         = Code("kb_kernel_sample.c", line_spacing=0.7, language="c")
        kernel_code.scale(0.7).to_corner(LEFT)
        cpu_img            = ImageMobject("img/crop_cpu.png")
        cpu_img.scale(0.5).move_to(keyboard_svg.get_center() + 3*UP)
        instruction_label  = Tex("CPU Instruction")
        kernel_instruction = VGroup(instruction_label, kernel_code).arrange(DOWN)
        kernel_instruction.to_corner(LEFT)
        self.add(kernel_instruction)
        self.add(keyboard_group)
        self.add(cpu_img)
        self.wait(2)

        # SB #2 - Step-in busy wait
        ins_arr                     = Arrow(
            start=cpu_img.get_center() + LEFT*0.5, 
            end=kernel_code.get_center() + RIGHT*2.5 + UP*1.25, 
            **file_arrow_style
        )
        ins_breakpoint_highlighter  = Rectangle(width=5.5, height=0.41, color=YELLOW)
        # self.play(Create(ins_arr))
        # self.wait(2)
        ins_breakpoint_highlighter.move_to(ins_arr.get_end() + LEFT*2.8)
        self.play(Create(ins_breakpoint_highlighter))
        # self.wait(1)
        # self.play(FadeOut(ins_arr))
        # self.wait(1)
        ins_breakpoint_highlighter.generate_target()
        ins_breakpoint_highlighter.target.set_fill(YELLOW, opacity=0.3).set_stroke(opacity=0)
        self.play(MoveToTarget(ins_breakpoint_highlighter))
        # self.wait(2)

        # # Step in until keyboard_state_activate()
        # for _ in range(7):
        #     ins_breakpoint_highlighter.target.move_to(ins_breakpoint_highlighter.get_center() + DOWN*0.3)
        #     self.play(MoveToTarget(ins_breakpoint_highlighter))
        #     self.wait(0.5)

        # keyboard_state_box.generate_target()
        # keyboard_state_box.target.set_fill(GREEN, opacity=0.6)
        # self.play(MoveToTarget(keyboard_state_box))
        # self.wait(2)

        # # Looping
        # for _ in range(2):
        #     ins_breakpoint_highlighter.target.move_to(ins_breakpoint_highlighter.get_center() + UP*0.3)
        #     self.play(MoveToTarget(ins_breakpoint_highlighter))
        #     self.wait(0.5)
        #     ins_breakpoint_highlighter.target.move_to(ins_breakpoint_highlighter.get_center() + DOWN*0.3)
        #     self.play(MoveToTarget(ins_breakpoint_highlighter))
        #     self.wait(0.5)


        # SB #3 - Keyboard interrupt - Get interrupted
        interrupt_arr = Arrow(
            start=keyboard_svg.get_center() + UP*0.5, 
            end=cpu_img.get_center() + DOWN*0.7, 
            **file_arrow_style
        )
        arr_label = Tex("IRQ1").move_to(interrupt_arr.get_center() + RIGHT)
        self.play(FadeIn(interrupt_arr, shift=UP), FadeIn(arr_label, shift=UP))
        self.wait(1)
        cpu_label = Tex("!", font_size=56, color=YELLOW)
        cpu_label.move_to(cpu_img.get_center() + RIGHT*0.5 + UP*0.5)
        self.play(FadeIn(cpu_label, shift=UP))
        self.wait(2)

        kernel_instruction.generate_target()
        kernel_instruction.target.to_corner(LEFT + UP)
        interrupt_code  = Code("kb_int.c", line_spacing=0.7, language="c").scale(0.65)
        interrupt_label = Tex("Interrupt Handler")
        interrupt_group = VGroup(interrupt_label, interrupt_code).arrange(DOWN).to_corner(LEFT + DOWN)
        ins_breakpoint_highlighter.target.move_to(kernel_instruction.target.get_center() + UP*0.7)
        self.play(FadeIn(interrupt_group, shift=UP), MoveToTarget(kernel_instruction), MoveToTarget(ins_breakpoint_highlighter))
        self.wait(2)

        ins_breakpoint_highlighter.target.move_to(interrupt_code.get_center() + UP*0.85).stretch_to_fit_width(8)
        self.bring_to_front(ins_breakpoint_highlighter)
        self.play(MoveToTarget(ins_breakpoint_highlighter))


        # End animation
        self.wait(5)