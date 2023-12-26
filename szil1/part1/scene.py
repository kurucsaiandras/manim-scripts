from manim import *
import sys
sys.path.insert(1, '../../helpers')

import helpers

class Part1(Scene):
    def construct(self):
        csuklo = helpers.makeCsuklo(2*LEFT)
        gorgo = helpers.makeGorgo(2*RIGHT)
        self.play(Write(csuklo), Write(gorgo))


with tempconfig({"quality": "low_quality", "preview": True}):
    scene = Part1()
    scene.render()