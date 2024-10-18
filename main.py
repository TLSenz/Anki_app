import sqlite3 
import functions
import userinterface

conn = sqlite3.connect('Sqlite3.db') 


cursor = conn.cursor()

cursor.execute("SELECT question FROM flashcards WHERE id = 1")
cards = cursor.fetchall()


print("Flights: ", cards)