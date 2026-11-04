drop database if exists human_body;
create database if not exists human_body;

use human_body;

create table hand (
    id          int             auto_increment primary key,
    finger      varchar(12)     not null default 'finger',
    what_hand   enum('høyre', 'venstre')      not null
);

insert into hand (finger, what_hand)
values
    ('Tommel', 'høyre'),
    ('Pekefinger', 'høyre'),
    ('Langfinger', 'høyre'),
    ('Ringfinger', 'høyre'),
    ('Lillefinger', 'høyre');

create table foot (
    id          int             auto_increment primary key,
    toes        varchar(12)     not null
);

insert into foot (toes)
values
    ('Stortå');

