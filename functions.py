import sqlite3


def get_cardarray(cardnumber):
    conn = sqlite3.connect('Anki.db')
    cursor = conn.cursor()
    get_card = """ SELECT * FROM Flashcards WHERE ID = ?"""
    cursor.execute(get_card, (cardnumber, ))
    card = cursor.fetchone()
    return card

def cal_score():
    pass

def return_card(DaysRevesion,Date,):
    conn = sqlite3.connect('Anki.db')
    cursor = conn.cursor()
    sql_returncard = """Insert into Flashcards (DaysRevesion) VALUES (?)""","""Insert into Flashcards (Date) VALUES (?)"""
    cursor.execute(sql_returncard, (DaysRevesion,Date))




