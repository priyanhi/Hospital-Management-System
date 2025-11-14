from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw 
import mysql.connector
from datetime import datetime
#import os
#print(os.path.exists(r"C:\Users\ASUS\OneDrive\Desktop\coding\new file\images\depositphotos_139341336-stock-photo-blur-hospital-interior.webp"))

win = Tk()
win.title("HOSPITAL MANAGEMENT")
win.state("zoomed")
win.config(bg = "black") 

"""""
ADDING  IMAGE FROM HERE 

WE IMPORT IMAGE FROM PILLOW LIBRARY    "from PIL import Image, ImageTk"
"""

# Open and resize image
img = Image.open(r"C:\Users\ASUS\OneDrive\Desktop\coding\new file\images\hospital-building-and-doctor-with-medical-equipment-and-pin-isolated-concept-3d-illustration-or-3d-rendering-png.webp")
img = img.resize((win.winfo_screenwidth(), win.winfo_screenheight()), Image.Resampling.LANCZOS)
bg_img = ImageTk.PhotoImage(img)

# Set image as background using Label
bg_label = Label(win, image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

frame1 =Frame(win,bd=15,relief=RIDGE)# we create a box insite the window so Frame(inside this we add view of are box)
frame1.place(x=0,y=44,width=1537,height=410)

label_frame_1 = LabelFrame(frame1,text="Patient Info",font = "ariel 10 bold", bd = 10, )
label_frame_1.place(x=10, y=0, width = 750, height = 280)
# ADDING IMAGE IN PATIENT INFO

img_path = r"C:\Users\ASUS\OneDrive\Desktop\coding\new file\images\depositphotos_139341336-stock-photo-blur-hospital-interior.webp"

# Resize image to fill the frame
patient_img = Image.open(img_path)
patient_img = patient_img.resize((740, 260), Image.Resampling.LANCZOS)
patient_bg = ImageTk.PhotoImage(patient_img)

# Place image inside the frame
bg_label2 = Label(label_frame_1, image=patient_bg)
bg_label2.place(x=0, y=0, relwidth=1, relheight=1)

# Keep image reference
label_frame_1.bg_image_ref = patient_bg



def fetch_data():
            _connection_ = mysql.connector.connect(host = "localhost",username = "root",password = "priyanshi@12345",database = "hospital management system")
            my_cursor = _connection_.cursor()
            my_cursor.execute("select * from hospital_table")
            row = my_cursor.fetchall()

            if len(row)!=0:
                table.delete(* table.get_children())
                for item in row:
                    table.insert("",END,value=item)
                    _connection_.commit()
            _connection_.close()




def get_data(event = ''):
    cursor_row = table.focus()
    data = table.item(cursor_row)
    row = data['values']

    Name_Of_Patient.set(row[0])
    Patient_ID.set(row[0])
    D_O_B.set(row[0])
    Patient_phone_Number.set(row[0])
    Name_Of_Docter.set(row[0])
    Check_up_Date.set(row[0])
    Next_Check_Up_Date.set(row[0])
    Dose_Name.set(row[0])
    Exp_Date.set(row[0])
    Issue_date.set(row[0])
    Total_Fee.set(row[0])





# not working 
def save():
    if entry_field_1.get() == "" or entry_field_2.get() =="":
        messagebox.showerror("Error","Sll field are required")


    else:
        _connection_ =  mysql.connector.connect(host="localhost", username = "root", password = "priyanshi@12345",database = "hospital management system")

        my_cursor = _connection_.cursor()
        my_cursor.execute("insert into hospital_table values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            Name_Of_Patient.get(),
            Patient_ID.get(),
            D_O_B.get(),
            Patient_phone_Number.get(),
            Name_Of_Docter.get(),
            Check_up_Date.get(),
            Next_Check_Up_Date.get(),
            Dose_Name.get(),
            Exp_Date.get(),
            Issue_date.get(),
            Total_Fee.get(), 
        ))
        _connection_.commit()
        fetch_data()
        _connection_.close()
        messagebox.showinfo("success","congratulation you'r task is compleated you'r record is save")

#---------------------- data formate-----------------------------------------------------------------------

def format_date(date_str):
    """Convert date like '12-11-2024' or '12/11/2024' to MySQL format '2024-11-12'"""
    for fmt in ("%d-%m-%Y", "%d/%m/%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(date_str, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return None


#-----------------------------continue from here---------------------------------------------------------------------------------
def pre():
    txt_fram.insert(END,"Name Of Patient: \t\t\t"+Name_Of_Patient.get()+'\n')
    txt_fram.insert(END,"Patient ID: \t\t\t"+Patient_ID.get()+'\n')
    txt_fram.insert(END,"DOB: \t\t\t"+D_O_B.get()+'\n')
    txt_fram.insert(END,"Patient Address: \t\t\t"+Patient_Address.get()+'\n')
    txt_fram.insert(END,"Patient Phone Number: \t\t\t"+Patient_phone_Number.get()+'\n')
    txt_fram.insert(END,"Patient Email: \t\t\t"+Patient_Email.get()+'\n')
    txt_fram.insert(END,"Name Of Docter: \t\t\t"+Name_Of_Docter.get()+'\n')
    txt_fram.insert(END,"Patient Problem: \t\t\t"+Patient_problem.get()+'\n')
    txt_fram.insert(END,"Patient Blood Group: \t\t\t"+Patient_Blood_Group.get()+'\n')
    txt_fram.insert(END,"Issue Date: \t\t\t"+Issue_date.get()+'\n')
    txt_fram.insert(END,"Dose Name: \t\t\t"+Dose_Name.get()+'\n')
    txt_fram.insert(END,"Daily Dose: \t\t\t"+Daily_Dose.get()+'\n')
    txt_fram.insert(END,"Exp. Date: \t\t\t"+Exp_Date.get()+'\n')
    txt_fram.insert(END,"Next Check Up Date: \t\t\t"+Next_Check_Up_Date.get()+'\n')
    txt_fram.insert(END,"Check Up Date: \t\t\t"+Check_up_Date.get()+'\n')
    txt_fram.insert(END,"Total Fee: \t\t\t"+Total_Fee.get()+'\n')



 # error here           
def delet():
    selected_row = table.focus()
    if not selected_row:
         messagebox.showerror("Error","Please select a record to delete.")
         return
    
    data =table.item(selected_row)
    row = data["values"]

    if not row:
         messagebox.showerror("Error","no data found in selected roe.")
         return
    patient_id =  row[1]
    _connection_ = mysql.connector.connect(
        host = 'localhost',
        username = 'root',
        password = 'priyanshi@12345',
        database = 'hospital management system'
        )
    
    my_cursor = _connection_.cursor()
    querry = 'DELETE FROM hospital_table WHERE `Patient ID` =%s'

    value = (Patient_ID.get(),)

    my_cursor.execute(querry, (patient_id,))
    _connection_.commit()
    _connection_.close()
    fetch_data()
    messagebox.showinfo('Deleted','yeee your patient data has been deleted by you')


def clear():
     Name_Of_Patient.set('')
     Patient_ID.set('')
     D_O_B.set('')
     Patient_Address.set('')
     Patient_phone_Number.set('')
     Patient_Email.set('')
     Name_Of_Docter.set('')
     Patient_problem.set('')
     Patient_Blood_Group.set('')
     Issue_date.set('')
     Dose_Name.set('')
     Daily_Dose.set('')
     Exp_Date.set('')
     Next_Check_Up_Date.set('')
     Check_up_Date.set('')
     Total_Fee.set('')


def Exit():
     conform = messagebox.askyesno('confirmation','you taking exit. Your work is done? ')
     if conform>0:
          win.destroy()
          return
        
        








#label for patient information 
Label(label_frame_1, text="Name Of Patient").place(x=10, y=10)
Label(label_frame_1, text="Patient ID").place(x=10, y=40)
Label(label_frame_1, text="DOB").place(x=10, y=70)
Label(label_frame_1, text="Patient Address").place(x=10, y=100)
Label(label_frame_1, text="Patient Phone Number").place(x=10, y=130)
Label(label_frame_1, text="Patient Email").place(x=10, y=160)
Label(label_frame_1, text="Name Of Doctor").place(x=10, y=190)
Label(label_frame_1, text="Patient Problem").place(x=10, y=220)
Label(label_frame_1, text="Patient Blood Group").place(x=380, y=10)
Label(label_frame_1, text="Issue Date").place(x=380, y=40)
Label(label_frame_1, text="Dose Name").place(x=380, y=70)
Label(label_frame_1, text="Daily Dose").place(x=380, y=100)
Label(label_frame_1, text="Exp. Date").place(x=380, y=130)
Label(label_frame_1, text="Next Check-up Date").place(x=380, y=160)
Label(label_frame_1, text="check up date").place(x=380, y=190)
Label(label_frame_1, text="Total Fee").place(x=380, y=220)

Name_Of_Patient = StringVar()
Patient_ID = StringVar()
D_O_B = StringVar()
Patient_Address = StringVar()
Patient_phone_Number = StringVar()
Patient_Email = StringVar()
Name_Of_Docter = StringVar()
Patient_problem = StringVar()
Patient_Blood_Group= StringVar()
Issue_date = StringVar()
Dose_Name = StringVar()
Daily_Dose = StringVar()
Exp_Date = StringVar()
Next_Check_Up_Date = StringVar()
Check_up_Date = StringVar()
Total_Fee = StringVar()

entry_field_1 = Entry(label_frame_1,bd=4,textvariable=Name_Of_Patient)
entry_field_1.place(x=130,y=10,width=150)

entry_field_2 = Entry(label_frame_1,bd=4,textvariable=Patient_ID)
entry_field_2.place(x=130,y=40,width=150)

entry_field_3 = Entry(label_frame_1,bd=4, textvariable=D_O_B)
entry_field_3.place(x=130,y=70,width=150)

entry_field_4 = Entry(label_frame_1,bd=4,textvariable=Patient_Address)
entry_field_4.place(x=130,y=100,width=150)

entry_field_5 = Entry(label_frame_1,bd=4,textvariable=Patient_phone_Number)
entry_field_5.place(x=130,y=130,width=150 )

entry_field_6 = Entry(label_frame_1,bd=4,textvariable=Patient_Email)
entry_field_6.place(x=130,y=160,width=150)

entry_field_7 = Entry(label_frame_1,bd=4,textvariable=Name_Of_Docter)
entry_field_7.place(x=130,y=190,width=150)

entry_field_8 = Entry(label_frame_1,bd=4,textvariable=Patient_problem)
entry_field_8.place(x=130,y=220,width=150)

entry_field_9 = Entry(label_frame_1,bd=4,textvariable=Patient_Blood_Group)
entry_field_9.place(x=510,y=10,width=150)

entry_field_10 = Entry(label_frame_1,bd=4,textvariable=Issue_date)
entry_field_10.place(x=510,y=40,width=150)

entry_field_11 = Entry(label_frame_1,bd=4,textvariable=Dose_Name)
entry_field_11.place(x=510,y=70,width=150)

entry_field_12 = Entry(label_frame_1,bd=4,textvariable=Daily_Dose)
entry_field_12.place(x=510,y=100,width=150)

entry_field_13 = Entry(label_frame_1,bd=4,textvariable= Exp_Date)
entry_field_13.place(x=510,y=130,width=150)

entry_field_14 = Entry(label_frame_1,bd=4,textvariable=Next_Check_Up_Date)
entry_field_14.place(x=510,y=160,width=150)

entry_field_15 = Entry(label_frame_1,bd=4,textvariable=Check_up_Date)
entry_field_15.place(x=510,y=190,width=150)

entry_field_16 = Entry(label_frame_1,bd=4,textvariable=Total_Fee)
entry_field_16.place(x=510,y=220,width=150)

Label(win, text = 'HOSPITAL MANAGEMENT SYSTEM', font = "impack 31 bold",fg = "black").pack(fill = 'x')

label_frame_2 = LabelFrame(frame1,text="prescription", font = "ariel 12 bold", bd = 10,)
label_frame_2.place(x=730, y= 0, width=770, height=280)

txt_fram = Text(label_frame_2, font = "impack 10 bold",width=40,height = 30,bg="white")
txt_fram.pack(fill=BOTH)

frame2 = Frame(win,bd=15,relief = RIDGE)
frame2.place(x=0, y=360, width=1537, height = 410)






delete_button = Button(win, text = "DELETE", font = "ariel 15 bold", bg = "green", fg = "white", bd = 6, cursor = "hand2", command = delet )
delete_button.place(x=0,y=750,width=270)

prescription_button = Button(win,text = "PRESCRIPTION", font = "ariel 15 bold", bg = "sky blue", fg = "white", bd = 6, cursor = "hand2", command = pre )
prescription_button.place(x=270, y = 750, width = 330)

save_button = Button(win,text = "SAVE", font = "ariel 15 bold", bg="green", fg = "white", bd = 6, cursor = "hand2", command = save)
save_button.place(x=600, y=750,width=340)

clear_button = Button(win,text = "CLEAR", font = "ariel 15 bold", bg = "sky blue", fg = "white", bd = 6, cursor = "hand2", command= clear)
clear_button.place(x=940,y=750, width= 350)

exit_button = Button(win,text = "EXIT",font = "ariel 15 bold", bg = "green", fg = "white", bd = 6, cursor = "hand2", command=Exit)
exit_button.place(x=1270, y=750,width=270)


scroll_x = ttk.Scrollbar(frame2,orient = HORIZONTAL)
scroll_x.pack(side="bottom",fill="x")

scroll_y = ttk.Scrollbar(frame2,orient=VERTICAL)
scroll_y.pack(side="right",fill="y")







frame2_bg_path = r"C:\Users\ASUS\OneDrive\Desktop\coding\new file\images\depositphotos_150901550-stock-photo-blurred-hospital-background.webp "  # <-- your image path

# Open, resize and convert the image
frame2_img = Image.open(frame2_bg_path)
frame2_img = frame2_img.resize((1537, 410), Image.Resampling.LANCZOS)
frame2_photo = ImageTk.PhotoImage(frame2_img)

# Create label to hold image and place it inside frame2
frame2_bg_label = Label(frame2, image=frame2_photo)
frame2_bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Keep reference to avoid garbage collection
frame2.bg_ref = frame2_photo


#_________________________________________________________________________________________________________________________


style = ttk.Style()
style.theme_use("default")

# Set Treeview background & foreground colors
style.configure("Treeview",
                background="#982b2b",       # light gray or similar to image
                foreground="black",
                rowheight=25,
                fieldbackground="#9e3434")

# Change selected row color
style.map('Treeview', background=[('selected', 'skyblue')])

#______________________________________________________________________________________________________________________________





#step 7
table = ttk.Treeview(frame2,columns=("nop","pid","dob","ppn","nod","cud","ncud","dn","ed","id","tf"))
scroll_x = ttk.Scrollbar(command = table.xview)
scroll_y = ttk.Scrollbar(command=table.yview)


table.heading('nop',text="Name Of Patient")
table.heading('pid',text="Patient ID")
table.heading('dob',text='DOB')
table.heading('ppn',text= 'Patient Phone Number')
table.heading('nod',text='Name Of Docter')
table.heading('cud',text='Check up date')
table.heading('ncud',text= 'Next Check Up Date')
table.heading('dn',text='Dose Name')
table.heading('ed',tex='Exp Dose')
table.heading('id',text= 'Issue Date')
table.heading('tf',text='Total Fee')

table['show']='headings'
table.pack(fill=BOTH,expand=1)

table.column('nop',width=100)
table.column('pid',width=100)
table.column('dob',width=100)
table.column('ppn',width=100)
table.column('nod',width=100)
table.column('cud',width=100)
table.column('ncud',width=100)
table.column('dn',width=100)
table.column('ed',width=100)
table.column('id',width=100)
table.column('tf',width=100)
mainloop()