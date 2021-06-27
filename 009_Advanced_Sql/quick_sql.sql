-- using rank with order
select rank() over(order by name desc) as name_rank,*
 from mytable-- order by Name desc
---------------------------------------------------------------------------------------------------------------------------
-- using rank with order and filter the middle
with result as
(
select rank() over(order by name desc) as name_rank,*
 from mytable-- order by Name desc
) select * from result where name_rank between 10 and 15
---------------------------------------------------------------------------------------------------------------------------
-- Diff b/w rank and dense rank
Original data  100, 100, 100, 99, 98, 98, 97, 90
Rank             1,    1,   1,  4,  5,  5, 6,  7
Dense_rank       1,    1,   1,   2, 3,  3, 4,  5
Percent_rank     
Row num          1,    2,   3,   4,  5, 6, 7, 8
---------------------------------------------------------------------------------------------------------------------------
-- Row number
select row_number() over(order by name desc) as name_row,
*
 from mytable

-- Partition
-- Partition will first order the result by typeid, and then it will order by the name and assign rank
--e.g
OriginalData    (1, 100), (1, 100), (2, 90), (2, 85), (2, 75), (3, 100), (33, 95) --(type id, name)
Rank                   1,        1,       1,      2,        3,        1,      2
select row_number() over( partition by typeid order by name desc) as name_row,
*
 from mytable-- order by Name desc
 
 ---------------------------------------------------------------------------------------------------------------------------
 ---Aggregate function with group by
 --original data -  (1,100), (2, 90), (3, 100), (4, 90), (5, 90) - (id, value)
 --Group by value
  --group 1 (100) - (1, 100), (3, 100)
  --grup 2  (90)  - (2, 90), (4, 90), (5, 90)
  select value,
  count(1),
  sum(id),
  sum(value),
  avg(value)
  from mytable
  group by value
  
  --this  above query will give the result as
100  2  4    200  100
90   3  11   270  90
  
---------------------------------------------------------------------------------------------------------------------------  
  
