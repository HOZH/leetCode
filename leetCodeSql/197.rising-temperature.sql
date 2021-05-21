--
-- @lc app=leetcode id=197 lang=mysql
--
-- [197] Rising Temperature
--

-- @lc code=start
# Write your MySQL query statement below
select weather.id As 'Id' from weather join weather w on DATEDIFF(weather.recordDate, w.recordDate) = 1 and weather.Temperature > w. Temperature; 

-- @lc code=end

