USE mgpu_ico_db_05;
CREATE TABLE authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    author_id INT,
    title VARCHAR(255),
    publication_year YEAR,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);
INSERT INTO authors (first_name, last_name)
VALUES 
('Джордж', 'Оруэлл'),
('Джоан', 'Роулинг'),
('Харуки', 'Мураками'),
('Эрих', 'Мариа Ремарк'),
('Стивен', 'Кинг');

INSERT INTO books (author_id, title, publication_year)
VALUES
(1, '1984', 1949),
(1, 'Скотный двор', 1945),
(2, 'Гарри Поттер и философский камень', 1997),
(2, 'Гарри Поттер и Дары Смерти', 2007),
(3, 'Норвежский лес', 1987),
(3, '1Q84', 2011),
(4, 'Три товарища', 1936),
(5, 'Оно', 1986),
(5, 'Под куполом', 2009),
(5, 'Доктор Сон', 2013);

SELECT b.title, b.publication_year, a.first_name, a.last_name
FROM books b
JOIN authors a ON b.author_id = a.author_id
WHERE b.publication_year > 2010;
