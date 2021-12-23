load data infile '/var/lib/mysql-files/20-Books/Integrated_Library_System__ILS__Data_Dictionary.csv' ignore
into table LibraryDataDictonary
    fields terminated by ','
    enclosed by '"'
    lines terminated by '\n'
    ignore 1 lines
    (Code, Description, CodeType, @col4, @col5, @col6, @col7)
    set FormatGroup = IF(@col4='', null, @col4),
        FormatSubgroup = IF(@col5='', null, @col5),
        CategoryGroup = IF(@col6='', null, @col6),
        CategorySubgroup = IF(@col7='', null, @col7);
show warnings limit 10;