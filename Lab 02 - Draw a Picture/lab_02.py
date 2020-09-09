# Start by importing arcade. 
import arcade
arcade.open_window(600, 600, "Drawing Lab")

# This places the sky blue background color.
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# This is the start of the drawing.
arcade.start_render()

# Draw grass.
arcade.draw_lrtb_rectangle_filled(0, 599, 199, 0, arcade.csscolor.GREEN)

# Draw a sun.
arcade.draw_circle_filled(50, 549, 50, arcade.csscolor.YELLOW)

# Draw a trail using the polygon function.
arcade.draw_polygon_filled(((0, 150),
                            (125, 115),
                            (325, 165),
                            (599, 135),
                            (599, 95),
                            (325, 125),
                            (125, 75),
                            (0, 110)),
                           arcade.csscolor.DARK_GRAY)

# Draw the trunk of tree 1.
arcade.draw_lrtb_rectangle_filled(120, 145, 250, 175, arcade.csscolor.BROWN)

# Draw a triangle shaped top of tree 1.
arcade.draw_triangle_filled(100, 250, 165, 250, 132.5, 300, arcade.csscolor.GREEN)

# Draw a trunk of tree 2.
arcade.draw_lrtb_rectangle_filled(350, 380, 275, 170, arcade.csscolor.BROWN)

# Draw an arc shaped top of tree 2.
arcade.draw_arc_filled(365, 275, 60, 100, arcade.csscolor.GREEN, 0, 180)

# Draw a pond made from the polygon function.
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

# Draw a fish jumping out of the pond.
# Draw an ellipse body with center of (450,65) width of 25 and height of 15.
# Draw a triangle tail with points at (425,55) (450,65) and (425,75).
# Draw a point for an eye at (455,66) and size 5.
arcade.draw_ellipse_filled(450, 65, 25, 15, arcade.csscolor.ORANGE)
arcade.draw_triangle_filled(425, 55, 450, 65, 425, 75, arcade.csscolor.ORANGE)
arcade.draw_point(455, 66, arcade.csscolor.BLACK, 5)

# Draw a flower with a stem.
# Draw 4 ellipses for the pedals.
# Draw a circle center.
# Draw a rectangle as the stem.
arcade.draw_lrtb_rectangle_filled(250, 255, 50, 10, arcade.csscolor.DARK_GREEN)
arcade.draw_ellipse_filled(262.5, 50, 20, 10, arcade.csscolor.HOTPINK)
arcade.draw_ellipse_filled(252.5, 60, 10, 20, arcade.csscolor.HOTPINK)
arcade.draw_ellipse_filled(242.5, 50, 20, 10, arcade.csscolor.HOTPINK)
arcade.draw_ellipse_filled(252.5, 40, 10, 20, arcade.csscolor.HOTPINK)
arcade.draw_circle_filled(252.5, 50, 5, arcade.csscolor.YELLOW)

# Draw a rhombus shaped kite in the sky.
arcade.draw_polygon_filled(((450, 455),
                           (465, 440),
                           (450, 410),
                           (435, 440)),
                           (arcade.csscolor.TOMATO))

# Draw a line connecting a rhombus shaped kite to the ground.
arcade.draw_line(450, 410, 500, 199, arcade.csscolor.BLACK)

# Draw an arrow shaped kite.
arcade.draw_polygon_filled(((250, 430),
                            (270, 360),
                            (250, 380),
                            (230, 360)),
                            (arcade.csscolor.LIME_GREEN))

# Draw a string connected to arrow shaped kite.
arcade.draw_line(250, 380, 225, 199, arcade.csscolor.BLACK)


# This ends the drawing.
arcade.finish_render()

# Show a continuous window.
arcade.run()
