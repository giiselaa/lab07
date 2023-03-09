import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class Cohete:
    def __init__(self, center_x, center_y, scale, color_general, color_puntas, cambiar_x, cambiar_y):
        self.center_x = center_x
        self.center_y = center_y
        self.scale = scale
        self.color_general = color_general
        self.color_puntas = color_puntas
        self.cambiar_x = cambiar_x
        self.cambiar_y = cambiar_y

    def dibujar_cohete(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, 50 * self.scale, 100 * self.scale, self.color_general
                                     )

        arcade.draw_triangle_filled(self.center_x, self.center_y + 100 * self.scale, self.center_x - 25 * self.scale,
                                    self.center_y + 50 * self.scale, self.center_x + 25 * self.scale, self.center_y +
                                    50 * self.scale, self.color_puntas)

        arcade.draw_rectangle_filled(self.center_x - 25 * self.scale, self.center_y - 50 * self.scale, 10 * self.scale,
                                     25 * self.scale, self.color_puntas)
        arcade.draw_rectangle_filled(self.center_x + 25 * self.scale, self.center_y - 50 * self.scale, 10 * self.scale,
                                     25 * self.scale, self.color_puntas)

        arcade.draw_circle_filled(self.center_x, self.center_y + 20 * self.scale, 10 * self.scale, arcade.color.BLACK)

    def update(self):

        self.center_y += self.cambiar_y
        self.center_x += self.cambiar_x


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.DARK_BLUE)

        self.cohete = Cohete(0, 0, 0.5, arcade.color.WHITE, arcade.color.RED, 3, 3)

    def on_draw(self):
        arcade.start_render()
        self.cohete.dibujar_cohete()

    def update(self, delta_time):
        self.cohete.update()


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")
    arcade.run()


main()
