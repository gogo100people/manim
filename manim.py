from manim import *
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
        inputShape = Text("Lemonfur.", color=RED) # Light Blue Triangle
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
                inputShape["."][0],
                outputShape
            )
        )
        self.wait(1)
        self.play(
            FadeOut(inputShape),
            FadeOut(outputShape),
            FadeOut(arrow)
        )
