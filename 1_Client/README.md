need to run pip install mysql-connector-python
need to run using python3

To run the client application, run
python3 client.py <command> [flags]

in a terminal. For example,

python3 client.py search –-title lightning --author Rick

There are four commands that can be used.


search
This command searches the database and returns book related information (ID, name, author, and subjects) and book availability information (item location and item count).

The user can search by title, author, or subject using flags after the command. The user can also limit the amount of records they get using a flag (default 10). One of the title, author, or subject flags must be used for this command. If a flag argument contains a space, enclose the argument with single quotes (e.g. “The lightning thief”)

Flags
–-title (-t)
--author (-a)
--subject (-s)
--limit (-m)


checkout
This command adds a checkout record to the library checkout database.

The user specifies the bib number, item barcode, item type, collection, and call number using flags. To add a checkout record, the item type and collection must be a known code to the library database. To see a list of known codes use the codes command. All the flags must be used for this command.

Flags
–-number (-n)
--barcode (-b)
--type (-y)
--collection (-c)
--callnumber (-u)


update
This command updates either the item location or the number of available copies of a book in the library collections database.

The user must specify the ID of the collection they want to update. Then the user specifies either the updated item location or number of copies.  To update the item location, the location must be a known code to the database.

Flags
--id (-i)
--location (-l)
--copies (-o)


codes
This command lists the codes that are used by the database and their corresponding description.

The user must specify the code type of the codes they want to list. The code types can be either ItemType, ItemLocation, or ItemCollection.

Flags
--codetype (-d)
