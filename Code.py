import tkinter as tk

# Dictionary to store candidate votes
candidate_votes = {"Candidate 1": 0, "Candidate 2": 0, "Candidate 3": 0}

def vote(candidate):
    candidate_votes[candidate] += 1
    print(f"You voted for {candidate}")

def submit_votes():
    result_window = tk.Toplevel(root)
    result_window.title("Results")

    for candidate, votes in candidate_votes.items():
        label = tk.Label(result_window, text=f"{candidate}: {votes} votes")
        label.pack()

# Create the main window
root = tk.Tk()
root.title("Online Voting System")

# Create labels and buttons for candidates
label1 = tk.Label(root, text="Candidate 1")
label1.pack()
button1 = tk.Button(root, text="Vote", command=lambda: vote("Candidate 1"))
button1.pack()

label2 = tk.Label(root, text="Candidate 2")
label2.pack()
button2 = tk.Button(root, text="Vote", command=lambda: vote("Candidate 2"))
button2.pack()

label3 = tk.Label(root, text="Candidate 3")
label3.pack()
button3 = tk.Button(root, text="Vote", command=lambda: vote("Candidate 3"))
button3.pack()

# Create a Submit button
submit_button = tk.Button(root, text="Submit Votes", command=submit_votes)
submit_button.pack()

# Start the GUI event loop
root.mainloop()
