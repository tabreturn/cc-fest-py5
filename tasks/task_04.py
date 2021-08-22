# thonny plotter example (view > plotter)
# (also check out view > outline for functions)

def setup():
    size(300, 300)
    frame_rate(5)

def draw():
    background(100)
    theta = frame_count/10.
    translate(width/2, height/2)
    x = sin(theta)
    y = cos(theta)
    circle(x*50, y*50, 10)
    print('x:', x, 'y:', y*-1)

