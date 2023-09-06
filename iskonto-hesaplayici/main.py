import customtkinter
import tkinter
from CTkMessagebox import CTkMessagebox

def Calculate():
    if (opt_var.get() != 0):
        try:
            discountResultLabel.configure(text="")
            totalResultLabel.configure(text="")

            totalValue = totalEntry.get()
            discountValue = discountEntry.get()
            totalValueT = float(totalValue)
            discountValueT = float(discountValue)
            result1 = (totalValueT * discountValueT) / 100
            result2 = totalValueT - result1

            if (opt_var.get()==1):
                optms = "  ₺"
            elif (opt_var.get()==2):
                optms = "  €"
            elif (opt_var.get()==3):
                optms = "  $"
            discountResultLabel.configure(text=str(result1)+optms)
            totalResultLabel.configure(text=str(result2)+optms)
        except ValueError:
            CTkMessagebox(title="Hata", message="Lütfen boşlukları eksiksiz ve doğru doldurun.", icon="cancel")
    else:
        CTkMessagebox(title="Hata", message="Lütfen para birimi seçin.", icon="cancel")
        

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.geometry("700x500")
root.title("İskonto Hesaplama Aracı")
root.resizable(width=False, height=False)
root.iconbitmap("icon.ico")

### Main Frame
mainFrame = customtkinter.CTkFrame(master=root) 
mainFrame.pack(padx=10,pady=10, fill="both", expand=True)

### On Frame
onFrame = customtkinter.CTkFrame(master=mainFrame, height=200)
onFrame.pack(padx=10, pady=10, fill="x", expand=False, side=customtkinter.TOP)
onFrameLeft = customtkinter.CTkFrame(master=onFrame, height=200)
onFrameLeft.pack(padx=10, pady=10, fill="y", expand=False, side=customtkinter.LEFT)
onFrameFinal = customtkinter.CTkFrame(master=onFrame, height=200)
onFrameFinal.pack(padx=10, pady=10, fill="both", expand=True, side=customtkinter.RIGHT)
totalLabel = customtkinter.CTkLabel(master=onFrameLeft, text="Toplam Tutar : ", font=("Rocoto", 15))
totalLabel.pack(padx=10, pady=37.5, fill="both", side=customtkinter.TOP)
discountLabel = customtkinter.CTkLabel(master=onFrameLeft, text="İskonto Yüzdesi : ", font=("Rocoto", 15))
discountLabel.pack(padx=10, pady=37.5, fill="both", side=customtkinter.BOTTOM)
onFrameRight = customtkinter.CTkFrame(master=onFrame, height=200)
onFrameRight.pack(padx=10, pady=10, fill="both", expand=True, side=customtkinter.RIGHT)
totalEntry = customtkinter.CTkEntry(master=onFrameRight)
totalEntry.pack(padx=10, pady=37.5, fill="none", side=customtkinter.TOP)
discountEntry = customtkinter.CTkEntry(master=onFrameRight)
discountEntry.pack(padx=10, pady=37.5, fill="none", side=customtkinter.BOTTOM)
totalLabel = customtkinter.CTkLabel(master=onFrameFinal, text="Para Birimi : ", font=("Rocoto", 15))
totalLabel.pack(padx=10, pady=10, fill="both", side=customtkinter.TOP)
opt_var = tkinter.IntVar(value=0)
opt1 = customtkinter.CTkRadioButton(master=onFrameFinal, text="₺", variable=opt_var, value=1, font=("Roboto", 15))
opt1.pack( expand=True, pady=2)
opt2 = customtkinter.CTkRadioButton(master=onFrameFinal, text="€", variable=opt_var, value=2)
opt2.pack( expand=True, pady=2)
opt3 = customtkinter.CTkRadioButton(master=onFrameFinal, text="$", variable=opt_var, value=3)
opt3.pack(expand=True, pady=2)


### Center Frame
centerFrame = customtkinter.CTkFrame(master=mainFrame, height=40)
centerFrame.pack(padx=10, pady=10, fill="x", expand=True, side=customtkinter.TOP)
calcButton = customtkinter.CTkButton(master=centerFrame, text="Hesapla", font=("Roboto", 15), command=Calculate)
calcButton.pack(fill="none", expand=True, pady=5, padx=5)

### Under Frame
underFrame = customtkinter.CTkFrame(master=mainFrame, height=200)
underFrame.pack(padx=10, pady=10, fill="x", expand=False, side=customtkinter.BOTTOM)
underFrameLeft = customtkinter.CTkFrame(master=underFrame, height=200)
underFrameLeft.pack(padx=10, pady=10, fill="y", expand=False, side=customtkinter.LEFT)
discountUnderLabel = customtkinter.CTkLabel(master=underFrameLeft, text="Uygulanan İskonto Tutarı : ", font=("Rocoto", 15))
discountUnderLabel.pack(padx=10, pady=20, fill="both", side=customtkinter.TOP)
totalUnderLabel = customtkinter.CTkLabel(master=underFrameLeft, text="Genel Toplam Tutar : ", font=("Rocoto", 15))
totalUnderLabel.pack(padx=10, pady=20, fill="both", side=customtkinter.TOP)
underFrameFinal = customtkinter.CTkFrame(master=underFrame)
underFrameFinal.pack(padx=10, pady=10, fill="both", expand=True, side=customtkinter.RIGHT)
discountResultLabel = customtkinter.CTkLabel(master=underFrameFinal, text="", font=("Rocoto", 17.5))
discountResultLabel.pack(padx=10, pady=20, side=customtkinter.TOP)
totalResultLabel = customtkinter.CTkLabel(master=underFrameFinal, text="", font=("Rocoto", 17.5))
totalResultLabel.pack(padx=10, pady=20, side=customtkinter.BOTTOM)

root.mainloop()
