---
title: "Data Science Questions Creating a Data Science question Candidate experience Scoring a Data Science question in tests"
title_slug: "data-science-questions-creating-a-data-science-question-candidate-experience-scoring-a-data-science-question-in-tests"
source_url: "https://support.hackerrank.com/articles/5187107609-data-science-questions"
article_slug: "5187107609-data-science-questions"
last_updated_exact: "Apr 22, 2026, 4:49 PM"
last_updated_relative: "Last updated 4 days ago"
breadcrumbs:
  - "Library"
  - "Question Types"
  - "Projects Questions"
---

# Data Science Questions Creating a Data Science question Candidate experience Scoring a Data Science question in tests

_Last updated: Apr 22, 2026, 4:49 PM (Last updated 4 days ago)_

Data Science questions help you evaluate candidates on real-world data science skills using hands-on, practical challenges.

These questions assess a candidate’s ability to:

- Perform data wrangling and preprocessing

- Build statistical and predictive models

- Create meaningful data visualizations

- Implement machine learning algorithms

The platform includes challenge-specific scoring rubrics to ensure consistent and efficient evaluations.

# Creating a Data Science question

To create a Data Science question:

1.  Log in to your **HackerRank for Work** account using your credentials.

2.  Go to the **Library** tab. 

3.  Click **Create Question**.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1772609520474-image.png?Expires=253370764800&Signature=PkR9q2TEQOCbnHek7TmbuSNWLJrtVx3OeyBsvjHTxI0mdhmpx4Imm-~4RPltSE-uqYYhvF0spfsjJhsfXqWE7YiY5EbcNOyp3bFeFiMq0DcTOpL1S-U5C-oN3M0ywlkVrvMjsOGQm75FJ-h7yFzo6sTdpwt~DQSeXB6P24ljBc~giAAh2aDWboD1aaMS02h-S9gbDuWHunk8j4k-IaMkYB4FKOuuBYI0SIl6b1I-kKtoQUmyDNyPjP~FXQPSUdyl4MEWo6~gt-Hz48czzNA2F~IOqrdzbY2XkgLVMpOohB9YJvyghIHaE2Ia4ORkx3AA~jza2AGEsvToC0NKS06Rbw__&Key-Pair-Id=K3NV4LZ47N8M46)

4.  Select **Data Science** under **Projects**.

The Data Science question creation workflow begins with the following three steps.

## Step 1: Environment

1.  In the **Environment Settings** section, choose one of the following kernels:

    - **Python**

    - **R**

    - **Julia**

      **Note: **

      - The default environment is VS Code. You cannot change this setting.

      - Click **Package Info** to view the list of supported packages. For more details, see [📄 Package Information for Data Science Questions](/articles/6282504591).

2.  Click **Next**.

## Step 2: Project Setup

1.  Set up the project using one of the following methods:

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1776698888142-image.png?Expires=253370764800&Signature=l5GIUER-0kc8-AYxsqncjUIzomdhxNtBgXPTsBJLoDLSCwqetCAqCpFsBcg0NozxHIKB-ftb9TaoY7HJXHJpTuXjm5VaOBzxwxQl~0kCNi2xpMLBnAvZIi2g1ZQfDI5gfMmavwqsnRQPby9hNSUFZ7mB3A6ieo1v60RZhaPUqX52G6B~2vCOV-b-bUbDniNsmljRaUnsLJcZCTHcULQNFTkQiEmmcZolZ9H6cgKlqP3Qg5EUP3psxCsGzqO6Mf1-vde3kx90Vf1aqsM5Mljy3BpfQfEJQ~f4HRXp5yJG6G2mK076ce-KrDZWAwODYhuNE5Eaz3A1mNDjMH6VK2Kq7g__&Key-Pair-Id=K3NV4LZ47N8M46)

    - **Upload Zip:** Upload the project file in ZIP format. The file size should be within 5MB.

    - **GitHub URL:** Enter the repository URL and click **Clone Project**. If the repository is private, the IDE requests permission to connect using a one-time access token.

      **Note:** HackerRank does not store your GitHub credentials.

      The **Project Setup** section also includes a preconfigured sample project for the VS Code framework.

      ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1776698939647-image.png?Expires=253370764800&Signature=Ep~FIxfrddkI~gRG9m6AgoRXGKjqnODfUqTi-kNsB017UtKf8N5ENlqso517kuCYItFK8leyj-NU6hRziXfaw4srPad-9CFLX9Wt3LG2oZXj9ojM-3VHxlWUnuzm9UMfBAtTDDMR0oM036Kr~R0e3H40zz4j371Rq9AofNxR0P3NmKLkRIL0RLEFyg1Sa82fyJNYH9Ap~PeMGU3CpIzinT0UHCAvUw6bst1xeMwgalrBiK~6Cir9az~MYDFyk3oQw0hIVVDg6BYW-sGAOLeeIJOdi-qtYBjwLnQ1XsA4Q8k-W8nPBI4tNmkoSxBgVTHdnTABauDdCLbPd6WyVxx9vg__&Key-Pair-Id=K3NV4LZ47N8M46)

      **Note**: To specify which files open by default when the project loads, configure the `default_open_paths` field in the `hackerrank.yml` file in the following format:

      <span class="mr-auto truncate">Plain Text</span>

      ```
      configuration:
        default_open_paths:
          - <file_name>
      ```

      ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1776854913374-image.png?Expires=253370764800&Signature=QIOfrVYj01aI8RAGhba-KMtuB8oJMiwx3xfZ4Laptd2yOA0I1~OzwdN1q93ik1haI1dX4jwbN3g9QydL65z~io2mgJuhomRRXhzV73QCwZwAjxml3zpU1qM1W6VDzYdYc0GrcXe4BXx6fB9vvDAv1mhomXGkmQtyFWZVezuBKkf04gjmvCHJYSf2RZLFTb0PztSYYIuzF7wJHUnriNKsAP7WzmzxuAgDcnzuifq8ESo-XlTmwJ-Uf7rOVsF6lZGVLAW2to8cFhNTXO3WA~KruTUlk9T1BfgKSn8LXcw-0kdrnJKuL8CVROYyoBhzKZ6My1NKckUee749iFLy1wqoFQ__&Key-Pair-Id=K3NV4LZ47N8M46)

2.  (Optional) Click **Browse Files** under **Additional Files** to upload supporting resources, such as datasets, scoring scripts, or other required files.

    **Note:** If you enable automatic evaluation with a custom metric, upload the scoring script and the expected output file in this section.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1776698977448-image.png?Expires=253370764800&Signature=vYrOOiiIBqj5lH4T5yc2BkE277w~wOXAHoVGQDXIbAOjJWzU1ly3pFfob5iToe7A8tfDtzLTLnGkDmuGuI21oaqBJJNzqSGl0~ksAqw1s-9hAzB2Yxw6fVXSSvPMPoAQuhzdwxx55ax~QxEWWaPE4V6MxX8X~W78m5sjHt3l5GDTEDFPkwlnsSS68PZbuSTc42LUnijwcEjPAqhWrd7Aa8cfR7pFkL9Y0FueOwJVZI-Qk~aH4-uTZS-Q8bbYF9h9EYYuWY1~1fxn1r1JjGyV9eOaMufZrgpWxipNjn7EWxXYn1X75CaTN40zB141C~7-bLg~Xgw7Y~eBEgWdxZTboQ__&Key-Pair-Id=K3NV4LZ47N8M46)

    - The total size of uploaded files must not exceed **500 MB**.

    - Each individual file must not exceed **100 MB**.

    - Add large files to `.gitignore` to prevent increasing the project size.

    - HackerRank supports externally hosted datasets with a maximum total size of 5 GB. When you use external datasets, ensure that your solution runs within the platform’s machine specifications:

      - **CPU:** 2 vCPUs

      - **Memory:** 16 GB RAM

      - **Storage:** 20 GB disk

3.  Toggle **Automatic Scoring** to choose the evaluation mode.

    - **Manual evaluation:** Disable **Automatic Scoring** to require manual evaluation.

      ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1776699011672-image.png?Expires=253370764800&Signature=Kzn7iJvl9btdKjCFvANmw~SoK03so8Tpsoe8A1YYx1AkU~SHaSpdxuP-6u4LnHCCrBRj243Y8SeI6EpF97pr47aASFUv1Y12O8cVEtSCOqtqyBF9t-6cWFIEglCQGCoU07322eRxGio0ItUxAAYRAZTNS9qF-8hmXwCBT7LfuyBp5lXIldIOoSKPVE-zoOIcRc2a9qwguOx4Z4ZjbToctgocNQS1aL3oZRTNgQx3w3W3~o2ZbvnCT8K3m6wbIw~UrpKdcjM0q8x5sU7T2-E9p4~33LqIRiwjqsF7RGN6O3MGGmOXyVp3Y0juFCEVp7nEVLHpBd3HYw45Q5Du4exLkA__&Key-Pair-Id=K3NV4LZ47N8M46)

      Add evaluation materials in **Step 3: Question Details** under **Interviewer Guidelines**, such as scoring rubric, solution notebook, actual output, evaluation script, and evaluation criteria.\
      Reviewers can use these materials to assign scores manually. For more information about manual scoring, see [Manual scoring](https://support.hackerrank.com/articles/5187107609-data-science-questions#manual-scoring).

    - **Automatic evaluation:** Enable **Automatic Scoring** to allow the platform to evaluate submissions automatically.

      When you enable Automatic Scoring:

      1.  Select a **Scoring Metric**. Choose a **standard metric** from the dropdown, or select **Custom** to define your own evaluation logic.

          - If you select a **standard metric** (For example, Categorization Accuracy, Mean F-Score, Log Loss, AUC-ROC Curve, Root Mean Squared Logarithmic Error, Average Precision):

            ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1776699154016-image.png?Expires=253370764800&Signature=pcisSGEgiLpWfVc78TFuLJetMouof~Wotak4py5H4TQ9xMp8n1QJnciPB35CQ0ZZV7L9uQbAJiq3WuBvefI3eECrt~opsEFn8WbzKStXuMZPt7IpTHqVl6xSdSghydqN5SYgzIg19WTcXOAJ81eUDZ12hcoSqZSyJRISdAFfQg4W9BLIQWWqp3n-0ql9YjHnGpNw~~bdKa8jk1gLnGoqVa04FLT~EUr9ds~~TJ6OqecjCDcCU10Z742iPQMNocV2dpDnl7yYLETf0BUdm0GUjEyqZLqy1hXaX6Fk69DyHf4OeNJIcUoP8JjQYvYVo8lI56Y066Jrz5w6adH7X-zMWw__&Key-Pair-Id=K3NV4LZ47N8M46)

            1.  Enter the filename that candidates must use for their final submission in the **Candidate Submission CSV Filename** field.

            2.  Click **Browse Files** under **Expected Result** to upload the CSV file (for example, actual_output.csv) that contains the actual results used to generate the score. After uploading the file, map the required columns under **Expected Result Format**.

            3.  Click **Browse Files** under **Sample Submission** to upload the CSV file (for example, sample_submission.csv) that you expect candidates to submit. After uploading the file, map the required columns under **Sample Submission Format**.

                ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1776699191402-image.png?Expires=253370764800&Signature=ES25YIUUf1JSACWXHQ7nCXCCujAcoblUahMsPmrrd4X0UG1oFlH1H-kW6zQnt0MHhfSExWC7noVTZ39Y1VU8zNZyNLflh4ih7HaAS8wBgF4b2MXiP1Ckd-ixPZyhpnNach6uROYMypRZ76MLK4EqqBUv~RSBg5t2a~~5wa~1s5NMU4g5zD7AZ9yB6MH4tAa1SqpJulVUET0r7Roye1EE0wsYkBZemBlztYHuLybkjg1edkSkIhfhclx7D18bj7pLIZyzpGWLjyXIKsTHutLZoSaV90JwT8i3z5-YAGq5SGxV1jI0po5Q-YLGuB4Z6L8ZciD~tZ~27FnHIarvX7pFEw__&Key-Pair-Id=K3NV4LZ47N8M46)

          - If you select **Custom:**

            ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1776699233197-image.png?Expires=253370764800&Signature=fgRnGQhLpwKJhbDBXB697HV4q5BzuQjCzTNJgXDD~h2TdL9r8IKLUlqScMjcDIsGaqLb8trvP3eqXYK0~0uMShy7KGf7Ig1xuJ-OdGGFNYQcm41buZg3F5YP8artCzC7mzoNIYQZ5635Vw2qn8V8LfFcVaXD2WI7qp0c51HFUrAfsVd3tK49OsXC9sxwMRFSlz0xj96AaHCs7tOejJiHKwkgtI6cUznEFGnj3jKeRrKYINooEQtH8urHyuedp1lgi4lOhOrQQBY3wodQzVBdply8MhQdK-AHn6eLIoBQlHaYOnClZsgLLBIGYIrFRgwOuydMcTtkzBO33Wkmi0EkfQ__&Key-Pair-Id=K3NV4LZ47N8M46)

            1.  Create a scoring script that:

                - Evaluates the candidate’s submission (For example, `submission.csv`)

                - Compares it with the expected output file (For example, `actual_output.csv`)

                - Calculates relevant metrics such as accuracy, precision, recall, and F-score

                  The scoring script must return the final score in the following format:

                  `FS_SCORE: X%`

                  ```
                  #!/usr/bin/env python
                  # coding: utf-8 import pandas as pd
                  from sklearn.metrics import accuracy_score
                  import sys def score(actual_data, sub_data):
                  if actual_data.shape != sub_data.shape:
                  print('Shape Mismatch')
                  return 0
                  if actual_data.columns.tolist() != sub_data.columns.tolist():
                  print('Columns Mismatch')
                  return 0

                  actuals = actual_data['popularity'].tolist()
                  preds = sub_data['popularity'].tolist() try:
                  return accuracy_score(actuals, preds)
                  except:
                  print('Error in Evaluation')
                  return 0 def read_data(actual_file, submission_file):
                  try:
                  actual_data = pd.read_csv(actual_file)
                  sub_data = pd.read_csv(submission_file)

                  return actual_data, sub_data
                  except:
                  print('File Not Found')
                  print("FS_SCORE:0 %")

                  try:
                  actual_data, submission_data = read_data(sys.argv[1], sys.argv[2])
                  score = score(actual_data, submission_data)
                  print("FS_SCORE:" + str(score * 100) + " %")
                  except Exception as e:
                  print(e)
                  print('Score could not be calculated')
                  print("FS_SCORE:0 %")
                  ```

                  Ensure the script handles edge cases, always returns a score, and runs without errors.

                  If the script fails or does not return a valid score, the platform assigns no score and requires manual review.

            2.  Upload the following files under **Additional Files**:

                ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1776699285922-image.png?Expires=253370764800&Signature=R5v45wc51siTX6YimxhFjPqckR1a4qTyOfrqONM1UTAcWcyfnmynWXVOlwn3HZMymthlnu~hAlT1axnvMcVq5cFPDtjvMhM3RPpnPEmo~50tPGPsMjADeM3OY9~bafiX4PswV7f8mtIinUa4pb6L0pNNd77lrhuREoqodXPq1MlYaGmIThblH7b7d41RoUZ5q-8ykiYjIsfUzFcnPXqdVkRJ6d3Ow3Pc95xBIMn-RtaU-U3vg5hd5LGjYVMnamGwoW2PdD4kn1czs7NmLbfDyTDN69xeFU43kK9X9tL~K~3nBuQyDngGnWyflu3Vg3QBi6AC2CMDJNgaG~xhy1NruQ__&Key-Pair-Id=K3NV4LZ47N8M46)

                - Scoring script (For example, `score.py `or `score.sh`)

                - Expected output file (For example, `actual_output.csv`)

            3.  Enter the expected submission filename in the **Candidate Submission CSV Filename** field.

            4.  Upload the expected result file under **Expected Result**, if required.

            5.  Define the scoring command inside `hackerrank.yml`.\
                Example:

                ```
                scoring:
                command: python evaluation_files/score.py evaluation_files/actual_output.csv
                ```

                ![hackerrankyml.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1772610331466-hackerrankyml.png?Expires=253370764800&Signature=de86GZRiVrcRn9zVcShWcMdn7TgBaH-ntcPBhn8o-47VrhU9L6V-FfiWGTELA1ZNJTHQqtCQqcEduGwc7ocJ2uUwrxsq59sFiW3G8c5CASizM4DDjkLJayXo6YzmvN~s6qoLpAJWRFhIhaX57cb5RZP84QaG7l8Di52u-h42hwDRlF9o9olp8cZ5XJT1jOWBBziI1Ng8Ga9Bl0P~CODjI46GfUTKgwUMni-ZC5bKv5NqIuA~3PfPr6-j2iNYNlbWt7nu34NFld2kjdQJIjygdCQfJ5zSUj5G0OKMmZ0wsrFPyAivCiMzZb0EACO4XkJYnIHyCqH0C~jq7LRrRaUhrA__&Key-Pair-Id=K3NV4LZ47N8M46)

                The scoring command must execute successfully, produce valid output, and return a valid score.

4.  Click **Validate**.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1776699505233-image.png?Expires=253370764800&Signature=QY2gv1dggQ4f1WzhaFxDdhYBt9HU8EsVnWLF56eSF3t1Ncc-JOJnamZA48y-csQZ~UQpDCRdV~5TjEl6kpV5d5GoHiS~Ki6VZ4dcXRx106imwETDJ8rJy-MMSn0Ov-ZVkcdoqGIk3PqQbMieFXskiGkVPjHEVnsO0lMbmJGMioPZ4mFsKX3MvZ3YBw5kijbxwd8ABmi2ngzhrVrfgxUGWp3BQQFb~O8ODBxeUtneEMNGarhxrUc2Lbdle1A~K6oqFa8aJWvHmNApwsbbvQhanysxc0K~uLvg81CAltw3rypo6kNBs5mDpQtQxBfWRpHCGEI5TQLT9m-ykOMnEj1tAQ__&Key-Pair-Id=K3NV4LZ47N8M46)

    **Note:** Click **Revert** to restore the project to the last successful validation state.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1776699684859-image.png?Expires=253370764800&Signature=qjz~mCopxDjfb~affmryP820-t8bOdElbUm~Ty0TKJzutb7JjIRy9PFg663p4geA3mZ7OqsJl~EPpGYmdI56DO9SecUtrOrihcSZwhOgshxrG3oqW4RPDrqSeY3EJCMX12LTb0qUG~BMKc8eWrXl4U6X7b2QBB5Q80mfzQ8qo6LYyy14F9sX8spWWQ1EBYP6yOufgE8Q5E-nhOkQ4bu927~MprhTAmFQD4mInpeDlrBj1ReBCpOb1HPNJq66YLsICxISsyW8F6ObUa5rxJ6cA5dNqYjmOgtu3FpYzLRUxAtRQU1-l9Y9a5lVS-0v6DWfcAyfzfW4eutCHhdiWZ~VDQ__&Key-Pair-Id=K3NV4LZ47N8M46)

5.  Click **Next**.

## Step 3: Question details

1.   In the **Question details** section:

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1772610432791-image.png?Expires=253370764800&Signature=hWSv2vFf5NwdjMEOPqrNrnRMIZLAHXy3l~-P8AGAXo7Ro8wCCIa0iUTQhKZHfD27Iu-v0BulscGJN5ychvmdTSnN2RdYYhgzoQtLMkwf0wsTDz~KuXEZQwmE2gciVaBVp0vCwH5Auh3sulinFZLoq1BnyU~7VxQyd1d1B0V6DCv1LPzkyN8EmL7ZXiJV4BcXZc5toPkcmUloDHQFnG~Eiol1JGDg1DpdZU~Xad2wthx-~yrJ~RvbTrmfBXBNo672o28lSN8eJijhbJTvo~ySg4e2wyNuAdEpDR5qcmz7XEbfQj4xf4xxCBRHRji9biWbu7za6YXp4iuQ3Wms8iDgAA__&Key-Pair-Id=K3NV4LZ47N8M46)

    1.  Enter the **Question name.**

    2.  Enter the **Score** based on difficulty.

    3.  Add **Recommended time** in minutes.

    4.  Add **Tags** from the drop-down list or create new ones.

    5.  Describe the problem in the **Problem description** field. You can use the formatting menu to format the text or to include elements such as tables or images.

2.  Add **Interviewer guidelines** for internal use, such as evaluation criteria, hints, or reference solutions.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1772610447185-image.png?Expires=253370764800&Signature=Eu~fwaQn86XRjOXwgOWo60DNazUBxCcG7AEKPcMFtr-viSm7lqTBdZG4b8xNZmAmwRXJ~yHl0dHXacdS2ED44A1B1nTkxWQRRXXko-1~f8O2p1-fINQMMdsLU9mmHOFagcxmp2Lxpjh-WK-RZ7VNWFjYkjS5PBiWvaA135dj1yk6nevW1~p954cT7CAScSJ1Z3tz8eLEgZ6i96jz1ab~HHkBAV83OR5o2~~Lb3oRfWB636j-JEq6mQK2-oEIVAnRJXmUpGC5huTnLXT77-ordrZBtWrNuM2inDX2XXR-zsaH1m9LNfMnNFjTSNZx2dKPjbZ4mfsPJ5qirBGZQ83dqA__&Key-Pair-Id=K3NV4LZ47N8M46)

    **Note:** If you selected manual evaluation, add the evaluation criteria in **Interviewer Guidelines**.

3.  (Optional) Add **Software Instructions** to specify required packages or software versions. If you leave this field empty, the platform uses the default instructions.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1772610752280-image.png?Expires=253370764800&Signature=aHEIF4pPZzx-7EXCF0Ui-3IuO2hat-z~hpw0VKPtLbRaxAcp74a-tbR0ddDBLqlU-5YeMGTqqxXQ5P81NamItYQnz9-iX~pH-ed5aE3amUlL3xIgYdNy0SbHz1x9EcgJAYaVopZoRTvIKS6ELVXFvETZAqKk-ddEAkmJjK798qeaf5m9hRvyYaUXwUduzP6Z7~uvi2ooZXULsHTz8t1WF76oZrGM7oB9gZMGMczi~dXNXMvvl06z0XqTYqnY7qEnm10i0yP4~bBW~zyX-sOxT6SZhAaDRFan0i5nZFTSUP3PDKOH2xzNN1AazyoADvrzlF31mCjvVSR6rcx18mVCqw__&Key-Pair-Id=K3NV4LZ47N8M46)

    **Note:** Click **Try question** to view how the question appears to candidates.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1772610684194-image.png?Expires=253370764800&Signature=dIZK1YJvO3S6Kpo3TLyz4kcNKX7M9A2WFq6lfXIbWrgTx3okFcikDzqHPF5N-bGQGSNjPNmBI6HjK0pUjhKGvOqaEfiU2tSJRyc-aDIj0i0BOr6oE8m3p1XDGd3-hMtSQB8hmKr2IPnFSt-GVKzDRur-G81xv6P6rPkcJGdmCjucizB1HQkhrAyOb6Zp01xt0zC91JWM8-F7MfvgFUAxRh2WJFQj4Rxt5lEM5d6vH-~JKr~tG1os4hcOFBZGI5lGeBA7hnLh2ft6oz2LMq3nU1RFRjaJK3apAr2YkCcRl~BYpqwZy4Q-qMFyZONqFY0l6KkXeSL1hkI0DMG~T7TZYA__&Key-Pair-Id=K3NV4LZ47N8M46)

4.  Click **Save**.

The question appears under **My Company** questions in the HackerRank Library.

# Candidate experience

Candidates solve these challenges in an embedded VS Code IDE within HackerRank Projects.

![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1776699940887-image.png?Expires=253370764800&Signature=JGmfuuC~3cb-vOrpEF1NfJnxfgoTWJ2K45Y3wJIUmgN17x~QxqdUxILJ0wFpsVeSqfYDO4oFVTLE8SLsrkWgjn2A9ZNQ22YHABcNRWFhGgkRE7v~rvJXwuhw58KnTkbc5ryttkWaN149r8BlAvrLEJ3NIvoJKwNvxjgimydePQtltainH3VtT7ldGrJhq9MNEwHjt4kzxjOUss333u5-uRzBZqiNvXPddjLB8fjI4gxE9hj-LSuIZKslojqI5biN2KbtJqyT1YmouHl~whRD9dulaKih4fOX-EHFSpjlHDXGrcAMfywYTCu8gKBtVgg2qF3~hjzgNFQf-MvklD04fA__&Key-Pair-Id=K3NV4LZ47N8M46)

# Scoring a Data Science question in tests

You can evaluate a Data Science question using **Automatic** or **Manual** scoring.

## Automatic scoring

When you enable **Automatic Scoring**, the platform evaluates the question based on the selected scoring metric and configuration.

The system generates the score automatically and displays it in the candidate report.

## Manual scoring

You can use manual scoring when **Automatic Scoring** is disabled or when a submission requires manual review.

To manually score a question:

1.  Open the candidate’s **Detailed Test Report**. For more information, see [📄 Viewing a Candidate's Detailed Test Report](/articles/8263794320).

2.  Expand **Problem Statement**.

3.  Scroll to **Interviewer Guidelines**. This section may include the solution notebook and evaluation criteria. 

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1772610822742-image.png?Expires=253370764800&Signature=lr0rqAI5GqdPBjO-mn8J7wtIs1rYvFQQaGkw059vCM7w8-AaSLRDUqfh6htiJujGstTl1Xayh5OjDv8f4XoxWmcgYfc1uu66na-LkzzLZt4fnJcvyY5CL7nfYBgFmJdbfGmXewOrMYXPe~mCBVBjTtKfzhkzh8goUSJLNXWTTFFjITi9F6~3BJMUbPtevu4w0vDrbrUySSTYVJK9sfdkl4IbxZ1HazRl0ORaxq4n1gHfwe6a3Z~LbS-mSI9QEvVasfhSxq3LPVTlbEpuOPcnS-etH0UWkm9DiqvZeWhT0~Tod5rY8xIn2~AUHlEww88d0Pck5meCMYCkHSuvf5yvNw__&Key-Pair-Id=K3NV4LZ47N8M46)

4.  Review the candidate’s submitted solution using one of the following options:

    - Download the submission as a ZIP file.

    - Launch a temporary VS Code session.

    Launching a VS Code session allows you to:

    - Review all submitted files

    - Run data cells and scripts

    - Explore the submission environment

<!-- -->

1.  Enter the score in the **Score** field after you complete your review.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1772610837042-image.png?Expires=253370764800&Signature=NC14GJJ0MY9F5zHoVP2YS72QArp~DrVfdC5vOknajLAyGIEKtn6OP~dSppPz8XOdWrXXOova930I070r~-rVgRyfW4JCfjomujgNJEApLHy0is29akaUkryG~hkLmi0u7nnqcw2~kcJSbDQaTk7beSgIE8DTnv07UPW4aMmj5p~jcOGEZidcjrHNFUvj5WZZ6-rvp5p2hBe9hdHajFCDnx03WgqF3u3cnW9hZ5ZhB2GaiDhdxOY4XyS9AZ6z7HMOGJBZtkaL3djuSw4jPHZEOVdeBzS8CBbj4EdKsEsS1G4SK2ax2sDBS6iZkKbd0MY~qgQgQPu4DnmD-XTP~8Q8XQ__&Key-Pair-Id=K3NV4LZ47N8M46)

\
