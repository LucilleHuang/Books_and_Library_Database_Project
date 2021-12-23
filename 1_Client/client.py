import argparse
import mysql.connector
from datetime import date, datetime, timedelta
import sys

parser = argparse.ArgumentParser()
parser.add_argument("command")
parser.add_argument("-t", "--title")
parser.add_argument("-a", "--author")
parser.add_argument("-s", "--subject")
#parser.add_argument("-r", "--rating")

parser.add_argument("-n", "--number")
parser.add_argument("-b", "--barcode")
parser.add_argument("-i", "--type")
parser.add_argument("-c", "--collection")
parser.add_argument("-l", "--callnumber")

args = parser.parse_args()

cnx = mysql.connector.connect(
    host="marmoset04.shoshin.uwaterloo.ca",
    user="j349huan",
    password="123Abc!!",
    database="db356_j349huan"
)

#test query
cursor = cnx.cursor()
andFlag = False

LIMIT = 10

if (args.command == "Search"):
    """  ignore rating and description for now
    query = "SELECT G.Name, G.Authors, G.Desciption, G.Rating, G.CountsOfReview"
    query += " FROM LibraryCollectionISBN AS LCI"
    query += " INNER JOIN GoodReadBook AS G"
    query += " ON G.ISBN = LCI.ISBN"
    query += " INNER JOIN LibraryCollection AS LC"
    query += " ON LC.id = LCI.id"
    """
    query = "SELECT Title, Author, Subjects, ItemLocation, ItemCount FROM LibraryCollection"

    if (args.title or args.author or args.subject):
        query = query + " WHERE"
    else:
        sys.exit("Must specity either a title, author, or subject")

    if (args.title):
        query = query + " TITLE LIKE '%" + args.title + "%'"
        andFlag = True

    if (args.author):
        if (andFlag):
            query = query + " AND"
        query = query + " Author LIKE '%" + args.author + "%'"
        andFlag = True

    if (args.subject):
        if (andFlag):
            query = query + " AND"
        query = query + " Subjects LIKE '%" + args.subject + "%'"
        andFlag = True
    
    query = query + " LIMIT " + str(LIMIT)

    cursor.execute(query)
    result = cursor.fetchall()

    for x in result:
        print("Title: " + str(x[0]))
        print("Author: " + str(x[1]))
        print("Subjects: " + str(x[2]))
        print("Item Location: " + str(x[3]))
        print("Item Count: " + str(x[4]))
        print("\n")


elif (args.command == "Checkout"):
    query = "INSERT INTO LibraryCheckout"
    query +=  " (Bibnumber, ItemBarcode, ItemType, Collection, CallNumber, CheckoutDateTime)"
    query += " VALUE (%s, %s, %s, %s, %s, %s)"

    if (not(args.number and args.barcode and args.type and args.collection and args.callnumber)):
        sys.exit("Must specify Bibnumber, Barcode, Type, Collection, and Number")

    checkout = (args.number, args.barcode, args.type, args.collection, args.callnumber, datetime.now())

    cursor.execute(query, checkout)

    cnx.commit()

elif (args.command == "UpdateStatus"):
    print("Update Status")
    #TODO
elif (args.command == "AddBook"):
    print("Add Book")
    #TODO

cursor.close()
cnx.close()