

class Screen_size():
    def __init__(self, screen_width, text_width, screen_height, text_height):
        self.screen_width = screen_width
        self.text_width = text_width
        self.screen_height = screen_height
        self.text_height = text_height

    def size(input):
        m=input.screen_width // 2 - input.text_width // 2, input.screen_height // 2 - input.text_height // 2
        return m





screen_width=800
screen_height=400
text_width=193
text_height=20

awnser=Screen_size(screen_width, text_width, screen_height, text_height)

print(awnser.size())