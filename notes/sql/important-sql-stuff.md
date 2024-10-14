---
layout: page
title: SQL stuff to remember
---
### count(*) vs count(id)
- **Use `COUNT(*)`**: When you want to count **all rows**, regardless of whether columns contain `NULL` values. Since `emp_id` is typically a primary key (or not `NULL`), `COUNT(*)` and `COUNT(emp_id)` will generally give the same result in this scenario.
    
- **Use `COUNT(emp_id)`**: If you specifically want to count non-`NULL` values in the `emp_id` column. This could be useful if `emp_id` is nullable (which is rare) or if you’re counting a different nullable column.

### where vs having
- use `HAVING` to filter after aggregation
- use `GROUP BY` to filter before aggregation

