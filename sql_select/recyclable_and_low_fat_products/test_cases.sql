-- Write your test queries here
-- Example 1

-- Input: Products table
CREATE TABLE Products (
    product_id INT,
    low_fats CHAR(1),
    recyclable CHAR(1)
);

INSERT INTO Products (product_id, low_fats, recyclable) VALUES
(0, 'Y', 'N'),
(1, 'Y', 'Y'),
(2, 'N', 'Y'),
(3, 'Y', 'Y'),
(4, 'N', 'N');

-- Query: Fetch product_id where low_fats = 'Y' and recyclable = 'Y'
SELECT product_id
FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y';

-- Expected Output:
-- +-------------+
-- | product_id  |
-- +-------------+
-- | 1           |
-- | 3           |
-- +-------------+
