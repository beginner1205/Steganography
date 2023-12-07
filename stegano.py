from tkinter import *
import tkinter.filedialog
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image
from io import BytesIO
import os
class IMG_Stegno:
    def main(self, root):
            root.title('ImageSteganography')
            root.geometry('500x600')
            root.resizable(width =False, height=False)
            root.config(bg = '#e3f4f1')
            frame = Frame(root)
            frame.grid()
        
            title = Label(frame,text='Image Steganography')
            title.config(font=('Times new roman',25, 'bold'),bg = '#e3f4f1')
            title.grid(pady=10)
            title.grid(row=1)
    
            encode = Button(frame,text="Encode",command= lambda :self.encode_frame1(frame), padx=14,bg = '#e3f4f1' )
            encode.config(font=('Helvetica',14), bg='#e8c1c7')
            encode.grid(row=2)
            decode = Button(frame, text="Decode",command=lambda :self.decode_frame1(frame), padx=14,bg = '#e3f4f1')
            decode.config(font=('Helvetica',14), bg='#e8c1c7')
            decode.grid(pady = 12)
            decode.grid(row=3)
    
            root.grid_rowconfigure(1, weight=1)
            root.grid_columnconfigure(0, weight=1)

    def back(self,frame):
            frame.destroy()
            self.main(root)

    def encode_frame1(self,F):
            F.destroy()
            F2 = Frame(root)
            label1= Label(F2,text='Select the Image in which \n you want to hide text :')
            label1.config(font=('Times new roman',25, 'bold'),bg = '#e3f4f1')
            label1.grid()
    
            button_bws = Button(F2,text='Select',command=lambda : self.encode_frame2(F2))
            button_bws.config(font=('Helvetica',18), bg='#e8c1c7')
            button_bws.grid()
            button_back = Button(F2, text='Cancel', command=lambda : IMG_Stegno.back(self,F2))
            button_back.config(font=('Helvetica',18),bg='#e8c1c7')
            button_back.grid(pady=15)
            button_back.grid()
            F2.grid()
    
    def decode_frame1(self,F):
            F.destroy()
            d_f2 = Frame(root)
            lablel1 = Label(d_f2, text='Select Image with Hidden text:')
            lablel1.config(font=('Times new roman',25,'bold'),bg = '#e3f4f1')
            lablel1.grid()
            lablel1.config(bg = '#e3f4f1')
            button_bws = Button(d_f2, text='Select', command=lambda :self.decode_frame2(d_f2))
            button_bws.config(font=('Helvetica',18), bg='#e8c1c7')
            button_bws.grid()
            button_back = Button(d_f2, text='Cancel', command=lambda : IMG_Stegno.back(self,d_f2))
            button_back.config(font=('Helvetica',18), bg='#e8c1c7')
            button_back.grid(pady=15)
            button_back.grid()
            d_f2.grid()

    def encode_frame2(self,e_F2):
            e_pg= Frame(root)
            myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
            if not myfile:
                messagebox.showerror("Error","You have selected nothing !")
            else:
                my_img = Image.open(myfile)
                new_image = my_img.resize((300,200))
                img = ImageTk.PhotoImage(new_image)
                label3= Label(e_pg,text='Selected Image')
                label3.config(font=('Helvetica',14,'bold'))
                label3.grid() 
                board = Label(e_pg, image=img)
                board.image = img
                self.output_image_size = os.stat(myfile)
                self.o_image_w, self.o_image_h = my_img.size
                board.grid()
                label2 = Label(e_pg, text='Enter the message')
                label2.config(font=('Helvetica',14,'bold'))
                label2.grid(pady=15)
                text_a = Text(e_pg, width=50, height=10)
                text_a.grid()
                encode_button = Button(e_pg, text='Cancel', command=lambda : IMG_Stegno.back(self,e_pg))
                encode_button.config(font=('Helvetica',14), bg='#e8c1c7')
                data = text_a.get("1.0", "end-1c")
                button_back = Button(e_pg, text='Encode', command=lambda : [self.enc_fun(text_a,my_img),IMG_Stegno.back(self,e_pg)])
                button_back.config(font=('Helvetica',14), bg='#e8c1c7')
                button_back.grid(pady=15)
                encode_button.grid()
                e_pg.grid(row=1)
                e_F2.destroy()
        
    def decode_frame2(self,d_F2):
            d_F3 = Frame(root)
            myfiles = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
            if not myfiles:
                messagebox.showerror("Error","You have selected nothing !")
            else:
                my_img = Image.open(myfiles, 'r')
                my_image = my_img.resize((300, 200))
                img = ImageTk.PhotoImage(my_image)
                label4= Label(d_F3,text='Selected Image :')
                label4.config(font=('Helvetica',14,'bold'))
                label4.grid()
                board = Label(d_F3, image=img)
                board.image = img
                board.grid()
                hidden_data = self.decode(my_img)
                label2 = Label(d_F3, text='Hidden data is :')
                label2.config(font=('Helvetica',14,'bold'))
                label2.grid(pady=10)
                text_a = Text(d_F3, width=50, height=10)
                text_a.insert(INSERT, hidden_data)
                text_a.configure(state='disabled')
                text_a.grid()
                button_back = Button(d_F3, text='Cancel', command= lambda :self.Page_3(d_F3))
                button_back.config(font=('Helvetica',14),bg='#e8c1c7')
                button_back.grid(pady=15)
                button_back.grid()
                d_F3.grid(row=1)
                d_F2.destroy()
            
    def decode(self, image):
            image_data = iter(image.getdata())
            data = ''
    
            while (True):
                pixels = [value for value in image_data.__next__()[:3] +
                        image_data.__next__()[:3] +
                        image_data.__next__()[:3]]
                # string of binary data
                binary_str = ''
                for i in pixels[:8]:
                    if i % 2 == 0:
                        binary_str += '0'
                    else:
                        binary_str += '1'
    
                data += chr(int(binary_str, 2))
                if pixels[-1] % 2 != 0:
                    return data
    def generate_Data(self,data):
            new_data = []
            for i in data:
                new_data.append(format(ord(i), '08b'))
            return new_data

   