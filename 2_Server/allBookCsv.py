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
# path = r'C:/Users/lucil/Documents/_Changed/TrackWithGit/ECE356_Books_and_Library_Database_Project/Data/'
all_files = glob.glob("book*_reordered.csv", root_dir=path)
cursor = cnx.cursor()

createTable_qry = (
    f'''drop table if exists GoodReadBook;
        create table GoodReadBook(
            Id  Bigint          not null,
            Name char(255)      not null,
            Authors	char(100)   not null,
            Desciption	Text,
            ISBN	    char(13) not null,
            Language	char(6),
            pagesNumber	decimal(7),
            PublishDay	decimal(2) not null,
            Publisher	char(100),
            PublishMonth    decimal(2) not null,
            PublishYear	    decimal(4) not null,
            PublishDate     Datetime not null,
            Rating	decimal (2,1) not null,
            RatingDist1	decimal(6) not null,
            RatingDist2	decimal(6) not null,
            RatingDist3	decimal(6) not null,
            RatingDist4	decimal(6) not null,
            RatingDist5	decimal(6) not null,
            RatingDistTotal	decimal(7) not null,
            CountsOfReview	decimal(7) not null,
            primary key (Id)
        );
''')
cursor.execute(createTable_qry, multi=True)
result = cursor.fetchall()
for x in result:
    print(x)

for filename in all_files:
    print('loading '+filename)
    qry = (f"load data infile '/var/lib/mysql-files/20-Books/{filename}' ignore "
        f'''into table GoodReadBook
    fields terminated by ','
    enclosed by '"'
    lines terminated by '\\n'
    ignore 1 lines
    (Id,
    Name,
    Authors,
    Desciption,
    ISBN,
    Language,
    pagesNumber,
    PublishDay,
    Publisher,
    PublishMonth,
    PublishYear,
    Rating,
    @RatingDist1,
    @RatingDist2,
    @RatingDist3,
    @RatingDist4,
    @RatingDist5,
    @RatingDistTotal,
    CountsOfReview,
    @CountsOfTextReview)
    set
        RatingDist1 = RIGHT(@RatingDist1, LENGTH(@RatingDist1) - REGEXP_INSTR(@RatingDist1, ':')),
        RatingDist2 = RIGHT(@RatingDist2, LENGTH(@RatingDist2) - REGEXP_INSTR(@RatingDist2, ':')),
        RatingDist3 = RIGHT(@RatingDist3, LENGTH(@RatingDist3) - REGEXP_INSTR(@RatingDist3, ':')),
        RatingDist4 = RIGHT(@RatingDist4, LENGTH(@RatingDist4) - REGEXP_INSTR(@RatingDist4, ':')),
        RatingDist5 = RIGHT(@RatingDist5, LENGTH(@RatingDist5) - REGEXP_INSTR(@RatingDist5, ':')),
        RatingDistTotal = RIGHT(@RatingDistTotal, LENGTH(@RatingDistTotal) - REGEXP_INSTR(@RatingDistTotal, ':')),
        PublishDate = DATE_ADD(DATE_ADD(MAKEDATE(PublishYear, 1), INTERVAL (PublishMonth)-1 MONTH), INTERVAL (PublishDay)-1 DAY);
show warnings limit 10;
        ''')
    # print(qry)
    cursor.execute(qry, multi=True)
    result = cursor.fetchall()
    for x in result:
        print(x)

cursor.close()
cnx.close()