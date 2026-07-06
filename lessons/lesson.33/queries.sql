select version();

select *
from generate_series(1, 10) as idx, floor(random() * 100) as rnd;



insert into "users" (username, email, full_name)
select
      'user_' || rnd || '_' || idx
    , 'user_' || rnd || '_' || idx || '@example.com'
    , 'User Name ' || rnd || ' ' || idx
from generate_series(1, 1000) as idx, floor(random() * 100) as rnd;
