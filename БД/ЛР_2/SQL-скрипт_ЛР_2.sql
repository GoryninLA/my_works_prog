CREATE TABLE Authors 
    ( 
     author_id    INTEGER  NOT NULL , 
     first_name   VARCHAR (50)  NOT NULL , 
     last_name    VARCHAR (50)  NOT NULL , 
     birth_date   DATE , 
     nathionality VARCHAR (20) 
    ) 
;

ALTER TABLE Authors 
    ADD CONSTRAINT Authors_PK PRIMARY KEY ( author_id ) ;

CREATE TABLE BookCopies 
    ( 
     copy_id          INTEGER  NOT NULL , 
     book_id          INTEGER  NOT NULL , 
     inventory_number VARCHAR (20)  NOT NULL , 
     status           VARCHAR (20) , 
     acquisition_date DATE , 
     candition        VARCHAR (50) , 
     reader_id        INTEGER  NOT NULL , 
     loan_date        DATE  NOT NULL , 
     due_date         DATE  NOT NULL , 
     return_date      DATE , 
     Books_book_id    INTEGER  NOT NULL 
    ) 
;

ALTER TABLE BookCopies 
    ADD CONSTRAINT BookCopies_PK PRIMARY KEY ( copy_id, book_id ) ;

CREATE TABLE Books 
    ( 
     book_id                 INTEGER  NOT NULL , 
     author_id               INTEGER  NOT NULL , 
     title                   VARCHAR (100)  NOT NULL , 
     publication_year        INTEGER  NOT NULL , 
     gener_id                INTEGER  NOT NULL , 
     publisher_id            INTEGER , 
     Authors_author_id       INTEGER  NOT NULL , 
     Genres_gener_id         INTEGER  NOT NULL , 
     Publishers_publisher_id INTEGER  NOT NULL 
    ) 
;

ALTER TABLE Books 
    ADD CONSTRAINT Books_PK PRIMARY KEY ( book_id ) ;

CREATE TABLE Genres 
    ( 
     gener_id    INTEGER  NOT NULL , 
     gener_name  VARCHAR (50)  NOT NULL , 
     description TEXT 
    ) 
;

ALTER TABLE Genres 
    ADD CONSTRAINT Genres_PK PRIMARY KEY ( gener_id ) ;

CREATE TABLE Publishers 
    ( 
     publisher_id   INTEGER  NOT NULL , 
     publisher_nmae VARCHAR (100) , 
     country        VARCHAR (50) , 
     founded_year   INTEGER 
    ) 
;

ALTER TABLE Publishers 
    ADD CONSTRAINT Publishers_PK PRIMARY KEY ( publisher_id ) ;

CREATE TABLE Readers 
    ( 
     reader_id          INTEGER  NOT NULL , 
     first_name         VARCHAR (50)  NOT NULL , 
     last_name          VARCHAR (50)  NOT NULL , 
     email              VARCHAR (100)  NOT NULL , 
     registration_date  DATE  NOT NULL , 
     phone              VARCHAR (20) , 
     BookCopies_copy_id INTEGER  NOT NULL , 
     BookCopies_book_id INTEGER  NOT NULL 
    ) 
;

ALTER TABLE Readers 
    ADD CONSTRAINT Readers_PK PRIMARY KEY ( reader_id ) ;

ALTER TABLE BookCopies 
    ADD CONSTRAINT BookCopies_Books_FK FOREIGN KEY 
    ( 
     Books_book_id
    ) 
    REFERENCES Books 
    ( 
     book_id
    ) 
;

ALTER TABLE Books 
    ADD CONSTRAINT Books_Authors_FK FOREIGN KEY 
    ( 
     Authors_author_id
    ) 
    REFERENCES Authors 
    ( 
     author_id
    ) 
;

ALTER TABLE Books 
    ADD CONSTRAINT Books_Genres_FK FOREIGN KEY 
    ( 
     Genres_gener_id
    ) 
    REFERENCES Genres 
    ( 
     gener_id
    ) 
;

ALTER TABLE Books 
    ADD CONSTRAINT Books_Publishers_FK FOREIGN KEY 
    ( 
     Publishers_publisher_id
    ) 
    REFERENCES Publishers 
    ( 
     publisher_id
    ) 
;

ALTER TABLE Readers 
    ADD CONSTRAINT Readers_BookCopies_FK FOREIGN KEY 
    ( 
     BookCopies_copy_id,
     BookCopies_book_id
    ) 
    REFERENCES BookCopies 
    ( 
     copy_id,
     book_id
    ) 
;
