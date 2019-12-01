class Point(object):
    x = 0
    y = 0
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


def GetLinePara(line):
    line.a = line.p1.y - line.p2.y
    line.b = line.p2.x - line.p1.x
    line.c = line.p1.x * line.p2.y - line.p2.x*line.p1.y


def GetCrossPoint(line1, line2):
    GetLinePara(line1)
    GetLinePara(line2)
    d = line1.a * line2.b - line2.a * line1.b
    p = Point()
    p.x = (line1.b * line2.c - line2.b * line1.c) * 1.0 /d
    p.y = (line1.c * line2.a - line2.c * line1.a) * 1.0 /d
    return p

#small pipe
p1 = Point(306663.1164, 2775320.0432)
p2 = Point(306666.4803, 2775317.2526)
line1 = Line(p1, p2)

#big pipe
p3 = Point(306671.790157843, 2775340.76755534)
p4 = Point(306662.918528736, 2775314.63928705)
line2 = Line(p3, p4)

Pcross = GetCrossPoint(line1, line2)
print "Cross Point: ", Pcross.x, Pcross.y
