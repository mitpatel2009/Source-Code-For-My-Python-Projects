#Import
from tkinter import*
import requests

# The Code which will bring the data to my AI and then the AI will judge if it is fraud or normal transaction
def classify():
    global textField, textField2, textField3, textField4, textField5, textField6, textField7, textField8 , result
    key = "51250000-761a-11ed-91e2-51e3cda1e793592857f7-a2d7-4619-91ae-5005bf3893fe"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"
    # Getting the values form all textboxs
    data1 = textField.get()
    data2 = textField2.get()
    data3 = textField3.get()
    data4 = textField4.get()
    data5 = textField5.get()
    data6 = textField6.get()
    data7 = textField7.get()
    data8 = textField8.get()

    # sending data to AI
    inputs = [data1,data2,data3,data4,data5,data6,data7,data8]
    print(inputs)
    # Deleting the text in my textbox after you check if it is a normal or fraud transaction
    textField.delete(0, END)
    textField2.delete(0, END)
    textField3.delete(0, END)
    textField4.delete(0, END)
    textField5.delete(0, END)
    textField6.delete(0, END)
    textField7.delete(0, END)
    textField8.delete(0, END)
    response = requests.post(url, json={ "data" : inputs })
    # AI response
    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        result = topMatch['class_name']
        confidence = topMatch['confidence']
        print(f'Result: {result}')
        print(f'Confidence: {confidence}')
    else:
        response.raise_for_status()

     # To show if it is a fraud or normal transaction on GUI
    if result == "Normal_Transaction":
    	lbl_result.config( text = "This is a Normal Transaction", font = medium)
    else:
    	lbl_result.config( text = "This is a Fraud Transaction.", font = medium)






# setting my canvas
canvas = Tk()
canvas.geometry("600x500")
canvas.title("Credit Card Fraud Detection")
# to display the result
lbl_result = Label(canvas, text= "",pady = 25 )
lbl_result.grid(row = 12, column = 2)
#font sizes
small = ("poppins", 15, "bold")
big = ("poppins", 35, "bold")
medium = ("poppins", 20, "bold")
lbl = Label(canvas, text = "Result: ", font = medium, pady = 25)
lbl.grid(row = 12, column = 0, columnspan = 5)
#header
lbl_title = Label(canvas, text = 'Credit Card Fraud Detection App', font = big)



#body

lbl_title.grid(row = 0, column = 0,columnspan = 4, pady = 20)

lbl_txn_amount = Label(canvas, text = "Average Transaction Amount:", font = medium,) 
lbl_txn_amount.grid(row = 2 ,column = 1 )
textField = Entry(canvas,justify='center', width = 20, font = small ,bg = 'light pink' , fg = 'black')
textField.grid(row = 2, column = 2)
textField.focus()
lbl2 = Label(canvas, text = "Average Number of transaction per Day: ", font = medium)
lbl2.grid(row = 3, column = 1)
textField2 = Entry(canvas,justify='center', width = 20, font = small ,bg = 'light pink' , fg = 'black')
textField2.grid(row = 3, column = 2)
textField2.focus()
lbl3 = Label(canvas, text = "Home Latitude: ", font = medium)
lbl3.grid(row = 4, column = 1)
textField3 = Entry(canvas,justify='center', width = 20, font = small ,bg = 'light pink' , fg = 'black')
textField3.grid(row = 4, column = 2)
textField3.focus()
lbl4 = Label(canvas, text = "Home Longitude:  ", font = medium)
lbl4.grid(row = 5, column = 1)
textField4 = Entry(canvas,justify='center', width = 20, font = small ,bg = 'light pink' , fg = 'black')
textField4.grid(row = 5, column = 2)
textField4.focus()
lbl5 = Label(canvas, text = "Transaction Latitude: ", font = medium)
lbl5.grid(row = 6, column = 1)
textField5 = Entry(canvas,justify='center', width = 20, font = small ,bg = 'light pink' , fg = 'black')
textField5.grid(row = 6, column= 2)
textField5.focus()
lbl6 = Label(canvas, text = "Transaction Longitude: ", font = medium)
lbl6.grid(row = 7, column = 1)
textField6 = Entry(canvas,justify='center', width = 20, font = small ,bg = 'light pink' , fg = 'black')
textField6.grid(row = 7, column = 2)
textField6.focus()
lbl7 = Label(canvas, text = "Actual Number of Transaction per day:  ", font = medium)
lbl7.grid(row = 8, column= 1)
textField7 = Entry(canvas,justify='center', width = 20, font = small ,bg = 'light pink' , fg = 'black')
textField7.grid(row =8, column=2)
textField7.focus()
lbl8 = Label(canvas, text = "Actual Transaction Amount: ", font = medium,)
lbl8.grid(row = 9, column = 1,)
textField8 = Entry(canvas,justify='center', width = 20, font = small,bg = 'light pink' , fg = 'black')
textField8.grid(row = 9, column =2)
textField8.focus()
#Check
btn1 = Button(canvas, text = "Check", width = 7,height = 2,  command= classify,pady = 10)
btn1.grid(row= 10, column = 1,columnspan = 100)


canvas.mainloop()
