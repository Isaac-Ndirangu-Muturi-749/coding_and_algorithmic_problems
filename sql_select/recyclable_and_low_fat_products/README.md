To find the `product_id` of products that are both low fat and recyclable, we can use a simple SQL `SELECT` statement with a `WHERE` clause to filter rows where both `low_fats` and `recyclable` are `'Y'`.

### SQL Query:

```sql
SELECT product_id
FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y';
```

### Explanation:
- We select the `product_id` from the `Products` table.
- The `WHERE` clause ensures that we only get products where both the `low_fats` column is `'Y'` (indicating low fat) and the `recyclable` column is `'Y'` (indicating the product is recyclable).

### Example Output:
For the given input:

| product_id  | low_fats | recyclable |
|-------------|----------|------------|
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |

The query will return:

| product_id  |
|-------------|
| 1           |
| 3           |
