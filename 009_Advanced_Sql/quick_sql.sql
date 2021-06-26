-- using rank with order
select rank() over(order by name desc) as name_rank,*
 from mytable-- order by Name desc

-- using rank with order and filter the middle
with result as
(
select rank() over(order by name desc) as name_rank,*
 from mytable-- order by Name desc
) select * from result where name_rank between 10 and 15

-- Diff b/w rank and dense rank
Original data  100, 100, 100, 99, 98, 98, 97, 90
Rank             1,    1,   1,  4,  5,  5, 6,  7
Dense_rank       1,    1,   1,   2, 3,  3, 4,  5
Percent_rank     
Row num          1,    2,   3,   4,  5, 6, 7, 8

-- Row number
select row_number() over(order by name desc) as name_row,
*
 from mytable

