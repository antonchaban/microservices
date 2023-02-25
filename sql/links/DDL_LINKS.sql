drop table if exists LINKS;

create table LINKS
(
    id            serial primary key,
    code          varchar not null unique,
    user_id       integer not null references USERS (id),
    expires_stamp timestamp default null,
    created_stamp timestamp default current_timestamp
);