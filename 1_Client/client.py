import argparse
import mysql.connector

parser = argparse.ArgumentParser()
parser.add_argument("command")
parser.add_argument("-t", "--title")
parser.add_argument("-a", "--author")
parser.add_argument("-s", "--subject")
args = parser.parse_args()

cnx = mysql.connector.connect(
    host="marmoset04.shoshin.uwaterloo.ca",
    user="-----",
    password="-----",
    database="-----"
)

#test query
cursor = cnx.cursor()

if (args.command == "Search"):
    cursor.execute("-----")
    result = cursor.fetchall()

    for x in result:
        print(x)

    if (args.title):
        print("Title")
    if (args.author):
        print("Author")
    if (args.subject):
        print("Subject")
    print("Search")
    #TODO
elif (args.command == "CheckStatus"):
    print("Check Status")
    #TODO
elif (args.command == "UpdateStatus"):
    print("Update Status")
    #TODO
elif (args.command == "AddBook"):
    print("Add Book")
    #TODO

cursor.close()
cnx.close()