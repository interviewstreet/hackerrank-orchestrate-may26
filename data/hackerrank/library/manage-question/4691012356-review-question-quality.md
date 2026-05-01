---
title: "Review Question Quality"
title_slug: "review-question-quality"
source_url: "https://support.hackerrank.com/articles/4691012356-review-question-quality"
article_slug: "4691012356-review-question-quality"
last_updated_exact: "May 12, 2025, 11:29 AM"
last_updated_relative: "Last updated 12 months ago"
breadcrumbs:
  - "Library"
  - "Manage Question"
---

# Review Question Quality

_Last updated: May 12, 2025, 11:29 AM (Last updated 12 months ago)_

## Overview

Question quality is important for making HackerRank tests more effective. The Quality Review page helps you to analyze the Coding Question based on the following four parameters:  

- The overall number of test cases included

- The number of ‘Sample test cases’ added

- Whether the question uses auto-generated code stubs

- Whether the question has descriptive tags

It would be best if you aimed to meet all 'high-quality' conditions on your Questions before using them in HackerRank tests and interviews. 

You can view the question quality under the **Quality Review** tab, which displays [📄 Creating a Coding Question](/articles/6372874906). After you have added the problem statement, test cases, and code stubs to a Question, the last step involves reviewing the question quality and making any recommended changes to improve the question.

**Prerequisites**

You must have a HackerRank for Work account.

**Steps**

1.  From the **HackerRank Library** or from the **Questions** tab of a Test, click **Create Question** to create a new Question. Alternatively, from the **Library**, select your Question to edit and review quality.

2.  In the relevant Question tabs, define the [problem statement](https://support.hackerrank.com/articles/7816600113-defining-the-problem-details%3A-coding-and-database-engineer-questions), score, programming languages, [code stubs](https://support.hackerrank.com/articles/9168425479-generating-code-stubs), and [test cases](https://support.hackerrank.com/articles/3245197419-test-cases-in-coding-questions).

3.  Proceed to the last step in the **Quality Review** tab.

This page automatically generates and displays a quality review for your Question based on whether your Question includes the recommended number of sample and hidden test cases and auto-generated code stubs.

You can follow the recommendations provided on the **Quality Review** page to improve your Question quality.

<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047117209-?Expires=253370764800&amp;Signature=FVCtsQRMR1aO3DcN1tRsc1bH9zYaam~6CPjBH7hp8kgTWiLC8BsQB6He4ayUf1mLAE5VRtTkTU11hOP0LKUqm-kXBptX2NWB3U5~bBNuFWI0vjen6Iv5aDjgWK~GkR7uvqQoQB8AWdJDS0b4auxZqvxb62U6EkEl1fx4saVz7YX90oeMeuTNAljW-25ZdjlmqD-8tG~aT7mG4wtWYg2CCTDgsZbdpfYbdlaZLND5tKT7gn6MvjmsNkyMhpVOc7YxVFj8Vq3TtjkN6y7O7USRAQKRJf1QB~RS7vZZDX2Eh~iAqIX2uzNG7gj8DdKvgblZ2yGomqgygYPgxlBES6sUIg__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

*The Question 'Quality Review' page*

The following sections in this article also guide you through the best practices and recommendations to be followed while creating your Questions in HackerRank for Work.

## Understanding the Question Quality Parameters

1.  **The overall number of test cases in the Question**\
    Adding Test cases ensures that a coding question is automatically evaluated. Without any test cases, a question will not be scored and might defeat the purpose of an assessment. Therefore, it is recommended that you add at least 3-4 sample test cases, of which 1-3 are present in the statement, and an overall 3-15 test cases of easy, medium, and hard difficulty levels to each Question.

2.  **Sample test cases in the Question**\
    Sample test cases improve question comprehension. It allows your candidates to quickly understand the Question and the expected output from their solution. This improves their likelihood of attempting the Question and adds to their positive test experience. It is recommended that you include at least two or more sample test cases in your Question.  

3.  **Whether the question uses auto-generated code stubs**\
    The best practice is using HackerRank’s auto-generated code stubs (or boilerplate code). Code stubs are recommended because they help your candidates to directly read input and write output using STDIN and STDOUT, respectively. This also helps prevent situations where a candidate writes the right code but fails to display the output correctly using STDOUT.

    However, you may NOT be able to use HackerRank’s auto-generated code stubs in specific scenarios. For example, HackerRank does not provide auto-generated stubs for:

    - reading in a binary tree or

    - returning a class object from a function

    You may also choose not to use the auto-generated code stubs in scenarios where you want the candidates to display their output in your desired format, and perhaps, you want to assess them on their ability to deal with STDIN and STDOUT.

    In the above scenarios, you can retain the default code stubs, or you can choose to write your code stubs (user-modified code stubs) for all the programming languages you want to allow in your Tests.

**Note**: Writing your code stubs (user-modified code stubs) requires additional effort. However, once you write them, you can reuse them in the other Questions.

1.  **Whether the questions have Descriptive tags**\
    According to best practices, every question needs to have at least two tags that describe and classify the question. Standard tags that need to be inserted into every question include the difficulty level: 'Easy, Medium, or Hard,' skills or area of expertise the question assesses: 'Algorithms, Problem Solving, Data Structures, and so on. Tags that further describe the question, such as specific concepts tested in the question, required knowledge, etc.

    Ensuring that your Question follows the above-mentioned best practices and recommendations helps create good quality questions. When good quality questions are a part of your Tests, it adds to your candidate’s positive experience and your Company's goal to attract and hire only the best talent.

***Recommended Articles:***

- [📄 Test Cases in Coding Questions](/articles/3245197419)
  \
- [📄 Defining Test Cases for Coding Questions](/articles/8626818013)
  \
- [📄 Generating Code Stubs](/articles/9168425479)
  \
