import io
import base64
# Python3
import tkinter as tk
from urllib.request import urlopen

class gui():
    def destroy(self):
        self.root.destroy()

    def open_image(self,url):
        self.root = tk.Tk()
        self.root.title("display a website image")
        button = tk.Button(self.root, text = 'root quit', command=self.destroy)
        button.pack(side = 'bottom')
        # a little more than width and height of image
        w = 520
        h = 250
        x = 80
        y = 100
        # use width x height + x_offset + y_offset (no spaces!)
        self.root.geometry("%dx%d+%d+%d" % (w, h, x, y))
        # this GIF picture previously downloaded to tinypic.com
        image_url = url
        image_byt = urlopen(image_url).read()
        image_b64 = base64.encodestring(image_byt)
        photo = tk.PhotoImage(data=image_b64)
        # create a white canvas
        cv = tk.Canvas(bg='black')
        cv.pack(side= 'top',fill= 'both', expand = 'yes')
        # put the image on the canvas with
        # create_image(xpos, ypos, image, anchor)
        cv.create_image(200, 40, image=photo, anchor='nw')
       
        self.root.mainloop()
if __name__ == '__main__':
    gui = gui()
    gui.open_image("https://www4d.wolframalpha.com/Calculate/MSP/MSP17471494c3h81h9h61d000003bchc8e652591b7e?MSPStoreType=image/gif&s=6")
