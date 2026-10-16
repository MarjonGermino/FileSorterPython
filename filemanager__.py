import shutil; import pathlib; import tkinter; import platform
programmingLanguages = ["txt","py", "html", "css", "js", "java", "cpp", "c", "cs", "php", "rb", "swift", "kt", "go", "rs", "ts", "lua", "dart", "r", "sql", "sh", "ps1", "pl", "scala", "hs", "m", "go", "asm"]
videos = ["mp4", "mov", "avi", "mkv", "webm", "flv", "wmv", "m4v", "mpg", "mpeg", "3gp", "3g2", "ogv", "vob", "ts", "mts", "m2ts", "divx", "f4v", "rm", "rmvb", "asf", "amv", "mxf", "roq", "nsv", "yuv"]
images = ["jpg","jpeg","png","gif","webp","bmp","tiff","tif","svg","ico","heic","heif","raw","cr2","nef","arw","dng","psd","ai","eps"]
music = ["mp3", "wav", "flac", "aac", "ogg", "m4a", "wma", "alac", "aiff", "aif", "opus", "amr", "mid", "midi", "caf", "ra", "mka", "dts", "ac3"]

# Function to print to the output box
def print_to_window(text):
    output.config(state="normal")       # temporarily enable to insert
    output.insert("end", text + "\n")   # add text
    output.see("end")                   # auto-scroll to bottom
    output.config(state="disabled")     # lock it again
lineBeak = lambda: output.insert("end", "" +"\n")
p = pathlib.Path("../Sort_Files")
def runCMD():
    found = False
    for x in programmingLanguages: #programming languages
        for f in p.glob(f"*.{x}"):   # find all .txt files in directory py
            shutil.move(str(f), "programming")        # move file
            found = True
            print_to_window(f"moved: {str(f)[14:]} - 'Into programming'")
    lineBeak()
    for x in videos: #Vidoes
        for f in p.glob(f"*.{x}"):
            shutil.move(str(f), "Vidoes")
            print_to_window(f"moved: {str(f)[14:]} - 'Into Videos'")
            found = True
    lineBeak()
    for x in images: #Images
        for f in p.glob(f"*.{x}"):
            shutil.move(str(f), "Images")
            print_to_window(f"moved: {str(f)[14:]} - 'Into Images'")
            found = True
    lineBeak()
    for x in music: #Music
        for f in p.glob(f"*.{x}"):
            shutil.move(str(f), "Music")
            print_to_window(f'moved: {str(f)[14:]} - Into Music')
            found = True
    for f in p.glob("*.*"):
        if f.name.startswith("."): #skip hidden files
            continue
        shutil.move(f, "Others")
        print_to_window(f"Did not reconize {str(f)[14:]} - Moved into Others")
        found = True
    lineBeak()
    if not found:
        print_to_window("   Nothing was found to sort")
def clearCMD():
    output.config(state="normal")
    output.delete("1.0", "end")
    output.config(state="disabled")
def helpCMD():
    print_to_window("-"*57)
    print_to_window('Put all of the files within the "Sort_files" folder')
    print_to_window('After putting the files. press the "Move Files" button to sort the files')
    print_to_window("-"*57)

                        #############################⬇  ⬇GUI⬇  ⬇#############################
root = tkinter.Tk()
root.title("Sort Files in")
root.geometry("430x300"); root.resizable(False, False)

# Button Frame
buttonFrame = tkinter.Frame(root, pady=5); buttonFrame.pack(fill="x", padx=10)
#Buttons
if platform.system() == "Darwin": #If Its Mac Os
    def make_button(parent, txt, color, text_color, command, **grid_args):
        btn = tkinter.Label(parent, text=txt, bg=color, fg=text_color, cursor="hand2", padx=10, pady=5)
        btn.bind("<Button-1>", lambda e: command())
        btn.grid(**grid_args)
        return btn

    make_button(buttonFrame, "Move Files",    "#2A962E", "white",   runCMD,    row=0, column=0, columnspan=2, pady=2,   sticky="ew")
    make_button(buttonFrame, "Clear Text",    "#DADADA", "black",   clearCMD,  row=1, column=0, padx=2,       pady=2,   sticky="ew")
    make_button(buttonFrame, "Help",          "#DADADA", "black",   helpCMD,   row=1, column=1, padx=2,       pady=2,   sticky="ew")
    make_button(buttonFrame, "Close Program", "#ba2217", "white",   root.quit, row=2, column=0, columnspan=2, pady=2,   sticky="ew")

    buttonFrame.columnconfigure(0, weight=1)
    buttonFrame.columnconfigure(1, weight=1)
else:
    tkinter.Button(buttonFrame, text="Move Files", width=40, bg="#4CAF50", fg="white", command=runCMD).grid(row=0, column=0, columnspan=2, pady=2)
    tkinter.Button(buttonFrame, text="Clear Text", bg="#DADADA", width=18, command=clearCMD).grid(row=1, column=0, padx=2)
    tkinter.Button(buttonFrame, text="Help", bg="#DADADA", width=18, command=helpCMD).grid(row=1, column=1, padx=2)
    tkinter.Button(buttonFrame, text="Close Program", width=40, bg="#f44336", fg="white", command=root.quit).grid(row=2, column=0, columnspan=2, pady=2)



frame = tkinter.Frame(root, bg="gray")
frame.pack(fill="both", expand=True)
# Scrollbar
scrollbar = tkinter.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# Text widget (read-only output area)
output = tkinter.Text(frame, yscrollcommand=scrollbar.set, state="disabled")
output.pack(fill="both", expand=True)

scrollbar.config(command=output.yview)

root.mainloop()