import argparse

parser = argparse.ArgumentParser()
parser.add_argument("command")
parser.add_argument("-t", "--title")
parser.add_argument("-a", "--author")
parser.add_argument("-s", "--subject")
args = parser.parse_args()

if (args.command == "Search"):
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