---
title: "Generating Code Stubs"
title_slug: "generating-code-stubs"
source_url: "https://support.hackerrank.com/articles/9168425479-generating-code-stubs"
article_slug: "9168425479-generating-code-stubs"
last_updated_exact: "Dec 13, 2024, 5:15 AM"
last_updated_relative: "Last updated 1 year ago"
breadcrumbs:
  - "Library"
  - "Additional Resources"
  - "Programming Questions"
---

# Generating Code Stubs

_Last updated: Dec 13, 2024, 5:15 AM (Last updated 1 year ago)_

## Overview

You can generate a boilerplate code that saves your time while setting up a coding question. This boilerplate code or code stub handles the inputs and outputs in the code.

Adding code stubs is strongly recommended to save candidates time to avoid minor errors pertaining to the input and output format. The pre-generated code stub allows them to focus on the algorithm required to solve the problem instead of the input and output syntax.

## Code Stub Parameters

The code stub can be automatically generated for most the languages by specifying the following:

- **Function Name**: You can only specify one function for the automated code stub generation. However, if you require more than one function, you can select the language and manually type the code stub for that particular language.

- **Return Type**: The function's return type defines the type of value returned by the function. It can be a string, integer, boolean, long integer, integer array, etc. 

- **Function Parameters**: Function parameters are the particular variables or input arguments used to refer to a particular data provided as an input. Optionally, you can specify the parameters along with their input type. You can specify more than one function parameter if required.

## Sample

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td data-colspan="1" data-rowspan="1"><p><strong>Problem Description</strong></p>
<p>Write a program that reads a string and finds the first non-repeated character in that string. Treat the characters as case-sensitive. Therefore, "a" and "A" are different. You will be required to complete a given function <em>nonRepeated.</em></p>
<p><strong>Input Format</strong></p>
<p>There is one sentence in the input that contains String Str.</p>
<p><strong>Constraints</strong></p>
<ul>
<li><p>The length of the string is less than 256 characters.</p></li>
<li><p>It is guaranteed that there will be at least one non-repeated character in the given string</p></li>
</ul>
<p><strong>Sample Test Case with Explanation</strong></p>
<p>Sample Input:</p>
<pre data-language="plaintext"><code>balloonbA</code></pre>
<p>Sample Output:</p>
<pre data-language="plaintext"><code>a</code></pre>
<p>Explanation</p>
<p>"a" is the first character that is not repeated in the given string.</p>
<p><strong>Output Format</strong></p>
<p>A single character that represents the first character in <em>Str</em> that is not repeated.</p>
<p><strong>Code Stub</strong></p>
<ul>
<li><p>Function Name: <em>nonRepeated</em></p></li>
<li><p>Return Type: String</p></li>
<li><p>Function Parameters</p>
<ul>
<li><p>Type: String</p></li>
<li><p>Name: <em>Str</em></p></li>
</ul></li>
</ul></td>
</tr>
</tbody>
</table>

However, if you expect candidates to be familiar with the handling of input and output, you might choose not to generate any code stubs. Candidates have to write the complete code from scratch in this case.

Currently, you cannot generate code stubs automatically for the following languages:

- Cobol

- Elixir

- F#

- OCaml

- Racket

- Smalltalk

- VB.NET

- D

- Fortran

- Groovy

- Pascal

- Common Lisp (SBCL)

- Verilog

For these languages, you can type the code stub manually in the editor.

### Test Case Input Format

To learn more about the input format for test cases, check out the [Test Case Input Format](https://support.hackerrank.com/hc/en-us/articles/115008319188-Test-Case-Input-Format) article. 

###
