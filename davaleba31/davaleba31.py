import sqlite3

conn = sqlite3.connect('deposits.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE Deposits(
        DepositID INTEGER PRIMARY KEY AUTOINCREMENT,
        DepOwnerName TEXT NOT NULL,
        DateOfBirth TEXT NOT NULL,
        City TEXT NOT NULL,
        StreetName TEXT NOT NULL,
        DepositAmount REAL,
        Interest REAL,
        Commision REAL,
        Total REAL        
    )
''')

conn.commit()

depositors = [
    ('Daniel Subeliani', '1995-09-12', 'Tbilisi', 'Kipshidze Street', 2000, 0.05, 50, 2050),
    ('Kote Markozashvili', '1998-02-23', 'Batumi', 'Gorgasali Street', 1800, 0.04, 40, 1840),
    ('Davit Makharadze', '1996-11-04', 'Tbilisi', 'Rustaveli Street', 2500, 0.06, 60, 2560),
    ('Amiran Kotia', '1994-11-28', 'Tbilisi', 'Rustaveli Street', 1200, 0.03, 30, 1230),
    ('Tornike Bechvaia', '1995-06-16', 'Batumi', 'Gorgasali Street', 900, 0.02, 20, 920),
]

cursor.executemany('''
    INSERT INTO Deposits(DepOwnerName, DateOfBirth, City, StreetName, DepositAmount, Interest, Commision, Total)
    VALUES(?, ?, ?, ?, ?, ?, ?, ?)
''', depositors)

conn.commit()

# გამოიტანეთ აბსოლუტურად ყველა დეპოზიტორი:
cursor.execute('SELECT * FROM Deposits')
all_depositors = cursor.fetchall()
for depositor in all_depositors:
    print(depositor)

# გამოიტანეთ ყველა ის დეპოზიტორი, რომლის დეპოზიტიც არის 1500-ზე მეტი:
cursor.execute('SELECT * FROM Deposits WHERE DepositAmount > 1500')
depositors_more_than_1500 = cursor.fetchall()
for depositor in depositors_more_than_1500:
    print(depositor)

# გამოიტანეთ ყველა ის დეპოზიტორი, რომელიც ცხოვრობს თბილისში რუსთაველის ქუჩაზე:
cursor.execute('SELECT * FROM Deposits WHERE City = "Tbilisi" AND StreetName = "Rustaveli Street"')
tbilisi_rustaveli_depositors = cursor.fetchall()
for depositor in tbilisi_rustaveli_depositors:
    print(depositor)

# გამოიტანეთ ყველა ის დეპოზიტორი, რომელიც ცხოვრობს ბათუმში, გორგასალიზ ქუჩაზე, დეპოზიტი აქვთ 1000-ზე მეტი და 2000-ზე ნაკლები:
cursor.execute('SELECT * FROM Deposits WHERE City = "Batumi" AND StreetName = "Gorgasali Street" AND DepositAmount > 1000 AND DepositAmount < 2000')
batumi_gorgasali_depositors = cursor.fetchall()
for depositor in batumi_gorgasali_depositors:
    print(depositor)


# გამოიტანეთ ყველა ის დეპოზიტორი რომლის სახელიც იწყება ასო “დ”-ზე:
cursor.execute('SELECT * FROM Deposits WHERE DepOwnerName LIKE "D%"')
d_depositors = cursor.fetchall()
for depositor in d_depositors:
    print(depositor)

# გაასუფთავეთ მთლიანი ცხრილი:
cursor.execute('DELETE FROM Deposits')
conn.commit()

# წაშალეთ ცხრილი Deposits:
cursor.execute('DROP TABLE Deposits')
conn.commit()

conn.close()