import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

win1 = tk.Tk()
win1.title("Weather Forecasting")
win1.geometry("900x500")
win1.configure(bg="black")
win1.resizable(False, False)
#------------------------------------------------------------------------------------------
#                                  Sign up Page
#--------------------------------------------   ----------------------------------------------
def signup_1():
    scrn0 = tk.Toplevel(win1)
    scrn0.title("Signup Page")
    scrn0.geometry("900x500")
    scrn0.resizable(False,False)
    scrn0.config(bg='#1A2421')
    url1 = "C:\\Users\\DELL\\OneDrive\\Desktop\\proj\\signup.png"
    img1 = Image.open(url1)
    new_width = 400
    new_height = 350
    img1 = img1.resize((new_width,new_height),Image.Resampling.NEAREST)
    temp_path = "C:\\Users\\DELL\\OneDrive\\Desktop\\proj\\temp_signup.png"
    img1.save(temp_path)
    
    img1_tk = tk.PhotoImage(file=temp_path) 
    
    label = tk.Label(scrn0, image=img1_tk, bg='#1A2421')
    label.image = img1_tk
    label.place(x=50, y=50)

#-----------------------------------------------------------------------------------------
#                                 SIGN UP ENTRY
#----------------------------------------------------------------------------------------
    def save_signup_entry():
        global signup_username, signup_password
        signup_username = user1.get()
        signup_password = pswd1.get()
        close_signup_page()
    def close_signup_page():
        scrn0.destroy()
    def on_enter(e):
                user1.delete(0, 'end')

    def on_leave(e):
        name = user1.get()
        if name=='':
            user1.insert(0, 'Enter your name')
# --------------------------------------------------
    
    frame1 = tk.Frame(scrn0, width=350, height=350, bg="#1A2421")
    frame1.place(x=480, y=70)
    signup1 = tk.Label(frame1, text="Sign up", fg="red", bg="#1A2421", font=("italy", 23, "bold"))
    signup1.place(x=110, y=5)
    user1 = tk.Entry(frame1, width=25, border=0, bg="grey", fg="white", font=("times", 15))
    user1.place(x=60, y=80)
    user1.insert(0, 'Enter your name')
    user1.bind('<FocusIn>',on_enter)
    user1.bind('<FocusOut>',on_leave)
    tk.Frame(frame1, width=300, height=2, bg="black").place(x=40, y=107)
    
    
# PASSWORD
#---------
    def on_enter(e):
        pswd1.delete(0, 'end')

    def on_leave(e):
        name = pswd1.get()
        if name=='':
            pswd1.insert(0, 'Enter your password')

    pswd1 = tk.Entry(frame1, width=25, border=0, bg="grey", fg="white", font=("times", 15))
    pswd1.place(x=60, y=150)
    pswd1.insert(0, 'Enter your password')
    pswd1.bind('<FocusIn>',on_enter)
    pswd1.bind('<FocusOut>',on_leave)
    tk.Frame(frame1, width=300, height=2, bg="black").place(x=40, y=177)

    tk.Button(frame1, width=39, pady=7, text="Sign Up", bg='red', fg='white', border=0,command=save_signup_entry).place(x=55, y=220)
    label = tk.Label(frame1,text="Aldready have an account?",fg='white',bg='#1A2421',font=("italy", 9))
    label.place(x=85,y=270)
    signup = tk.Button(frame1, width=6, text='Sign in', border=0, bg='#1A2421', cursor='hand2', fg='#ADD8E6',command=close_signup_page)
    signup.place(x=235, y=270)


#------------------------------------------------------------------------------------------
#                                  Sign IN and home page
#-------------------------------------------------------------------------------------------
def signin_1():
    log = user.get()
    in1 = pswd.get()
    if user.get()==signup_username and pswd.get()==signup_password:
        scrn1 = tk.Toplevel(win1)
        scrn1.title("Weather Application")
        scrn1.config(bg='#191970')
        scrn1.geometry("900x500")
        scrn1.resizable(False,False)
        # search bar
        # ----------
        url2 = "C:\\Users\\DELL\\OneDrive\\Desktop\\proj\\search.png"
        search_img = Image.open(url2)
        new_width = 300
        new_height = 50
        search_img1 = search_img.resize((new_width,new_height),Image.Resampling.NEAREST)
        temp_path = "C:\\Users\\DELL\\OneDrive\\Desktop\\proj\\temp_search.png"
        search_img1.save(temp_path)
        search_img_tk = ImageTk.PhotoImage(search_img1) 
        label = tk.Label(scrn1, image=search_img_tk, bg='#191970')
        label.image = search_img_tk
        label.place(x=20, y=20)

        textfield = tk.Entry(label,justify='center',width=20,font=("poppins",15,'bold'),bg='#404040',border=0,fg='white')
        textfield.place(x=20,y=12)
        textfield.focus()

        # weather prog
        # ------------
        def getweather():
            city=textfield.get()

            geolocator = Nominatim(user_agent="geoapiExercises")
            location = geolocator.geocode(city)
            obj = TimezoneFinder()
            result = obj.timezone_at(lng=location.longitude,lat=location.latitude)

            home = pytz.timezone(result)
            local_time = datetime.now(home)
            current_time = local_time.strftime("%I:%M %p")
            clock.config(text=current_time)
            

            # weather
            api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=ad7c6ffad9b692afd889ba10e804c4d8"

            json_data = requests.get(api).json()

            if 'weather' in json_data:
                condition = json_data['weather'][0]['main']
                description = json_data['weather'][0]['description']
                temp = int(json_data['main']['temp'] - 273.15)
                pressure = json_data['main']['pressure']
                humidity = json_data['main']['humidity']
                wind = json_data['wind']['speed']

                t.config(text=(temp,"°"))
                c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"))
                w.config(text=wind)
                h.config(text=humidity)
                d.config(text=description)
                p.config(text=pressure)
                
            else:
            # Handle the case where the 'weather' key is not present in the API response
                print("Weather data not available")

        # search_icon
        #---------------    
        url3 = "C:\\Users\\DELL\\OneDrive\\Desktop\\proj\\search_icon.png"
        searchicon_img = Image.open(url3)
        new_width = 30
        new_height = 30
        searchicon_img1 = searchicon_img.resize((new_width,new_height),Image.Resampling.NEAREST)
        temp_path1 = "C:\\Users\\DELL\\OneDrive\\Desktop\\proj\\temp_search_icon.png"
        searchicon_img1.save(temp_path1)
        searchicon_img_tk = ImageTk.PhotoImage(searchicon_img1)
        button = tk.Button(scrn1,image=searchicon_img_tk,borderwidth=0,cursor='hand2',bg='#353935',command=getweather)
        button.place(x=270, y=30)

        # background style
        # ----------------
        frame2 = tk.Frame(scrn1, width=820, height=400, bg="#1ab5ef",relief="ridge",borderwidth=3)
        frame2.place(x=30, y=70)

        # time
        # ----
        name = tk.Label(frame2,font=("arial",15,"bold"),bg='#1ab5ef')
        name.place(x=400,y=300)
        clock = tk.Label(frame2,font=("Helvetica",20),bg='#1ab5ef')
        clock.place(x=450,y=350)

        # process desc and wordings
        # -------------------------

        la1 = tk.Label(frame2,text='WIND',font=("Helvetica",15,"bold"),fg="white",bg='#1ab5ef')
        la1.place(x=50, y=50)

        la2 = tk.Label(frame2,text='HUMIDITY',font=("Helvetica",15,"bold"),fg="white",bg='#1ab5ef')
        la2.place(x=250, y=50)

        la3 = tk.Label(frame2,text='DESCRIPTION',font=("Helvetica",15,"bold"),fg="white",bg='#1ab5ef')
        la3.place(x=450, y=50)

        la4 = tk.Label(frame2,text='PRESSURE',font=("Helvetica",15,"bold"),fg="white",bg='#1ab5ef')
        la4.place(x=650, y=50)

        t = tk.Label(frame2,font=("arial",70,"bold"),fg='#ee666d',bg='#1ab5ef')
        t.place(x=350,y=150)
        c = tk.Label(frame2,font=("arial",10,"bold"),bg='#1ab5ef')
        c.place(x=470,y=210)
            
        w = tk.Label(frame2,text="...",font=("arial",17,"bold"),bg="#1ab5ef")
        w.place(x=60,y=80)

        h = tk.Label(frame2,text="...",font=("arial",17,"bold"),bg="#1ab5ef")
        h.place(x=280,y=80)

        d = tk.Label(frame2,text="...",font=("arial",17,"bold"),bg="#1ab5ef")
        d.place(x=460,y=80)

        p = tk.Label(frame2,text="...",font=("arial",17,"bold"),bg="#1ab5ef")
        p.place(x=670,y=80)

        clock = tk.Label(frame2,font=("arial",10,"bold"),bg="#1ab5ef")
        clock.place(x=10,y=130)

        url4 = "C:\\Users\\DELL\\OneDrive\\Desktop\\proj\\logo.png"
        logo_img = Image.open(url4)
        new_width2 = 150
        new_height2 = 150
        logo_img1 = logo_img.resize((new_width2,new_height2),Image.Resampling.NEAREST)
        temp_path4 = "C:\\Users\\DELL\\OneDrive\\Desktop\\proj\\temp_logo.png"
        logo_img1.save(temp_path4)
        logo_img_tk = ImageTk.PhotoImage(logo_img1) 
        label4 = tk.Label(scrn1, image=logo_img_tk, bg='#1ab5ef')
        label4.image = logo_img_tk
        label4.place(x=220, y=210)
       # url4 = "C:\\Users\\DELL\\OneDrive\\Desktop\\w logo.png"
       # logo = tk.PhotoImage(file=url4)
      #  logo1 = tk.Label(frame2, image=logo, bg='#1ab5ef').place(x=40,y=80)
        
        scrn1.mainloop()
    elif user.get()!=signup_username and pswd.get()!=signup_password:
        messagebox.showerror("Invalid",'invalid username and password')
# -----------------------------------------------------------------------------------------
url = "C:\\Users\\DELL\\OneDrive\\Desktop\\proj\\142.png"
img = tk.PhotoImage(file=url) 
tk.Label(win1, image=img, bg='black',fg='purple').place(x=50, y=50)

frame = tk.Frame(win1, width=350, height=350, bg="black")
frame.place(x=480, y=70)

signin = tk.Label(frame, text="Sign in", fg="#87CEEB", bg="black", font=("italy", 23, "bold"))
signin.place(x=120, y=5)

#---------------------------------------------------------------------------------------

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name = user.get()
    if name=='':
        user.insert(0, 'Username')
user = tk.Entry(frame, width=25, border=0, bg="#4682B4", fg="black", font=("times", 15))
user.place(x=60, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave) 

tk.Frame(frame, width=300, height=2, bg="black").place(x=40, y=107)

#---------------------------------------------------------------------------------------
def on_enter(e):
    pswd.delete(0, 'end')

def on_leave(e):
    name = pswd.get()
    if name=='':
        pswd.insert(0, 'Password')

pswd = tk.Entry(frame, width=25, border=0, bg="#4682B4", fg="black", font=("times", 15))
pswd.place(x=60, y=150)
pswd.insert(0, 'Password')
pswd.bind('<FocusIn>',on_enter)
pswd.bind('<FocusOut>',on_leave)
tk.Frame(frame, width=300, height=2, bg="black").place(x=40, y=177)

#---------------------------------------------------------------------------------------
tk.Button(frame, width=39, pady=7, text="Sign in", bg='#1434A4', fg='white', border=0,command=signin_1).place(x=45, y=220)
label = tk.Label(frame,text="Dont have an account?",fg='white',bg='black',font=("italy", 9))
label.place(x=85,y=270)


signup = tk.Button(frame, width=6, text='Sign Up', border=0, bg='black', cursor='hand2', fg='red',command=signup_1)
signup.place(x=215, y=270)












win1.mainloop()
