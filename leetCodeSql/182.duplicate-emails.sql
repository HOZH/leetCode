--
-- @lc app=leetcode id=182 lang=mysql
--
-- [182] Duplicate Emails
--

-- @lc code=start
# Write your MySQL query statement below
select Email from (select Email,count(Email) as c from person group by Email) as temp where c>1;



-- @lc code=end

