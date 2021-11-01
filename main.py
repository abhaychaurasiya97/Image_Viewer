from tkinter import filedialog
from tkinter import *
import os
from PIL import Image,ImageTk

def convert_image():
	pass
def new_image():
	global img_list
	global tk_image
	global put_image
	global img_name
	global file_size
	global forward_button
	global back_button
	global image_number
	
	
	
	try:
		path=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select an image file",filetypes=(('Image Files','.jpg'),('Image Files','.gif'),('Image Files','.png'),('Image Files','.tiff')))
		folder=path
		img_name.grid_forget()
		put_image.grid_forget()
		file_size.grid_forget()
		image_number.grid_forget()
		if len(path)>0:
				
			img_list.clear()
			tk_image.clear()
		folder=path[0:path.rfind("/")+1]
		path=path[path.rfind("/")+1:]
		os.chdir(folder)
		search_img(folder)
		put_image=Label(image=ImageTk.PhotoImage(Image.open(path)))
		put_image.grid(row=0,column=0,columnspan=3,padx=5,pady=5)
		img_name=Label(root,text=path)
		back_button=Button(root,text="<<",command=lambda:back(img_list.index(path)))
		forward_button=Button(root,text=">>",command=lambda:forward(img_list.index(path)+2))
		image_number=Label(root,text=f"{img_list.index(path)+1} of {len(img_list)}")
		file_size=Label(root,text=str(round(os.path.getsize(path)/1024000,3))+"  MB")
		if img_list.index(path)==0:
			back_button=Button(root,text="<<",state=DISABLED)
		if img_list.index(path)==len(img_list)-1:
			forward_button=Button(root,text=">>",state=DISABLED)
		image_number.grid(row=2,column=0,columnspan=3,sticky=E,padx=10,pady=5)
		put_image.grid(row=0,column=0,columnspan=3,padx=5,pady=5)
		back_button.grid(row=1,column=0,padx=10)
		img_name.grid(row=1,column=1,padx=10)
		forward_button.grid(row=1,column=2,padx=10)
		file_size.grid(row=2,column=0,columnspan=3,sticky=W,padx=10,pady=5)
	except:
		pass
	
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

root=Tk()


root.title("My First Image Viewer")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.config(bg='#9da4a3')
root.overrideredirect(False)
root.geometry("+100+100")
valid_img=('.jpg','.gif','.png','.tga')
img_list=[]
tk_image=[]
	
def move(event):
	root.geometry(f"+{event.x_root}+{event.y_root}")

def search_img(path):
	global img_list
	global tk_image
	
	for files in os.listdir(path):
		if files.endswith(valid_img):
			img_list.append(files)
	img_list.sort()
	for i in img_list:
		x,y=Image.open(i).size
		if x>w or y>h:
			tk_image.append(ImageTk.PhotoImage(Image.open(i).resize((w,h))))
		else:
			tk_image.append(ImageTk.PhotoImage(Image.open(i)))
		
	
search_img(os.getcwd())
if len(tk_image)==0:
	img_name=Label(root,text="----")
	put_image=Label(root,text="No image file is available in this folder")
	file_size=Label(root,text='0')
	forward_button=Button(root,text=">>",state=DISABLED)
else:
	put_image=Label(image=tk_image[0])
	img_name=Label(root,text=img_list[0])
	file_size=Label(root,text=str(round(os.path.getsize(img_list[0])/1024000,3))+"  MB")


	forward_button=Button(root,text=">>",command=lambda:forward(2))
back_button=Button(root,text="<<",command=back,state=DISABLED)
image_number=Label(root,text=f"1 of {len(img_list)}")


image_number.grid(row=2,column=0,columnspan=3,sticky=E,padx=10,pady=5)
put_image.grid(row=0,column=0,columnspan=3,padx=5,pady=5)
back_button.grid(row=1,column=0,padx=10)
img_name.grid(row=1,column=1,padx=10)
forward_button.grid(row=1,column=2,padx=10)
file_size.grid(row=2,column=0,columnspan=3,sticky=W,padx=10,pady=5)

menubar=Menu(root)
menu_list= Menu(menubar)
menubar.add_command(label="Open...",command=new_image)
menubar.add_command(label="Exit",command=root.quit)
root.configure(menu=menubar)
root.grid_rowconfigure(0, weight=1) 
root.grid_columnconfigure(0, weight=1)

root.grid_columnconfigure(2, weight=1)
root.bind("<Control-w>",quit)
root.mainloop()
