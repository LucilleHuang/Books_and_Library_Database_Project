import argparse
import mysql.connector
from datetime import date, datetime, timedelta
import sys

parser = argparse.ArgumentParser()
parser.add_argument("command")
# search
parser.add_argument("-t", "--title")
parser.add_argument("-a", "--author")
parser.add_argument("-s", "--subject")
#parser.add_argument("-r", "--rating")
parser.add_argument("-m", "--limit")

#checkout
parser.add_argument("-n", "--number")
parser.add_argument("-b", "--barcode")
parser.add_argument("-y", "--type")
parser.add_argument("-c", "--collection")
parser.add_argument("-u", "--callnumber")

#update location or copies
parser.add_argument("-l", "--location")
parser.add_argument("-o", "--copies")
parser.add_argument("-i", "--id")

#get codes
parser.add_argument("-d", "--codetype")

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
commaFlag = False

LIMIT = 10

if (args.command == "search"):
    """  ignore rating and description for now
    query = "SELECT G.Name, G.Authors, G.Desciption, G.Rating, G.CountsOfReview"
    query += " FROM LibraryCollectionISBN AS LCI"
    query += " INNER JOIN GoodReadBook AS G"
    query += " ON G.ISBN = LCI.ISBN"
    query += " INNER JOIN LibraryCollection AS LC"
    query += " ON LC.id = LCI.id"
    """
    query = "SELECT id, Title, Author, Subjects, ItemLocation, ItemCount FROM LibraryCollection"

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
    
    if (args.limit):
        query = query + " LIMIT " + args.limit
    else:
        query = query + " LIMIT " + str(LIMIT)

    try:
        cursor.execute(query)
        result = cursor.fetchall()

        for x in result:
            print("ID: " + str(x[0]))
            print("Title: " + str(x[1]))
            print("Author: " + str(x[2]))
            print("Subjects: " + str(x[3]))
            print("Item Location: " + str(x[4]))
            print("Item Count: " + str(x[5]))
            print("\n")
    except:
        print("An error occured")


elif (args.command == "checkout"):
    query = "INSERT INTO LibraryCheckout"
    query +=  " (Bibnumber, ItemBarcode, ItemType, Collection, CallNumber, CheckoutDateTime)"
    query += " VALUE (%s, %s, %s, %s, %s, %s)"

    if (not(args.number and args.barcode and args.type and args.collection and args.callnumber)):
        sys.exit("Must specify Bibnumber, Barcode, Type, Collection, and Number")

    checkout = (args.number, args.barcode, args.type, args.collection, args.callnumber, datetime.now())
    try:
        cursor.execute(query, checkout)

        cnx.commit()
    except:
        print("An error occured")

elif (args.command == "update"):
    if (not args.id):
        sys.exit("Must specify id of collection")
    if (not(args.location or args.copies)):
        sys.exit("Must specify either location or number of available copies")
    query = "UPDATE LibraryCollection SET"
    if (args.location):
        query = query + " ItemLocation = '" + args.location + "'"
        commaFlag = True
    if (args.copies):
        if commaFlag:
            query = query + ","
        query = query + " ItemCount = '" + args.copies + "'"
    query = query + " WHERE id = '" + args.id + "'"

    try:
        cursor.execute(query)

        cnx.commit()
    except:
        print("An error occured")

elif (args.command == "codes"):
    query = "SELECT Code, Description FROM LibraryDataDictonary"

    if (args.codetype):
        query = query + " WHERE CodeType = '" + args.codetype + "'"

    try:
        cursor.execute(query)
        result = cursor.fetchall()

        for x in result:
            print("Code: " + str(x[0]))
            print("Description: " + str(x[1]))
            print("\n")
    except:
        print("An error occured")

cursor.close()
cnx.close()