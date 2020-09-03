import arcade
arcade.open_window(600, 600, "Drawing Lab")

# Background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Start of Drawing
arcade.start_render()

# Draw Grass
# left of 0, right of 599
# bottom of 0, top 0f 199
arcade.draw_lrtb_rectangle_filled(0, 599, 199, 0, arcade.csscolor.GREEN)

# Draw a Sun
# Center of (50,549)
# Radius of 50
arcade.draw_circle_filled(50, 549, 50, arcade.csscolor.YELLOW)

# Draw a Trail
arcade.draw_polygon_filled(((0, 150),
                            (125, 115),
                            (325, 165),
                            (599, 135),
                            (599, 95),
                            (325, 125),
                            (125, 75),
                            (0, 110)),
                           arcade.csscolor.DARK_GRAY)

# Draw Base of Tree
arcade.draw_lrtb_rectangle_filled(120, 145, 250, 175, arcade.csscolor.BROWN)

# End of Drawing
arcade.finish_render()

# Continuous Window
arcade.run()