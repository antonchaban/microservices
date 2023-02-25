drop table if exists LINKS;
drop table if exists USERS;

create table USERS
(
    id            serial primary key,
    username      varchar not null unique,
    password      varchar not null,
    created_stamp timestamp default current_timestamp
);