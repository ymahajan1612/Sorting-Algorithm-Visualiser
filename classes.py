import pygame
pygame.init()
white = (255, 255, 255)
green = (71, 120, 62)
bright_green = (0, 255, 0)
maroon = (128, 0, 0)
navy = (65, 67, 118)
orange = (255, 165, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
purple = (128, 0, 128)
grey = (128, 128, 128)
black = (0, 0, 0)
sky_blue = (0, 193, 247)
teal = (55, 103, 123)

WIDTH = 1280
HEIGHT = 720

class Window:
    def __init__(self, width, height, caption=None, icon=None, background_img=None, background_colour=None):
        self.width = width  # window's width
        self.height = height  # height
        self.caption = caption
        self.icon = icon
        self.background_img = background_img
        self.background_colour = background_colour

    def create_window(self):
        display = pygame.display.set_mode((self.width, self.height))  # setting up display dimensions
        self.display = display  # Creates new attribute: display
        if self.caption:
            pygame.display.set_caption(self.caption)  # setting caption
        if self.icon:
            img = pygame.image.load(self.icon)  # setting window icon
            pygame.display.set_icon(img)
        if self.background_img:  # setting background image
            img = pygame.image.load(self.background_img)  # loading background image
            display.blit(img, (0, -200))  # Drawing image to window
        elif self.background_colour:  # if there is a background colour
            display.fill(self.background_colour)
        return display  # returns the display

    # method to refresh window
    def update_window(self, colour=None, background=None):
        if background:
            self.display.blit(background, (0, 0))
            background.set_alpha(200)
        elif self.background_img:
            image = pygame.image.load(self.background_img)
            self.display.blit(image, (0, -200))
        elif colour:
            self.display.fill(colour)
        elif self.background_colour:
            self.display.fill(self.background_colour)

class Tools():  # Parent class: Tools
    def __init__(self, x, y, font, font_size, font_colour, colour=black, text="", width=0,
                 height=0):
        self.x = x
        self.y = y
        self.font = font
        self.font_colour = font_colour
        self.font_size = font_size
        self.colour = colour
        self.text = text
        self.width = width
        self.height = height
        self.active = False

    def isClicked(self, pos):
        if self.x < pos[0] < self.x + self.width and pos[1] > self.y and pos[1] < self.y + self.height:
            if pygame.mouse.get_pressed()[0]:
                self.active = True
        else:
            self.active = False

        return self.active

    def get_text(self):
        return self.text

    def draw(self):
        pass

class Text(Tools):
    def __init__(self, x, y, font, width, height, colour, text, font_size):
        super(Text, self).__init__(x, y, font, width, height, colour, text)  # inheriting from Tools
        self.font_size = font_size

    def update_text(self, new_text):
        self.text = new_text

    def get_y(self):
        return self.y

    def set_y(self, pixels):
        if self.y:
            self.y += pixels
        else:
            self.y = pixels

    def draw(self, display):  # method to display text to screen
        font = pygame.font.SysFont(self.font, self.font_size)  # setting font
        text_surface = font.render(str(self.text),True, self.colour)  # rendering text surface
        display.blit(text_surface, (self.x, self.y))  # displaying text to screen


class Button(Tools):
    def __init__(self, x, y, font, font_size, font_colour, colour, text, width, height):
        super().__init__(x, y, font, font_size, font_colour, colour, text, width, height)
        self.x_pos = self.x-self.width/2
        self.y_pos = self.y-self.height/2

    def draw(self, display, outline=True):  # Option for outline on button
        if outline:
            pygame.draw.rect(display, outline,
                             (self.x_pos - 2, self.y_pos - 2, self.width + 4, self.height + 4))  # larger rect.
        pygame.draw.rect(display, self.colour, (self.x_pos, self.y_pos, self.width, self.height))  # Create button rectangle
        if self.text != "" and self.font != "":
            font = pygame.font.SysFont(self.font, self.font_size)  # initialising Pygame font
            text = font.render(self.text, True, self.font_colour)  # Rendering font
            display.blit(text, (self.x_pos + (self.width / 2 - text.get_width() / 2),
                                self.y_pos + (self.height / 2 - text.get_height() / 2)))  # Drawing text to screen

    def deactivate(self):
        self.active = False

class Slider(Tools):
    def __init__(self, x, y, max_val, min_val, default_val, colour, width, height, dp=1):
        super(Slider, self).__init__(x, y, colour, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max_val = max_val
        self.min_val = min_val
        self.default_val = default_val
        self.scale = self.get_scale()
        self.slider_square = pygame.Rect((self.default_val * self.scale + self.x - 25, self.y), (50, self.height))
        self.slider_rect = pygame.Rect(x - 25, self.y, self.width + 50, self.height)
        self.colour = colour
        self.square_colour = black
        self.max_x = self.slider_rect.x + self.slider_rect.width
        self.active = False
        self.dp = dp  # dp: decimal places

    def get_scale(self):  # returns slider's scale
        scale = self.width / (self.max_val - self.min_val)
        return scale

    def draw(self, display):
        pygame.draw.rect(display, self.colour, self.slider_rect)  # draws slider rectangle
        pygame.draw.rect(display, self.square_colour, self.slider_square)  # draws slider's square

    def set_colour(self, hover_colour):  # changing the colour when slider is clicked
        self.square_colour = hover_colour

    def get_value(self):  # returns the value of the slider
        value = (self.slider_square.left + 25 - self.x) / self.scale
        return round(value, self.dp)  # returns value rounded to specified dp

    def set_value(self, num):
        self.value = num

    def get_dimensions(self):  # gets slider dimensions
        return self.slider_rect.x, self.y, self.slider_rect.width

    def update(self, new_pos):
        if new_pos < self.x:
            new_pos = self.x
        elif new_pos > self.x + self.width:
            new_pos = self.x + self.width
        self.slider_square.left = new_pos - 25

    def deactivate(self):
        self.active = False