import mysql.connector
import glob

cnx = mysql.connector.connect(
    host="marmoset04.shoshin.uwaterloo.ca",
    user="j349huan",
    password="123Abc!!",
    database="db356_j349huan"
)

path = r'/var/lib/mysql-files/20-Books/' # path on marmoset
# below is the path on local to get the list of filenames
# path = r'C:/Users/lucil/Documents/_Changed/TrackWithGit/ECE356_Books_and_Library_Database_Project/Data/Library/'
all_files = glob.glob("Checkouts*.csv", root_dir=path)
cursor = cnx.cursor()

createTable_qry = (
    f'''drop table if exists LibraryCheckout;
    create table LibraryCheckout(
        Bibnumber decimal(7)    not null,
        ItemBarcode char(13)    not null,
        ItemType    char(7)     not null,
        Collection  char(7)     not null,
        CallNumber char(59),
        CheckoutDateTime    dateTime    not null,
        primary key (ItemBarcode, CheckoutDateTime),
        FOREIGN KEY (ItemType) REFERENCES LibraryDataDictonary(Code),
        FOREIGN KEY (Collection) REFERENCES LibraryDataDictonary(Code)
    );
''')
cursor.execute(createTable_qry, multi=True)
result = cursor.fetchall()
for x in result:
    print(x)

for filename in all_files:
    print('loading '+filename)
    qry = (f"load data infile '/var/lib/mysql-files/20-Books/{filename}' ignore "
        f'''into table LibraryCheckout
            fields terminated by ','
            enclosed by '"'
            lines terminated by '\\n'
            ignore 1 lines
            (Bibnumber,
            ItemBarcode,
            ItemType,
            Collection,
            @CallNumber,
            @CheckoutDateTime)
            set
                CallNumber = IF(@CallNumber='', null, @CallNumber),
                CheckoutDateTime = STR_TO_DATE(@CheckoutDateTime, "%m/%d/%Y %r");
        show warnings limit 10;
        ''')
    # print(qry)
    cursor.execute(qry, multi=True)
    result = cursor.fetchall()
    for x in result:
        print(x)

cursor.close()
cnx.close()