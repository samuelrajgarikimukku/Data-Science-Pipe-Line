SELECT * FROM public.students

\copy public.students
FROM 'C:/Users/samue/Desktop/raw.csv'
WITH (FORMAT csv, HEADER true);


