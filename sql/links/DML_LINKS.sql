delete
from LINKS
where user_id in (select id from USERS where username in ('root', 'Kolya_SP'));

insert into LINKS(code, user_id, expires_stamp)
select 'rootLinkOne', id, null
from USERS
where username = 'root';

insert into LINKS(code, user_id, expires_stamp)
select 'rootLinkTwo', id, current_timestamp + interval '1 week'
from USERS
where username = 'root';

insert into LINKS(code, user_id, expires_stamp)
select 'kolyaLinkOne', id, null
from USERS
where username = 'Kolya_SP';

insert into LINKS(code, user_id, expires_stamp)
select 'kolyaLinkTwo', id, current_timestamp + interval '1 week'
from USERS
where username = 'Kolya_SP';