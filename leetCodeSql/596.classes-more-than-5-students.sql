--
-- @lc app=leetcode id=596 lang=mysql
--
-- [596] Classes More Than 5 Students
--

-- @lc code=start
# Write your MySQL query statement below
select class from (select count(distinct student) as c,class from courses group by class) as temp where c>=5;


-- @lc code=end

