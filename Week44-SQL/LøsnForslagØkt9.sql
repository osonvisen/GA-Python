/*
LØSNINGSFORSLAG

Oppgave 1
a) Gjentas to ganger: StudentName og CourseName
Emma tar to kurs, derfor dukker hun opp to ganger.
Python basics dukker opp to ganger fordi to studenter tar kurset.
Hvorfor? Primærnøkkelen består av to kolonner, men StudentName er bare avhengig av StudentId,
og CourseName er bare avhengig av CourseId.
Hva kan gå galt?
Navn må endres i alle rader der f.eks. Emma Olsen står. Glemmer vi en eller flere kolonner, så
vet vi ikke på et senere tidspunkt hvilket navn som er riktig.
Vi har en sammensatt primærnøkkel. Det betyr at når vi registrerer en ny student, må denne studenten
også ha et kurs. Slutter studenten på kurset, må hele linjen slettes, og vi har ingen historikk.

b)
Tabell1: Student
Columns:
StuentId        PRIMARY KEY
StudentName

Tabell2: Course
CourseId        PRIMARY KEY
CourseName

Tabell3: Enrollment
StudentId       PRIMARY KEY FOREIGN KEY
CourseId        PRIMARY KEY FOREIGN KEY

c)
Vi endrer nå navnet til studentene kun i tabellen Student. Navnet står bare på ett sted, så alle
påmeldinger endres automatisk.
Vi registerer en student på et kurs i tabellen Enrollment.

Kommandoene:
UPDATE Student SET StudentName = "Emma Berg"
WHERE StudentId = 1;

INSERT INTO Enrollment(StudentId, CourseId) VALUES
(2, 102);

INSERT INTO Student(StudentId, StudentName) VALUES
(3, 'Henrik Ibsen');

INSERT INTO Enrollment(StudentId, CourseId) VALUES
(3, 101);


Oppgave 2
a)
create user 'country_reader'@'%' identified by 'HemmeligPassord1!';

grant select on world.country to 'country_reader'@'%';

show grants for 'country_reader'@'%';

b)
Bruk +-tegnet til å opprette en ny forbindelse. Velg world under fanen schemas,
og bruk brukernavn og passord til den nye brukeren. Test forbindelsen før du trykker OK.
Kontrollert innloggingen med SELECT CURRENT_USER();

c)
Kjørt begge kommandoene,SELECT * FROM world.country; og SELECT * FROM world.city;
og bare den første fungerte.
Hvorfor?
Fordi vi har satt rettighetene for denne brukeren til bare country, og ikke til city.
*/

