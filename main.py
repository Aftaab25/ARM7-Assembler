# Importing Libraries
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import font
import tkinter.messagebox as tmsg


import re
import os


# main function
# create a new file
def newFile():
    global File
    root.title("Untitled - AssemblyCode")
    File = None
    textArea.delete(1.0, END)

# open a file from the device
def openFile():
    global File
    File = askopenfilename(defaultextension=".asm", filetypes=[("All Files", "*.*"), ("Assembly Code", "*.asm")])
    if File == "":
        File = None
    else:
        root.title(os.path.basename(File))
        textArea.delete(1.0, END)
        f = open(File, "r")
        textArea.insert(1.0, f.read())
        f.close()

# save the file
def saveFile():
    global File
    if File == None:
        File = asksaveasfilename(initialfile = "Untitled.asm", defaultextension = ".asm", filetypes = [("All Files", "*.*"), ("Assembly Code", "*.asm")])
        if File == "":
            File = None
        else:
            f = open(File, "w")
            f.write(textArea.get(1.0, END))
            f.close()
            
            root.title(os.path.basename(File) + " -> AssemblyCode")
    else:
        f = open(File, "w")
        f.write(textArea.get(1.0, END))
        f.close()

# cut the selected text
def cut():
    textArea.event_generate(("<<Cut>>"))

# paste the selected text
def paste():
    textArea.event_generate(("<<Paste>>"))

# copy the selected text
def copy():
    textArea.event_generate(("<<Copy>>"))

# directs the user to the intstruction set Page for each category
def branchInstr():
    # Branch intstructions =>
    topBranch = Toplevel()
    topBranch.geometry("750x680") 
    topBranch.title("Arm Instruction Set")
    headerFrame = Frame(topBranch)
    headerFrame.pack(fill=X)
    branchFrame = Frame(topBranch)
    branchFrame.pack(fill=X)

    Label(headerFrame, text="ARM7 Instruction Set", font="firacode 20 underline").pack()
    Label(branchFrame, text="\nBrach Instructions", font="firacode 16 underline", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=1)
    Label(branchFrame, text="B   => Unconditional Branch", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=2)
    Label(branchFrame, text="BNV => Brach Never", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=3)
    Label(branchFrame, text="BCS => Brach if carry set", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=4)
    Label(branchFrame, text="BCC => Brach carry clear", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=5)
    Label(branchFrame, text="BVS => Brach if overflow set", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=6)
    Label(branchFrame, text="BVC => Brach if overflow clear", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=7)
    Label(branchFrame, text="BMI => Brach if minus", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=8)
    Label(branchFrame, text="BPL => Brach if plus", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=9)
    Label(branchFrame, text="BEQ => Brach if equal", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=10)
    Label(branchFrame, text="BNE => Brach if not equal", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=11)
    Label(branchFrame, text="BHI => Brach if higher", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=12)
    Label(branchFrame, text="BHS => Brach if higher or same", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=13)
    Label(branchFrame, text="BLO => Brach if lower", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=14)
    Label(branchFrame, text="BLS => Brach if lower or same", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=15)
    Label(branchFrame, text="BGT => Brach if greater than", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=16)
    Label(branchFrame, text="BGE => Brach if greater than or equal", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=17)
    Label(branchFrame, text="BLT => Brach if less than", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=18)
    Label(branchFrame, text="BLE => Brach if less than or equal", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=19)
    Label(branchFrame, text="BL  => Brach with Link", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=20)
    Label(branchFrame, text="BLX => Brach with Link and exchange", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=21)

def stackInstr():
    # Stack Instructions =>
    topStack = Toplevel()
    topStack.geometry("900x900")
    topStack.title("Arm Instruction Set")
    headerFrame = Frame(topStack)
    headerFrame.pack(fill=X)
    stackFrame = Frame(topStack)
    stackFrame.pack(fill=X)
    Label(headerFrame, text="ARM7 Instruction Set", font="firacode 20 underline").pack()
    Label(stackFrame, text="\nStack Operations/Instructions", font="firacode 16 underline", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=1)
    Label(stackFrame, text="STMFA : Like Normal push of 8051 (Pre increment Push)\n\tEg: STMFA SP1, {R0-R4};\n\tR0, R1, R2, R3, R4 will be pushed on the stack\n\tBefore each Push SP will be incremented", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=2)
    Label(stackFrame, text="STMEA : Post increment Push\n\tEg: STMEA SPI, {R0-R4}\n\tR0, R1, R2, R3, R4 will be pushed on the stack\n\tAfter each Push SP will be incremented", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=3)
    Label(stackFrame, text="STMFD : Pre decrement Push\n\tEg: STMFD SPI, {R0-R4}\n\tR0, R1, R2, R3, R4 will be pushed on the stack\n\tBefore each Push SP will be decremented", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=4)
    Label(stackFrame, text="STMED : Post decrement Push\n\tEg: STMED SPI, {R0-R4}\n\tR0, R1, R2, R3, R4 will be pushed on the stack\n\tAfter each Push SP will be decremented", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=5)
    Label(stackFrame, text="LDMFA : Like Normal pop of 8051 (Post decrement Pop)\n\tEg: LDMFA SP1, {R0-R4};\n\tR0, R1, R2, R3, R4 will be popped from the stack\n\tAfter each Pop SP will be decremented", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=6)
    Label(stackFrame, text="LDMEA : Pre decrement Pop\n\tEg: LDMEA SPI, {R0-R4}\n\tR0, R1, R2, R3, R4 will be popped from the stack\n\tBefore each Pop SP will be decremented", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=7)
    Label(stackFrame, text="LDMFD : Post decrement Push\n\tEg: LDMFD SPI, {R0-R4}\n\tR0, R1, R2, R3, R4 will be popped from the stack\n\tAfter each Pop SP will be incremented", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=8)
    Label(stackFrame, text="LDMED : Pre decrement Push\n\tEg:LDMED SPI, {R0-R4}\n\tR0, R1, R2, R3, R4 will be popped on the stack\n\tBefore each Pop SP will be incremented", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=9)

def loadStoreInstr():
    # Load & Store Instructions =>
    topLoadStore = Toplevel()
    topLoadStore.geometry("850x850")
    topLoadStore.title("Arm Instruction Set")
    headerFrame = Frame(topLoadStore)
    headerFrame.pack(fill=X)
    loadStoreFrame = Frame(topLoadStore)
    loadStoreFrame.pack(fill=X)
    Label(headerFrame, text="ARM7 Instruction Set", font="firacode 20 underline").pack()
    Label(loadStoreFrame, text="\nLoad-Store Operations/Instructions", font="firacode 16 underline", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=1)
    Label(loadStoreFrame, text="LDR   : Load Register\n\tEg: LDR R0, [R1];\n\tR0 gets the data pointed by R1 (32 bits)", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=2)
    Label(loadStoreFrame, text="LDRB  : Load Byte into Register\n\tEg: LDRB R0, [R1];\n\tR0 gets byte data pointed by R1 (8 bits)\n\tRemaining bits in R0 becomes 0.", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=3)
    Label(loadStoreFrame, text="LDRH  : Load Halfword into Register\n\tEg: LDRH R0, [R1];\n\tR0 gets halfword data pointed by R1 (16 bits)\n\tRemaining bits in R0 becomes 0.", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=4)
    Label(loadStoreFrame, text="LDRSB : Load signed byte\n\tSame as above but signed.", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=5)
    Label(loadStoreFrame, text="LDRSH : Load signed halfword\n\tSame as above but signed.", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=6)
    Label(loadStoreFrame, text="STR   : Store Register\n\tEg: STR R0, [R1];\n\tData from R0 gets stored at the location pointed by R1 (32 bits)", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=7)
    Label(loadStoreFrame, text="STRB  : Store Byte from Register\n\tEg: STRB R0, [R1];\n\tData from R0 gets stored at the location pointed by R1 (8 bits)\n\tRemaining bits in R0 becomes 0.", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=8)
    Label(loadStoreFrame, text="STRH  : Store Halfword from Register\n\tEg: STRH R0, [R1];\n\tData from R0 gets stored at the location pointed by R1 (16 bits)\n\tRemaining bits in R0 becomes 0.", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=9)
    Label(loadStoreFrame, text="STRSB : Store signed byte\n\tSame as above but signed.", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=10)
    Label(loadStoreFrame, text="STRSH : Store signed halfword\n\tSame as above but signed.", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=11)

def movArithmeticInstr():
    # Move and Arithmetic Intstructions =>
    topMovArithmetic = Toplevel()
    topMovArithmetic.geometry("800x700")
    topMovArithmetic.title("Arm Instruction Set")
    headerFrame = Frame(topMovArithmetic)
    headerFrame.pack(fill=X)
    movArithFrame = Frame(topMovArithmetic)
    movArithFrame.pack(fill=X)
    Label(headerFrame, text="ARM7 Instruction Set", font="firacode 20 underline").pack()
    Label(movArithFrame, text="\nData Movement Instructions", font="firacode 16 underline", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=1)
    Label(movArithFrame, text="MOV   : Moves a value into register\n\tEg: MOV R0, R1;\tR0 <- R1\n\tEg: MOV R0, #25H; R0 <- 25H", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=2)
    Label(movArithFrame, text="MVN   : Move Not (1's complement)\n\tEg: MVN R0, R1;\n\tR0 <- 1's complement of R1", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=3)
    Label(movArithFrame, text="\nArithmetic Instructions", font="firacode 16 underline", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=4)
    Label(movArithFrame, text="ADD   : Basic Addition\n\tEg: ADD R0, R1, R2;\tR0 <- R1 + R2", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=5)
    Label(movArithFrame, text="ADC   : Add with carry\n\tEg: ADC R0, R1, R2;\tR0 <- R1 + R2 + Carry", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=6)
    Label(movArithFrame, text="SUB   : Basic Subtraction\n\tEg: SUB R0, R1, R2;\tR0 <- R1 - R2 + Carry", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=7)
    Label(movArithFrame, text="SBC   : Subtract with borrow (!carry)\n\tEg: SBC R0, R1, R2;\tR0 <- R1 - R2 - !Carry", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=8)
    Label(movArithFrame, text="RSB   : Reverse Subtraction\n\tEg: RSB R0, R1, R2;\tR0 <- R2 - R1", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=9)
    Label(movArithFrame, text="RSC   : Reverse Subtraction with carry\n\tEg: RSC R0, R1, R2;\tR0 <- R2 - R1 - !Carry", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=10)
    Label(movArithFrame, text="\nTo affect the flags, add an 'S' to the command, for eg: ADDS R0, R1, R2", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=11)
    

def logicalInstr():
    # Logical Instructions =>
    topLogical = Toplevel()
    topLogical.geometry("1050x550")
    topLogical.title("Arm Instruction Set")
    headerFrame = Frame(topLogical)
    headerFrame.pack(fill=X)
    logicFrame = Frame(topLogical)
    logicFrame.pack(fill=X)
    Label(headerFrame, text="ARM7 Instruction Set", font="firacode 20 underline").pack()
    Label(logicFrame, text="\nLogic Instructions", font="firacode 16 underline", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=1)
    Label(logicFrame, text="AND   : AND\n\tEg: ADD R0, R1, R2;\tR0 <- R1 AND R2", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=2)
    Label(logicFrame, text="ORR   : OR\n\tEg: OR R0, R1, R2;\tR0 <- R1 OR R2", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=3)
    Label(logicFrame, text="EOR   : EX-OR\n\tEg: EOR R0, R1, R2;\tR0 <- R1 XOR R2", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=4)
    Label(logicFrame, text="BIC   : AND with complement\n\tEg: BIC R0, R1, R2;\tR0 <- R1 AND (NOT)R2", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=5)
    Label(logicFrame, text="CMP   : Ordinary Compare\n\tEg: CMP R0, R1;\n\tPerform R0 - R1 but does not store the result.", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=6)
    Label(logicFrame, text="CMN   : Compare with Negated value\n\tEg: CMN R0, R1;\tPerform R0 + R1 but does not store the result.", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=7)
    Label(logicFrame, text="TST   : Logical AND, Only affects flags\n\tEg: TST R0, R1;\tPerforms R0 AND R1, does not store the result, but affects the flag.", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=8)
    Label(logicFrame, text="TEQ   : Logical XOR, Only affects flags\n\tEg: TEQ R0, R1;\tPerforms R0 XOR R1, does not store the result, but affects the flag.", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=9)

def mulInstr():
    # Multiply and Long Mutltiply operations =>
    topMultiply = Toplevel()
    topMultiply.geometry("750x500")
    topMultiply.title("Arm Instruction Set")
    headerFrame = Frame(topMultiply)
    headerFrame.pack(fill=X)
    mulFrame = Frame(topMultiply)
    mulFrame.pack(fill=X)
    Label(headerFrame, text="ARM7 Instruction Set", font="firacode 20 underline").pack()
    Label(mulFrame, text="\nMultiply Instructions", font="firacode 16 underline", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=1)

def flagInstr():
    # Flag operations =>
    topFlag = Toplevel()
    topFlag.geometry("750x450")
    topFlag.title("Arm Instruction Set")
    headerFrame = Frame(topFlag)
    headerFrame.pack(fill=X)
    flagFrame = Frame(topFlag)
    flagFrame.pack(fill=X)
    Label(headerFrame, text="ARM7 Instruction Set", font="firacode 20 underline").pack()
    Label(flagFrame, text="\nFlag related Instructions operating on CPSR/ SPSR", font="firacode 16 underline", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=1)
    Label(flagFrame, text="MRS Rd, CPSR:   Rd gets value of CPSR\n\t\tEg: MRS R0, CPSR;\n\t\tR0 gets the value of CPSR", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=2)
    Label(flagFrame, text="MRS Rd, SPSR:   Rd gets value of SPSR\n\t\tEg: MRS R0, SPSR;\n\t\tR0 gets the value of SPSR", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=3)
    Label(flagFrame, text="MSR CPSR, Rm:   CPSR gets value of Rm\n\t\tEg: MSR CPSR, R0;\n\t\tCPSR gets the value of R0", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=4)
    Label(flagFrame, text="MSR SPSR, Rm:   SPSR gets value of Rm\n\t\tEg: MSR SPSR, R0;\n\t\tSPSR gets the value of R0", font="firacode 13", justify=LEFT, anchor="w").grid(sticky=W, column=0, row=5)


# assemble the code and check the result
def assemble():
    tmsg.showinfo("Result", textArea.get(1.0, END))

# About page
def about():
    tmsg.showinfo("ARM ASSEMBLER", "An Arm7 Assembler by Aftaab Siddiqui (18BEC004) & Nishit Chechani (18BEC065)")
 

if __name__ == '__main__':
    # root/window of the App
    root = Tk()
    root.title("ARM ASSEMBLER")
    root.geometry("1000x750")
    
    # Text Area
    textArea = Text(root, font="lucida 14") 
    File = None
    textArea.pack(expand = True, fill=BOTH)

    # MenuBar
    mymenu = Menu(root) # Creating a menubar (Main Menu)
    
    # ==========================================================================
    m1 = Menu(mymenu, tearoff=0) # tearoff = 0, as tearoff is not needed
    m1.add_command(label="New", command=newFile)    # Submenu under File Section to create a new file.
    m1.add_command(label="Open", command=openFile)  # Submenu under File Section to Open a file.
    m1.add_command(label="Save", command=saveFile)  # Submenu under File Section to Save (Save as) a new file.
    root.config(menu=mymenu)
    mymenu.add_cascade(label="File", menu=m1)
    
    # ==========================================================================
    m2 = Menu(mymenu, tearoff=0) # tearoff = 0, as tearoff is not needed
    m2.add_command(label="Cut", command=cut)    # Submenu under File Section to create a new file.
    m2.add_command(label="Copy", command=copy)  # Submenu under File Section to Open a file.
    m2.add_command(label="Paste", command=paste)  # Submenu under File Section to Save (Save as) a new file.
    root.config(menu=mymenu)
    mymenu.add_cascade(label="Edit", menu=m2)
    
    # ==========================================================================
    # The details can be shown using submenus for each category of intstructions
    m3 = Menu(mymenu, tearoff=0) # tearoff = 0, as tearoff is not needed
    m3.add_command(label="Brach Instructions", command=branchInstr)    # Submenu under File Section to create a new file.
    m3.add_command(label="Stack Operations", command=stackInstr)  # Submenu under File Section to Open a file.
    m3.add_command(label="Load & Store", command=loadStoreInstr)  # Submenu under File Section to Save (Save as) a new file.
    m3.add_command(label="MOV & Arithmetic", command=movArithmeticInstr)  # Submenu under File Section to Save (Save as) a new file.
    m3.add_command(label="Logical Instructions", command=logicalInstr)  # Submenu under File Section to Save (Save as) a new file.
    m3.add_command(label="Multiply Instructions", command=mulInstr)  # Submenu under File Section to Save (Save as) a new file.
    m3.add_command(label="Flag Instructions", command=flagInstr)  # Submenu under File Section to Save (Save as) a new file.
    root.config(menu=mymenu)
    mymenu.add_cascade(label="Instruction Set", menu=m3)
    
    # Adding the remaining menus directly as they dont have any submenu
    mymenu.add_command(label="Assemble", command=assemble)
    mymenu.add_command(label="Quit", command=quit)
    mymenu.add_command(label="About", command=about)
    root.config(menu=mymenu)

    # Adding a scrollbar
    scroll = Scrollbar(textArea)
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(command=textArea.yview)
    textArea.config(yscrollcommand=scroll.set, relief="raised")

    root.mainloop()
