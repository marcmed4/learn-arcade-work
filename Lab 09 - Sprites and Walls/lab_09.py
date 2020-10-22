
# Artwork from http://kenney.nl

import random
import arcade

# Game Constraints
SPRITE_SCALING = .45
SPRITE_SCALING_COIN = .35
SPRITE_SCALING_CAR = .35
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"
SPRITE_SPEED = .75
VIEWPORT_MARGIN = 40
NUMBER_OF_COINS = 100
CAR_COUNT = 2
MOVEMENT_SPEED = 5
sound = arcade.load_sound("jingles_SAX00.ogg")


# Create the car class
class Car(arcade.Sprite):
    # Make code to cause car to follow player
    def follow_sprite(self, player_sprite):
        if self.center_y < player_sprite.center_y:
            self.center_y += min(SPRITE_SPEED, player_sprite.center_y - self.center_y)
        elif self.center_y > player_sprite.center_y:
            self.center_y -= min(SPRITE_SPEED, self.center_y - player_sprite.center_y)
        if self.center_x < player_sprite.center_x:
            self.center_x += min(SPRITE_SPEED, player_sprite.center_x - self.center_x)
        elif self.center_x > player_sprite.center_x:
            self.center_x -= min(SPRITE_SPEED, self.center_x - player_sprite.center_x)


# Create the class for the game
class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Sprite lists
        self.player_list = None

        # Set up the player
        self.player_sprite = None

        # List for walls, coin, and car
        self.coin_list = None
        self.wall_list = None
        self.car_list = None

        self.physics_engine = None

        # Used in scrolling
        self.view_bottom = 0
        self.view_left = 0

        # establish the score
        self.score = 0

    # Game set up
    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.car_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite("monkey.png", 0.125)
        self.player_sprite.center_x = 20
        self.player_sprite.center_y = 40
        self.player_list.append(self.player_sprite)

        # -- Set up several columns of walls
        for y in range(0, 1000, 100):
            for x in range(0, 1000, 32):
                # Randomly skip a box so the player can find a way through
                if random.randrange(5) > 0:
                    wall = arcade.Sprite("slice.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)

        # Create bottom edge
        for x in range(0, 1000, 32):
            wall = arcade.Sprite("slice01_01.png", SPRITE_SCALING)
            wall.center_x = x
            self.wall_list.append(wall)

        # Create left edge
        for y in range(0, 1000, 32):
            wall = arcade.Sprite("slice01_01.png", SPRITE_SCALING)
            wall.center_y = y
            self.wall_list.append(wall)

        # --- Place walls with a list
        coordinate_list = [[0, 1000],
                           [32, 1000],
                           [64, 1000],
                           [96, 1000],
                           [128, 1000],
                           [160, 1000],
                           [192, 1000],
                           [224, 1000],
                           [256, 1000],
                           [288, 1000],
                           [320, 1000],
                           [352, 1000],
                           [384, 1000],
                           [416, 1000],
                           [448, 1000],
                           [480, 1000],
                           [512, 1000],
                           [544, 1000],
                           [576, 1000],
                           [608, 1000],
                           [640, 1000],
                           [672, 1000],
                           [704, 1000],
                           [736, 1000],
                           [768, 1000],
                           [800, 1000],
                           [832, 1000],
                           [864, 1000],
                           [896, 1000],
                           [928, 1000],
                           [960, 1000],
                           [992, 1000]]

        # Loop through coordinates to create top edge
        for coordinate in coordinate_list:
            wall = arcade.Sprite("slice01_01.png", SPRITE_SCALING)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

            # --- Place walls with a list
            coordinate_list = [[1000, 0],
                               [1000, 32],
                               [1000, 64],
                               [1000, 96],
                               [1000, 128],
                               [1000, 160],
                               [1000, 192],
                               [1000, 224],
                               [1000, 256],
                               [1000, 288],
                               [1000, 320],
                               [1000, 352],
                               [1000, 384],
                               [1000, 416],
                               [1000, 448],
                               [1000, 480],
                               [1000, 512],
                               [1000, 544],
                               [1000, 576],
                               [1000, 608],
                               [1000, 640],
                               [1000, 672],
                               [1000, 704],
                               [1000, 736],
                               [1000, 768],
                               [1000, 800],
                               [1000, 832],
                               [1000, 864],
                               [1000, 896],
                               [1000, 928],
                               [1000, 960],
                               [1000, 992]]

            # Loop through coordinates to create right edge
            for coordinate in coordinate_list:
                wall = arcade.Sprite("slice01_01.png", SPRITE_SCALING)
                wall.center_x = coordinate[0]
                wall.center_y = coordinate[1]
                self.wall_list.append(wall)

        # Create the coins
        for i in range(NUMBER_OF_COINS):

            coin = arcade.Sprite("flat_medal1.png", SPRITE_SCALING_COIN)

            coin_placed_successfully = False

            # Ensure coins do not get placed on walls
            while not coin_placed_successfully:
                coin.center_x = random.randrange(0, 1000)
                coin.center_y = random.randrange(0, 1000)

                wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)
                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    coin_placed_successfully = True

            self.coin_list.append(coin)

        # Place the cars
        for i in range(CAR_COUNT):
            car = Car("police_E.png", SPRITE_SCALING_CAR)

            # Position the car
            car.center_x = random.randrange(SCREEN_WIDTH)
            car.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.car_list.append(car)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.BABY_BLUE)

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0

    # Draw components of the game
    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()
        self.car_list.draw()

        # Show the score
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 20)
        arcade.draw_text(output, 920, 20, arcade.color.WHITE, 20)

        # Check to see if the game is over
        if len(self.coin_list) == 0:
            arcade.draw_text("Game Over", 150, 600, arcade.color.WHITE, 100)
            output = f"Score: {self.score}"
            arcade.draw_text(output, 250, 500, arcade.color.WHITE, 75)

    # Assign functions to the keys
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if len(self.coin_list) > 0:
            if key == arcade.key.UP:
                self.player_sprite.change_y = MOVEMENT_SPEED
            elif key == arcade.key.DOWN:
                self.player_sprite.change_y = -MOVEMENT_SPEED
            elif key == arcade.key.LEFT:
                self.player_sprite.change_x = -MOVEMENT_SPEED
            elif key == arcade.key.RIGHT:
                self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # --- Manage Scrolling ---

        # Keep track of if we changed the boundary. We don't want to call the
        # set_viewport command if we didn't change the view port.
        changed = False

        # Scroll left
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        # If we changed the boundary values, update the view port to match
        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)

        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(sound)

        if len(self.coin_list) > 0:
            for car in self.car_list:
                car.follow_sprite(self.player_sprite)

        car_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.car_list)

        for car in car_hit_list:
            self.score -= .5


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
