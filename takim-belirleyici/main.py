import customtkinter
import tkinter
from CTkMessagebox import CTkMessagebox
from CTkListbox import *
import random

pCount = 0

def AddPlayer():
    global pCount
    PlayerName = str(mainFrameEntry.get())
    if (PlayerName != ""):
        mainFrameLeftTopList.insert(pCount, PlayerName)
        mainFrameEntry.delete(0, customtkinter.END)
        pCount +=  1
        pCountLabel.configure(text=f"Toplam Oyuncu : {pCount}")
    else:
        CTkMessagebox(title="Hata", message="Eklemek için isim girin.", icon="cancel")
    
def DeleteAll():
    global pCount
    if (pCount != 0):
        mainFrameLeftTopList.delete(0, pCount)
        team1.delete(0, customtkinter.END)
        team2.delete(0, customtkinter.END)
        mainFrameEntry.delete(0, customtkinter.END)
        pCount = 0
        pCountLabel.configure(text=f"Toplam Oyuncu : {pCount}")
    else:
        CTkMessagebox(title="Hata", message="Zaten oyuncu yok.", icon="cancel")

def DeleteSelected():
    global pCount
    selected = mainFrameLeftTopList.curselection()
    if (selected != None):
        mainFrameLeftTopList.delete(selected)
        mainFrameEntry.delete(0, customtkinter.END)
        pCount -= 1
        pCountLabel.configure(text=f"Toplam Oyuncu : {pCount}")
    else:
        CTkMessagebox(title="Hata", message="Seçilen bir oyuncu yok.", icon="cancel")

def TeamMix():
    global pCount
    players = []
    copCount = pCount
    if (pCount >= 2):
        if (team1.size() != 0):
            team1.delete(0, customtkinter.END)
            team2.delete(0, customtkinter.END)
        mainFrameLeftTopList.select(0)
        for i in range(0, copCount):
            player = mainFrameLeftTopList.get(i)
            players += [player]
        random.shuffle(players)
        for x in range(0, pCount):
            if (x < copCount/2):
                team1.insert(x, players[x])
            elif (x >= copCount/2):
                team2.insert(x, players[x])
    elif (pCount == 0):
        CTkMessagebox(title="Hata", message="Listede oyuncu yok.", icon="cancel")
    else:
        CTkMessagebox(title="Hata", message="Takımlara dağıtmak için en az 2 oyuncu gerekli.", icon="cancel")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.geometry("800x600")
root.title("Takım Belirleme Aracı")
root.resizable(width=False, height=False)
root.iconbitmap("icon.ico")

# MAIN FRAME
mainFrame = customtkinter.CTkFrame(master=root)
mainFrame.pack(fill="both", expand=True)

mainFrameRight = customtkinter.CTkFrame(mainFrame, width=540)
mainFrameRight.pack(side=customtkinter.RIGHT, fill="both",expand=True, padx=5, pady=5)
mainFrameLeft = customtkinter.CTkFrame(mainFrame, width=240)
mainFrameLeft.pack(side=customtkinter.RIGHT, fill="y", expand=False, padx=5, pady=5)

mainFrameLeftTop = customtkinter.CTkFrame(mainFrameLeft, width=230, height=500)
mainFrameLeftTop.pack(side=customtkinter.TOP, fill="both", expand=True, padx=5, pady=5)
mainFrameLeftTopLabel = customtkinter.CTkLabel(mainFrameLeftTop, text="OYUNCU LİSTESİ", font=("Roboto", 13, "bold"))
mainFrameLeftTopLabel.pack(padx=5)
mainFrameLeftTopLabel = customtkinter.CTkLabel(mainFrameLeftTop, text="İSİM : ", font=("Roboto", 11))
mainFrameLeftTopLabel.pack(padx=5)
mainFrameEntry = customtkinter.CTkEntry(mainFrameLeftTop)
mainFrameEntry.pack()
Add = customtkinter.CTkButton(master=mainFrameLeftTop, text= "Listeye Ekle", fg_color="#27A20E", hover_color="#195B0C", font=("Roboto", 13), command=AddPlayer)
Add.pack(pady=5)
mainFrameLeftTopList = CTkListbox(mainFrameLeftTop, height=250)
mainFrameLeftTopList.pack(padx=5, pady=5)
pCountLabel = customtkinter.CTkLabel(mainFrameLeftTop, text=f"Toplam Oyuncu : {pCount}", font=("Roboto", 11))
pCountLabel.pack(padx=5)

DelSelected = customtkinter.CTkButton(master=mainFrameLeftTop, text= "Seçili Oyuncuyu Sil", fg_color="#B52525", hover_color="#731818", font=("Roboto", 13), command=DeleteSelected)
DelSelected.pack(pady=5)
DelAll = customtkinter.CTkButton(master=mainFrameLeftTop, text= "Tüm Listeleri Temizle", fg_color="#B52525", hover_color="#731818", font=("Roboto", 13), command=DeleteAll)
DelAll.pack(pady=5)

mainFrameLeftBottom = customtkinter.CTkFrame(mainFrameLeft, width=230, height=80)
mainFrameLeftBottom.pack(side=customtkinter.TOP, fill="both", expand=True, padx=5, pady=5)
Mix = customtkinter.CTkButton(master=mainFrameLeftBottom, text= "Takımları Dağıt", font=("Roboto", 13), command=TeamMix)
Mix.pack(fill="none", expand=True)

mainFrameRightTop = customtkinter.CTkFrame(mainFrameRight, width=530, height=340)
mainFrameRightTop.pack(side=customtkinter.TOP, fill="both", expand=True,padx=5, pady=5)
mainFrameRightTopLabel = customtkinter.CTkLabel(mainFrameRightTop, text="1. TAKIM", font=("Roboto", 13, "bold"))
mainFrameRightTopLabel.pack(padx=5)
team1 = CTkListbox(mainFrameRightTop)
team1.pack(fill="both", expand=True, padx=15, pady=15)

mainFrameRightBottom = customtkinter.CTkFrame(mainFrameRight, width=530, height=340)
mainFrameRightBottom.pack(side=customtkinter.TOP, fill="both", expand=True, padx=5, pady=5)
mainFrameRightBottomLabel = customtkinter.CTkLabel(mainFrameRightBottom, text="2. TAKIM", font=("Roboto", 13, "bold"))
mainFrameRightBottomLabel.pack(padx=5)
team2 = CTkListbox(mainFrameRightBottom)
team2.pack(fill="both", expand=True, padx=15, pady=15)

root.mainloop()
