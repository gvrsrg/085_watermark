import tkinter
from tkinter import filedialog as fd
from PIL import Image




def main():
    def add_watermark():

        label1.config(text=input.get())

    def select_file():
        file = fd.askopenfile(mode='r')
        python_image = tkinter.PhotoImage(file=file.name)
        image_field.create_image(0, 0, image=python_image)
        image_field.update()
        '''
        input.insert(0, file.name)
        input.config(width=len(file.name))
        input.winfo_screenwidth()
        input.update()
        with Image.open(file.name) as im:
            im.rotate(45).show()
        '''

    window = tkinter.Tk()
    window.title("Watermarking")



    label1 = tkinter.Label(text="label 1")
    label1.pack()
    click_count = 0

    button = tkinter.Button(text="Add watermark", command=add_watermark)
    button.pack()

    file_button = tkinter.Button(text="Select file", command=select_file)
    file_button.pack()

    input = tkinter.Entry()
    input.pack()

    image_field = tkinter.Canvas()
    image_field.pack()

    window.mainloop()

if __name__ == "__main__":
    main()


