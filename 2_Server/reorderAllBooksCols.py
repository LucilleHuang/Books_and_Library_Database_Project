import pandas as pd
import numpy as np
import glob

# path = r'/var/lib/mysql-files/20-Books/' # path on marmoset
# below is the path on local to get the list of filenames
path = r'C:/Users/lucil/Documents/_Changed/TrackWithGit/ECE356_Books_and_Library_Database_Project/Data/'
all_files = glob.glob("book*.csv", root_dir=path)
for filename in all_files:
    books = pd.read_csv(path+filename, index_col=None, header=0)
    if 'Desciption' not in books.columns:
        books['Desciption'] = np.nan
    if 'CountsOfTextReview' not in books.columns:
        books['CountsOfTextReview'] = np.nan
    cols = ['Id',
        'Name',
        'Authors',
        'Desciption',
        'ISBN',
        'Language',
        'pagesNumber',
        'PublishDay',
        'Publisher',
        'PublishMonth',
        'PublishYear',
        'Rating',
        'RatingDist1',
        'RatingDist2',
        'RatingDist3',
        'RatingDist4',
        'RatingDist5',
        'RatingDistTotal',
        'CountsOfReview',
        'CountsOfTextReview']
    books_reordered = books[cols]
    filename = filename.split('.')[0]
    books_reordered.to_csv(path_or_buf=path+filename+'_reordered.csv',index=False)