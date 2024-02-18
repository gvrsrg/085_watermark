import tkinter
from tkinter import filedialog as fd
from PIL import Image, ImageTk, ImageDraw, ImageFont

class App:
    def __init__(self):
        def add_watermark():

            self.label1.config(text=self.input.get())
            self.draw = ImageDraw.Draw(self.image)
            w, h = self.image.size
            x, y = int(w / 2), int(h / 4)
            if x > y:
                font_size = y
            elif y > x:
                font_size = x
            else:
                font_size = x

            font = ImageFont.truetype("arial.ttf", int(font_size / 6))
            self.draw.text((x, y), self.input.get(), fill=(128, 128, 128), font=font, anchor='ms')
            self.photo = ImageTk.PhotoImage(self.image)
            self.image_field.create_image(0, 0, anchor='nw', image=self.photo)

        def select_file():

            self.file = fd.askopenfile(mode='r')
            self.image = Image.open(self.file.name)
            self.photo = ImageTk.PhotoImage(self.image)
            self.image_field.create_image(0, 0, anchor='nw', image=self.photo)

        def save_file():
            self.wm_file = fd.asksaveasfile()
            self.image.save(self.wm_file.name)

        self.window = tkinter.Tk()
        self.window.title("Watermarking")

        self.label1 = tkinter.Label(text="label 1")
        self.label1.pack()

        self.button = tkinter.Button(text="Add watermark", command=add_watermark)
        self.button.pack()

        self.file_button = tkinter.Button(text="Select file", command=select_file)
        self.file_button.pack()

        self.save_button = tkinter.Button(text="Save file", command=save_file)
        self.save_button.pack()

        self.input = tkinter.Entry()
        self.input.pack()

        self.image_field = tkinter.Canvas()
        self.image_field.pack()

        self.window.mainloop()


if __name__ == "__main__":
    app = App()

