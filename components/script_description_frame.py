import customtkinter as ctk

class ScriptDescriptionFrame(ctk.CTkFrame):

    ##############################Initialize the ScriptDescriptionFrame with the parent widget.#############################

    def __init__(self, parent):
        """status       
        :param parent: Parent widget
        """
        super().__init__(parent, corner_radius=0, fg_color="gray15", border_width=0)
        self.pack(side="right", fill="both", expand=True, padx=0, pady=0)

        # GUI Elements
        self.title_label = ctk.CTkLabel(
            self,
            text="Script Description",
            font=("Open Sans", 16, "bold"),
            anchor="w"
        )
        self.title_label.pack(pady=(10, 5), padx=10, anchor="w")

        self.description_text = ctk.CTkTextbox(
            self,
            wrap="word",
            font=("Open Sans", 12),
            state="disabled",
            fg_color="gray20",
            text_color="white",
            border_width=0
        )
        self.description_text.pack(fill="both", expand=True, padx=10, pady=10)

    ##############################Set the description text for the selected script.#############################

    def set_description(self, description):
        """     
        :param description: Description text to display
        """
        self.description_text.configure(state="normal")
        self.description_text.delete("1.0", "end")
        self.description_text.insert("1.0", description)
        self.description_text.configure(state="disabled")