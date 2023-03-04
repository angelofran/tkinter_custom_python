import customtkinter as ctk
import tkinter.messagebox as tkmb
from tkinter import *
import sqlite3 as sq
import login


class app(ctk.CTk):
	def __init__(self):
		self.app = ctk.CTk()
		ctk.set_appearance_mode("dark")
		ctk.set_default_color_theme("blue")
		self.app.geometry("500x600")
		self.app.resizable(False, False)
		self.app.title("To do")
		self.screen_register()


	def cadastrar(self):
		with sq.connect('database.db') as connect:
			cursor = connect.cursor()
			table ="""CREATE TABLE IF NOT EXISTS USER(NAME Text NOT NULL, LASTNAME Text NOT NULL,
			EMAIL Text NOT NULL, PASSWORD Text NOT NULL);"""
			cursor.execute(table)

			email = self.user_email.get()
			password = self.user_pass.get()
			lastname = self.user_lastname.get()
			username = self.user_entry.get()
			if email == "" or password == "" or lastname == "" or username == "":
				tkmb.showwarning("Warning", message="Preencha todos os campos.")
			elif len(password) < 8:
				tkmb.showwarning("Warning", message="Use passwords mais seguras")
				self.user_pass.delete(0, END)
			else:
				insert = f'''INSERT INTO USER(NAME, LASTNAME, EMAIL, PASSWORD) VALUES ('{username}', '{lastname}', '{email}', '{password}')'''
				cursor.execute(insert)
				connect.commit()
				self.user_email.delete(0, END)
				self.user_pass.delete(0, END)
				self.user_lastname.delete(0, END)
				self.user_entry.delete(0, END)

				tkmb.showinfo("Info", message="Conta criada com sucesso.")
				self.app.destroy()
				login()


	def screen_register(self):
	
		self.label = ctk.CTkLabel(self.app,text="To do", font=("Century Gothic bold", 22))

		self.label.pack(pady=20)


		self.frame = ctk.CTkFrame(master=self.app)
		self.frame.pack(pady=20,padx=40,fill='both',expand=True)

		self.label = ctk.CTkLabel(master=self.frame,text='Sign Up')
		self.label.pack(pady=12,padx=10)


		self.user_entry= ctk.CTkEntry(master=self.frame,placeholder_text="Username")
		self.user_entry.pack(pady=12,padx=10)


		self.user_lastname= ctk.CTkEntry(master=self.frame,placeholder_text="Last name")
		self.user_lastname.pack(pady=12,padx=10)

		self.user_email= ctk.CTkEntry(master=self.frame,placeholder_text="Email")
		self.user_email.pack(pady=12,padx=10)

		self.user_pass= ctk.CTkEntry(master=self.frame,placeholder_text="Password",show="*")
		self.user_pass.pack(pady=12,padx=10)


		self.button = ctk.CTkButton(master=self.frame,text='Sign Up',command=self.cadastrar, corner_radius=10, fg_color="#9268d6", hover_color="#54348c")
		self.button.pack(pady=12,padx=10)

		self.checkbox = ctk.CTkCheckBox(master=self.frame,text='Remember Me')
		self.checkbox.pack(pady=12,padx=10)

		self.label1 = ctk.CTkButton(master=self.frame,text='Já tenho conta, clique aqui.', fg_color="#2C2B2C", hover_color="#2C2B2C", corner_radius=15, command=login.login)	
		self.label1.pack(pady=10,padx=10)

	


if __name__ == "__main__":
	app().app.mainloop()
		