/*
Enter your query here.
*/

select min(start_date) max_start_date, 
       max(end_date) max_end_date 
from (
    select 
        start_date, 
        end_date, 
        sum(end_ind) over (order by start_date) as grp 
    from (
        select 
            start_date, 
            end_date, 
            prv_end_date, 
            case when (end_date -  prv_end_date = 1) then 0 else 1 end as end_ind  
        from (
            select  
                start_date, 
                end_date, 
                lag(end_date) over (order by start_date) as prv_end_date 
            from projects
                order by start_date
            ) t1 
        ) t2
        order by start_date
    ) t3
group by grp
order by max_end_date - max_start_date,  min(start_date)