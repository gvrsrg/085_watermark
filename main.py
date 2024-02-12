import tkinter
from tkinter import filedialog as fd




def main():
    def add_watermark():

        label1.config(text=input.get())

    def select_file():
        file = fd.askopenfile(mode='r')
        input.config(text=file.name)

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

    window.mainloop()

if __name__ == "__main__":
    main()


