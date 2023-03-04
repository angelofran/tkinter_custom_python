import customtkinter as ctk
import tkinter.messagebox as tkmb
from tkinter import *
import sqlite3 as sq



def login():
	new_window = ctk.CTk()

	new_window.title("Log In")

	new_window.geometry("500x400")
	new_window.resizable(False, False)

	label = ctk.CTkLabel(new_window, text="To do", font=("Century Gothic bold", 22))
	label.pack(pady=20)


	frame = ctk.CTkFrame(master=new_window)
	frame.pack(pady=20,padx=40,fill='both',expand=True)

	label = ctk.CTkLabel(master=frame,text='Log In')
	label.pack(pady=12,padx=10)


	user_entry= ctk.CTkEntry(master=frame,placeholder_text="Username")
	user_entry.pack(pady=12,padx=10)


	user_pass = ctk.CTkEntry(master=frame,placeholder_text="Password",show="*")
	user_pass.pack(pady=12,padx=10)
	
	def logar():
		with sq.connect('database.db') as connect:
			cursor = connect.cursor()
			
			user = user_entry.get()
			password = user_pass.get()

			log = f'''SELECT * FROM USER WHERE (NAME = '{user}' AND PASSWORD = '{password}')'''
			cursor.execute(log)
			dados = cursor.fetchone()
			if user in dados and password in dados:
				tkmb.showinfo("To do", message="Log In feito com sucesso.")
				connect.commit()
			elif user in dados or password in dados:
				tkmb.showinfo("To do", message="Senha/Name incorrectos.")
			elif user == "" or password == "":
				tkmb.showinfo("To do", message="Preencha todos os campos.")

	button = ctk.CTkButton(master=frame,text='Log In',command=logar, corner_radius=10, fg_color="#9268d6", hover_color="#54348c")
	button.pack(pady=12,padx=10)

	label1 = ctk.CTkButton(master=frame,text='Ainda não tenho conta, clique aqui.', fg_color="#2C2B2C", hover_color="#2C2B2C", corner_radius=15, command=new_window.destroy)	
	label1.pack(pady=10,padx=10)

	new_window.mainloop()