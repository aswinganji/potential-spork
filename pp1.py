from tkinter import*
root = Tk()
root.title("Quick!")
root.geometry("1000x1000")

label1 = Label(root, text = "Text1")
label2 = Label(root, text = "Text2")
label3 = Label(root)
input1 = Entry(root)
input2 = Entry(root)

dic1 = {}
class pointy():
    def dic(self):
        global dic1
       
        
        
class pointy2(pointy):
    
    def pointy1(self,key,value):
        dic1[key] = value
        label3['text'] = dic1
        print(dic1)
            
input3 = input1.get()
input4 = input2.get()
obj1 = pointy2()


button = Button(root,text = "Click Here",command = obj1.pointy1(input3,input4))
label1.pack()
label2.pack()
label3.pack()
input1.pack()
input2.pack()
button.pack()
root.mainloop()
