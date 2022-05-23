# Hindawi Texts for Stylo (in progress)

- `_metadata_books_man.yml` is the file where URIs must be assigned (763 - about half of files have their URIs, folowing the OpenITI converntions)

- running `_reformat_for_stylo.py` will convert files for which URIs are created into clean texts suitable for use with rStylo:
    - texts are renamed following the rStylo convention: `Author_Title`
    - texts are stripped of punctuation, short vowels; only Arabic letters remain;
    - Arabic is normalized (oinly one form of alif; alif maqsuras into yas; chairs of hamsas converted into hamzas)

- the script requires library `openiti`
- crete folder `stylo_selection` (must be named exactly like this)

# Adding more texts

- `_metadata_books_man.yml` can be edited by adding more URIs for cases where URI is `NotAssignedYet.Book.HindawiXXXXXXXX`.
    - `NotAssignedYet` must be replaced with the name of the Author, starting with 4 digits indicating his/her year of death in HIJRI calendar.
    - `Book` must be replaced with one or two words from the title of the book
    - `HindawiXXXXXXXX` remains as is.
- run the python script again to get more texts.

# Original Books

- These files are hardly good for conventional reading; you can find originals on <https://www.hindawi.org/> in either EPUB or PDF format;
- the fastest way to get to a specific book is to use te following link:
    - `https://www.hindawi.org/books/` + the numeric ID of the book (8 digits, like `39429258`); these IDs can be found in the metadata file under `01#BookID###::::`