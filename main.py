# Base code found at: https://github.com/codefirstio/tkinter-data-entry.git

from tkinter import *
from tkcalendar import *
from tkinter import ttk
from tkinter import messagebox
import datetime

def my_options():
    window = Tk()
    window.title("Menu")

    frame = Frame(window)
    frame.pack()

    # options frame
    options_frame = LabelFrame(frame, text="Options")
    options_frame.grid(row=0, column=0, padx=10, pady=10)

    options_label = Label(options_frame, text="Review the available options. Make a selection to continue.")
    options_label.grid(row=0, column=0, padx=10, pady=10)

    # menu frame
    menu_frame = LabelFrame(frame)
    menu_frame.grid(row=1, column=0, padx=10, pady=10)
        # option 1: add coursework
    option_1_button = Button(menu_frame, text="[1] Add Assignment", command=my_coursework)
    option_1_button.grid(row=1, column=0)

        # option 2: view calendar
    option_2_button = Button(menu_frame, text="[2] View Calendar", command=my_calendar)
    option_2_button.grid(row=2, column=0)
    
        # option 3: view courses
    option_3_button = Button(menu_frame, text="[3] View Courses", command=my_courses)
    option_3_button.grid(row=3, column=0)

    window.mainloop()

def courses_list(new_entry):
    courses_list = new_entry.get().split(", ")
    return courses_list

# option 1: add coursework
def my_coursework():
    # coursework information form
    window = Tk()
    window.title("Coursework Information Form")
    frame = Frame(window)
    frame.pack()

    # Assignment Information
    assignment_info_frame = LabelFrame(frame)
    assignment_info_frame.grid(row=0, column=0, padx=10, pady=10)

        # Name
    title_label = Label(assignment_info_frame, text="Title:")
    title_label.grid(row=0, column=0, sticky="e")
    title_entry = Entry(assignment_info_frame)
    title_entry.grid(row=0, column=1)

        # Type (homework, quiz, exam, project, etc.)
    type_label = Label(assignment_info_frame, text="Type:")
    type_label.grid(row=1, column=0, sticky="e")
    type_combobox = ttk.Combobox(assignment_info_frame, values=["Homework", "Quiz", "Exam", "Project", "Other"])
    type_combobox.grid(row=1, column=1)

        # Course
    course_label = Label(assignment_info_frame, text="Course:")
    course_label.grid(row=2, column=0, sticky="e")
    course_combobox = ttk.Combobox(assignment_info_frame, values=courses_list(courses_entry))
    course_combobox.grid(row=2, column=1)

        # Delivery
    delivery_label = Label(assignment_info_frame, text="Delivery:")
    delivery_label.grid(row=3, column=0, sticky="e")
    delivery_combobox = ttk.Combobox(assignment_info_frame, values=["In Class", "Online", "Other"])
    delivery_combobox.grid(row=3, column=1)

        # Additional Notes
    notes_label = Label(assignment_info_frame, text="Additional Notes:")
    notes_label.grid(row=4, column=0, sticky="e")
    notes_entry = Entry(assignment_info_frame)
    notes_entry.grid(row=4, column=1)

        # Due Date
    due_date_frame = LabelFrame(frame)
    due_date_frame.grid(row=0, column=1, padx=10, pady=10)

    due_date_label = Label(due_date_frame, text="Due Date:")
    due_date_label.grid(row=5, column=0)
            # Month
    month_combobox = ttk.Combobox(due_date_frame, values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], width=11)
    month_combobox.grid(row=5, column=1)
            # Day
    day_spinbox = Spinbox(due_date_frame, from_=1, to=31, width=3)
    day_spinbox.grid(row=5, column=2)
            # Year
    year_spinbox = Spinbox(due_date_frame, from_=datetime.date.today().year, to=datetime.date.today().year+10, width=5)
    year_spinbox.grid(row=5, column=3)

        # Due Time
    due_time_label = Label(due_date_frame, text="Due Time:")
    due_time_label.grid(row=6, column=0)
            # Hour
    hour_spinbox = Spinbox(due_date_frame, from_=1, to=12, width=3)
    hour_spinbox.grid(row=6, column=1)
            # Minute
    minute_spinbox = Spinbox(due_date_frame, from_=0, to=59, width=3)
    minute_spinbox.grid(row=6, column=2)
            # AM/PM
    am_pm_combobox = ttk.Combobox(due_date_frame, values=["AM", "PM"], width=3)
    am_pm_combobox.grid(row=6, column=3)

    def submit():
        title = title_entry.get()
        if title:
            print("Confirmation: " + title + " has been added to your planner.")
        else:
            messagebox.showwarning(title="Error", message="Title is required.")

    button = Button(frame, text="Submit", command=submit)
    button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

    window.mainloop()

# option 2: view calendar
def my_calendar():
    # view calendar with daily assignments
    # Calendar tutorial found at: https://youtu.be/fqfy-3IoVvs
    # Calendar help: https://python-forum.io/thread-26731.html
    window = Tk()

    today = datetime.date.today()
    cal = Calendar(window, selectmode="day", font=('Palatino', 25), year=today.year, month=today.month, day=today.day)
    cal.pack(pady=20)

    def grab_date():
        my_label.config(text="Your assignments for " + cal.get_date() + " are:")
        
    my_button = Button(window, text="Get Date", command=grab_date)
    my_button.pack(pady=20)

    my_label = Label(window, text="")
    my_label.pack(pady=20)

    window.mainloop()

# option 3: view courses
def my_courses():
    window = Tk()
    window.title("Course List")

    frame = Frame(window)
    frame.pack()

    courses_listbox = Listbox(frame, text=semester_combobox.get() + " Courses")
    courses_listbox.grid(row=0, column=0, padx=10, pady=10)
    for item in courses_list(courses_entry):
        courses_listbox.insert(END, " " + item)
    # test --> courses_list(courses_entry) (possibly str(courses_list(courses_entry)), extra space currently before each course)

# home screen
window = Tk()
window.title("Assignment Tracker")

frame = Frame(window)
frame.pack()

    # Welcome Message
welcome_frame = LabelFrame(frame)
welcome_frame.grid(row=0, column=0, padx=10, pady=10)
welcome_label = Label(welcome_frame, text="Welcome! This is a simple program to help you keep track of your coursework. To begin, please complete the following fields.\n\nNOTE: Separate courses with commas.", justify="left", wraplength=275)
welcome_label.grid(row=0, column=0, sticky="news")

    # User Information
user_info_frame = LabelFrame(frame)
user_info_frame.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    # Name
name_label = Label(user_info_frame, text="Name:", justify="left")
name_label.grid(row=1, column=0)
name_entry = Entry(user_info_frame)
name_entry.grid(row=1, column=1)

    # Semester
semester_info_frame = LabelFrame(frame)
semester_info_frame.grid(row=2, column=0, padx=10, pady=5, sticky="w")

    # Courses
semester_label = Label(semester_info_frame, text="Semester:", justify="left")
semester_label.grid(row=2, column=0)
semester_combobox = ttk.Combobox(semester_info_frame, values=["Fall", "Spring", "Summer"], width=10)
semester_combobox.grid(row=2, column=1)
today = datetime.date.today()
academic_year_spinbox = ttk.Spinbox(semester_info_frame, from_=datetime.date.today().year, to=datetime.date.today().year+5, width=4)
academic_year_spinbox.grid(row=2, column=2)

courses_info_frame = LabelFrame(frame)
courses_info_frame.grid(row=3, column=0, padx=10, pady=5, sticky="w")

courses_label = Label(courses_info_frame, text="Courses:", justify="left")
courses_label.grid(row=3, column=0)
courses_entry = Entry(courses_info_frame)
courses_entry.grid(row=3, column=1)
courses_list(courses_entry)

# navigation menu
navigation_frame = LabelFrame(frame, text="Navigation Menu")
navigation_frame.grid(row=4, column=0, padx=10, pady=10)

exit_button = Button(navigation_frame, text="Exit", command=window.destroy)
exit_button.grid(row=4, column=0)

continue_button = Button(navigation_frame, text="Continue", command=my_options)
continue_button.grid(row=4, column=1)

window.mainloop()