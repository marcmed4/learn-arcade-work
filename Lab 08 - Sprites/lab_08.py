import random
import arcade

# Game constraints
SPRITE_SCALING_PLAYER = 0.3
SPRITE_SCALING_ART = 0.2
SPRITE_SCALING_BRUSH = 0.2
ART_COUNT = 50
BRUSH_COUNT = 25

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Sounds when sprite is hit
explosion_sound = arcade.load_sound("explosioncrunch.ogg")
force_sound = arcade.load_sound("forceField.ogg")


# Create the good sprite class
class ART(arcade.Sprite):

    # Bring good sprites back to the top of the screen
    def reset_pos(self):

        self.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    # Move the good sprites down
    def update(self):
        self.center_y -= 1

        # Check to see if the good sprites hit the bottom
        if self.top < 0:
            self.reset_pos()


# Create the bad sprite class
class Brush(arcade.Sprite):

    # Initializer
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

    # Cause the bad sprites to bounce
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


# Create the main class
class MarcGame(arcade.Window):

    # Initializer
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Marc's Sprite Game")

        # Create the list
        self.player_list = None
        self.art_list = None
        self.brush_list = None

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

        # Set the background color
        arcade.set_background_color(arcade.color.LIGHT_STEEL_BLUE)

    # Set up the game
    def setup(self):

        self.player_list = arcade.SpriteList()
        self.art_list = arcade.SpriteList()
        self.brush_list = arcade.SpriteList()

        self.score = 0

        self.player_sprite = arcade.Sprite("monkey.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the good sprites
        for i in range(ART_COUNT):

            art = ART("art.png", SPRITE_SCALING_ART)

            art.center_x = random.randrange(SCREEN_WIDTH)
            art.center_y = random.randrange(SCREEN_HEIGHT)

            self.art_list.append(art)

        # Create the bad sprites
        for i in range(BRUSH_COUNT):

            brush = Brush("brush.png", SPRITE_SCALING_BRUSH)

            brush.center_x = random.randrange(SCREEN_WIDTH)
            brush.center_y = random.randrange(SCREEN_HEIGHT)
            brush.change_x = random.randrange(-3, 4)
            brush.change_y = random.randrange(-3, 4)

            self.brush_list.append(brush)

    # draw the parts of the game
    def on_draw(self):
        arcade.start_render()

        self.art_list.draw()
        self.player_list.draw()
        self.brush_list.draw()

        # Show the score
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 20)

        if len(self.art_list) == 0:
            arcade.draw_text("Game Over", 100, 200, arcade.color.WHITE, 100)
            output = f"Score: {self.score}"
            arcade.draw_text(output, 200, 325, arcade.color.WHITE, 75)

    # Set the monkey up to teh mouse
    def on_mouse_motion(self, x, y, dx, dy):
        # Stop mouse movement if no good sprites are left
        if len(self.art_list) > 0:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    # Allow sprites to collide with game character and disappear
    def update(self, delta_time):

        self.art_list.update()

        art_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.art_list)

        for art in art_hit_list:
            art.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(force_sound)

        if len(self.art_list) > 0:
            self.brush_list.update()

        brush_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.brush_list)

        for brush in brush_hit_list:
            brush.remove_from_sprite_lists()
            self.score -= 1
            arcade.play_sound(explosion_sound)


# Make the main function
def main():
    window = MarcGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
