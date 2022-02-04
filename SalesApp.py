from tkinter import *
import math

root=Tk()
root.title("Sales App")
root.geometry("400x400")
label=Label(root)
label.place(relx=0.5, rely=0.1,anchor=CENTER)
label2=Label(root)
label2.place(relx=0.5, rely=0.2,anchor=CENTER)
labelmax=Label(root)
labelmax.place(relx=0.5, rely=0.3,anchor=CENTER)
labelmin=Label(root)
labelmin.place(relx=0.5, rely=0.4,anchor=CENTER)
month=("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")
profit=(567843,459783,983475,984358,764535,637254,328642,745678,437683,473854,266237,608594)
def min():
  minprofit=min(profit)
  minprofitindex=profit.index(minprofit)

  profitmonth=month[minprofitindex]
  print("Minimum Profit Of "+str(minprofit)+" Was Recorded In The Month Of "+str(profitmonth))
  labelmin["text"]="Minimum Profit Of "+str(minprofit)+" Was Recorded In The Month Of "+str(profitmonth)

def max():
  maxprofit=max(profit)
  maxprofitindex=profit.index(maxprofit)

  profitmonth=month[maxprofitindex]
  print("Maximum Profit Of "+str(maxprofit)+" Was Recorded In The Month Of "+str(profitmonth))
  labelmax["text"]="Maximum Profit Of "+str(maxprofit)+" Was Recorded In The Month Of "+str(profitmonth)

buttonmax=Button(root,text="Max Button",command=max)
buttonmax.place(relx=0.5, rely=0.5, anchor=CENTER)
buttonmin=Button(root,text="Min Button",command=min)
buttonmin.place(relx=0.5, rely=0.6, anchor=CENTER)
root.mainloop()