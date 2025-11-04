def setup():
    global pathImg
    size(400, 600)
    imageMode(CENTER)
    pathImg = loadImage("path.png")
    pathImg.resize(width + 30, height + 30)

    background(252, 246, 224)

    # 第一层：路径上随机发光点
    for y in range(0, height, 40):
        for x in range(0, width + 50, 40):
            c = pathImg.get(x, y)
            if c != color(255, 255, 255) and random(10) < 5:
                offsetX = x + random(-10, 10)
                offsetY = y + random(-10, 10)
                s = random(40, 60)
                blurEllipse(offsetX, offsetY, s / 2, color(246, 212, 88))

    # 第二层：背景发光层
    for y in range(0, height + 50, 25):
        for x in range(0, width + 50, 25):
            c = pathImg.get(x, y)
            if c == color(252, 246, 224):
                offsetX = x + random(-10, 10)
                offsetY = y + random(-10, 10)
                s = random(40, 60)
                t = map(y, 0, height / 2, 0, 1)
                cc = lerpColor(color(89, 96, 64), color(200, 223, 144), t)
                blurEllipse(offsetX, offsetY, s / 2, cc)

    # 加强光晕点
    blurEllipse(width / 2 + 10, 250, 25, color(142, 136, 124))
    blurEllipse(width / 2, 520, 25, color(234, 110, 74))
    saveFrame("output.png")


def blurEllipse(cx, cy, coreR, c):
    noStroke()
    for i in range(int(coreR)):
        r = coreR - i
        a = map(i, 0, coreR, 0, 255)
        fill(red(c), green(c), blue(c), a)
        ellipse(cx, cy, r * 2, r * 2)


def draw():
    pass


def mousePressed():
    background(234, 110, 74)
