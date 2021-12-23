import mysql.connector
import glob

cnx = mysql.connector.connect(
    host="marmoset04.shoshin.uwaterloo.ca",
    user="j349huan",
    password="123Abc!!",
    database="db356_j349huan"
)

path = r'/var/lib/mysql-files/20-Books/' # use your path
all_files = glob.glob(path + "Checkouts*.csv")
cursor = cnx.cursor()
for filename in all_files:
    sql=(f"select {filename};")
    print(sql)
    qry = (f"load data infile {filename} ignore"
        '''into table LibraryCheckout
            fields terminated by ','
            enclosed by '"'
            lines terminated by '\n'
            ignore 3794500 lines
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
    cursor.execute(sql)

    result = cursor.fetchall()
    for x in result:
        print(x)

cursor.close()
cnx.close()