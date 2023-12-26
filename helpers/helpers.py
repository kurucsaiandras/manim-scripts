from manim import *

def makeCsuklo(position):
    return Triangle(color=WHITE, fill_opacity=0.5).scale(0.3).shift(position)

def makeGorgo(position):
    gorgo_top = Triangle(color=WHITE, fill_opacity=0.5).scale(0.3).shift(position)
    gorgo_bot = Line(gorgo_top.get_left(), gorgo_top.get_right()).shift(0.35 * DOWN)
    return VGroup(gorgo_top, gorgo_bot)

def makeMegoszloTeher(q, start_point, end_point, scale):
    start_top = start_point + q*scale * UP
    end_top = end_point + q*scale * UP

    #TODO: dont scale tips and stroke
    start = Arrow(start=start_top, end=start_point, color=BLUE, buff=0)
    end = Arrow(start=end_top, end=end_point, color=BLUE, buff=0)
    fill = Polygon(start_top, end_top, end_point, start_point, color=BLUE, fill_opacity=0.3, stroke_opacity=0.0)
    topLine = Line(start_top, end_top, color=BLUE)
    #TODO: optional felirat
    return VGroup(start, end, fill, topLine)

def makeTeher(F, force_point, scale):
    start = force_point + F*scale * UP
    #TODO: vizszintes/fuggoleges, merre mutat, stb
    #TODO: optional felirat
    #TODO: dont scale tips and stroke
    return Arrow(start=start, end=force_point, color=GREEN, buff=0, max_tip_length_to_length_ratio=0.15)

def makeTamaszEroY(tamasz, size, side):
    if side == 'down':
        end = tamasz.get_bottom() + 0.05*DOWN
        start = end + size*DOWN
        return Arrow(start=start, end=end, color=RED, buff=0, max_tip_length_to_length_ratio=0.15)
    if side == 'up':
        end = tamasz.get_top() + 0.05*UP
        start = end + size*UP
        return Arrow(start=start, end=end, color=RED, buff=0, max_tip_length_to_length_ratio=0.15)

def makeTamaszEroX(tamasz, size, side):
    if side == 'left':
        end = tamasz.get_left() + 0.05*LEFT
        start = end + size*LEFT
        return Arrow(start=start, end=end, color=RED, buff=0, max_tip_length_to_length_ratio=0.15)
    if side == 'right':
        end = tamasz.get_right() + 0.05*RIGHT
        start = end + size*RIGHT
        return Arrow(start=start, end=end, color=RED, buff=0, max_tip_length_to_length_ratio=0.15)
    
def makeKotaX(start_point, lengths):
    kotaLines = []
    kotaNums = []
    kotaSize = 0.1
    p = start_point.copy()
    kotaLines.append(Line(p + kotaSize*UP, p + kotaSize*DOWN))
    for l in lengths:
        p += l*RIGHT
        kotaLines.append(Line(p + kotaSize*UP, p + kotaSize*DOWN))
        kotaNums.append(Text(str(l)).scale(0.5).shift(p + l/2*LEFT + 0.2*UP))
    ret = VGroup(Line(start_point, p))
    for i in range(len(kotaLines)):
        ret.add(kotaLines[i])
    for i in range(len(kotaNums)):
        ret.add(kotaNums[i])
    return ret

def makeKotaY(start_point, lengths):
    kotaLines = []
    kotaNums = []
    kotaSize = 0.1
    p = start_point.copy()
    kotaLines.append(Line(p + kotaSize*LEFT, p + kotaSize*RIGHT))
    for l in lengths:
        p += l*UP
        kotaLines.append(Line(p + kotaSize*LEFT, p + kotaSize*RIGHT))
        kotaNums.append(Text(str(l)).scale(0.5).shift(p + l/2*DOWN + 0.2*RIGHT))
    ret = VGroup(Line(start_point, p))
    for i in range(len(kotaLines)):
        ret.add(kotaLines[i])
    for i in range(len(kotaNums)):
        ret.add(kotaNums[i])
    return ret