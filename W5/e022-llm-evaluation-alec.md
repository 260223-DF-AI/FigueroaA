## Task 1.1

Microsoft Copilot:

| Criterion | Score (1-5) | Notes |
| --------- | ----------- | ----- |
| Syntax correctness (valid BigQuery SQL) | 5 | The SQL syntax looks complex but functional |
| Window function usage (correct frame clause) | 5 | Uses 6 preceeding syntax|
| Rolling average logic (correct 7-day calculation) | 5 | Uses AVG and not SUM|
| Column references match the provided schema | 5 | The columns are correct |
| Overall: would this query run correctly? | 5 | This code looks like it will run, and the llm predicts missing dates  |



| Criterion | Score (1-5) | Notes |
| --------- | ----------- | ----- |
| Syntax correctness (valid BigQuery SQL) | 5 | Exact same code as Copilot |
| Window function usage (correct frame clause) | 5 | Exact same code as Copilot |
| Rolling average logic (correct 7-day calculation) | 5 | Exact same code as Copilot |
| Column references match the provided schema | 5 | Exact same code as Copilot |
| Overall: would this query run correctly? | 5 | Exact same code as Copilot |

### Task 1.2: Fact Check

| Statement from LLM | Verified? (Yes/No/Unsure) | Source Used to Verify |
| BQ stores data in a columnar format (Capacitor), inspired by the Dremel paper and similar in concept (but not identical) to Parquet or ORC | Yes |  Google Cloud Blog |
| BQ flattens nested data into Repetition and Definition levels | Yes | Google Cloud Blog
## Ratings for LLMs

| Category | Score (1-10) | Justification |
| -------- | ------------ | ------------- |
| SQL generation accuracy | | |
| Factual reliability | | |
| Hallucination frequency | | |
| Safety and boundaries | | |
| Response to constraints | | |
| Overall usefulness for data engineering | | |