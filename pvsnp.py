from manim import *
class TitleCard(Scene):
    def construct(self):
        p = Circle().shift(UP)
        np = Circle().scale(2)
        complete = Circle().scale(4).shift(DOWN*4)
        self.play(ShowCreation(p))
        self.wait(1)
        self.play(ShowCreation(np))
        self.wait(1)
        self.play(ShowCreation(complete))
        self.wait(2)
        title = TextMobject("Title Goes Here").scale(2).to_edge(edge=UP)
        self.play(Write(title))