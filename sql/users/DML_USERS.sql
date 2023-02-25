delete from USERS where username in ('root', 'Kolya_SP');

insert into USERS (username, password)
values ('root', '{bcrypt}$2a$10$Zam0u6RYgvyRfPuvm4d.HOyRSeYpvzPbBdTazI85/Ad4uVNcJV74e'), -- [root] bcrypt 10 rounds
       ('Kolya_SP', '{bcrypt}$2a$10$lGAtN/0sT6qyzvWB0xIZ1OUpO0q2V9slGy.SIDEnUn5096Y3FC57a'); -- [Kolya_SP] bcrypt 10 rounds