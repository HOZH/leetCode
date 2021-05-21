--
-- @lc app=leetcode id=1179 lang=mysql
--
-- [1179] Reformat Department Table
--

-- @lc code=start
# Write your MySQL query statement below
Select
ID
, sum(Case When Month = 'Jan' Then Revenue End) as Jan_Revenue
, sum(Case When Month = 'Feb' Then Revenue End) as Feb_Revenue
, sum(Case When Month = 'Mar' Then Revenue End) as Mar_Revenue
, sum(Case When Month = 'Apr' Then Revenue End) as Apr_Revenue
, sum(Case When Month = 'May' Then Revenue End) as May_Revenue
, sum(Case When Month = 'Jun' Then Revenue End) as Jun_Revenue
, sum(Case When Month = 'Jul' Then Revenue End) as Jul_Revenue
, sum(Case When Month = 'Aug' Then Revenue End) as Aug_Revenue
, sum(Case When Month = 'Sep' Then Revenue End) as Sep_Revenue
, sum(Case When Month = 'Oct' Then Revenue End) as Oct_Revenue
, sum(Case When Month = 'Nov' Then Revenue End) as Nov_Revenue
, sum(Case When Month = 'Dec' Then Revenue End) as Dec_Revenue
From Department
Group By ID

-- @lc code=end

