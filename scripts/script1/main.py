import customtkinter as ctk

app = ctk.CTk()
app.title("Testowy skrypt z customtkinter")

label = ctk.CTkLabel(app, text="Hello, World!", font=("Arial", 20))
label.pack(padx=20, pady=20)

app.mainloop()