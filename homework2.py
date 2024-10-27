from tkinter import*

root = Tk()
root.title("Student Information Window")
root.geometry("450x300")
root.config(background = "#BCD8C1")

#creating the labels
user_name = Label(root,text = "Name").place(x = 40,y = 60)
grade = Label(root,text = "Grade").place(x = 40,y =100)
section= Label(root,text = "Section").place(x = 40,y =140)
age = Label(root,text = "Age").place(x = 40,y =180)

#creating the text boxes
user_input = Entry(root,width = 30).place(x = 120,y = 60)
grade_input = Entry(root,width = 30).place(x = 120,y = 100)
sect_input = Entry(root,width = 30).place(x = 120,y = 140)
age_input = Entry(root,width = 30).place(x = 120,y = 180)

#creating the submit button
submit_btn = Button(root,text ="Submit", command = root.destroy).place(x = 90, y = 230)
root.mainloop()