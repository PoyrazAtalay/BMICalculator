import tkinter

def click_calculate_button():
    bmi_calculate()
    show_bmi_result()

def bmi_calculate():
    global your_bmi
    global your_weight
    global your_height

    your_weight = int(weight_input.get())
    your_height = int(height_input.get())
    your_bmi = your_weight / (your_height/100)**2

def show_bmi_result():
    global your_height
    global your_bmi
    global  bmi_level

    if your_bmi < 18.5:
        bmi_level = 0
    elif 18.5 <= your_bmi < 25:
        bmi_level = 1
    elif 25 <= your_bmi < 30:
        bmi_level = 2
    elif 30 <= your_bmi:
        bmi_level = 3

    result_text.config(text=f"Result : {result_list[bmi_level]}")
    ideal_weight_text.config(text=f"Ideal Weight : {your_height - 100 - ((your_height - 100)/20)}")

your_weight = 0
your_height = 0
your_bmi = 0
bmi_level = 0

result_list = ["Underweight", "Normal weight", "Overweight", "Obesity"]

screen = tkinter.Tk()
screen.title("BMI Calculator")
screen.geometry("250x330")
screen.configure(bg="white")

weight_text = tkinter.Label(bg="white",fg="black", text="Enter Your Weight (kg)")
weight_text.pack(pady=10)

weight_input = tkinter.Spinbox(bg="white", fg="black", from_=30, to=180, width=3)
weight_input.pack(pady=10)
weight_input.focus()

height_text = tkinter.Label(bg="white",fg="black", text="Enter Your Height (cm)")
height_text.pack(pady=10)

height_input = tkinter.Spinbox(bg="white", fg="black", from_=140, to=220, width=3)
height_input.pack(pady=10)

calculate_button = tkinter.Button(text="CALCULATE", command=click_calculate_button,bg="white", fg="black")
calculate_button.pack(pady=10)

result_text = tkinter.Label(bg="white",fg="black", text="Result : ")
result_text.pack(pady=10)

ideal_weight_text = tkinter.Label(bg="white",fg="black", text="Ideal Weight : ")
ideal_weight_text.pack()

screen.mainloop()