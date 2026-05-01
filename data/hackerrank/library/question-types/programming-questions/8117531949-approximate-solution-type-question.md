---
title: "Approximate Solution Type Questions Creating an approximate solution question Scoring an approximate solution question in tests"
title_slug: "approximate-solution-type-questions-creating-an-approximate-solution-question-scoring-an-approximate-solution-question-in-tests"
source_url: "https://support.hackerrank.com/articles/8117531949-approximate-solution-type-question"
article_slug: "8117531949-approximate-solution-type-question"
last_updated_exact: "Mar 27, 2026, 4:02 PM"
last_updated_relative: "Last updated 1 month ago"
breadcrumbs:
  - "Library"
  - "Question Types"
  - "Programming Questions"
---

# Approximate Solution Type Questions Creating an approximate solution question Scoring an approximate solution question in tests

_Last updated: Mar 27, 2026, 4:02 PM (Last updated 1 month ago)_

Approximate Solution questions allow you to assess a candidate’s ability to solve optimization problems where more than one correct answer exists, such as in image processing or computer vision.

For example, consider a question that asks for a list of five prime numbers less than 100. There are 25 prime numbers in this range, so a candidate can submit any combination of five prime numbers and still receive a correct result. In the custom checker, you can also assign partial credit. For example, if a candidate lists three prime numbers and two composite numbers, you can award three points out of five.\
Unlike the binary pass-or-fail scoring used for coding questions, a custom checker lets you apply your own logic and assign partial scores for more accurate evaluation.

# Creating an approximate solution question

To create an approximate solution question:

1.  Log in to your **HackerRank for Work** account using your credentials.

2.  Go to the **Library** tab.

3.  Click **Create Question**.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1771238266937-image.png?Expires=253370764800&Signature=AfdC~UAqvBPmaa4bGcAfT8c-J243N2qru9k-WkqcTaa~Vj9yf-cf2qz3VRInOgfvHD8001wbn0q3grlOjxWG6azh87a3doVw9g3yUKQf~LFntuMDSOJCDWDbS6dKu1IWEH4X0urSrVsvfuST432vBxI6mkwRIUgjA2q6t6DZgIzorBr-BH66lpK7XOap58uzILtw0y3kuxZGe-f1TiMolXPI7pLziIbWXMDfPlEp5V8aSDvy0Z7vZEeBihjmDyy48fz3efL85EmtoLrORO1IkWlh6AclFKBxrBSTC24o90D1apcQxtQcc7th5-s8~uMazOYPv30gNavCRK872JWJYw__&Key-Pair-Id=K3NV4LZ47N8M46)

4.  Select **Approximate Solution** under **Programming**.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1771238469187-image.png?Expires=253370764800&Signature=gaBuTw1XxRpe2jZlXXCSYrJ8~-tzm0FQxdsFBod7MY75mTFizsQlzuaYFvLjDGvxh2JLDrxkfBZEtcQb0FkFbXaXogUncCxUSDyCwIFpjyiFIJiy8E6Blzy4HFNKt7SSyGmQSy~YDr13wShU5U8X6Vtw-6Bde8W8qIL5wmSFu786AiYaDesdBOOdnuxRenr9LiXy12XzJoSwTd9He~9yCbKYTbJQjWMPPn2lrQTa1WPW3ltGaO02GJJahP7~TS5hC5CxWDW3lX72IVxHlJdtFCIYnnp8mNRYcPR3BmratMbpYcRHDMxx~5yOo7zEIUWnIYUjms7GtAXRkPovj8ZonA__&Key-Pair-Id=K3NV4LZ47N8M46)

The approximate solution question creation workflow opens with the following five steps.

## Step 1: Question Details

1.   In the **Problem details** section:

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1771238516473-image.png?Expires=253370764800&Signature=L5ZB0kpKVDVlyaIPTGPXxeeRKZGPVV~jsqIkz2wT9CVWC8AKsQxplmJoNZV~d4xeiTKVZ8x1C8i0vbMSZRsBEg6GdtvzRBuOF0CI~MdyQYa-hgZ8XhV79g7jXpR3YvZjOd7pnIsO-H2OHMyN4RmZm41CrCSN4-O6Gvvtp9zTMb-K5TP9uCGmHRSXDQBxwgmoaXsyY-Jb9kk75EgroNpqknrjKJpP4Pss38ocDyU8XWBF9bIbabF8r9MDDoETu6RRdQUjkB2aoNA~lGiwUcl~iedI45nUd0LTR19FRzR-8hw1zBvs27XHBzw0OcXxJQ~ABT3oBCHNjS0IKUg5X2iJ7w__&Key-Pair-Id=K3NV4LZ47N8M46)

    1.  Enter the question name.

    2.  Describe the problem in the **Problem description** field. You can use the formatting menu to format the text or to include elements such as tables or images.

        **Note:** Click **See candidate preview** to view how the question appears to candidates.

2.  In the **Question properties** section:

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1771238533443-image.png?Expires=253370764800&Signature=GaSuU83MZxMAv6IqdN6OfKMkEHlAnQKcZH2aqtpKZXQU2JNrRBvop5~TKVM1VQsCzRYwVOd25lr7tQlPNC-EXEGp7WRR20R3zMxFp-VOzBmRull-wJj7w3lYvu3moCPhbsONCWkCiBRoYa3VE-g9Lys2ziSERan1mOpaXtBm8QRld758ad80SPlVUrbE7dUB9OEkrcLaUso6XVckVH01tzmzfiO9hk~3LQ3EjMFogqC8qceIkjjA7mR8KL9wi3VjQfLTEAVNhChtH49Dn6cUPZxB~kjLhz5MnBQW9~C614J8VB-Cb-uyJV7Fp6ysqYaNIB81doSgbMc26vm0aGT58Q__&Key-Pair-Id=K3NV4LZ47N8M46)

    1.  Add **Recommended time** in minutes.

    2.  (Optional) Add **Tags** from the drop-down list or create new ones.

3.  (Optional) Add **Interviewer guidelines** for internal use, such as evaluation notes, hints, or reference solutions.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1771238542860-image.png?Expires=253370764800&Signature=WQoUbFs~~srb2goN-s1XrkuJ6W0gBKivBX7Pfpf3eIWQWSUIb0MUYO0lM89sI7016XRXASWCPoguEHmnLu4MtlxkxdW-LmADcY8Gw~bJz1iy4YyYgtnWJlYZuZgW545LggsbJ3t84Y8YWjKjjvwUZCXFQ5jeTgn63lMYZ5OgkVYd2b32pO4R4wzjT2q8ks8GOlEqKMsgObi5ETpKMvFm1rbhz75Vc56Mw5zXlpgq0hJtOxmfvS79qnOa35c1JAeUsvX2FNsTE4RYvmbSE7KYmmk5~baCWvSnCzf1CLpsCbBX6h237zp03LDbyXzeiHk9ktul9nsmwrsMXi6uHdRwWA__&Key-Pair-Id=K3NV4LZ47N8M46)

4.  Click **Next**.

## Step 2: Languages

![languagesapprox.gif](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1771238620836-languagesapprox.gif?Expires=253370764800&Signature=tQDpPPD8WJQBAH054Kkj5-BMBWhoQL1C8c07jegpKgp0mKDI6z~fnY76nqgvQmxnotEAIYjwO0T136Ndv-55z4wedbjvjusxMtKoMmPMmar01vGjd8rxM02DA1h2LRhE6A6sA4Yf6RvPa2yr75jsZcxX5ydso5vXMS6J7XSIZ8328NBmrTkfpZBRdUpLJSQJpva1K5lJrzwD4LCtU8yQimawj4ySJ~JhfV0P3ntuo4gTbbmgbVCpa1tOi0pLoR~Ag18MBpXM05YfYTczWRCy81vlG249CN9kSFEikRjnEJ~wvJ79sE0vtVyLW4IbhTruJn~jJym9Y2PIQzYn8Bd0TA__&Key-Pair-Id=K3NV4LZ47N8M46)

1.  Select the programming languages that candidates can use to attempt the question.\
    The platform groups languages into two categories:

    - **Popular languages:** The platform automatically generates code stubs.

      Select the **Popular languages** checkbox to include all popular languages.

    - **Other languages:** You must generate code stubs manually.

      Select the **Other languages** checkbox to include all other languages.

2.  Click **Next**.

    **Note:**

    - Click **Select all** to enable all languages.

    - Click **Clear all** to remove all selections.

    - Use the search bar to find a specific language.

## Step 3: Code Stubs

Define the function signature and generate code stubs for supported languages.

1.  Enter the **Function name**.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1771238657739-image.png?Expires=253370764800&Signature=lywXWOBiLQ2Pt2BT-2Ussgjd92Nlk6ijj-HQ~CVCE8meaLgzFY-ajKrWlEY5pGJP8B6~6SbNVuPm55No3WSskurpnyg~tt2fqWkbwzvnavHp2c4Dxu6NsoEdYhoWt1glfyJQVnHECBXo5Hm6ErXLJc04VMlMZCYaKKe8PM9qBq9EHgwqzLlNpIULZ0aYFWaBMSm83UD5v~h-6QGt7fG59JSRHVN7QiexGZrVOwhZk-rkXG1eqK1ez-gtoA3RSBW8lr-ICiJm~DLDxN665314o8qVnHZD7B9bgEi7CSg7-MGk2JmPuRqOu1R5rhcSbws9J4py5yfzZ7kN-Y87f2iFBw__&Key-Pair-Id=K3NV4LZ47N8M46)

2.  Select a **Return type** from the dropdown.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1771238666115-image.png?Expires=253370764800&Signature=Bf5e8XZ~nfmbe9YC1OZzjOx4XRJ52TEdxhkLkhOgtUB0j1RJNKULOtXXbOw6E1QrTstb79-MJF1LgWUBGCZuN5jRZqLQjyjTGXhaXmNQKEq~kvnr96WzGL9UHdm5VIQh~R2QxU8eSUuInqQ6HaKjvYuCgpCk-Ng8c6Fs0Z2wbQFE7dqzJU3WsODGEhsmUbpclT4XPpyk5Z2wVt0wEN3EmphHPkbPP-gef1-l8-OB9nb-RNBFREme8IfkiTB9xZQaePt6vjO3x~Gw2ncmOPAtFIBUrTk2OpEaG6VEwAjK0LsPpmE0bo~kdKcizyqI0qbg~ZskSefNERtpc7wz1cQofA__&Key-Pair-Id=K3NV4LZ47N8M46)

3.  (Optional) Click **Add function parameters**.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1771238729601-image.png?Expires=253370764800&Signature=hupm7KyIQT8yX0fgxPecax9-rR663qZDPpBI9YyVlr4GQkKrPzhpYKcH4CTsEQgUSbMs5PjyCZQah8WRbE7Ee1FsIpSUovcAYMMiQsTXgO3tGc6q4vHuJOjz0DbsqION-ub-yU0r9zNAfSUhsVwhrCmtkzvJWYZa0JxJ6IKdvwHBWS3kURGVbYeyY27ZCkAUSGttQn2dYiMzWIrgjoRqQEYmPrN53PusWQOEs0l3ZtJJAFq29jcAt3HoDJR2fibvbQPnJv-Q7Q2wBPT0fzgpU73Dpew808FMiHnyEwLZ6UuLq4bAXpBZppmobu3xy05dKPUqchWbmAjxR3Y5yXXghQ__&Key-Pair-Id=K3NV4LZ47N8M46)

    1.  Select a **Type** from the dropdown.

    2.  Enter the **Parameter Name**.

        **Note:** Click the **✕** icon to remove a parameter.

4.  Click **Generate code**.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1771238760102-image.png?Expires=253370764800&Signature=AzPxkr496-gskkyOCv7uuGm-4lzyvRpKEMIweycLOQXWySnzzpS5aPUjWLu0gB7YAdCIOUXFJTYg-4JoGoc7tFqy6336vDPtadk9bfQZHVlQgaAYMZjj1KC01Erm1wFyWpwXWPeQ5Pyr8wLAT8k6v8JO8sMxzCKTP8StgX08J8Jx7Y2S1Yg7hlL6KvlQrak35a8E0JS-qgX~5AyWuAFMn6MRrwMj9cTG1Jt2Dpsfhmwxljx7tMVys-sxNfZlik-FYYTiqCRGqSRwQlJud5ZIdnHEO-heQHFuLXv1xoCSkftfDJnqLSXwPdAhbUPDvwFVkqEgeFxRQQkHMW2o1Byixg__&Key-Pair-Id=K3NV4LZ47N8M46)

    The platform generates code stubs for the **Popular languages** selected in Step 2 and displays a success message. If you selected languages under **Other**, follow the steps in Handle unsupported languages.

5.  (Optional) Review the generated code.

6.  (Optional) Click **View in IDE** to open the code in the IDE.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1771238780225-image.png?Expires=253370764800&Signature=L4MvzxilfSNqMdOlhRI0GsdvJfLmJHIzSfxCVzfZuebJr9pl~mMYSD4IC62aiHABqRXEmFSpEIKruFdkSlHhq0o76OvcD6HHp7rbi460LjgPyVVLNYcoVC5zxezwN4PqPiCe4bQcFa-TF4r1fooJajoCS5hyhwARzwjkDNGXYsp-LR0WazvohcsGZmX3dHqfMJBdZnSqoruy-xXapodAi4AqFJWvD-Ixqzxlw6DiEXtJGafOb-n5GbNdO7TPfMoyCFcuN1UJZTmt8Sa3AK6om40ab22Zzwl04fgLElN3HPUws-K1p7VCZ0KyX-F7gObPUpgNz0FWEa9nmfQjdHa2sA__&Key-Pair-Id=K3NV4LZ47N8M46)

7.  Click the settings icon to enable or disable **Keep code stubs editable**. The option is enabled by default.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1771238791721-image.png?Expires=253370764800&Signature=Fl5ptCTSQVsircnsZ9bbWHVMUN0oAUgZCPxTLB~-R5bt3Nf17aMfbY7yTLC0zktlt8maDQIwuE-IWPD695mjG~8-~I569ttlbgc7uRzZgnQTjVOtdhhCi6bVZ5dyCSSvXYZRtXsS1a4xx5IoLxYcKU-UKqaPoIn3IJFZXHsQxHeBdv~GoZhZCFi7Ru5-EJ6SFsRKM-vzSJlrptFUQnZ8Bo1j-Y8U3uFb~idZbOEYg4vtyNxvJO21uQO3ryU0UTUyoGES-RISagQqQ37V6hnCG89Dy7zL8YjNOoWgEEDLy8GXYYamCBLilA8izFFiW2GGFDo2KJUakUs5YH7zgl1u2Q__&Key-Pair-Id=K3NV4LZ47N8M46)

8.  Click **Next**.

### Handle unsupported languages

If you select languages that do not support automatic code stub generation, the platform displays a dialog listing the unsupported languages.

![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1771238928822-image.png?Expires=253370764800&Signature=f8XDhHRHz5Y01vqXMVlAhE060D5M3Yc7r1dk-AQfBDs3FPP5a4uVSGwkXAvk9UISC1G7U5Vq5KpzWqmqps4EEG4XDSFhpRFoAJCpuCIxWSn9ZOxWzO0FiPoNsoOrDh14wgWNSPhLzUlb7xIce8BN8VVO-JlPRbvlXqXascxd7jN6lxupb-2vvnZMan5ZwWQ8bTsIxLr3PSdY-Bw6bb-zS4awKxkkb0yns9bcMUoo7tSXfxton0I8FOsWK-nIsGuaIigkzeZkaLhnUI9HZcVVkbWhvYA6y5Hrec2xp9nYBskn5NcDrbnmPF1AChRMtae3IyS7IY2jGmJ~G2NJyvU7jw__&Key-Pair-Id=K3NV4LZ47N8M46)

Choose one of the following options:

- **Unselect these languages:** Removes the unsupported languages from the question.

- **Keep these languages & manually add code stubs:** Keeps the languages and continues without auto-generated stubs. You must add the code stubs manually.

To add code stubs manually:

1.  Open the code editor.

2.  Search for the required language.

3.  Add the code stub manually.

4.  Click **Confirm**.

## Step 4: Testcases

Use this step to upload solutions and define test cases for the question.

![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1771238961688-image.png?Expires=253370764800&Signature=MFvLU9NNttp43BcfLwcFxcYuoRF0GNs1yRNAcvayDT~4kYaBzD7IjcJLbUskyKQjO3pjDEv5ipWXf5JqppuFJij7Dos3lgBcMinDw9nRAbIAJ0jP4Im3aUCw7bFQjhSa1D1gDXmSZK53XyMBWiQXUZwlCh3Z6nMjeMCVliXn8YDwrYfnVyf8WgKymiJ-eie06DSkC5XoemaItzYdixqoFGAzZdYfqdNiJM4qTf7u1YKAHjiI10jyIzsxembzYwXgF8Ae~pG9qOYJkph7OWnJq~CJP6osb-9vJLUyTNWVbmx3Wjo40NobG~65FBe9nGuOCayhJtBqXveva4awEMjLIQ__&Key-Pair-Id=K3NV4LZ47N8M46)

1.  In the **Upload Solution** section:

    1.  Click **Upload Solution** to upload a solution file.

    2.  In the **Upload Solution** dialog:

        1.  Click **Select file** and choose the solution file.

        2.  Click **Language** and select the language of the solution file, or select **Auto detect**. Auto detect is enabled by default.

        3.  Click **Upload**.

2.  In the **Testcases** section:

    1.  Click **Add test case** to manually add test cases. 

    2.  In the **Add test case** dialog:

        ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1771238980971-image.png?Expires=253370764800&Signature=DgD6rCTdgKfanMUznILEt~b7t1~r-DxaKiSKfsxNd2fHKCnmNjS3jPtMc4-ICr0KacCsDF0n6oudC55WFvFbUTOB5VdWPAIaLut3AlvKjCrJ5MQAeyi-1gdjHovOFqpTFh-4ZrSbDKv1KM-xoDPWQQ0P-uOglpLoQALW7jhUP4MAIpBuKc3vWMCKTXYE4Ln64DPfoeICSdmUIU1UYBw0cEg-OO~fG5743AGEMeAVxibq~ix13HmqPabFe~BmfnWI~HG2gxt93Ax-9OdDd9sQoZMKd0whFNHWZDlB1eCzElARmurQ5aNJJbRH6OyA4hft~~eNirEzOYY6o77AUV46Yg__&Key-Pair-Id=K3NV4LZ47N8M46)

        1.  Enter the **Name** of the test case.

        2.  Select a difficulty level from the **Difficulty** dropdown

        3.  Assign a **Score**.

        4.  (Optional) Enter **Input** values.

        5.  (Optional) Enter **Output** values.

        6.  (Optional) Select **Mark as sample test case** to make the test case visible as a sample. For more information on test cases, see [📄 Test Cases in Coding and Approximate Solution Questions](/articles/3245197419).

        7.  Click **Save**.

## Step 5: Custom Checker

Use the custom checker to define scoring logic.

![customcheckerapprox.gif](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1771239059690-customcheckerapprox.gif?Expires=253370764800&Signature=EK99azIP5o9IF99zV8X6zxpvNuQJoMpDkBnwMEoKrY2gEZXtvOmFZyahVI8ZjVlegCMSjn6T4uf0MBlqhehmszuSn3BQP~XViP5hK75J063xBhBz-snU254tc6f1rNeFWsz26Fs-V8VZeIquF1nAO1jMK6KDqBbixf5d2l77cagVULTzl9ikFa86V0pQFbroa5d1jtUQk4uf9F6Oo6Wb5GIBxCc8fUf-BlcyO5a2ndapG9aFTjp9ItosGh8nsHj7GMKmRN1Ss-iBC79QsqCFw0muahoIT-f9nw3bP4-iwzXSj9YBv-8EGNV-tWci7JBbQXz4OOYKcEPHnK5tt5cgJg__&Key-Pair-Id=K3NV4LZ47N8M46)

1.  Edit the body of the custom checker.\
    For more information on the custom checker, see [📄 Custom Checker in Approximate Solution Type Questions](/articles/6515044510).

2.  Click **Save question**.

The question appears under **My Company** questions in the HackerRank Library.

# Scoring an approximate solution question in tests

Approximate Solution questions use automatic scoring.

- If you configure a custom checker, the platform uses it to score submissions.

- If you do not configure a custom checker, the platform scores the question like a standard coding question using test cases.

## How scoring works with a custom checker

When you use a custom checker, the platform evaluates submissions at the test case level using your scoring logic.

1.  The platform runs the candidate’s code once for each test case.

2.  For each test case:

    - The candidate’s output is passed to the custom checker.

    - The custom checker evaluates the output and assigns a score.

3.  The platform adds the scores from all test cases to calculate the candidate’s final score.

For more information on the custom checker, see [📄 Custom Checker in Approximate Solution Type Questions](/articles/6515044510).

\

\
