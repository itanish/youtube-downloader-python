import youtube_dl
import tkinter as tk
from tkinter import messagebox as mb

root = tk.Tk()

def setStatus():
	mb.showinfo(title="Youtube Downloader", message = "Your video is successfully downloaded!!!")
	status.config(text = "Downloaded!!!")

def write_slogan():

	ydl = youtube_dl.YoutubeDL()
	
	r = ydl.extract_info(str(E1.get()), download=False)

	options = {
			'outtmpl': r['title']+'.mp4'
	}
	
	
	ydl = youtube_dl.YoutubeDL(options)
	
	
	
	ydl.download([str(E1.get())])	
	setStatus()
	
	#4tk.messagebox.showinfo(title="Youtube Downloader", message = "Your video is successfully downloaded!!!")

framea = tk.Frame(root)
framea.pack(side = tk.TOP)

w = tk.Label(framea, text="Hello Welcome to Youtube Downloader!", padx=10,pady=10)
w.grid(columnspan=2)
#w.pack()

L1 = tk.Label(framea, text="URL :", padx=10,pady=10)
#L1.pack( side = tk.LEFT)
E1 = tk.Entry(framea, bd =5, width=70)
#E1.pack(side = tk.RIGHT)

L1.grid(row=1,column=0)
E1.grid(row=1,column=1)

B = tk.Button(framea, text ="Download", command = write_slogan, padx=10,pady=10)

B.grid(rowspan=2,columnspan=2)

L2 = tk.Label(framea, text ="Video will be downloaded to working directory.")
L2.grid(columnspan=2)



status = tk.Label(root, text="Status: Enter URL and click Download", bd=1, anchor = tk.W, relief = tk.SUNKEN)
status.pack(fill = tk.X, side = tk.BOTTOM)


root.mainloop()


