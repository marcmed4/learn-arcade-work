import arcade

SCREEN_WIDTH = 685
SCREEN_HEIGHT = 710


def draw_head_1(x, y):
    """Draw the head of the cat"""
    arcade.draw_ellipse_filled(150 + x, 150 + y, 170, 150, arcade.csscolor.GRAY)


def draw_head_2(x, y):
    """Draw the head of the 2nd cat"""
    arcade.draw_ellipse_filled(350 + x, 150 + y, 170, 150, arcade.csscolor.BEIGE)


def draw_eyes_1(x, y):
    """Draw the green eyes of the cat"""
    arcade.draw_circle_filled(130 + x, 165 + y, 15, arcade.csscolor.GREEN)
    arcade.draw_circle_filled(130 + x, 165 + y, 8.5, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(170 + x, 165 + y, 15, arcade.csscolor.GREEN)
    arcade.draw_circle_filled(170 + x, 165 + y, 8.5, arcade.csscolor.BLACK)


def draw_eyes_2(x, y):
    """Draw the blue eyes of the cat"""
    arcade.draw_circle_filled(330 + x, 165 + y, 15, arcade.csscolor.BLUE)
    arcade.draw_circle_filled(330 + x, 165 + y, 8.5, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(370 + x, 165 + y, 15, arcade.csscolor.BLUE)
    arcade.draw_circle_filled(370 + x, 165 + y, 8.5, arcade.csscolor.BLACK)


def draw_nose_mouth(x, y):
    """Draw the nose and mouth of the cat"""

    # Nose
    arcade.draw_triangle_filled(140 + x, 150 + y, 160 + x, 150 + y, 150 + x, 130 + y, arcade.csscolor.LIGHT_PINK)

    # Mouth
    arcade.draw_line(150 + x, 130 + y, 150 + x, 115 + y, arcade.csscolor.LIGHT_PINK)
    arcade.draw_parabola_outline(125 + x, 130 + y, 150 + x, -15, arcade.csscolor.LIGHT_PINK)
    arcade.draw_parabola_outline(175 + x, 130 + y, 150 + x, -15, arcade.csscolor.LIGHT_PINK)


def draw_ears_1(x, y):
    """Draw the ears of the 1st cat"""
    arcade.draw_triangle_filled(100 + x, 210 + y, 130 + x, 220 + y, 115.5 + x, 260 + y, arcade.csscolor.GREY)
    arcade.draw_triangle_filled(200 + x, 210 + y, 170 + x, 220 + y, 185.5 + x, 260 + y, arcade.csscolor.GREY)
    arcade.draw_triangle_filled(110 + x, 210 + y, 120 + x, 220 + y, 115.5 + x, 240 + y, arcade.csscolor.LIGHT_GREY)
    arcade.draw_triangle_filled(190 + x, 210 + y, 180 + x, 220 + y, 185.5 + x, 240 + y, arcade.csscolor.LIGHT_GREY)


def draw_ear_2(x, y):
    """Draw the ears of the 2nd cat"""
    arcade.draw_triangle_filled(300 + x, 210 + y, 330 + x, 220 + y, 315.5 + x, 260 + y, arcade.csscolor.BEIGE)
    arcade.draw_triangle_filled(400 + x, 210 + y, 370 + x, 220 + y, 385.5 + x, 260 + y, arcade.csscolor.BEIGE)
    arcade.draw_triangle_filled(310 + x, 210 + y, 320 + x, 220 + y, 315.5 + x, 240 + y, arcade.csscolor.LIGHT_SALMON)
    arcade.draw_triangle_filled(390 + x, 210 + y, 380 + x, 220 + y, 385.5 + x, 240 + y, arcade.csscolor.LIGHT_SALMON)


def draw_cat_1(x, y):
    """Includes all parts to draw entire cat 1"""
    draw_head_1(0 + x, 0 + y)
    draw_eyes_1(0 + x, 0 + y)
    draw_nose_mouth(0 + x, 0 + y)
    draw_ears_1(0 + x, 0 + y)


def draw_cat_2(x, y):
    """Includes all parts to draw entire cat 2"""
    draw_head_2(0 + x, 0 + y)
    draw_eyes_2(0 + x, 0 + y)
    draw_nose_mouth(200 + x, 0 + y)
    draw_ear_2(0 + x, 0 + y)


def main():
    """THis is the main function"""
    arcade.open_window(685, 710, "Function Drawing")
    arcade.set_background_color(arcade.csscolor.TAN)
    arcade.start_render()

    draw_cat_1(-65, -75)
    draw_cat_1(-65, 100)
    draw_cat_1(-65, 275)
    draw_cat_1(-65, 450)

    draw_cat_2(-95, -75)
    draw_cat_2(-95, 100)
    draw_cat_2(-95, 275)
    draw_cat_2(-95, 450)

    draw_cat_1(275, -75)
    draw_cat_1(275, 100)
    draw_cat_1(275, 275)
    draw_cat_1(275, 450)

    draw_cat_2(245, -75)
    draw_cat_2(245, 100)
    draw_cat_2(245, 275)
    draw_cat_2(245, 450)

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started
