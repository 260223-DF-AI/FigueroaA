USERS
|user_id(PK)|user_fname|user_lname|phone_num|email|city|state|
|---|---|---|---|---|---|---|
| 1           | dylan      | parrot    | 5948831704  | no@gmail.com | Chicago|   IL  |

TRANSACTIONS
| tranc_id | user_id(FK) | trans_date | location | trans_total |
|---|---|---|---|---|
1 | 1 | 2020-03-19 | Chicago, IL | $59.99

```sql
IF NOT EXISTS (SELECT 1 FROM USERS WHERE user_id = <incoming_user_id>)
BEGIN
    INSERT INTO USERS (user_fname, user_lname, phone_num, email, city, state)
    VALUE
END

tmp_user_id = SELECT user_id FROM USERS WHERE user = incoming_user

INSERT INTO TRANSACTIONS (trans_id, user_id, trans_date, location, trans_total)
VALUES ()
```