drop table if exists LibraryCheckout;

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

load data infile '/var/lib/mysql-files/20-Books/Checkouts_By_Title_Data_Lens_2005.csv' ignore
into table LibraryCheckout
    fields terminated by ','
    enclosed by '"'
    lines terminated by '\n'
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