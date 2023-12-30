import tkinter as tk
import re
window = tk.Tk()
window.configure(bg="grey")
window.title("M$ Timeline Cleaner")
greeting = tk.Label(text="Enter your timeline below!", bg="grey")
greeting.pack()
timeline_initial = tk.Text(highlightbackground="grey")
timeline_initial.pack()

def cleanup_click():
    raw_timeline = timeline_initial.get("1.0", tk.END)
    sremoved = re.sub(r"\s+", " ", raw_timeline)
    dateremoval = re.sub("[[]\d+/\d+ ", "[", sremoved)
    formatting = dateremoval.replace('[Yesterday ', '[').replace('[', '\n').replace(']', '').replace('AM', 'AM -').replace('PM', 'PM -').replace('Edited', '')
    likeremoval = re.sub("\d+ liked", "", formatting)
    finaltext = likeremoval.replace('()', '')
    final_timeline.insert("1.0", finaltext)
    final_timeline.delete("1.0", "2.0")
    cleanup_button.configure(state=tk.DISABLED)
    return 'break'

cleanup_button = tk.Button(text="click to clean up the timeline!", highlightbackground="grey", command=cleanup_click)
cleanup_button.pack()
final_timeline = tk.Text(highlightbackground="grey")
final_timeline.pack()

def destroy():
    exit = window.destroy()
    
exit_button = tk.Button(text="Exit", highlightbackground="grey", command=destroy)
exit_button.pack(side=tk.RIGHT)

def restart_click():
    final_timeline.delete("1.0", tk.END)
    timeline_initial.delete("1.0", tk.END)
    cleanup_button.configure(state=tk.NORMAL)
restart_button = tk.Button(text="Clear & Restart", highlightbackground="grey", command=restart_click)
restart_button.pack(side=tk.LEFT)

def select_all_initial(event):
    timeline_initial.tag_add(tk.SEL, "1.0", tk.END)
    return 'break'

timeline_initial.bind("<Command-Key-a>", select_all_initial)
timeline_initial.bind("<Command-Key-A>", select_all_initial)

def select_all_final(event):
    final_timeline.tag_add(tk.SEL, "1.0", tk.END)
    return 'break'

final_timeline.bind("<Command-Key-a>", select_all_final)
final_timeline.bind("<Command-Key-A>", select_all_final)
window.mainloop()