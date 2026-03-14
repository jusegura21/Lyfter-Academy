CREATE TABLE lyfter_car_rental.users (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    birth_date DATE NOT NULL,
    account_status BOOLEAN NOT NULL DEFAULT TRUE
)

INSERT INTO lyfter_car_rental.users
(name, username, password, email, birth_date, account_status) VALUES
('name1','user1','pass1','user1@email.com','1990-01-01',TRUE),
('name2','user2','pass2','user2@email.com','1991-02-02',FALSE),
('name3','user3','pass3','user3@email.com','1992-03-03',TRUE),
('name4','user4','pass4','user4@email.com','1993-04-04',FALSE),
('name5','user5','pass5','user5@email.com','1994-05-05',TRUE),
('name6','user6','pass6','user6@email.com','1995-06-06',TRUE),
('name7','user7','pass7','user7@email.com','1996-07-07',FALSE),
('name8','user8','pass8','user8@email.com','1997-08-08',TRUE),
('name9','user9','pass9','user9@email.com','1998-09-09',FALSE),
('name10','user10','pass10','user10@email.com','1999-10-10',TRUE),
('name11','user11','pass11','user11@email.com','1990-11-11',FALSE),
('name12','user12','pass12','user12@email.com','1991-12-12',TRUE),
('name13','user13','pass13','user13@email.com','1992-01-13',TRUE),
('name14','user14','pass14','user14@email.com','1993-02-14',FALSE),
('name15','user15','pass15','user15@email.com','1994-03-15',TRUE),
('name16','user16','pass16','user16@email.com','1995-04-16',FALSE),
('name17','user17','pass17','user17@email.com','1996-05-17',TRUE),
('name18','user18','pass18','user18@email.com','1997-06-18',TRUE),
('name19','user19','pass19','user19@email.com','1998-07-19',FALSE),
('name20','user20','pass20','user20@email.com','1999-08-20',TRUE),
('name21','user21','pass21','user21@email.com','1990-09-21',FALSE),
('name22','user22','pass22','user22@email.com','1991-10-22',TRUE),
('name23','user23','pass23','user23@email.com','1992-11-23',TRUE),
('name24','user24','pass24','user24@email.com','1993-12-24',FALSE),
('name25','user25','pass25','user25@email.com','1994-01-25',TRUE),
('name26','user26','pass26','user26@email.com','1995-02-26',FALSE),
('name27','user27','pass27','user27@email.com','1996-03-27',TRUE),
('name28','user28','pass28','user28@email.com','1997-04-28',TRUE),
('name29','user29','pass29','user29@email.com','1998-05-29',FALSE),
('name30','user30','pass30','user30@email.com','1999-06-30',TRUE),
('name31','user31','pass31','user31@email.com','1990-07-01',FALSE),
('name32','user32','pass32','user32@email.com','1991-08-02',TRUE),
('name33','user33','pass33','user33@email.com','1992-09-03',TRUE),
('name34','user34','pass34','user34@email.com','1993-10-04',FALSE),
('name35','user35','pass35','user35@email.com','1994-11-05',TRUE),
('name36','user36','pass36','user36@email.com','1995-12-06',FALSE),
('name37','user37','pass37','user37@email.com','1996-01-07',TRUE),
('name38','user38','pass38','user38@email.com','1997-02-08',TRUE),
('name39','user39','pass39','user39@email.com','1998-03-09',FALSE),
('name40','user40','pass40','user40@email.com','1999-04-10',TRUE),
('name41','user41','pass41','user41@email.com','1990-05-11',FALSE),
('name42','user42','pass42','user42@email.com','1991-06-12',TRUE),
('name43','user43','pass43','user43@email.com','1992-07-13',TRUE),
('name44','user44','pass44','user44@email.com','1993-08-14',FALSE),
('name45','user45','pass45','user45@email.com','1994-09-15',TRUE),
('name46','user46','pass46','user46@email.com','1995-10-16',TRUE),
('name47','user47','pass47','user47@email.com','1996-11-17',FALSE),
('name48','user48','pass48','user48@email.com','1997-12-18',TRUE),
('name49','user49','pass49','user49@email.com','1998-01-19',FALSE),
('name50','user50','pass50','user50@email.com','1999-02-20',TRUE)


CREATE TABLE lyfter_car_rental.cars (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    brand VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    mfg_year INTEGER NOT NULL,
    car_status BOOLEAN NOT NULL);

INSERT INTO lyfter_car_rental.cars
(brand, model, manufacture_year, car_status) VALUES
('Toyota','Corolla',2018,true),
('Honda','Civic',2019,true),
('Ford','Focus',2017,false),
('Chevrolet','Cruze',2020,true),
('Nissan','Sentra',2018,true),
('Hyundai','Elantra',2021,true),
('Kia','Rio',2019,false),
('Mazda','Mazda3',2020,true),
('Volkswagen','Jetta',2017,true),
('Subaru','Impreza',2018,false),
('Toyota','Camry',2021,true),
('Honda','Accord',2020,true),
('Ford','Fusion',2019,false),
('Chevrolet','Malibu',2018,true),
('Nissan','Altima',2021,true),
('Hyundai','Sonata',2020,false),
('Kia','Optima',2019,true),
('Mazda','CX5',2021,true),
('Volkswagen','Passat',2017,false),
('Subaru','Legacy',2018,true),
('Toyota','RAV4',2022,true),
('Honda','CRV',2021,false),
('Ford','Escape',2020,true),
('Chevrolet','Equinox',2019,true),
('Nissan','Rogue',2022,false),
('Hyundai','Tucson',2021,true),
('Kia','Sportage',2020,true),
('Mazda','CX30',2022,false),
('Volkswagen','Tiguan',2019,true),
('Subaru','Forester',2021,true),
('Toyota','Yaris',2017,false),
('Honda','Fit',2018,true),
('Ford','Fiesta',2017,true),
('Chevrolet','Spark',2019,false),
('Nissan','Versa',2020,true),
('Hyundai','Accent',2018,true),
('Kia','Soul',2019,false),
('Mazda','Mazda2',2017,true),
('Volkswagen','Polo',2018,true),
('Subaru','XV',2020,false),
('Toyota','Highlander',2022,true),
('Honda','Pilot',2021,true),
('Ford','Explorer',2020,false),
('Chevrolet','Traverse',2019,true),
('Nissan','Pathfinder',2022,true),
('Hyundai','SantaFe',2021,false),
('Kia','Sorento',2020,true),
('Mazda','CX9',2021,true),
('Volkswagen','Atlas',2019,false),
('Subaru','Outback',2022,true);

CREATE TABLE lyfter_car_rental.rentals
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
    rental_date date NOT NULL DEFAULT CURRENT_DATE,
    rental_status boolean NOT NULL DEFAULT TRUE,
    car_id integer NOT NULL,
    user_id integer NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_car_id FOREIGN KEY (car_id)
        REFERENCES lyfter_car_rental.cars (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT fk_user_id FOREIGN KEY (user_id)
        REFERENCES lyfter_car_rental.users (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
);

ALTER TABLE IF EXISTS lyfter_car_rental.rentals
    OWNER to postgres;

INSERT INTO lyfter_car_rental.users (name, username,password,email,birth_date,account_status)
VALUES ('Julian', 'juli21','galletas','juli21sefa@gmail.com','1996-03-21',TRUE);

INSERT INTO lyfter_car_rental.cars (brand, model, mfg_year, car_status)
VALUES ('Audi', 'Q5', 2014 ,TRUE);

UPDATE users
SET account_status=FALSE WHERE id=51;

UPDATE lyfter_car_rental.cars
SET car_status=FALSE WHERE id=1;

INSERT INTO lyfter_car_rental.rentals (car_id,user_id) VALUES (1,51);

//devolucion
UPDATE lyfter_car_rental.rentals
SET rental_status=FALSE 
WHERE id = 1 ;

UPDATE lyfter_car_rental.cars
SET car_status =TRUE 
WHERE id= (SELECT car_id FROM lyfter_car_rental.rentals WHERE id=1);
// 
//carros alquilados y disponibles
SELECT * FROM lyfter_car_rental.rentals
WHERE rental_status=TRUE

SELECT id FROM lyfter_car_rental.cars
WHERE car_status=TRUE ;
