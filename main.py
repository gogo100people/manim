from manim import * # type: ignore
import os

class ImageInterpolationEx(Scene):
    def construct(self):
        img = ImageMobject(np.uint8([[63, 0, 0, 0],
                                     [0, 127, 0, 0],
                                     [0, 0, 191, 0],
                                     [0, 0, 0, 255]
                                     ]))

        img.height = 2
        img1 = img.copy()
        img2 = img.copy()
        img3 = img.copy()
        img4 = img.copy()
        img5 = img.copy()

        img1.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        img2.set_resampling_algorithm(RESAMPLING_ALGORITHMS["lanczos"])
        img3.set_resampling_algorithm(RESAMPLING_ALGORITHMS["linear"])
        img4.set_resampling_algorithm(RESAMPLING_ALGORITHMS["cubic"])
        img5.set_resampling_algorithm(RESAMPLING_ALGORITHMS["box"])
        img1.add(Text("nearest").scale(0.5).next_to(img1, UP))
        img2.add(Text("lanczos").scale(0.5).next_to(img2, UP))
        img3.add(Text("linear").scale(0.5).next_to(img3, UP))
        img4.add(Text("cubic").scale(0.5).next_to(img4, UP))
        img5.add(Text("box").scale(0.5).next_to(img5, UP))

        x = Group(img1, img2, img3, img4, img5)
        x.arrange()
        self.add(x)

class AreaScene(Scene):
    def construct(self):
        inputShape = Text("Lemonfur", color=RED) # Light Blue Triangle
        outputShape = Text("No Story", color=GREEN)

        outputShape.to_edge(DOWN)
        inputShape.to_edge(UP)
        arrow = Arrow()
        self.play(Create(arrow))
        self.play(Rotate(arrow, 0-PI/2))
        self.play(Write(inputShape))
        self.wait(1)
        self.play(
            Transform(
                inputShape,
                outputShape
            )
        )
        self.wait(1)
        self.play(
            FadeOut(inputShape),
            FadeOut(outputShape),
            FadeOut(arrow)
        )

class LegendarySMPPromo(Scene):
    def construct(self):
        text_legendarySMP = Text("Legendary SMP")
        text_legendarySMP.to_edge(UP)
        text_apply = Text("Apply Now")
        text_apply.to_edge(UP)
        text_in = Text("You are in!", color=GREEN)

        text_vidapp = Text("Create a\n30sec to 1min\n video application")
        text_vidapp_approve = Text("And if we approve it")
        text_vidapp_in = Text("You are in!", color=GREEN)
        text_vidapp_in.shift(DOWN)
        text_havefun = Text("Have fun!")

        circle = Circle()
        check = Text("✓")

        self.play(Write(text_legendarySMP))
        self.play(Create(circle))
        self.play(Transform(text_legendarySMP, text_apply))
        self.play(Circumscribe(text_apply))
        self.play(Create(check))
        self.play(FadeOut(text_apply), FadeOut(text_legendarySMP), FadeOut(circle), FadeOut(circle))
        self.wait(1)
        self.play(FadeOut(check))
        
        self.wait(3)

        self.play(
            Write(text_in),
            run_time=4
        )
        self.wait(1)
        self.play(Uncreate(text_in))
        self.play(Create(text_vidapp))
        self.wait(3)
        self.play(Transform(text_vidapp, text_vidapp_approve), Write(text_vidapp_in))
        self.wait(3)
        self.play(FadeOut(text_vidapp), FadeOut(text_vidapp_approve), FadeOut(text_vidapp_in))
        self.play(Write(text_havefun))
        self.wait(1)
        self.play(Unwrite(text_havefun))