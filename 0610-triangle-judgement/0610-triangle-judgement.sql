# Write your MySQL query statement below
select x,y,z,
    case
        when abs(x)+abs(y)>abs(z) and abs(z)+abs(y)>abs(x) and abs(x)+abs(z)>abs(y) then "Yes"
        else "No"
    end as triangle
from Triangle