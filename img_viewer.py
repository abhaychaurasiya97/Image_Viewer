from tkinter import *
from tkinter.ttk import *
import os
from PIL import Image,ImageTk
from pynput.keyboard import Key,Controller,Listener


root=Tk()
root.title("My First Image Viewer")
root.iconphoto(False, ImageTk.PhotoImage(file='download.png'))
key_control=Controller()
valid_img=('.jpg','.gif','.png','.tga')
img_list=[]
tk_image=[]
def back(image_position):
	global put_image
	global back_button
	global forward_button
	global img_name
	global file_size
	
	img_name.grid_forget()
	put_image.grid_forget()
	file_size.grid_forget()
	put_image=Label(image=tk_image[image_position-1])
	img_name=Label(root,text=img_list[image_position-1])
	image_number=Label(root,text=f"{image_position} of {len(img_list)}")
	file_size=Label(root,text=str(round(os.path.getsize(img_list[image_position-1])/1024000,3))+"  MB")
	back_button=Button(root,text="<<",command=lambda:back(image_position-1))
	forward_button=Button(root,text=">>",command=lambda:forward(image_position+1))
	if image_position==1:
		back_button=Button(root,text="<<",state=DISABLED)
	put_image.grid(row=0,column=0,columnspan=3,padx=5,pady=5)
	back_button.grid(row=1,column=0,padx=10)
	img_name.grid(row=1,column=1,padx=10)
	forward_button.grid(row=1,column=2,padx=10)
	image_number.grid(row=2,column=0,columnspan=3,sticky=E,padx=10,pady=5)
	file_size.grid(row=2,column=0,columnspan=3,sticky=W,padx=10,pady=5)

def forward(image_position):
	
	global put_image
	global back_button
	global forward_button
	global img_name
	global file_size
	file_size.grid_forget()
	img_name.grid_forget()
	put_image.grid_forget()
	put_image=Label(image=tk_image[image_position-1])
	img_name=Label(root,text=img_list[image_position-1])
	image_number=Label(root,text=f"{image_position} of {len(img_list)}")
	file_size=Label(root,text=str(round(os.path.getsize(img_list[image_position-1])/1024000,3))+"  MB")
	back_button=Button(root,text="<<",command=lambda:back(image_position-1))
	forward_button=Button(root,text=">>",command=lambda:forward(image_position+1))
	if image_position==len(img_list):
		forward_button=Button(root,text=">>",state=DISABLED)
	put_image.grid(row=0,column=0,columnspan=3,padx=5,pady=5)
	back_button.grid(row=1,column=0,padx=10)
	img_name.grid(row=1,column=1,padx=10)
	forward_button.grid(row=1,column=2,padx=10)
	image_number.grid(row=2,column=0,columnspan=3,sticky=E,padx=10,pady=5)
	file_size.grid(row=2,column=0,columnspan=3,sticky=W,padx=10,pady=5)
	
	
def search_img():
	path=os.getcwd()
	
	for files in os.listdir(path):
		if files.endswith(valid_img):
			img_list.append(files)
	img_list.sort()
	
search_img()

for i in img_list:
	tk_image.append(ImageTk.PhotoImage(Image.open(i)))


put_image=Label(image=tk_image[0])

back_button=Button(root,text="<<",command=back,state=DISABLED)
img_name=Label(root,text=img_list[0])
forward_button=Button(root,text=">>",command=lambda:forward(2))
image_number=Label(root,text=f"1 of {len(img_list)}")
file_size=Label(root,text=str(round(os.path.getsize(img_list[0])/1024000,3))+"  MB")

image_number.grid(row=2,column=0,columnspan=3,sticky=E,padx=10,pady=5)
put_image.grid(row=0,column=0,columnspan=3,padx=5,pady=5)
back_button.grid(row=1,column=0,padx=10)
img_name.grid(row=1,column=1,padx=10)
forward_button.grid(row=1,column=2,padx=10)
file_size.grid(row=2,column=0,columnspan=3,sticky=W,padx=10,pady=5)

root.mainloop()
