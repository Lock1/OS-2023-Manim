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
        keyboard_svg.scale(0.5).to_corner(RIGHT + DOWN)
        kernelcode         = Code("kb_kernel_sample.c", line_spacing=0.7, language="c")
        kernelcode.scale(0.7).to_corner(LEFT)
        cpu_img            = ImageMobject("img/crop_cpu.png")
        cpu_img.scale(0.5).move_to(keyboard_svg.get_center() + 3*UP)
        instruction_label  = Tex("CPU Instruction")
        kernel_instruction = VGroup(instruction_label, kernelcode).arrange(DOWN)
        kernel_instruction.to_corner(LEFT)
        self.add(kernel_instruction)
        self.add(keyboard_svg)
        self.add(cpu_img)
        self.wait(2)

        # SB #2 - Step-in busy wait
        ins_arr                     = Arrow(
            start=cpu_img.get_center() + LEFT*0.5, 
            end=kernelcode.get_center() + RIGHT*2.5 + UP*1.25, 
            **file_arrow_style
        )
        ins_breakpoint_highlighter  = Rectangle(width=5.5, height=0.41, color=YELLOW)
        self.play(Create(ins_arr))
        self.wait(2)
        ins_breakpoint_highlighter.move_to(ins_arr.get_end() + LEFT*2.8)
        self.play(Create(ins_breakpoint_highlighter))
        self.wait(1)
        self.play(FadeOut(ins_arr))
        self.wait(1)
        ins_breakpoint_highlighter.generate_target()
        ins_breakpoint_highlighter.target.set_fill(YELLOW, opacity=0.3).set_stroke(opacity=0)
        self.play(MoveToTarget(ins_breakpoint_highlighter))
        self.wait(2)

        # Step in until keyboard_state_activate()
        for _ in range(7):
            ins_breakpoint_highlighter.target.move_to(ins_breakpoint_highlighter.get_center() + DOWN*0.3)
            self.play(MoveToTarget(ins_breakpoint_highlighter))
            self.wait(0.5)

        for _ in range(3):
            ins_breakpoint_highlighter.target.move_to(ins_breakpoint_highlighter.get_center() + UP*0.3)
            self.play(MoveToTarget(ins_breakpoint_highlighter))
            self.wait(0.5)
            ins_breakpoint_highlighter.target.move_to(ins_breakpoint_highlighter.get_center() + DOWN*0.3)
            self.play(MoveToTarget(ins_breakpoint_highlighter))
            self.wait(0.5)

        

        # SB #3 - Get interrupted
        # interruptcode = Code("kb_int.c", line_spacing=0.7, language="c")
        # interruptcode.scale(0.7).to_corner(LEFT + DOWN)
        # self.play(FadeIn(interruptcode, shift=UP))


        # End animation
        self.wait(5)