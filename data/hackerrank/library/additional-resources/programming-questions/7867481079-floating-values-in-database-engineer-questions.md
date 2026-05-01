---
title: "Floating Values in Database Engineer Questions"
title_slug: "floating-values-in-database-engineer-questions"
source_url: "https://support.hackerrank.com/articles/7867481079-floating-values-in-database-engineer-questions"
article_slug: "7867481079-floating-values-in-database-engineer-questions"
last_updated_exact: "Dec 13, 2024, 5:08 AM"
last_updated_relative: "Last updated 1 year ago"
breadcrumbs:
  - "Library"
  - "Additional Resources"
  - "Programming Questions"
---

# Floating Values in Database Engineer Questions

_Last updated: Dec 13, 2024, 5:08 AM (Last updated 1 year ago)_

## Overview

When you create a Database Engineer question, you can upload a CSV to create a table. Each of the database systems that are supported, handles floating-point values differently. This article provides you with an example to show how each database system handles the floating-point values. Currently, HackerRank supports Microsoft SQL, MySQL, Oracle, and DB2 databases.

## Floating Point Values Sample

The following example shows how different database systems handle the data. When creating a Database Engineer question, take into account that the queries return different results depending on the database system used, and scoring is done by basic string comparison.

![dbrank.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046693828-?Expires=253370764800&Signature=uHKe6hPneBUFLMFWyrm6agELjbgvhGb0UQxm56mCVDQktn7~MQS6d7Zk1ZXxykEeG1a~ZlTTp4Zu4ENjrJNZDxsW-Qv7Uc4F7p9Mfh27QdCcoJgukZIiUCKt3v5xAUV4F0D7BDEFX2tclNp37O3TPibLL0d3erZpa9dccH5jL2-WUzW0HnjevJPgRFdiTqJKIwp~NuOMquJ4X33w6IjgudCW6iPAk30xB4Hq~pP0ML4tX1tJzGnt9fPyP8ah2BdqGeUijna7nnk5OmXf1qMshYx6~aJe2s6ib5bzvRWhS8Jc~jBt88hezI7dFHbU97DvwsWZYh5zCWrMCfp8PnzjuA__&Key-Pair-Id=K3NV4LZ47N8M46)

\
A table named Employee with the following CSV with 5 columns. The points column is afloat.

Id,cid,aid,points,score:\
1,5608,1,0.59,4\
1,5608,2,8.70,5\
1,5608,3,4.99,1\
1,5608,5,2.88,3\
1,5608,9,0.79,1\
1,5608,5,7.58,1\
For the query "SELECT \* from Employee", the following databases treat the float data in the following ways:

**Oracle**\
In Oracle, the points column is of type FLOAT. The output is as follows:\
1 5608 1 .59 4 \
1 5608 2 8.7 5 \
1 5608 3 4.99 1 \
1 5608 5 2.88 3 \
1 5608 9 .79 1 \
1 5608 5 7.58 1\
Oracle database trims the leading zeros.\
**MySQL**\
In MySQL, the points column is of type FLOAT. The output is as follows:\
1 5608 1 0.59 4 \
1 5608 2 8.7 5 \
1 5608 3 4.99 1 \
1 5608 5 2.88 3 \
1 5608 9 0.79 1 \
1 5608 5 7.58 1\
MySQL prints the data as it is provided.\
**MS SQL**\
In MS SQL, the points column is of type REAL. The output is as follows:\
1 5608 1 0.58999997 4 \
1 5608 2 8.6999998 5 \
1 5608 3 4.9899998 1 \
1 5608 5 2.8800001 3 \
1 5608 9 0.79000002 1 \
1 5608 5 7.5799999 1\
MS SQL prints an approximate value. Use the data type DECIMAL (10, precision) to fix the places after the decimal that are required in the output. If you change the schema-creating SQL we generated from the CSV so that the points column is of type DECIMAL(10, 2), the output changes to this:\
1 5608 1 .59 4 \
1 5608 2 8.70 5 \
1 5608 3 4.99 1 \
1 5608 5 2.88 3 \
1 5608 9 .79 1 \
1 5608 5 7.58 1\
MS SQL removes the leading zeros.\
**DB2**\
In DB2, the points column is of type DECFLOAT. The output is as follows:\
1 5608 1 0.59 4 \
1 5608 2 8.7 5 \
1 5608 3 4.99 1 \
1 5608 5 2.88 3 \
1 5608 9 0.79 1 \
1 5608 5 7.58 1\
DB2 prints the data as it is provided.
