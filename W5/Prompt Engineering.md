## Challenge 1.1: SQL Generation

Prompt 1:

"Generate BigQuery sql query to find the top 5 departments by average salary, and include the department name, average salary, and employee count. Only include departments with more than 10 employees and order by average salary descending"

Response outputs valid BigQuery sql code:

```
SELECT
  d.department_name,
  AVG(e.salary) AS average_salary,
  COUNT(e.employee_id) AS employee_count
FROM
  `your_dataset.employees` e
JOIN
  `your_dataset.departments` d
ON
  e.department_id = d.department_id
GROUP BY
  d.department_name
HAVING
  COUNT(e.employee_id) > 10
ORDER BY
  average_salary DESC
LIMIT 5;
```

## Challenge 1.2: Error Explanation

Prompt:

```
Please explain this error message in plain English and suggest a fix:
google.api_core.exceptions.BadRequest: 400 Syntax error: 
Expected end of input but got keyword SELECT at [3:1]
```

Response:

The Response mentions how a syntax error could be caused by missing semicolons, commas, and Paranthesis in a WITH clause in sql, as well as an extra SELECT keyword somewhere.

It also provides an example of a missing semi-colon at line 4 after a SELECT * FROM employees line. 

Evaluation:

However, from reports of this error asked from users on Stackoverflow, the error can also come from things like trying to merge a BigQuery dataframe with a pandas dataframe. Since it doesn't list an example like this I would rate the quality of the fix suggestion as a 4.

## Challenge 1.3: Data Dictionary Entry

Prompt:

```
Generate a data dictioary for a column 'customer_lifetime_value' in the 'dim_customer' table. The entry should include data, type, description, business definition, calucaltion method, and example values
```

Response:

The response is a little bit verbose, and provides mathematical formulas for calculating the Customer Lifetime Value. If the new team member can grasp the notation and logic of the formula, this can be seen as a good response.

Evaluation: The response has an example of the Customer Lifetime Value already generated, but the dictionary entry was prompted to include data type, description, business definition, and caluclation method. These values are not in the example table, but instead as part of the prompt where AI just talks about it.

I rate the response a 3 / 5

## Part 2 Few-Shot Prompting

### Challenge 2.1 Column Name Standardization

Microsoft Copolit was successfully able to convert the provided strings into snake case format. It did differ from Gemini with the `ShippingAddress Line1` example. Gemini provided `shipping_address_line1`, where Microsoft Copilot provided `shipping_address_line_1`, they provided different results probably because they were trained on different datasets where this distinction occurs.

### Challenge 2-2: SQL to Documentation

Prompt:

```
Use the following sql as an input example: SELECT customer_id, COUNT(*) as order_count 
FROM orders GROUP BY customer_id
Document the output like this: 

Query: Customer Order Count
Purpose: Counts the total number of orders per customer
Tables Used: orders
Output Columns: customer_id, order_count
Aggregation: COUNT grouped by customer_id

Using the above format, provide documentation on the following sql query:
SELECT p.category, 
       DATE_TRUNC(o.order_date, MONTH) as month,
       SUM(o.quantity * p.unit_price) as revenue,
       COUNT(DISTINCT o.customer_id) as unique_customers
FROM orders o
JOIN products p ON o.product_id = p.product_id
WHERE o.order_date >= '2024-01-01'
GROUP BY 1, 2
ORDER BY 1, 2
```

Response:

```
Query: Category‑Level Monthly Revenue & Unique Customer Count
Purpose: Calculates total monthly revenue and number of distinct customers for each product category
Tables Used: orders, products
Output Columns: category, month, revenue, unique_customers
Aggregation:

 - SUM(o.quantity * p.unit_price) grouped by category and month

 - COUNT(DISTINCT o.customer_id) grouped by category and month
```
Microsoft Copilot used the documentation format precisely and accurately.

##Challengeg 3.1: Cost Estimation

```
Think through this step by step:
I have a table of 500 million rows, where each row is approxiamtely 500 bytes.
Run a query that scans 3 columns out of the 20 total columns.
The query runs 4 times a day.
BigQuery charges $6.25 per TB scanned.
Assume columnar storage distributes data evenly across columns
How much per day will it cost me to use BigQuery on this table?
```

Response:

```
Let’s walk it through with the numbers you gave.

1. **Total table size**

- **Rows:** 500,000,000  
- **Row size:** 500 bytes  


500,000,000 times 500 = 250,000,000,000 bytes approx 250 GB


2. **Per-column size (20 columns, evenly distributed)**


250 GB / 20 = 12.5 GB per column


3. **Data scanned per query (3 columns)**


3 12.5 GB = 37.5 GB per query


4. **Data scanned per day (4 queries per day)**


37.5 GB times 4 = 150 GB per day


5. **Cost per day**

BigQuery: $6.25 per TB scanned. Take 1 TB ≈ 1024 GB:

Cost per GB ~ 6.25/1024 ~ 0.0061

Daily cost ~ 150 * 0.0061 ~ $0.92 per day

**Answer:** It will cost you roughly $0.90–$0.95 per day in BigQuery scan costs.
```
The model goes through eaach calculation step by step, making it easy to follow where it gets its numbers from.

The finaly answer is reasonable at ~92 cents per day. It is also concise, and lists out each step, improving readability. This is a 5/5 response

### Challenge 3.2 Pipeline Debugging

Prompt:

```
Consider this scenario:
An ETL pipline extracts data from  REST API, then transforms it with Python, and then load it into BigQuery.
The pipeline ran successfully for 30 days, and then started failing with this error:
google.api_core.exceptions.Forbidden: 403 Access Denied: 
BigQuery BigQuery: Permission bigquery.tables.create denied

Nothing in the pipeline code changed, and the GCP project and service account are the same.
Reason step by step on what the problems could be.
```



Response:
```
Here’s how I’d reason through this kind of failure—slowly, methodically, and with an eye for the subtle things that break long‑running pipelines even when “nothing changed.”

---

# 🧩 Step‑by‑Step Reasoning: Why a BigQuery Pipeline Suddenly Loses `bigquery.tables.create`

Below is a structured breakdown of the most likely causes, starting with the most common real‑world scenarios.

---

## 🔐 1. **The service account’s permissions changed indirectly**
Even if *you* didn’t change anything, permissions can change because:

### **a. IAM role was removed or modified by someone else**
- Another admin might have cleaned up roles.
- A security team may have enforced new least‑privilege policies.
- A custom role may have been edited and lost the `bigquery.tables.create` permission.

### **b. The service account was part of a group whose membership changed**
- If the service account inherited permissions through a Google Group, and the group was modified, permissions disappear instantly.

### **c. The service account was granted permissions via a project‑level role that was removed**
- For example, someone removed `BigQuery Admin` or `BigQuery Data Editor` from the project.

This is the **#1 cause** of sudden BigQuery permission failures.

---

## 🕒 2. **A temporary table or dataset creation pattern changed**
Your pipeline may have started creating tables where it didn’t before.

### Possible triggers:
- Schema drift in the API data → pipeline tries to create a new table.
- Partition expiration → BigQuery auto‑deleted a partitioned table, and now the pipeline tries to recreate it.
- A new date‑partition rolled over (e.g., monthly tables) → pipeline tries to create a new table for the first time in 30 days.

This explains why it worked for 30 days and then failed.

---

## 🗂️ 3. **Dataset‑level permissions were altered**
BigQuery permissions can be granted at:
- Project level
- Dataset level

If the dataset‑level ACL was changed:
- The service account may still have project‑level roles but **lost dataset‑level write access**.

This often happens when:
- Someone recreated the dataset.
- Someone applied a new dataset policy template.
- A Terraform/Deployment Manager job overwrote IAM bindings.

---

## 🧹 4. **A cleanup or automation job removed or replaced something**
Common culprits:
- A scheduled job deleted the dataset or table.
- A retention policy expired the table.
- A CI/CD pipeline reapplied infrastructure definitions that removed permissions.

If the pipeline only *appends* normally, but now must *create*, it will fail.

---

## 🔄 5. **The pipeline started running under a different identity**
Even if the code didn’t change, the runtime environment might have.

Examples:
- Cloud Composer / Cloud Run / Cloud Functions updated and now use a different default service account.
- A human changed the “Run as” service account in the UI.
- A new VM image or container changed the credentials path.

This is surprisingly common.

---

## 🔑 6. **Service account key expired or was rotated**
If you’re using a key file (not recommended), then:
- The key may have been revoked.
- A new key may have been created but not deployed.
- The key may now correspond to a different service account.

This can cause the pipeline to authenticate as a different identity with fewer permissions.

---

## 🧱 7. **BigQuery quotas or limits triggered a behavior change**
If a table reached a limit (e.g., partition count), BigQuery may require a new table to be created, which triggers the missing permission.

This is less common but still possible.

---

# 🧭 How to Diagnose Quickly

### 1. **Check which identity is actually making the request**
Look at the BigQuery audit logs:
- `principalEmail`
- `authenticationInfo`

If it’s not the expected service account, you’ve found your culprit.

### 2. **Check IAM for the service account**
Verify:
- Project‑level roles
- Dataset‑level roles
- Group memberships
- Custom role definitions

### 3. **Check whether the dataset or table was deleted or recreated**
Look at:
- Dataset audit logs
- Retention policies
- Terraform/infra deployment logs

### 4. **Check whether the pipeline started creating new tables**
Look at:
- Schema changes
- Partition boundaries
- Table naming logic

---

# 🎯 Most Likely Root Causes (Ranked)
1. **IAM role or dataset ACL changed** (intentional or accidental)
2. **Pipeline started needing to create a new table for the first time in 30 days**
3. **Service account identity changed due to environment changes**
4. **Dataset was recreated or overwritten**
5. **Key rotation or credential mismatch**

---

If you want, I can help you walk through a diagnostic checklist or interpret your audit logs.
```

The reasoning steps are logical, as it details possible causes for the error, ranging from permission roles being changed, to data limits being reached. The response is very verbose, so the prompt should try to constrain the explanations to a sentence or two if it needs a more clean response.

I'd give this response a 4/5. I learned that these types of prompts where the models tries to find many possible reasons for a problem should be constrained by a couple of sentences to keep the response from being messy and verbose.

### Challenge 4.1: Constrained Output

Prompt:

```
Write me a python function with the following elements:
1. The function name is 'validate_order_data'.
2. it takes in a parameter with type DataFrame from the pandas module
3. inside this parameter, check if there are any null values, negative amounts, future dats, and duplicate IDs
4. The function outputs a dinctionary with check results
5. maximum 30 lines of code
6. The function must include type hints
7. The function must have a docstring explaining what the function does
8. No external libraries beyond pandas and datetime

If there are explanations, please keep them concise.
```

Response:

```
Here’s a clean, compact implementation that fits your constraints while staying readable and practical:

python
from pandas import DataFrame
from datetime import datetime
from typing import Dict, Any

def validate_order_data(df: DataFrame) -> Dict[str, Any]:
    """
    Validate an order DataFrame for nulls, negative amounts,
    future dates, and duplicate IDs. Returns a dictionary
    summarizing validation results.
    """
    results: Dict[str, Any] = {}

    results["null_values"] = df.isnull().any().to_dict()

    if "amount" in df.columns:
        results["negative_amounts"] = (df["amount"] < 0).any()
    else:
        results["negative_amounts"] = None

    if "date" in df.columns:
        today = datetime.now().date()
        results["future_dates"] = (df["date"] > today).any()
    else:
        results["future_dates"] = None

    if "id" in df.columns:
        results["duplicate_ids"] = df["id"].duplicated().any()
    else:
        results["duplicate_ids"] = None

    return results
```

This model assumes the dataframe will have columns for null values, negative amounts, etc. But I want the columns to be actual logical data that is checked against those constraints. Null values should be a constrain, not a column. The prompt needs to be refined to illustrate this. As of now this is a 1/5 in quality.

## Reflection Questions
1. Chain-of-thought provided the best results for data engineering, besides my last prompt which needed to be revised and clarified.
2. The biggest impact was providing examples as the responses often made sense and aligned themselves to my expectations.
3. I would use zero-shot if I needed a general, non specific response to help guide me in the start of a brainstorming process. Few-shot when I need a little more specifics when brainstorming. Chain-of-thought is preferred when I am actually working on something complicated, and I need the model to follow my own thoughts and requirements.