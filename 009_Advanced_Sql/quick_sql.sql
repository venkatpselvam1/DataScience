-- using rank with order
select rank() over(order by name desc) as name_rank,*
 from deviceProfile.DeviceProfile-- order by Name desc

-- using rank with order and filter the middle
with result as
(
select rank() over(order by name desc) as name_rank,*
 from deviceProfile.DeviceProfile-- order by Name desc
) select * from result where name_rank between 10 and 15
