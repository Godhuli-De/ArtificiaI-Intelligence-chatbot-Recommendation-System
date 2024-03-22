'''Author History- Created by Rita, Updated by Godhuli'''
import openai
import tkinter as tk
from tkinter import messagebox
import constants
import chatFunctions as cf
from PIL import Image,ImageTk



global Name
Name=""

# Authenticate with the OpenAI API using the secret key
openai.api_key =constants.API_KEY

# Set up the Tkinter GUI
master = tk.Tk()
master.geometry("800x1000")
master.iconbitmap('chatty.ico')
master.title("HealthGenie.AI- Mental Health ChatBot")
master.config(bg = '#FFFFFF')
master.state("zoomed")

#Banner
label = tk.Label(master,text =constants.welcome,font=("Helvetica", 28,"bold"),fg='#5A5A5A')
label.pack(pady = 8)

#GenieLogo image
pic=Image.open("genie.png")
resized_image= pic.resize((100,100), Image.LANCZOS)
img = ImageTk.PhotoImage(resized_image)
my_label=tk.Label(master,image=img)
my_label.place(x=20,y=8)      

'''Author History- Created by Godhuli'''       
# function to open a new window For Sign In functionality:
def openNewWindow():
     
    # Sign in Window Setup
    newWindow = tk.Toplevel(master)
    newWindow.title("Sign In")
    newWindow.geometry("300x150")
    newWindow.iconbitmap('chatty.ico')
    
    #showuserDetails function
    def showUserDetails():
        Name =name.get().capitalize()
        if Name:
            Email=email.get()
            Password=password.get()
            messagebox.showinfo('Logged in', Name + " logged in successful")
            Logintext="Logged in as:"+Name
            print("Logged in as:"+Name)
            #Adding User Info to File
            cf.writeUserDetails(Name, Email,Password)
            #Logged in Label info                       
            login_label = tk.Label(master,text =Logintext,width=15,font=("Helvetica", 10))
            login_label.pack(side=tk.RIGHT,padx=10,pady = 5)
        else:
            msg="Username is required"
            print("Username is required")
            
            tk.Label(newWindow, text = msg, show='RED').grid(row = 8, column = 0, columnspan = 5)
            
        

    #Sign In page GUI 
    tk.Label(newWindow, text = 'Username ').grid(row = 5, column = 2,padx=2,pady=6)
    tk.Label(newWindow, text = 'Email ').grid(row = 6, column = 2,padx=2,pady=4)
    tk.Label(newWindow, text = 'Password ').grid(row = 7, column = 2,padx=2,pady=4)
    
    name = tk.Entry(newWindow)
    name.grid(row = 5, column = 3)
    email = tk.Entry(newWindow)
    email.grid(row = 6, column = 3)
    password = tk.Entry(newWindow, show = '*')
    password.grid(row = 7, column = 3)
    
    tk.Button(newWindow, text = "Login", command = showUserDetails).grid(row = 8, column = 0, columnspan = 5)
  
'''Author History- Created by Rita, Updated by Godhuli''' 
# Define function to display Health Genie's response
def display_response(): 
    user_input = input_box.get("1.0", tk.END).strip()
    if user_input:
        chat_log.config(state=tk.NORMAL)
        chat_log.config(foreground="#442265", font=("Verdana", 12 ))
        if Name==None or Name=="":
            chat_log.insert(tk.END, "You: " + user_input + "\n")
            responses = cf.get_response("You: " + user_input + "\nHealthGenie:")
        else: 
            chat_log.insert(tk.END, Name+": " + user_input + "\n")
            responses = cf.get_response(Name+": " + user_input + "\nHealthGenie:")
        
        
        chat_log.insert(tk.END, "HealthGenie: " + responses + "\n")
        chat_log.config(state=tk.DISABLED)
        input_box.delete("1.0", tk.END) 
 
    

# Button to Sign in
btn = tk.Button(master,text ="Click to Sign In",width=15,relief=tk.RAISED,bd=7,command = openNewWindow)
btn.pack(ipadx=5,ipady = 5)  

  
# Create frames for chat log and input box
chat_frame = tk.Frame(master)
input_frame = tk.Frame(master)

# Create scrollbar for chat log
scrollbar = tk.Scrollbar(chat_frame)

# Create chat log and input box
chat_log = tk.Text(chat_frame, height=25, width=145,bd=6, yscrollcommand=scrollbar.set)
input_box = tk.Text(input_frame, height=3, width=90)

# Configure scrollbar to work with chat log
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
scrollbar.config(command=chat_log.yview)


# Configure chat log and input box
chat_log.config(state=tk.DISABLED)
chat_log.pack(side=tk.LEFT, padx=5)
input_box.pack(side=tk.LEFT, padx=5, pady=5)

# Create send button
send_button = tk.Button(input_frame, text="Send",font=('Arial',15,),width=15, activebackground='gray',command=display_response)
send_button.pack(side=tk.LEFT, padx=10)

labelcp = tk.Label(master,text ='Powered by ChatGPT \n Implemented by- Godhuli De & Rita Salgado ',font=("Times", 8,"italic"),bg='#FFFFFF',fg='#b5b35c')
labelcp.pack(side=tk.BOTTOM, padx=5, pady=5)

#Exit Button
exit_button=tk.Button(master, text = "Exit",width=10,relief=tk.RAISED, command = master.quit )
exit_button.pack(side=tk.BOTTOM, padx=10, pady=10)

# Pack frames into master
chat_frame.pack(padx=10, pady=10)
input_frame.pack()

# Start GUI loop
master.mainloop()

