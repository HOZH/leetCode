--
-- @lc app=leetcode id=620 lang=mysql
--
-- [620] Not Boring Movies
--

-- @lc code=start
# Write your MySQL query statement below
select id,movie,description,rating from cinema where id%2<>0 and description<>'boring' order by rating  DESC
-- @lc code=end

