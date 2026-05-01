---
title: "Defining Test Cases for Coding Questions"
title_slug: "defining-test-cases-for-coding-questions"
source_url: "https://support.hackerrank.com/articles/8626818013-defining-test-cases-for-coding-questions"
article_slug: "8626818013-defining-test-cases-for-coding-questions"
last_updated_exact: "Mar 10, 2026, 1:03 PM"
last_updated_relative: "Last updated 2 months ago"
breadcrumbs:
  - "Library"
  - "Additional Resources"
  - "Programming Questions"
---

# Defining Test Cases for Coding Questions

_Last updated: Mar 10, 2026, 1:03 PM (Last updated 2 months ago)_

## Overview

Test cases help in validating candidates' code. They form the basis for automated evaluation of a candidate's code. A test case consists of an input to the code and an expected output. Once candidates submit the code, it is run against all the test cases. The output from the candidate's code is compared with the expected output to see whether the test case has passed or failed.

A sample test case with an explanation can also aid in explaining the problem better to the candidates. Ideally, you should use 2 to 3 such sample test cases to help the programmer understand the problem. We recommend having a total of 8 to 15 (ideally a total of 10) test cases that cover all the scenarios. The test cases should be of different sizes that cover different levels of complexity. No two test cases should test the same concept. 

**Note:** Please refer to the [Test Cases in your Coding Question](https://candidatesupport.hackerrank.com/hc/en-us/articles/4402921131155-Test-Cases-in-your-Coding-Question) to understand the usage of Test cases while creating coding questions for HackerRank Tests.

## Types of Test Cases

There are two types of test cases for each problem, a **Sample Test Case** and a **Hidden Test Case**.

### Sample Test Cases

Sample test cases are the test cases that the candidates can view and use to validate their code. They see both input and expected output values for these test cases. While creating the test cases, you can mark certain test cases as sample test cases. 

For example, see the illustration below of a sample test case defined for a coding question. The question requires the candidate to write code to find the first non-repeated character in a given string. 

![Sample_Test_Cases.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046585826-?Expires=253370764800&Signature=KFvVFWmL4lqXakjzuMqGLIvb4XKEI3cNoXBnBS~bh~agLlE89MD3HETyYsLcEn6aeJaNC36wUbPl-EzFVPTy6c12bqQCWNTlpOgxqbLrsISoGeNdNZrcA9uWwySyijo9pkD9ndzFOee~Ts-rPBB8gC8txITYr2tg9kkdIsIj3kdozhqhMhtrqxspgzmO9QA0XDdLlxRkY5PIcFmvubh5aEP-EsSI8fG17Wsv1gbrBUCdFcDFPJbC4ZCcoAXdrxuVvnyMnFhDo0o0~guqBNCdcU7ba0e4buzUBcBl0Y5z8pfMAIrmN4jMcoA6vwvmIFTL6Z4DqNjKON2f2hpYIixrdA__&Key-Pair-Id=K3NV4LZ47N8M46)

*Defining Sample Test Cases for a Coding Question*

In the test, when the candidate writes and compiles the code for the question, the sample test case is validated against the candidate's code. The candidate can view the sample test case execution results along with the input and expected output values as defined by you. Viewing the sample test case execution results helps the candidates understand their code's expected results. Candidates can also download their sample test cases.

The following image displays the candidate's view of sample test cases execution status after compiling the code in the test.

![Test_Case_execution_status.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046586178-?Expires=253370764800&Signature=KIVxdwsdUldapbNMtbEKvxucXW3Vrfm59oW-Ufh3GjHlxsYKxL085civiwpy6ooFaKElujlppQiVy3QuXI31XtTyUbmi7eiRkfateciEUB9v9cdAcaBoQOvOZOFFpvAOIWezo1d-OUjx50xpCDS9j3gsJ4nzINavArTu7sSUdpUliCVWKsGzb9WBZhH5cGmv-qYP~zuwK0C4ZJgmOVZiOmFch05lWoEJ2da~pjJjkq2FPyggvDv4PwlwpKKOC6NgIirhYuLUS7p653w6t5VClqItdo1iTWDitctwGcrPq9jpf4mq6yFHxXuMKbgP1ln0mSl2EAmcjO2MSyAb4ojXVg__&Key-Pair-Id=K3NV4LZ47N8M46)

*Sample Test Case Executed after Candidate Compiles the Code*

### Hidden Test Cases

While adding a test case to your coding question, if you do not mark it as a sample test case, it is considered hidden. Hidden test cases have evolved from the era of competitive programming.

You can include various corner cases as hidden test cases to evaluate candidates against different scenarios. When a candidate runs their code, the hidden test cases are indicated by the **lock** icon.

Unlike sample test cases, the candidates cannot see the input and expected output values for these hidden test cases. Although, they can see their output and debuggable output when they click on any of the hidden test case options. This feature is provided to candidates to give them a better debugging experience.

Consider a coding question where a candidate is required to write code to find the first non-repeated character in a given string. 

![Hidden_Test_Case.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046586504-?Expires=253370764800&Signature=oy45w-pPuh93nDS9XluTCTyOdDapcJpTgkhptwWZrkZ3nByDLY10tt4bXzaUTAAJC8ppBy3INFa~ZluG1RF6aPhXpu3AU0fzOYtAbs68rDIofq4wcqhoHpb8k4eJ4CnCz2oQjY0jWlb95g8tiA9qPFuZoq4x4zkrZ~32HAVkc3m9lD-KIkX96mRpo8qtjhnPt90KPaksInmrXF-IM6Vpwy~W~5C~misDT2mmvU6Gx2yEYKgJfB~u~jHhIRdW7ZCvP0BndiMqHOe6XqGI8KILP1-vkDZfkWRSj2K4pIzMnp5bt6tt8PZKwrZLRpGUJBQnAE99Mqh8nPlbv31Kr7D7Rg__&Key-Pair-Id=K3NV4LZ47N8M46)

*Defining Hidden Test Cases to Validate the Candidate's Code*

In the test, when a candidate writes and executes the code for this question, the hidden test case is validated against the candidate's code to return the test case execution result. If the candidate's code successfully executes the hidden test cases and returns the expected output, then the candidate achieves the score assigned for this test case.

![mceclip1.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046586838-?Expires=253370764800&Signature=kvTLCs3Eb1uN0h84ZOWeCCpH8AmmYzCPXJvylYxuRjA9aqOJ8lYunw3ql-B-7ANDJmmENHSCZIoq8Wer12ZUUMB4C1Hh0bLe1HuByvtyQA6f9~Yy61xLD5eQNleAGTfWS24uXwaYwXYTuU8rymQpRlyeFqaiUTFNxPCjizzfcL~i7nqE7RAPD8e-awUSbLU7yb6GNbEAGLeo82NpyoK5WDfLTOG4QeLL8H2QErkoedctTCPEbMFRQ1CeylkL3JQpyT9qpUi~V3Ff78peMTDe~rqdwV3TG7ptIvo90iuReO71MlaGankERNZGm7vj312Ed~ruic0KypfNOueFiQioGg__&Key-Pair-Id=K3NV4LZ47N8M46)

*Candidate's Code Execution and Test Case Results displayed in the test*

**Disabling the Output for Hidden Test Cases**

You can also choose not to show the output of the hidden test cases for the candidates. To disable the output for hidden test cases, follow the below steps.

- On the **Tests** home page, click on the desired test.

![question.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046587240-?Expires=253370764800&Signature=mRV1uZ4F4~B6C723y~hySOZOgkuN8290vNjWGw5KgadkCTGEb4fUxIE4YbvGhGwOdUaX2D6sxDTEsRdqFZ4Xr0PVdizMwrx8Oy1qI9aB29o8BQu4GJ5CC7efBfXQ2CfPmtNj-mih~3noQS4KTebdJS1QbkmcOUfYJZsmrTW5fGXDhvInNIIZWRArwA~MX9cETthckYZDXWw~qJo8hPrda7CW6O16s4K8GNlRv3VkGMRSQZAS91q93eBF~6UViZTjsU8jh3kEeFF9NIsVq2bYznOyRdBa8no-WFyf5qydpx4wSc8FBVe1rWDb5XGxZXZiuu8pRMlxoxPySY2OaEKbKg__&Key-Pair-Id=K3NV4LZ47N8M46)

- After clicking on the question, click on the S**ettings** tab and then the **Questions** option from the left.

![question_settings_.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046587596-?Expires=253370764800&Signature=mtFR15sukQil~IQvzJWqwQEMIQ19EqlGp2tpmmShXcYJaWu1oNr-WGi-x2m-BL5MV-LT5EaywJmCP6L8T8C7xVBvlMVJf4NNOBn9OnFnibwFRgKGdzBl0gUN1-zxIr9-b0GqojhF2~vMa9IMM~8MgZPBmbI3kQKA8EYQmGFXdMG7kXN799DAHcis7ka~Cqr4VVNSxZMlICqCUhE~mHECBM2ggEaCiVVX1UEbuHS411NtuRRhZXPy83piFXONzWhJM67LGL3hf6d3I1RWGcg9gzpygPHLAyNHhdFEok0DjSJrXQcr4nIxy~1GeuYBXsP4lYZ-53v-TB3QLVoLEdPmcA__&Key-Pair-Id=K3NV4LZ47N8M46)

- After clicking on the **Questions** tab, scroll down, you will find the option to disable the output for the hidden test cases as shown below. However, this is not recommended since showing the output helps the candidates to debug their code effectively. The option to show the output is selected by default. If you want to hide your output, you can deselect the **Show Output for the hidden test cases** checkbox.

![hidden_test_case_output.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046588009-?Expires=253370764800&Signature=HRLkvr2bMbVPx3udwCRbvwD9oiKAu6LwtHb1ahhYmWZGAqcvXTT2cCWjAMYHmgcqPO1LLkLMEkAwun2hvc-JQIHnEKfbThy3w6pKA3dJAnCs5ECMLxau7nYY5U3F2raeeUxvFk-yo56SA6Gw1rJJ7r1HAfKlXmiiN9YyzBicdV50OJ95UOrLUi7smiuj5fkK42-nUfvLD9is~vlrHP1f57~6Q-s9CGTZmGFKxStclUUCKpotK0EN7vciXfk1~860Iau4rYxUTtTQgG-QVHR4mVN~6P2xLffI8ec3gQD5068D3eP3Gdx55-vZyhYRwomBjby-xgiLEVawIVbRWdCkQg__&Key-Pair-Id=K3NV4LZ47N8M46)

**Note:** Our reports suggest that candidates tend to lose a lot of their test time while finding a solution or debugging because of hidden test cases. To reduce this challenge and give candidates a better debugging experience, HackerRank looks forward to moving away from hidden test cases in the future and introducing a breakpoint-based debuggable experience to candidates.

## Scoring

Not all test cases have the same difficulty level. While creating the test cases, you must ensure that more points are assigned to the difficult test cases as compared to the easy ones. This leads to a better distinction between outstanding, good, and average programmers. The sum of scores of all test cases is the total score assigned to a particular question. You can assign zero points to sample test cases if required. The overall score for a coding question is the sum of the scores of all the test cases which are successfully passed. 

In the following illustration, you can see the candidate's detailed test report in HackerRank displaying the score achieved for the question based on the test execution status.

![Test_Report_status_of_score_achieved_for_Test_case.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046588350-?Expires=253370764800&Signature=u6LRRc4f7AugPfrjtYyVP8e9UTr7RyF5dncNKU4gIO5k~3Y9HliAEo623l7kHfABt~AkzQDuxYvjzYWMNZA7IwiXvN3Rf9HiuPur5oodz1leu6CoKlcwJzbIyZUuE7njSMNHL-iefQ29XJzBppm6zJPHyFLy0V-QiHbO4qwt39PzDOvDvRlapoOvJ-Vh9mqLWo4gCP2WVIb~Np5K~sg89Ol6i5~OD9j-atfvDAcX8erPp~Yipm037zUUjYLXFA0aakLero1YaAQaBeVf1nzPfM1bIIal~X0rj9sfTVaU7VHBNaBfFFu9ZE2y~BumeYU0aTHxjGMYAO8Z4AfxTOdX8A__&Key-Pair-Id=K3NV4LZ47N8M46)

*Question Score displayed based on Test Case Execution Results*

## Sync Test Cases with Code Stubs

When you are using auto­generated code stubs, ensure that the input and expected output are in sync with the code stubs. You can refer to the tail portion to understand this.

*For example*:

- If the input is an array, you will always read in "n" (denotes array_size) first and then read "n" array elements in "n" separate lines. This is required to ensure consistency in reading input across different languages.

- If the input is a linked list, you will always read in "n" (denotes the number of elements to be added to the input linked list) and then read "n" elements in "n" separate lines.

\
