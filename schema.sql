drop table if exists received;
create table received (
    id integer primary key autoincrement,
    to_email text not null,
    from_email text not null,
    subject text not null,
    content text not null,
    date_str text not null,
    password text
);

drop table if exists sent;
create table sent (
    id integer primary key autoincrement,
    to_email text not null,
    from_email text not null,
    title text not null,
    content text not null,
    date_str text not null,
    password text
);

drop table if exists users;
create table users (
    id integer primary key autoincrement,
    user_name text not null,
    password text not null,
    email text not null
);
