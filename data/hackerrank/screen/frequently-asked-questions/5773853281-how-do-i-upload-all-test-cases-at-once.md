---
title: "How Do I Upload All Test Cases at Once?"
title_slug: "how-do-i-upload-all-test-cases-at-once"
source_url: "https://support.hackerrank.com/articles/5773853281-how-do-i-upload-all-test-cases-at-once"
article_slug: "5773853281-how-do-i-upload-all-test-cases-at-once"
last_updated_exact: "Dec 13, 2024, 5:47 AM"
last_updated_relative: "Last updated 1 year ago"
breadcrumbs:
  - "Screen"
  - "Frequently Asked Questions"
---

# How Do I Upload All Test Cases at Once?

_Last updated: Dec 13, 2024, 5:47 AM (Last updated 1 year ago)_

HackerRank allows you to upload all [test cases](https://support.hackerrank.com/hc/en-us/articles/115006611728-Defining-Test-Cases-for-Coding-Questions) for a Coding or Approximate Solution question as a zip file. This feature is particularly useful when dealing with large inputs or outputs, a high number of test cases, or when you prefer to use an external editor.

## Preparing the Zip File

To upload your test cases, organize them in a directory with the following structure:

#### **Example Problem**

|                     |                                    |
|---------------------|------------------------------------|
| **Input File Name** | **Corresponding Output File Name** |
| input000.txt        | output000.txt                      |
| input0.txt          | output0.txt                        |
| input1.txt          | output1.txt.                       |

For a given test case, the input and output files need to be associated with each other. The numbers in the input and output file names should match for them to be associated. For example, input0.txt and output0.txt are combined into a test case, as is input002.txt and output002.txt.

**Note**: Ensure that the directory contains only these files and no sub-directories before compressing it into a .zip file.

## Uploading the Zip File

You can upload the zip file directly on the **Test Cases** tab of a Coding or Approximate Solution question in HackerRank. Refer to the [Create a coding](https://support.hackerrank.com/hc/en-us/articles/115006421707) [question](https://support.hackerrank.com/hc/en-us/articles/115006421707) article to understand the detailed steps involved.

 

## Handling Zip Uploads and Test Case Scoring

When using a zip upload for test cases, each test case receives a default score of 10 points. The system does not retain or recognize any previous custom scores that may have been set for test cases in earlier uploads.

**Creating Zip Files for Mac users:**\
For Mac users, ensure that you create the zip file via the command line. Using Apple's "Compress" feature from the "Get Info" menu generates a zip format that is not compatible with the system, which may lead to issues during the upload process.

**Steps for Command Line Zip Creation (Mac):**

- Open Terminal.

- Navigate to the directory containing the files you want to compress.

- Run the following command: zip archive_name.zip \*.txt (Replace archive_name.zip with your desired zip file name).

\
