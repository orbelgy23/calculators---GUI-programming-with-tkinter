from tkinter import *

# Loan Calculator


class LoanCalculator:
    def __init__(self):
        window = Tk()
        window.title("Loan Calculator")
        window.configure(background="light green")
        #sticky can be N/S/W/E otherwise element will be in the center
        Label(window, font='helvetica 12 bold', bg="light green",
              text="Annual Interest Rate").grid(row=1, column=1, sticky=W)
        Label(window, font='helvetica 12 bold', bg="light green",
              text="Number of years").grid(row=2, column=1, sticky=W)
        Label(window, font='helvetica 12 bold', bg="light green",
              text="Loan amount").grid(row=3, column=1, sticky=W)
        Label(window, font='helvetica 12 bold', bg="light green",
              text="Monthly payment").grid(row=4, column=1, sticky=W)
        Label(window, font='helvetica 12 bold', bg="light green",
              text="Total payment").grid(row=5, column=1, sticky=W)

        # StringVar() is just a class from tkinter used to monitor any changes to the tkinter variables , anytime a variable changes
        # Entry function enables input so you create input label where user can enter information
        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable=self.annualInterestRateVar, justify=RIGHT).grid(row=1, column=2)
        self.numberOfYearsVar = StringVar()
        Entry(window, textvariable=self.numberOfYearsVar, justify=RIGHT).grid(row=2, column=2)
        self.loanAmountVar = StringVar()
        Entry(window, textvariable=self.loanAmountVar, justify=RIGHT).grid(row=3, column=2)
        self.monthlyPaymentVar = StringVar()
        lblMonthPayment = Label(window, font='helvetica 12 bold', bg="light green",
                                textvariable=self.monthlyPaymentVar).grid(row=4, column=2, sticky=E)
        self.totalPaymentVar = StringVar()
        lblTotalPayment = Label(window, font='helvetica 12 bold', bg="light green",
                                textvariable=self.totalPaymentVar).grid(row=5, column=2, sticky=E)
        # when adding a button we need to specify command variable that will be called when the button is clicked
        btComputePayment = Button(window, text="Compute Payment", bg="red", fg="white", font='Helvetica 14 bold',
                                  command=self.computePayment).grid(row=6, column=2, sticky=E)
        btClear = Button(window, text="Clear", bg="blue", fg="white", font='Helvetica 14 bold',
                         command=self.delete_all).grid(row=6, column=8, padx=20, pady=20, sticky=E)

        window.mainloop()

    def computePayment(self):
        monthlyPayment = self.getMonthlyPayment(
            float(self.loanAmountVar.get()),
            float(self.annualInterestRateVar.get())/1200,
            int(self.numberOfYearsVar.get()))

        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
        totalPayment = float(self.monthlyPaymentVar.get()) * 12 * int(self.numberOfYearsVar.get())
        self.totalPaymentVar.set(format(totalPayment, '10.2f'))

    def getMonthlyPayment(self, loanAmount, interestRate, numOfYears):
        monthlyPayment = loanAmount * interestRate / (1-1/(1 + interestRate)**(numOfYears * 12))
        return monthlyPayment

    def delete_all(self):
        # StringVar() doesnt have delete function so we can use the set function to clear
        self.monthlyPaymentVar.set("")
        self.loanAmountVar.set("")
        self.annualInterestRateVar.set("")
        self.numberOfYearsVar.set("")
        self.totalPaymentVar.set("")

# Calculator


class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.task = ""
        self.UserIn = StringVar()
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.user_input = Entry(self, bg="#5BC8AC", bd=29, insertwidth=4, width=24,
                                font=("Verdana", 20, "bold"), textvariable=self.UserIn, justify=RIGHT)
        self.user_input.grid(columnspan=4)

        self.user_input.insert(0, "0")

        self.button1 = Button(self, bg="#98DBC6", bd=12, text="7", padx=33, pady=25,
                              font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick(7))
        self.button1.grid(row=2, column=0, sticky=W)

        self.button2 = Button(self, bg="#98DBC6", bd=12, text="8", padx=35, pady=25,
                              font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick(8))
        self.button2.grid(row=2, column=1, sticky=W)

        self.button3 = Button(self, bg="#98DBC6", bd=12, text="9", padx=33, pady=25,
                              font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick(9))
        self.button3.grid(row=2, column=2, sticky=W)

        self.button4 = Button(self, bg="#98DBC6", bd=12, text="4", padx=33, pady=25,
                              font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick(4))
        self.button4.grid(row=3, column=0, sticky=W)

        self.button5 = Button(self, bg="#98DBC6", bd=12, text="5", padx=35, pady=25,
                              font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick(5))
        self.button5.grid(row=3, column=1, sticky=W)

        self.button6 = Button(self, bg="#98DBC6", bd=12, text="6", padx=33, pady=25,
                              font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick(6))
        self.button6.grid(row=3, column=2, sticky=W)

        self.button7 = Button(self, bg="#98DBC6", bd=12, text="1", padx=33, pady=25,
                              font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick(1))
        self.button7.grid(row=4, column=0, sticky=W)

        self.button8 = Button(self, bg="#98DBC6", bd=12, text="2", padx=35, pady=25,
                              font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick(2))
        self.button8.grid(row=4, column=1, sticky=W)

        self.button9 = Button(self, bg="#98DBC6", bd=12, text="3", padx=33, pady=25,
                              font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick(3))
        self.button9.grid(row=4, column=2, sticky=W)

        self.button10 = Button(self, bg="#98DBC6", bd=12, text="0", padx=33, pady=25,
                               font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick(0))
        self.button10.grid(row=5, column=0, sticky=W)

        self.Addbutton = Button(self, bg="#98DBC6", bd=12, text="+", padx=36, pady=25,
                                font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick("+"))
        self.Addbutton.grid(row=2, column=3, sticky=W)

        self.Subbutton = Button(self, bg="#98DBC6", bd=12, text="-", padx=39, pady=25,
                                font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick("-"))
        self.Subbutton.grid(row=3, column=3, sticky=W)

        self.Multbutton = Button(self, bg="#98DBC6", bd=12, text="*", padx=38, pady=25,
                                 font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick("*"))
        self.Multbutton.grid(row=4, column=3, sticky=W)

        self.Dividebutton = Button(self, bg="#98DBC6", bd=12, text="/", padx=39, pady=25,
                                   font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick("/"))
        self.Dividebutton.grid(row=5, column=3, sticky=W)

        self.Equalbutton = Button(self, bg="#E6D72A", bd=12, text="=", padx=100, pady=25,
                                  font=("Helvetica", 20, "bold"), command=self.CalculateTask)
        self.Equalbutton.grid(row=5, column=1, sticky=W, columnspan=2)

        self.Clearbutton = Button(self, bg="#E6D72A", bd=12, text="AC", width=28, padx=7,
                                  font=("Helvetica", 20, "bold"), command=self.ClearDisplay)
        self.Clearbutton.grid(row=1, sticky=W, columnspan=4)

    def buttonClick(self, number):
        self.task = str(self.task) + str(number)
        self.UserIn.set(self.task)

    def CalculateTask(self):
        self.data = self.user_input.get()
        try:
            self.answer = eval(self.data)
            self.displayText(self.answer)
            self.task = self.answer
        except SyntaxError as e:
            self.displayText("Invalid Syntax")
            self.task = ""

    def displayText(self, value):
        self.user_input.delete(0, END)
        self.user_input.insert(0, value)

    def ClearDisplay(self):
        self.task = ""
        self.user_input.delete(0, END)
        self.user_input.insert(0, "0")


# List of actions . Used for the show_menu


actions = ["Open Calculator", "Open Loan Calculator"]


def show_menu():
    i = 1
    print("\n")
    for action in actions:
        print(
            str(i) + ". " + action
        )
        i += 1

# main function


def handle_functions():
    show_menu()
    choice = int(input("\nWhat do you want to do? "))
    if choice == 1:
        calculator = Tk()
        calculator.title("Calculator")
        app = Application(calculator)
        calculator.resizable(width=False, height=False)
        calculator.mainloop()
        return 0
    if choice == 2:
        LoanCalculator()
        return 0
    else:
        print("\nInvalid Choice")


if __name__ == "__main__":
    handle_functions()



