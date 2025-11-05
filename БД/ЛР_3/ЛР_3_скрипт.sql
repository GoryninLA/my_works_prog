CREATE TABLE authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    birth_date DATE,
    nationality VARCHAR(50)
);


CREATE TABLE genres (
    genre_id INT AUTO_INCREMENT PRIMARY KEY,
    genre_name VARCHAR(50) NOT NULL,
    description TEXT
);


CREATE TABLE publishers (
    publisher_id INT AUTO_INCREMENT PRIMARY KEY,
    publisher_name VARCHAR(100),
    country VARCHAR(50),
    founded_year INT
);


CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    author_id INT NOT NULL,
    title VARCHAR(100) NOT NULL,
    publication_year INT NOT NULL,
    genre_id INT NOT NULL,
    publisher_id INT,
    CONSTRAINT fk_books_author FOREIGN KEY (author_id) REFERENCES authors(author_id),
    CONSTRAINT fk_books_genre FOREIGN KEY (genre_id) REFERENCES genres(genre_id),
    CONSTRAINT fk_books_publisher FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
);


CREATE TABLE readers (
    reader_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    registration_date DATE NOT NULL,
    phone VARCHAR(20)
);


CREATE TABLE book_copies (
    copy_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT NOT NULL,
    inventory_number VARCHAR(20) NOT NULL UNIQUE,
    status VARCHAR(20),
    acquisition_date DATE,
    book_condition VARCHAR(50),
    CONSTRAINT fk_copy_book FOREIGN KEY (book_id) REFERENCES books(book_id)
);


CREATE TABLE loans (
    loan_id INT AUTO_INCREMENT PRIMARY KEY,
    copy_id INT NOT NULL,
    reader_id INT NOT NULL,
    loan_date DATE NOT NULL,
    due_date DATE NOT NULL,
    return_date DATE,
    CONSTRAINT fk_loan_copy FOREIGN KEY (copy_id) REFERENCES book_copies(copy_id),
    CONSTRAINT fk_loan_reader FOREIGN KEY (reader_id) REFERENCES readers(reader_id)
);




INSERT INTO authors (first_name, last_name, birth_date, nationality) VALUES
('George', 'Orwell', '1903-06-25', 'British'),
('Jane', 'Austen', '1775-12-16', 'British'),
('Mark', 'Twain', '1835-11-30', 'American'),
('Fyodor', 'Dostoevsky', '1821-11-11', 'Russian'),
('J.K.', 'Rowling', '1965-07-31', 'British'),
('Stephen', 'King', '1947-09-21', 'American'),
('Ernest', 'Hemingway', '1899-07-21', 'American'),
('Haruki', 'Murakami', '1949-01-12', 'Japanese'),
('Leo', 'Tolstoy', '1828-09-09', 'Russian'),
('Agatha', 'Christie', '1890-09-15', 'British');

INSERT INTO genres (genre_name, description) VALUES
('Fiction', 'General fiction works'),
('Fantasy', 'Imaginative and magical worlds'),
('Mystery', 'Detective and mystery stories'),
('Classic', 'Timeless literature'),
('Science Fiction', 'Futuristic and speculative works'),
('Romance', 'Love and emotional relationships'),
('Horror', 'Scary and supernatural themes'),
('Adventure', 'Exciting and risk-filled stories'),
('Drama', 'Emotional, realistic narratives'),
('Historical', 'Based on past events');


INSERT INTO publishers (publisher_name, country, founded_year) VALUES
('Penguin Books', 'United Kingdom', 1935),
('HarperCollins', 'United States', 1989),
('Random House', 'United States', 1927),
('Bloomsbury', 'United Kingdom', 1986),
('Simon & Schuster', 'United States', 1924),
('Vintage Books', 'United States', 1954),
('Oxford University Press', 'United Kingdom', 1586),
('Macmillan Publishers', 'United Kingdom', 1843),
('Scholastic Press', 'United States', 1920),
('Knopf Publishing', 'United States', 1915);


INSERT INTO books (author_id, title, publication_year, genre_id, publisher_id) VALUES
(1, '1984', 1949, 1, 1),
(2, 'Pride and Prejudice', 1813, 6, 7),
(3, 'The Adventures of Tom Sawyer', 1876, 8, 3),
(4, 'Crime and Punishment', 1866, 4, 7),
(5, 'Harry Potter and the Philosopher''s Stone', 1997, 2, 4),
(6, 'The Shining', 1977, 7, 5),
(7, 'The Old Man and the Sea', 1952, 4, 6),
(8, 'Norwegian Wood', 1987, 9, 8),
(9, 'War and Peace', 1869, 10, 7),
(10, 'Murder on the Orient Express', 1934, 3, 1);


INSERT INTO readers (first_name, last_name, email, registration_date, phone) VALUES
('Alice', 'Johnson', 'alice.johnson@example.com', '2022-05-01', '+123456789'),
('Bob', 'Smith', 'bob.smith@example.com', '2022-06-10', '+198765432'),
('Charlie', 'Brown', 'charlie.brown@example.com', '2022-07-15', '+112233445'),
('Diana', 'Evans', 'diana.evans@example.com', '2022-08-12', '+123123123'),
('Ethan', 'Williams', 'ethan.williams@example.com', '2022-09-18', '+321321321'),
('Fiona', 'Clark', 'fiona.clark@example.com', '2022-10-05', '+987987987'),
('George', 'Miller', 'george.miller@example.com', '2023-01-21', '+654654654'),
('Hannah', 'Davis', 'hannah.davis@example.com', '2023-02-14', '+741852963'),
('Ivan', 'Petrov', 'ivan.petrov@example.com', '2023-03-30', '+852369741'),
('Julia', 'Adams', 'julia.adams@example.com', '2023-04-09', '+963258741');


INSERT INTO book_copies (book_id, inventory_number, status, acquisition_date, book_condition) VALUES
(1, 'INV-001', 'Available', '2020-01-10', 'Good'),
(1, 'INV-002', 'Borrowed', '2020-01-12', 'Good'),
(2, 'INV-003', 'Available', '2019-03-05', 'Excellent'),
(3, 'INV-004', 'Borrowed', '2021-04-21', 'Fair'),
(4, 'INV-005', 'Available', '2018-07-15', 'Good'),
(5, 'INV-006', 'Available', '2019-11-23', 'Excellent'),
(6, 'INV-007', 'Borrowed', '2022-02-02', 'Good'),
(7, 'INV-008', 'Available', '2021-06-17', 'Good'),
(8, 'INV-009', 'Borrowed', '2020-09-09', 'Excellent'),
(9, 'INV-010', 'Available', '2018-12-30', 'Good');


INSERT INTO loans (copy_id, reader_id, loan_date, due_date, return_date) VALUES
(2, 1, '2023-10-01', '2023-10-15', '2023-10-14'),
(4, 2, '2023-09-20', '2023-10-05', '2023-10-03'),
(7, 3, '2023-10-10', '2023-10-25', NULL),
(9, 4, '2023-10-15', '2023-10-30', NULL),
(1, 5, '2023-08-10', '2023-08-25', '2023-08-20'),
(5, 6, '2023-09-05', '2023-09-20', '2023-09-19'),
(6, 7, '2023-10-01', '2023-10-16', NULL),
(3, 8, '2023-07-01', '2023-07-16', '2023-07-14'),
(8, 9, '2023-06-10', '2023-06-25', '2023-06-23'),
(10, 10, '2023-10-18', '2023-11-02', NULL);

SELECT 
    b.title AS book_title,
    CONCAT(r.first_name, ' ', r.last_name) AS reader_name,
    l.loan_date AS date_issued
FROM loans l
JOIN readers r ON l.reader_id = r.reader_id
JOIN book_copies c ON l.copy_id = c.copy_id
JOIN books b ON c.book_id = b.book_id
WHERE l.return_date IS NULL
ORDER BY l.loan_date DESC;



SELECT 
    CONCAT(a.first_name, ' ', a.last_name) AS author_name,
    COUNT(l.loan_id) AS quantity_issue
FROM loans l
JOIN book_copies c ON l.copy_id = c.copy_id
JOIN books b ON c.book_id = b.book_id
JOIN authors a ON b.author_id = a.author_id
GROUP BY a.author_id
HAVING COUNT(l.loan_id) > 5
ORDER BY COUNT(l.loan_id) DESC;

SELECT 
    CONCAT(r.first_name, ' ', r.last_name) AS reader,
    b.title AS book_name,
    l.loan_date AS loan_date,
    l.due_date AS due_date,
    DATEDIFF(CURDATE(), l.loan_date) AS lasts_day
FROM loans l
JOIN readers r ON l.reader_id = r.reader_id
JOIN book_copies c ON l.copy_id = c.copy_id
JOIN books b ON c.book_id = b.book_id
WHERE l.return_date IS NULL
  AND DATEDIFF(CURDATE(), l.loan_date) > 14
ORDER BY DATEDIFF(CURDATE(), l.loan_date) DESC;


INSERT INTO loans (copy_id, reader_id, loan_date, due_date, return_date) VALUES
(7, 1, '2023-09-01', '2023-09-15', '2023-09-10'),
(7, 2, '2023-09-20', '2023-10-05', '2023-10-02'),
(7, 3, '2023-10-10', '2023-10-25', '2023-10-22'),
(7, 4, '2023-11-01', '2023-11-16', '2023-11-15'),
(7, 5, '2023-12-01', '2023-12-16', NULL),
(7, 6, '2024-01-05', '2024-01-20', NULL);
 