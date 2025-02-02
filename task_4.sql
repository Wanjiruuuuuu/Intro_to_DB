SELECT COLUMN_NAME, 
       DATA_TYPE, 
       CHARACTER_MAXIMUM_LENGTH, 
       IS_NULLABLE, 
       COLUMN_DEFAULT 
FROM information_schema.columns 
WHERE table_name = 'books' 
  AND table_schema = 'alx_book_store';

