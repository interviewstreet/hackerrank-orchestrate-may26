---
title: "Test Case Input Format"
title_slug: "test-case-input-format"
source_url: "https://support.hackerrank.com/articles/2461683826-test-case-input-format"
article_slug: "2461683826-test-case-input-format"
last_updated_exact: "Mar 11, 2026, 3:36 PM"
last_updated_relative: "Last updated 2 months ago"
breadcrumbs:
  - "Library"
  - "Additional Resources"
  - "Programming Questions"
---

# Test Case Input Format

_Last updated: Mar 11, 2026, 3:36 PM (Last updated 2 months ago)_

## Overview

Candidates debug their code by using custom input when some of the hidden test cases do not pass. If the question setter has uploaded a solution while creating the question then the expected output is readily available to the candidates. In this case, candidates can add their own input and run code to compare the expected output against their output. This helps candidates in debugging their code and understanding the reason why their test cases are failing. 

However, even if the question setter has not uploaded a solution while creating the question, candidates can use the custom input to debug their code. In this case, they can themselves determine the expected output and use the custom input to determine if their code is showing the same output as they determined.

## Custom Input Format - Sample

The candidates have to enter the input in a particular format to test their code. The following example explains the custom input format in detail:

**Integer Arrays**

**Problem statement**: For the given array of integers, write a function ***ArraySum*** to return the sum of its elements.

To generate the code stub automatically while creating a question, describe the function signature in the code stub form.

1.  Enter the function name, ***ArraySum***.

2.  Select the **INTEGER** as the return type.

3.  Select the **INTEGER ARRAY** from the function parameter type list and give the parameter a name ***n****.*

4.  Click on the **Generate Code** button to generate the code stub.\
    \

    ![input_array3.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046602447-?Expires=253370764800&Signature=Ovm82k-9K6a0BssGWssU2ZySYytBMpSwmdaQp84dKpSkyKl~Cg-yRYF~vRZyP-t-~pym5pjQtLcgMyupb0K5ZzBZsn8yTOnaj~6oZE2F6fhdNbOCvHpHOvY6a--ezVH4fI2rpJkBiqE1WUJvL-UAjGomxYiQg2uq8tJFr8TcNbM5KnurnjRAUt2gbUiTty38a6~ESKuuKPldo5Cp08Tj3dxQxl5ieJ1e~lNSM6NbBJjmk9-DjWLEITPcuxZTwlJHoLJu9C9F-sfR-Y1X5y-F~mOkX2N7pD-KZ0XqFGgyJEOFVMV0EK9nFh0ASz28LTRixOaHSqZ1UMrdS3-6ypQDGQ__&Key-Pair-Id=K3NV4LZ47N8M46)

    *Generating a code stub*

While creating test cases for this problem, be aware of the format the stub code is expecting. For a test input array of length Y, the test case input contains (Y + 1) lines. Here, the first line specifies the length of the array and each following line specifies the element of the array on a separate line.\
For example, for the input array \[10, 20, 30\] and integer n= 123, the test case's input that a candidate requires to enter is:

- 3

- 10

- 20

- 30

The test case's output would be the sum of the elements: **60**. 

![inputarray4.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046602893-?Expires=253370764800&Signature=CaxIndaes7Lk9TNK0cG47bTh3uxu9F92V4TQTZO02ZI2HKBRP~8OFRHPxybDm7p3EN9GcANuvTbS4SUetaT7DHvojKerN6A99Ngwkn-BlEqza6VNKM-c3Pu0YVVN2DmceuOAiswDqvvBPoyjoqBRMVNjEU5qDjf2uQXGFH85SH-eM9FqrZCuhATYa3CYk0PDV04FJyhFT8BzHYf0i3QhCbNCou42QMA3Iq0OS1JTZBvZtF3ISk1VyvkH0i7voH5OS8UZPVcwD1v4xJCIEboUW9VFKJRafm6SqAf3fwY-228BkA4thRfLgE5l90fYRAZXiPSxwk2eKnFfuqONl6zhfw__&Key-Pair-Id=K3NV4LZ47N8M46)

*Allowing code testing with custom input*

### Generating Code Stubs

For more information about generating code stubs, check out the [Generating Code Stubs](https://support.hackerrank.com/hc/en-us/articles/115006430067-Generating-Code-Stubs) article.
