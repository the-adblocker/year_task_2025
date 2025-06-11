-- mydb = mysql.connector.connect(
--     host="localhost",
--     user="root",
--     password="",
--     port="3307"
-- )

-- mycursor = mydb.cursor()


CREATE DATABASE bank;

USE bank;

CREATE TABLE account IF NOT EXISTS(
    id int NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    adress VARCHAR(255),
    phonenr CHAR(8),
    mail VARCHAR(255),
    pass VARCHAR(255),
    PRIMARY KEY (id)
);


CREATE TABLE game IF NOT EXISTS(
    game_id int NOT NULL AUTO_INCREMENT,
    game_name VARCHAR(255),
    game_desc VARCHAR(255),
    game_img VARCHAR(255),
    PRIMARY KEY (id)
);


CREATE TABLE scores IF NOT EXISTS(
    score_id int NOT NULL AUTO_INCREMENT,
    score int(10),
    current_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    constraint fk_account
    foreign key(account)
        references account(id)
);





-- first
CrEATE TABLE art (
    id int NOT NULL AUTO_INCREMENT,
    artsnavn VARCHAR(255),
    primary key (id)
)

-- then
CrEATE TABLE busk (
    id int NOT NULL AUTO_INCREMENT,
    busknavn VARCHAR(255),
    art int,
    primary key (id),
    constraint fk_art
    foreign key(art)
        references art(id)
)

insert into art (artsnavn) values ("furu");
insert into art (busknavn, art) values ("tre", 0);


SELECT artsnavn, busknavn From busknavn
Inner Join art On busk.art = art.id;