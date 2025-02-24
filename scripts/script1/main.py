import customtkinter as ctk

app = ctk.CTk()
app.title("Testowy skrypt z customtkinter")

label = ctk.CTkLabel(app, text="Hello, World!", font=("Arial", 20))
label.pack(padx=200, pady=200)

app.mainloop()