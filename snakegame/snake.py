import pyglet
from numpy import array
from random import randrange

class Snake(pyglet.window.Window):
    def __init__(self, x=500, y=500):
        super().__init__(x, y, caption='Snek')
        #self.set_icon(pyglet.image.load('snake_icon.png'))

        self.batch = pyglet.graphics.Batch()
        self.dx, self.dy = dx, dy = [20]*2
        self.score = 0

        self.v = array([1, 0])
        self.r = array([1, 1])

        x0, y0 = self.r

        self.score_label = pyglet.text.Label(f'SCORE: {self.score}',
                        font_name='Menlo',
                        x=40, y=40)
        '''self.title_label = pyglet.text.Label('SNAKE',
                        font_name='Menlo',
                        x=40, y=10)
        '''

        xmax, ymax = self.get_size()
        self.food = lambda : array((randrange(xmax-self.dx), randrange(ymax-self.dy)))
        self.foodcolor = lambda : (randrange(255) for i in range(3))
        self.foodpos = foodpos = self.food()

        self.square = pyglet.shapes.Rectangle(x0, y0,
                        dx-4, dy-4,
                        color=(255, 255, 255),
                        batch=self.batch)

        self.bite = pyglet.shapes.Rectangle(foodpos[0], foodpos[1],
                        dx-4, dy-4,
                        color=self.foodcolor(),
                        batch=self.batch)

        self.squares = []
        self.positions = [self.r]

    def changedir(self, direction):
        x = array([1, 0])
        y = array([0, 1])
        d = dict(r=x, u=y, l=-x, d=-y)

        dir = d[direction]
        if self.v[0] != dir[0] and self.v[1] != dir[1]:
            self.v = dir

    def eat(self):
        self.score += 1
        self.score_label.text = f'SCORE: {self.score}'
        print('SCORE:', self.score)

        self.squares.append(pyglet.shapes.Rectangle(self.r[0], self.r[1],
                        self.dx-4, self.dy-4,
                        color=(255, 255, 255),
                        batch=self.batch))

    def update(self, dt):
        r, v = self.r, self.v
        bite, square = self.bite, self.square
        dx = dy = self.dx

        if abs(r[0] - self.foodpos[0]) < self.dx and abs(r[1] - self.foodpos[1]) < self.dy:
            self.eat()

            self.foodpos = self.food()
            bite.x, bite.y = self.foodpos
            bite.color = self.foodcolor()

        if r[0]*r[1] < 0 or r[0] > self.get_size()[0] or r[1] > self.get_size()[1]:
            self.close()

        squares, positions = self.squares, self.positions
        positions.insert(0, tuple(self.r))

        self.r += self.v*dx

        self.square.x, self.square.y = x, y = self.r

        if self.score > 1:
            for p in positions[1:]:
                if p[0] == x and p[1] == y: self.close()

        if len(positions) > self.score: self.positions = positions[:self.score]

        for i, s in enumerate(squares):
            s.x, s.y = positions[i]

    def on_draw(self):
        self.clear()
        self.batch.draw()

        #self.title_label.draw()
        self.score_label.draw()

    def on_activate(self):
        self.clear()

        pyglet.clock.schedule_interval(self.update, 1/20.0)

    def on_key_press(self, symbol, mods):
        keys = 'uldr'
        symbols = (65362, 65361, 65364, 65363)

        if symbol in symbols:
            self.changedir(keys[symbols.index(symbol)])

        if symbol == pyglet.window.key.Q: self.close()


if __name__ == '__main__':
    s = Snake()
    pyglet.app.run()
