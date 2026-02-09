import customtkinter as ctk
import webbrowser
import threading

# Professional theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class ProjectAxisDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Window setup
        self.title("ProjectAxis Dashboard")
        self.geometry("600x500")
        
        # app icon
        self.iconbitmap("app_icon.ico")
        
        # Make it non-resizable for simplicity
        self.resizable(False, False)
        
        # Center window
        self.center_window()
        
        # ============ MAIN CONTAINER ============
        self.main_container = ctk.CTkFrame(self, fg_color="transparent")
        self.main_container.pack(fill="both", expand=True, padx=40, pady=40)
        
        # ============ HEADER ============
        self.header_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self.header_frame.pack(pady=(0, 30))
        
        # Logo/Title
        self.logo_frame = ctk.CTkFrame(self.header_frame, fg_color="transparent")
        self.logo_frame.pack()
        
        self.logo = ctk.CTkLabel(
            self.logo_frame,
            text="⚡",
            font=("Arial", 40),
            text_color="#3B82F6"
        )
        self.logo.pack()
        
        self.title = ctk.CTkLabel(
            self.logo_frame,
            text="PROJECTAXIS",
            font=("Arial", 28, "bold"),
            text_color="white"
        )
        self.title.pack(pady=(5, 0))
        
        self.subtitle = ctk.CTkLabel(
            self.logo_frame,
            text="Designed & Engineered for ProjectAxis by Subeesh",
            font=("Arial", 12),
            text_color="#94A3B8"
        )
        self.subtitle.pack(pady=(5, 0))
        
        # ============ STATUS INDICATOR ============
        self.status_frame = ctk.CTkFrame(self.main_container, fg_color="#1E293B", corner_radius=20)
        self.status_frame.pack(fill="x", pady=(0, 30))
        
        self.status_label = ctk.CTkLabel(
            self.status_frame,
            text="Status: ● Ready",
            font=("Arial", 12),
            text_color="#10B981"
        )
        self.status_label.pack(pady=12)
        
        # ============ CONTROL BUTTONS ============
        self.buttons_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self.buttons_frame.pack(pady=(0, 30))
        
        # Start Button
        self.start_btn = ctk.CTkButton(
            self.buttons_frame,
            text="🚀 START ENGINE",
            command=self.start_engine,
            width=250,
            height=50,
            font=("Arial", 16, "bold"),
            fg_color="#3B82F6",
            hover_color="#2563EB",
            corner_radius=10
        )
        self.start_btn.pack(pady=10)
        
        # Exit Button
        self.exit_btn = ctk.CTkButton(
            self.buttons_frame,
            text="⏹️ EXIT",
            command=self.quit_app,
            width=250,
            height=50,
            font=("Arial", 16, "bold"),
            fg_color="#6B7280",
            hover_color="#4B5563",
            corner_radius=10
        )
        self.exit_btn.pack(pady=10)
        
        # ============ SOCIAL LINKS ============
        self.social_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self.social_frame.pack(pady=(0, 30))
        
        # Portfolio Button
        self.portfolio_btn = ctk.CTkButton(
            self.social_frame,
            text="🌐 Portfolio",
            command=self.open_portfolio,
            width=120,
            height=35,
            font=("Arial", 12),
            fg_color="#1E293B",
            hover_color="#334155",
            corner_radius=8
        )
        self.portfolio_btn.pack(side="left", padx=5)
        
        # Instagram Button
        self.instagram_btn = ctk.CTkButton(
            self.social_frame,
            text="📸 Instagram",
            command=self.open_instagram,
            width=120,
            height=35,
            font=("Arial", 12),
            fg_color="#1E293B",
            hover_color="#334155",
            corner_radius=8
        )
        self.instagram_btn.pack(side="left", padx=5)
        
        # ============ FOOTER ============
        self.footer_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self.footer_frame.pack(fill="x")
        
        self.footer_label = ctk.CTkLabel(
            self.footer_frame,
            text="© 2024 ProjectAxis | Powered by Subeesh",
            font=("Arial", 10),
            text_color="#6B7280"
        )
        self.footer_label.pack()
    
    def center_window(self):
        """Center the window on screen"""
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        
        self.geometry(f"{width}x{height}+{x}+{y}")
    
    def start_engine(self):
        """Start the main application"""
        # Update button state
        self.start_btn.configure(
            text="▶️ ENGINE RUNNING...",
            state="disabled",
            fg_color="#6B7280"
        )
        self.status_label.configure(text="Status: ● Running", text_color="#F59E0B")
        
        # Launch in background thread
        threading.Thread(target=self.launch_main_app, daemon=True).start()
    
    def launch_main_app(self):
        """Launch the main application"""
        try:
            import app
            if hasattr(app, 'start_my_app'):
                app.start_my_app()
            elif hasattr(app, 'main'):
                app.main()
        except Exception as e:
            print(f"Error: {e}")
            # Reset button on error
            self.reset_engine()
    
    def reset_engine(self):
        """Reset engine button to ready state"""
        self.start_btn.configure(
            text="🚀 START ENGINE",
            state="normal",
            fg_color="#3B82F6"
        )
        self.status_label.configure(text="Status: ● Ready", text_color="#10B981")
    
    def open_portfolio(self):
        """Open portfolio link"""
        webbrowser.open("https://subeesh-zero.github.io/Profile/")
    
    def open_instagram(self):
        """Open Instagram link"""
        webbrowser.open("https://www.instagram.com/subeesh.zero")
    
    def quit_app(self):
        """Exit the application"""
        self.quit()

if __name__ == "__main__":
    app = ProjectAxisDashboard()
    app.mainloop()