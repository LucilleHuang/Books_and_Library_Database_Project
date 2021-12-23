drop table if exists LibraryCheckout;
drop table if exists LibraryCollectionISBN;
drop table if exists LibraryCollection;

create table LibraryCollection(
    Id int not null AUTO_INCREMENT,
    BibNum	decimal(7) not null,
    Title	text,
    Author	char(199),
    ISBN text,
    PublicationYear	char(96),
    Publisher	text,
    Subjects	text,
    ItemType	char(7) not null,
    ItemCollection	char(7) not null,
    FloatingItem	Boolean	not null,
    ItemLocation	char(7) not null,
    ReportDate	Date	not null,
    ItemCount	decimal(3) not null,
    primary key (Id),
    FOREIGN KEY (ItemType) REFERENCES LibraryDataDictonary(Code),
    FOREIGN KEY (ItemCollection) REFERENCES LibraryDataDictonary(Code),
    FOREIGN KEY (ItemLocation) REFERENCES LibraryDataDictonary(Code)
);

load data infile '/var/lib/mysql-files/20-Books/Library_Collection_Inventory.csv' ignore
into table LibraryCollection
    fields terminated by ','
    enclosed by '"'
    lines terminated by '\n'
    ignore 1 lines
    (BibNum,
    @Title,
    @Author,
    ISBN,
    @PublicationYear,
    @Publisher,
    @Subjects,
    ItemType,
    ItemCollection,
    @FloatingItem,
    ItemLocation,
    @ReportDate,
    ItemCount)
    set
        Title = IF(@Title='', null, @Title),
        Author = IF(@Author='', null, @Author),
        PublicationYear = IF(@PublicationYear='', null, @PublicationYear),
        Publisher = IF(@Publisher='', null, @Publisher),
        Subjects = IF(@Subjects='', null, @Subjects),
        FloatingItem = CASE WHEN @FloatingItem='Floating' THEN True
                            WHEN @FloatingItem='NA' THEN False
                            ELSE null END,
        ReportDate = STR_TO_DATE(@ReportDate, "%m/%d/%Y");
show warnings limit 10;

create table LibraryCollectionISBN(
    Id int not null,
    ISBN char(13),
    primary key (Id, ISBN),
    FOREIGN KEY (Id) REFERENCES LibraryCollection(Id)
);

insert into LibraryCollectionISBN
    with countISBN as 
    (select Id,
    LENGTH(ISBN) - LENGTH(REPLACE(ISBN, ',', '')) as count,
        ISBN
    from LibraryCollection
    where ISBN <> ''
    )

    select t.Id,
        j.ISBN
    from countISBN t
    join json_table(
    replace(json_array(t.ISBN), ', ', '","'),
    '$[*]' columns (ISBN char(13) path '$')
    ) j;

alter table LibraryCollection drop column ISBN;

CREATE INDEX BibNum ON LibraryCollection(BibNum);
