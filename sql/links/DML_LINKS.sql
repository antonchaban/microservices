delete
from LINKS
where user_id in (select id from USERS where username in ('root', 'Kolya_SP'));

insert into LINKS(code, url, user_id, expires_stamp)
select 'rootLinkOne', 'https://google.com', id, null
from USERS
where username = 'root';

insert into LINKS(code, url, user_id, expires_stamp)
select 'rootLinkTwo', 'https://google.com', id, current_timestamp + interval '1 week'
from USERS
where username = 'root';

insert into LINKS(code, url, user_id, expires_stamp)
select 'kolyaLinkOne', 'https://google.com', id, null
from USERS
where username = 'Kolya_SP';

insert into LINKS(code, url, user_id, expires_stamp)
select 'kolyaLinkTwo', 'https://google.com', id, current_timestamp + interval '1 week'
from USERS
where username = 'Kolya_SP';