# Base code found at: https://github.com/codefirstio/tkinter-data-entry.git
# Tkinter tutorials - codemy youtube channel (https://www.youtube.com/playlist?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV) & python docs (https://pythonbasics.org/)

from tkinter import *
from tkcalendar import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date
import os
import openpyxl
import pandas as pd

def courses_list(new_entry):
    courses_list = new_entry.get().split(", ")
    return courses_list

# option 1: add coursework
def add_coursework():
    hide_frames()
    style = ttk.Style()
    style.theme_use("clam")
    
    assignment_info_frame.grid(row=0, column=0, padx=10, pady=10)

        # Name
    title_label = Label(assignment_info_frame, text="Title:", font=("Arial", 18))
    title_label.grid(row=0, column=0, sticky="e")
    title_entry = Entry(assignment_info_frame, font=("Arial", 18))
    title_entry.grid(row=0, column=1, sticky="w")

        # Type (homework, quiz, exam, project, etc.)
    type_label = Label(assignment_info_frame, text="Type:", font=("Arial", 18))
    type_label.grid(row=1, column=0, sticky="e")
    type_combobox = ttk.Combobox(assignment_info_frame, values=["Homework", "Quiz", "Exam", "Project", "Other"], font=("Arial", 18))
    type_combobox.grid(row=1, column=1, sticky="w")

        # Course
    course_label = Label(assignment_info_frame, text="Course:", font=("Arial", 18))
    course_label.grid(row=2, column=0, sticky="e")
    course_combobox = ttk.Combobox(assignment_info_frame, values=courses_list(courses_entry), font=("Arial", 18))
    course_combobox.grid(row=2, column=1, sticky="w")

        # Delivery
    delivery_label = Label(assignment_info_frame, text="Delivery:", font=("Arial", 18))
    delivery_label.grid(row=3, column=0, sticky="e")
    delivery_combobox = ttk.Combobox(assignment_info_frame, values=["In Class", "Online", "Other"], font=("Arial", 18))
    delivery_combobox.grid(row=3, column=1, sticky="w")

        # Additional Notes
    notes_label = Label(assignment_info_frame, text="Notes:", font=("Arial", 18))
    notes_label.grid(row=4, column=0, sticky="e")
    notes_entry = Entry(assignment_info_frame, font=("Arial", 18))
    notes_entry.grid(row=4, column=1, sticky="w")

        # Due Date
    calendar_frame.grid(row=5, column=0, padx=5, pady=5)
    due_date_label = Label(assignment_info_frame, text="Due Date:", font=("Arial", 18))
    due_date_label.grid(row=5, column=0, padx=10, pady=10)

    today = date.today()
    # error: date pattern displayed as 2-digit year not 4-digit year
        # resolved: added date_pattern="m/d/y" to Calendar widget
    my_cal = Calendar(calendar_frame, selectmode="day", date_pattern="m/d/y", font=("Arial", 18), year=today.year, month=today.month, day=today.day, 
                      background="grey", bordercolor="black", disabledbackground="grey", headersbackground="grey", normalbackground="grey", 
                      foreground="yellow", normalforeground="black", headersforeground="blue")
    my_cal.config(background="black")
    my_cal.grid(row=6, column=0, padx=20, pady=20)

    def set_date():
        set_date_label.config(text=my_cal.get_date())

    due_date_frame.grid(row=7, column=0, padx=10, pady=10)
    set_date_button = Button(due_date_frame, text="Select Date", command=set_date, font=("Arial", 18))
    set_date_button.grid(row=7, column=0)
    
    set_date_label = Label(assignment_info_frame, font=("Arial", 18))
    set_date_label.grid(row=5, column=1, sticky="w")

        # Due Time
    due_time_frame.grid(row=9, column=0, padx=10, pady=10)
    due_time_label = Label(due_time_frame, text="Due Time:", font=("Arial", 18))
    due_time_label.grid(row=9, column=0, sticky="w")
   
            # Hour
    hour_spinbox = Spinbox(due_time_frame, from_=1, to=12, width=3, font=("Arial", 18))
    hour_spinbox.grid(row=9, column=1, sticky="w")
            # Minute
    minute_spinbox = Spinbox(due_time_frame, from_=0, to=59, width=3, font=("Arial", 18))
    minute_spinbox.grid(row=9, column=2, sticky="w")

            # AM/PM
    am_pm_combobox = ttk.Combobox(due_time_frame, values=["AM", "PM"], width=3, font=("Arial", 18))
    am_pm_combobox.grid(row=9, column=3, sticky="w")

# write to excel
    def write_excel():        
        filepath = "D:\ksu-is\\assignment_tracker\planner.xlsx"
        def sort_excel(filepath):
            # source code: https://stackoverflow.com/questions/27469182/how-to-sort-excel-sheet-using-python
            df = pd.read_excel(filepath)
        # error: format was not matching "%m/%d/%Y" or "%I:%M %p" (excel displayed datetime object instead of string)
            # resolved by converting each due date & due time item in dataframe to datetime object, then sorting, then converting back to string
        # documentation: https://www.programiz.com/python-programming/datetime/strptime
            # convert each due date & due time item in dataframe to datetime object
            df['Due Date'] = pd.to_datetime(df['Due Date'], format='%m/%d/%Y')
            df['Due Time'] = pd.to_datetime(df['Due Time'], format='%I:%M %p')
            # sort dataframe by due date & due time
            df = df.sort_values(by=['Due Date', 'Due Time'])
            # convert each due date & due time item in dataframe to string (to display easy-to-read formatting when writing to excel)
            df['Due Date'] = df['Due Date'].dt.strftime('%m/%d/%Y')
            df['Due Time'] = df['Due Time'].dt.strftime('%I:%M %p')
            # write dataframe to excel
            df.to_excel(filepath, index=False)

        title = title_entry.get()
        type = type_combobox.get()
        course = course_combobox.get()
        delivery = delivery_combobox.get()
        due_date = set_date_label.cget("text")
        minute = minute_spinbox.get()
        if int(minute) < 10:
            minute = "0" + minute
        hour = hour_spinbox.get()
        if int(hour) < 10:
            hour = "0" + hour
        due_time = hour + ":" + minute + " " + am_pm_combobox.get()
        notes = notes_entry.get()
        if not os.path.exists(filepath):
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            heading = ["Title", "Type", "Course", "Delivery", "Due Date", "Due Time", "Notes"]
            sheet.append(heading)
            workbook.save(filepath)
        workbook = openpyxl.load_workbook(filepath)
        sheet = workbook.active
        sheet.append([title, type, course, delivery, due_date, due_time, notes])
        workbook.save(filepath)
        messagebox.showinfo(title="Confirmation", message="Your assignment has been added to your Excel planner. Please open the file to view changes.")
        sort_excel(filepath)

    enter_frame.grid(row=10, column=0, padx=10, pady=10)
    button = Button(enter_frame, text="Submit", command=write_excel, font=("Arial", 18))
    button.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

    window.mainloop()

'''
# option 2: view calendar
def view_calendar():
    # view calendar with daily assignments
    # Calendar tutorial found at: https://youtu.be/fqfy-3IoVvs
    # Calendar help: https://python-forum.io/thread-26731.html
    hide_frames()
    today = datetime.date.today()
    cal = Calendar(calendar_frame, selectmode="day", font=(16), year=today.year, month=today.month, day=today.day)
    cal.pack(pady=20)

    def grab_date():
        if cal.get_date() == get_due_date(set_date_label):
            my_label.config(text="Your assignments for " + cal.get_date() + " are:")
        
    my_button = Button(window, text="View Assignments", command=grab_date)
    my_button.pack(pady=20)

    my_label = Label(window, text="")
    my_label.pack(pady=20)

    window.mainloop()
'''

# option 2: view courses
def view_courses():
    style = ttk.Style()
    style.theme_use("clam")

    hide_frames()
    course_list_frame.grid(row=0, column=0, padx=10, pady=10)
    course_list_heading = semester_combobox.get() + " " + academic_year_spinbox.get() + " Courses"
    courses_label = Label(course_list_frame, text=course_list_heading, font=("Arial", 18))
    courses_label.grid(row=0, column=0, padx=10, pady=10)
    courses_listbox = Listbox(course_list_frame, font=("Arial", 18))
    courses_listbox.grid(row=1, column=0, padx=10, pady=10)
    for item in courses_list(courses_entry):
        courses_listbox.insert(END, " " + item)

def hide_frames():
    welcome_frame.grid_forget()
    user_info_frame.grid_forget()
    semester_info_frame.grid_forget()
    courses_info_frame.grid_forget()
    course_list_frame.grid_forget()
    assignment_info_frame.grid_forget()
    due_date_frame.grid_forget()
    due_time_frame.grid_forget()
    calendar_frame.grid_forget()
    submit_frame.grid_forget()
    enter_frame.grid_forget()

def submit_user_info():
    name = name_entry.get()
    semester = semester_combobox.get()
    academic_year = academic_year_spinbox.get()
    course_list = courses_list(courses_entry)

    if name and semester and academic_year and course_list:
        messagebox.showinfo(title="Confirmation", message="Your information has been saved. Please select an option from the menu to continue.")
    else:
        messagebox.showerror(title="Error", message="Please complete all fields.")

# MAIN
window = Tk()
window.title("Assignment Tracker")

style = ttk.Style()
style.theme_use("clam")

my_menu = Menu(window)
window.config(menu=my_menu)

# Welcome Message
welcome_frame = Frame(window)
welcome_frame.grid(row=0, column=0, padx=10, pady=10)
welcome_label = Label(welcome_frame, text="Welcome! This is a simple program to help you keep track of your coursework. Complete the fields below to begin.\n\nNOTE: Enter courses with commas.", justify="left", wraplength=300, font=("Arial", 18))
welcome_label.grid(row=0, column=0, sticky="news")

    # User Information
user_info_frame = Frame(window, width=400, height=400)
user_info_frame.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    # Name
name_label = Label(user_info_frame, text="Name:", justify="left", font=("Arial", 18))
name_label.grid(row=1, column=0)
name_entry = Entry(user_info_frame, font=("Arial", 18))
name_entry.grid(row=1, column=1)

    # Semester
semester_info_frame = Frame(window)
semester_info_frame.grid(row=2, column=0, padx=10, pady=5, sticky="w")

    # Courses
semester_label = Label(semester_info_frame, text="Semester:", justify="left", font=("Arial", 18))
semester_label.grid(row=2, column=0)
semester_combobox = ttk.Combobox(semester_info_frame, values=["Fall", "Spring", "Summer"], width=10, font=("Arial", 18))
semester_combobox.grid(row=2, column=1)
today = date.today()
academic_year_spinbox = ttk.Spinbox(semester_info_frame, from_=date.today().year, to=date.today().year+5, width=4, font=("Arial", 18))
academic_year_spinbox.grid(row=2, column=2)

courses_info_frame = Frame(window)
courses_info_frame.grid(row=3, column=0, padx=10, pady=5, sticky="w")

courses_label = Label(courses_info_frame, text="Courses:", justify="left", font=("Arial", 18))
courses_label.grid(row=3, column=0)
courses_entry = Entry(courses_info_frame, font=("Arial", 18))
courses_entry.grid(row=3, column=1)
courses_list(courses_entry)

submit_frame = Frame(window)
submit_frame.grid(row=4, column=0, padx=10, pady=5)
button = Button(submit_frame, text="Submit", command=submit_user_info, font=("Arial", 18))
button.grid(row=4, column=0)

# create program menu
program_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=program_menu)
program_menu.add_command(label="Exit", command=window.quit)

# create options menu
options_menu = Menu(my_menu)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Add Assignment", command=add_coursework)
# options_menu.add_command(label="View Calendar", command=view_calendar)
options_menu.add_command(label="View Courses", command=view_courses)

# frames
assignment_info_frame = Frame(window)
calendar_frame = Frame(window)
due_date_frame = Frame(window)
due_time_frame = Frame(window)
enter_frame = Frame(window)
course_list_frame = Frame(window)

window.mainloop()