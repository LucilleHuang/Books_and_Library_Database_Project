drop table if exists LibraryDataDictonary;

create table LibraryDataDictonary(
    Code                char(7)     not null,
    Description         char(46)    not null,
    CodeType            enum('ItemType', 'ItemLocation', 'ItemCollection')  not null,
    FormatGroup         enum('Media', 'Internet', 'Equipment', 'Print'),
    FormatSubgroup      enum('Art', 'Audiobook Tape', 'Periodical', 'Video Tape', 'Data Disc', 'Audiobook', 'Film', 'Music Score', 'Document', 'Audio Disc', 'Kit', 'Folder', 'Audiobook Disc', 'Video Disc', 'Video', 'Book', 'Audio Tape'),
    CategoryGroup       enum('Reference', 'Fiction', 'Language', 'Nonfiction'),
    CategorySubgroup    enum('Picture', 'Biography', 'Holiday', 'ESL', 'Large Print'),
    primary key (CodeType, Code)
);
