import mysql.connector

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()

word = input("please enter word here: ")
End = "word does not exists. please check spelling."

def query(word):
    word = word.lower()
    if word in results:
        return word
    elif word.title() in results:
        return word
    elif word.upper() in reults:
        return word
    else:
        return End

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word)
results = cursor.fetchall()

while(word == results):
    word = query(word)
    print(results)
else:
    print(word)

if results:
    for results in results:
        print(results[1])
