import arcade
arcade.open_window(600, 600, "Drawing Lab")

# Background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Start of Drawing
arcade.start_render()

# Grass
# left of 0, right of 599
# bottom of 0, top 0f 199
arcade.draw_lrtb_rectangle_filled(0, 599, 199, 0, arcade.csscolor.GREEN)

# Sun
# Center of (50,549)
# Radius of 50
arcade.draw_circle_filled(50, 549, 50, arcade.csscolor.YELLOW)

# Running Trail
# Made Using Polygon Function
arcade.draw_polygon_filled(((0, 150),
                            (125, 115),
                            (325, 165),
                            (599, 135),
                            (599, 95),
                            (325, 125),
                            (125, 75),
                            (0, 110)),
                           arcade.csscolor.DARK_GRAY)

# Base of Tree 1
# Left of 120, Right of 145
# Top of 250, Bottom of 175
arcade.draw_lrtb_rectangle_filled(120, 145, 250, 175, arcade.csscolor.BROWN)

# Triangle Shaped Top of Tree 1
# Left Point (100,250)
# Right Point (165, 250)
# Top Point (132.5, 300)
arcade.draw_triangle_filled(100, 250, 165, 250, 132.5, 300, arcade.csscolor.GREEN)

# Trunk of Tree 2
# Left of 350, Right of 380
# Top of 275, Bottom of 170
arcade.draw_lrtb_rectangle_filled(350, 380, 275, 170, arcade.csscolor.BROWN)

# Arc Shaped Top of Tree 2
# Center of (365, 275
# Width of 60
# Height of 100
# Starting Angel is 0, Ending Angel is 180
arcade.draw_arc_filled(365, 275, 60, 100, arcade.csscolor.GREEN, 0, 180)

# Pond Made from Polygon Function
arcade.draw_polygon_filled(((325, 50),
                            (400, 80),
                            (430, 90),
                            (455, 95),
                            (500, 75),
                            (535, 70),
                            (550, 65),
                            (555, 58),
                            (465, 55),
                            (445, 40),
                            (400, 32),
                            (370, 12),
                            (335, 25)),
                           arcade.csscolor.AQUA)

# Fish jumping out of the pond
# ellipse body with center of (450,65) width of 25 and height of 15
# triangle tail with points at (425,55) (450,65) and (425,75)
# point for an at (455,66) and size 5
arcade.draw_ellipse_filled(450, 65, 25, 15, arcade.csscolor.ORANGE)
arcade.draw_triangle_filled(425, 55, 450, 65, 425, 75, arcade.csscolor.ORANGE)
arcade.draw_point(455, 66, arcade.csscolor.BLACK, 5)



# End of Drawing
arcade.finish_render()

# Continuous Window
arcade.run()