import io
import base64
# Python3
import tkinter as tk
from urllib.request import urlopen

def open_image(url):
    root = tk.Tk()
    root.title("display a website image")
    # a little more than width and height of image
    w = 520
    h = 250
    x = 80
    y = 100
    # use width x height + x_offset + y_offset (no spaces!)
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))
    # this GIF picture previously downloaded to tinypic.com
    image_url = url
    image_byt = urlopen(image_url).read()
    image_b64 = base64.encodestring(image_byt)
    photo = tk.PhotoImage(data=image_b64)
    # create a white canvas
    cv = tk.Canvas(bg='white')
    cv.pack(side='top', fill='both', expand='yes')
    # put the image on the canvas with
    # create_image(xpos, ypos, image, anchor)
    cv.create_image(10, 10, image=photo, anchor='nw')
    root.mainloop()

if __name__ == '__main__':
    open_image("https://www4d.wolframalpha.com/Calculate/MSP/MSP17471494c3h81h9h61d000003bchc8e652591b7e?MSPStoreType=image/gif&s=6")
