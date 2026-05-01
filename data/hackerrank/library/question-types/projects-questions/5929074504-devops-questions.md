---
title: "DevOps Questions Key benefits Creating a DevOps question Candidate experience Scoring a DevOps question in tests"
title_slug: "devops-questions-key-benefits-creating-a-devops-question-candidate-experience-scoring-a-devops-question-in-tests"
source_url: "https://support.hackerrank.com/articles/5929074504-devops-questions"
article_slug: "5929074504-devops-questions"
last_updated_exact: "Mar 26, 2026, 5:23 PM"
last_updated_relative: "Last updated 1 month ago"
breadcrumbs:
  - "Library"
  - "Question Types"
  - "Projects Questions"
---

# DevOps Questions Key benefits Creating a DevOps question Candidate experience Scoring a DevOps question in tests

_Last updated: Mar 26, 2026, 5:23 PM (Last updated 1 month ago)_

DevOps questions allow you to assess a candidate’s proficiency with Linux through hands-on tasks. Each question provides a sandboxed Linux virtual machine (VM) where candidates complete real-world scenarios, such as:

- Installing software packages

- Creating files with specific content

- Running command-line tools such as `grep`

# Key benefits

HackerRank provides the following benefits for DevOps question types:

- **Dedicated Sandbox VM:**

  - Provision an isolated Linux VM for each candidate.

  - Candidates interact with the VM through an in-browser terminal to complete all required tasks.

- **Performance evaluation**: Test administrators can review candidate performance using:

  - **Automated scoring scripts:** Scripts validate whether the candidate completes the assigned tasks correctly.

  - **Session playback:** Playback lets administrators verify:

    - Whether the candidate uses the manual page (manpage command).

    - Whether the candidate performs tasks from memory.

    - The overall command-line workflow during the session.

  - **Automated environment setup**: 

    - Offers a fully configured environment.

    - Test creators do not need to perform any manual setup.

# Creating a DevOps question

To create a DevOps question:

1.  Log in to your **HackerRank for Work** account using your credentials.

2.  Go to the **Library** tab. 

3.  Click **Create Question**.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1771230778483-image.png?Expires=253370764800&Signature=JiWExMnL-70KxO5JK7BefGvzwbxovPh8eJSYWwwisIQXYvhdG5yKtFZ4ikaDsjjAZqVM3-NrS5RdIK5f6nubm0amhI4gexxzwLobg5HEhagYKx49YLSCaAVlbQ-XHFjBrTgyGV0r9GsNg~Vq0HTm5jaoovLuPhyTt8LavfJbYicAok7f7F~rsIiPt70aJ5~C~LQz67D-eLnJgBaA9nUn5CAdTzOSWDK4Ao9EArja1bnE7IeIA6KHDS~Uw7dCeS3tZ1rvcuWc3V8~~WamSiK-bKUqixpoDMufOpYiErvWrmWJfA1Ib3Ih2qEwW0LA6Lnt3IH7mdprH8iKdgRrlsJJXg__&Key-Pair-Id=K3NV4LZ47N8M46)

4.  Select **DevOps** under **Projects**.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1771230464610-image.png?Expires=253370764800&Signature=G-6sse8q4AO0kM3hhUcAUfGZBCAywHrrnyyXOnBJYZi3QhdxGbhvFa~Dy2FfUAoRBCA1pVcUr99gyWBq8I4jt5p7Qg4DDyIwg4m5bq4HNKvVhNdTTYhGsAAsfGhd2VA1~H7l-P3EfNlXldzw8hTg03feZ0kgp9jUs74be3jgzN7vkaWv8y0bWHY48zXSrVDGjYQuUXOmCW0tSJBERGRqo0uOuWX7aEOp2fMqJa1aNcCJuW6v-Qo~lAkSyY0zTm1jth5JH2JjxX9302AMQrjJr0AutCyW0pWanAvsErMlMMzw1PK8s9adCoJTjA78m7-NrapSCQYho10ABvehfEey8Q__&Key-Pair-Id=K3NV4LZ47N8M46)

The DevOps question creation workflow opens with the following two steps.

## Step 1: Settings

This step configures the environment and scripts required for the question.

1.  In the **Environment Settings** section:

    1.  Select an operating system from the **Operating System** dropdown.

        ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1771230884166-image.png?Expires=253370764800&Signature=ZRY5ud2p0wsLwu28Hr8LiwGgEwrWiJ5rElwvpN9yRolaUni7aB8Uprx6Tawtz1fgJ~fUrbBqYjX5Rzqh0~-VZRSEREYkxJrTuerCZFvFGeEmw74qV8MLWl0yGVowI9nHhmK3UHfCEa3rzTqMU61SLYmD1VlCNmWfTg4C3KxSm5n7o0-bCBIDmQ9V57ry3ajSzgxKfPSFPuPLi58PysdY0GrmvTBMefJqlnBGy7rukklFESPORtXgKuJmJehylasRm39TiXRR3QoImqjXZHHDZQl2yS5uMmSeda4Y1xFu2pTcdZk7hrchVSn7Bv3EPcZSg5VPMNgcceYgURHZqyn7zg__&Key-Pair-Id=K3NV4LZ47N8M46)

    2.  Select **Yes** or **No** from the **Root Access** dropdown.

        ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1771230960510-image.png?Expires=253370764800&Signature=Ou9X3cqFYqQWo0RCxVitGPecfMVTLFejgGtPc~FOT6YvEp4O1~1pEH55KDC~70kbj3SsHVhEAT69GaHaUmDeuDVgAcVuJXw8QOrm-ilynADOzTvbE2OO-mLJENFaKnoYd-vfA0TYVrXmNJXlqy0dDwaCkZpanADlJLpsFT6REZ6ne8ktNn3EL~Up1W1bgiUIZE4tYOQmF~eB0O0jjHoyHZWn5mWljWzyAEAs0TKSg~KwD6l6AGBnwhvEqxczlI8sBiuQmYPhXrp4I0esLyjBqtbDkslVeDJRpZEzHluVY2TVoiFvpr0QUn1pmAAUDV5YH7NyVI8iFQy1uN1~bTm0eQ__&Key-Pair-Id=K3NV4LZ47N8M46)

        **Note:** Candidates receive root access through the `sudo` command. If any question in the test requires elevated privileges, the platform automatically grants the candidate root access for the entire session. 

2.  In the **Scripts** section:

    1.  Configure the **Setup Script** to initialize the environment before the candidate logs in. The platform executes this script at server startup. You can use this script to install packages or create sample files. The **Setup Script** timeout limit is five minutes.

        ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1771231045731-image.png?Expires=253370764800&Signature=hIcwCVCQwIYWHgwm3p0m3XwttX5ztGzWKX-0DIFoJaSvEgL6NXDkf7qqfb8yAdANbKf4esCcpEq8Y~abBjbWrLDR5EhlnCKPisqu6zWu6WmGmP1cJZvvcEVygZJwdO6agQObrIxMCdpcNuz0yuIw6GIIC0tTb5FidnGjrkQUc3ZG2RLh~KMbsWrIcwU3qKeLwohYH0Mev2rfHPavr-5eIjm4dLySkcMvuQuY1wZM5vOpu8uYL1dhL916GKiKSInggiPuHusJjOve3oyjJM4pR9oB54kqDRxyfd6tHRaFHfHsNL1pqa7tMbr~a5GVMAp6eQoLXxr4CbgXG8skGnC~Xw__&Key-Pair-Id=K3NV4LZ47N8M46)

    2.  Configure the **Scoring Script** to evaluate the candidate’s performance after they submit their solution. You can use this script to define custom scoring logic and award partial credit as needed. The **Scoring Script** timeout limit is twenty minutes. For more information, see [Scoring a DevOps Question in tests](https://support.hackerrank.com/articles/5929074504-devops-questions#scoring-a-devops-question-in-tests).

        ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1771231010089-image.png?Expires=253370764800&Signature=ZFzZ-xyscBEeCKoPlHHvprWniIVWz1XOUmWbb6gM6Dj6Y-1MugchqcNvCEzxDy94H4cgcpwoNVxgpUdA7rCvqQ-IM9EL~K3xu3lHE8AL0cokyZLFvm0~av38VnfhavYdzhfNijH-KwXSBT4xYgXgk2OmlfZjMaHgqiNa9tXVGbWhizs9MMwnvsOU4Y1o064ot2inQekvn0mNNMwl0iFF7RVkq7g9XvzYkBnqz5gwqZxqBMOkypwtZlxppaXH0mZLETUnM1AxYQfo13rkphgUr7h7e7NHCGRToJzxADZ4kb~LEtmjI795xXypi2dDRtQ4S2WBv7zWNNIufhV0gNegkA__&Key-Pair-Id=K3NV4LZ47N8M46)

    3.  (Optional) Configure the **Evaluator Solution** to store the correct answer to the problem for reference. You can use this script to solve the question during debugging or testing when you try the test as a recruiter or admin. The platform does not run this script. This script is placed in the /tmp folder.

        ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1771231021853-image.png?Expires=253370764800&Signature=mMVp5Wldsy~MYh-2ApNV~S1EZI07iNKeEVsGd46yHy1p0D45ndSNsE0-9PyVTnrJStfXxLD2crm3HwbgMeEkrB9nN1S7Dp0Kw6OWsXtl~Aa2nLWLbwP8nFSHMOUBZrV6NQ2xed2kkwx2rgseViNeTMj5-0amlPIKNQNvyLAuXyZZ-IoUM19j~eI8d2Flv~czYARE4qQIvVJOLCJuO2YGetvz70dDWS7u9w1dFTLDXKN9vzCYEutNzUxp85djdsPTS2FB3nIKWPr3vReU-BR0UPKHxQe0RlU3sUhFe2mSIiow43yfPdn5mn3xDgooA6e8WjIqfqj8LhOnMHF7WL-efA__&Key-Pair-Id=K3NV4LZ47N8M46)

        **Note:** Click the expand icon to view the script editor in full screen.

        ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1771231302040-image.png?Expires=253370764800&Signature=DFr6BuQGIct47HclZnb341UBluDCTZ~FPITiPnmrBkjZhkvwD5jliP9cXbK3cGJRljIMPSd~iuKHbhbbV3T-zvFNRIrsJAlQ206nu8Mm0eJFGIOgSzqZr8nTSj7JoqtUiMmN8VwBLDRV~5UTp2LMhl~ZU3ubS8lz8uONFCjyB04qtrdCSKVd~pLslc1Z00Fs8lctPZsz7TdS5i-ShloUxnyDEpqQML3Rxc49p7EWFh7dAY~aOkiVTsyGbOP12abQq1l6t5xRzfGR0Sh2la7EKR1cYqnYEzLFM5Lr~qng7xvMgimD3LWjC~ar6SZjMoq19oVJwmgC~e8ZQyvcL-m~OQ__&Key-Pair-Id=K3NV4LZ47N8M46)

3.  Click **Validate**.\
    A success message appears when validation completes.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1771231899649-image.png?Expires=253370764800&Signature=iFB49~EKr8HSQMrSlyLgJk8cHnDJVCw0XEiFRhoZEracLTqyC7v52WU3udwk9wPLf9vJGSwpWQdK3XvU8hj8rVVJIo-28zhq2~39g8PV4gA~IEZ5PmjQ-74TZ6HJQpp0olrgj62TCFbCIcB0YDSA4Z-sb0k07yZ8TSAQ11kOz0i1W4Rvxq2iPuuu8wRa2F~vNdvKK8Uuk6QJaEQhGXXvLuRgBLzh8AmHRvF70~yetbgYkfe42UtUn7YFHy1s-hW6p3hIMlFGAmRg9VW3YgQ3wT3GtuCx24bx3IkdzFJUu5qFRB~ArzNIkn72s2okxQUGi2QEKLTCn3aVDds6QabG-A__&Key-Pair-Id=K3NV4LZ47N8M46)

4.  Click **Next**.

**Note:**

- Validation fails if the **Setup Script** or **Scoring Script** does not run successfully. To troubleshoot, click **View Log**.

  ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1771231446397-image.png?Expires=253370764800&Signature=eSxVk1O6eFFzaXt6WvFD0~gmzHrvYJgw0rEM5Y8JBC6I3ChcdA7839kVaQkPU45fcdIbwnNqNqDPiSD3N0faEfb42-X6KAuaJH8-plaXiXZ1dyvOehYk9~4EUpfLmYTVmXorbH5JM1qg9KBwoGlDmCgGttPnBZWMyYhvJEh43HvttujkNtE0teuI0NLf96jHI3u0i0dOyhjQn~LQ99Nolwy2gt0THGM1rnARRZPMMxOzMcci-kzIYYac2hQNf6I~fHljr6zCVlHI-njF1WnPFx-MrgwQyYCgWc8-gUfG5~dAeTj0q3beGeUD28nJrBuyEnXURAklq-n~MVINJunidw__&Key-Pair-Id=K3NV4LZ47N8M46)

- If some test cases pass by default, the system displays a warning during validation. Hover over the information icon to view details.

  ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1771231462774-image.png?Expires=253370764800&Signature=iLzKa6iP75uem39I3uKHJaobXIU4UqtuCK1~FgvbdQBFV1lXKCDXmmalpnyTVKQa8BAcPF66rWcJIzXJ7u3uD7P8dNaAFKWxMz98UnJ141Cvg-lsGgz7To8xAGZQxJ9SCqxmwHviwZ399HX3FxIuMygVVxVt2wkf7HRRVA-s8hDQ6nAziVq-pZr3ZWZMEXglYFurtOgWj7tTC9XTD5LBa98qorusy1Doj7ndTHRFE4WiCRivtmz9bl8I5LPSbSlbKZINKUiHWNcQE~xRCd30DPnprEHYBP~NA2d8SZKJyYvAu5RWDcT8o4eJCGqpMnk66tOzicxghqhVKlOLl-EaCA__&Key-Pair-Id=K3NV4LZ47N8M46)

- If the scripts contain syntax errors, the system displays a dialog box. Click **View full log** to review the errors.

  ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1771231505401-image.png?Expires=253370764800&Signature=EJkuYyhrrX8evy~~wasE8baLcGcHUyxapKV1Y8Ofvsbqrf4ZiKJMBp-HkPMkJSD7FlITeInSwFzSOHz4Vp5kODHfKBgCHc4CakZjxHLHGN4DZRns3qP6nF3gnuSLtyjuI6xuFshL~mEZMDXTjGNdbj0XEnhJ-WF73mblMEIdrdC~7VdAMQQLesqFdWRG1FDnQT1ZKpeXlDPAZeENOG2nJM0Ilx2M39ZFr8Ef2Uqovjw-U9sNcHmW7xJ7YVU6C~YFN52xz6pjKG1rh5tiXyxT10--GifRhXtM7IxfS89-SIM8IjUZwqej6Mf0rppR91m4WT1MoAcLUIKeFJpiDXMhZg__&Key-Pair-Id=K3NV4LZ47N8M46)

## Step 2: Details

1.  In the **Problem Details** section:

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1771231670575-image.png?Expires=253370764800&Signature=sq-0acXc0QO0nYM4xdUxDFReb6wgnGqS20K2x0ofpCLfGOqLfrqyx7QqE2ASDSPWyOFYlDd2LJZsFLffik~bOJNPrLR0nZws00QaVw7iuvgZT7SQU6KOuV8SJMFjScwVqhvgi534fnHOKQcjy9oBxwb8a67jfMg0sdq6lGJJU2Pvw1VXQbobnWPOc8yW7PtxXUxQXaOaos7liVoDzPZai3x6KYr2Tbkdnwcehwqw7lUgVlmh6PzwVJiZdUt-3FqNBdSh2C3b1vbSFhxq3f8~H0SugzbH~p9iIiyzJ3cpF82dyaaxX8AzTQOgfX1XYlpRkHvKAcGPt0bpFBkb8EsTXg__&Key-Pair-Id=K3NV4LZ47N8M46)

    1.  Enter the **Question name.**

    2.  Enter the **Score** and **Recommended time** based on question difficulty.

        |                |            |                      |
        |----------------|------------|----------------------|
        | **Difficulty** | **Score**  | **Recommended Time** |
        | Easy           | 50 Points  | 15 Minutes           |
        | Medium         | 75 Points  | 30 Minutes           |
        | Hard           | 100 Points | 45-60 Minutes        |

    3.  Add **Tags** from the drop-down list or create new ones.

    4.  Describe the problem in the **Problem description** field. You can use the formatting menu to format the text or to include elements such as tables or images.

2.  (Optional) Add **Interviewer guidelines** for internal use, such as evaluation notes, hints, or reference solutions.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1771231722195-image.png?Expires=253370764800&Signature=U-~p-rr6oadWSyePqHu37T2T6XDNiTtvZWPLn5n4Q7-BifPz9g8gPFivQZB0bOTbIXKeaz0CuVKLSil5XS-8wKMi14D6BGaPQUCk3FMrzdiRfWG26wnNFj~CrSYBqqTsETQcn2Cu3pTVCw~ilGbdl-82Br2A12AlS92tbe8eofaaUPtNo44nZluppWLuqPDxD2jLGTEymSyFVUXjr1Ghn~8AREz9FUvpNvI777sZbKZ2aTQ61hS~mt1Fa-fspq8Kud7x37JKdK16B36~r1O5UXLjQpxeYoNie59-6rYf75yRf3~o1zrnm7Xf0SzQCyBfglFVevX7Mz8cfqW2NscDKQ__&Key-Pair-Id=K3NV4LZ47N8M46)

    **Note:** Click **Try question** to view how the question appears to candidates.

3.  Click **Save**.

The question appears under **My Company** questions in the HackerRank Library.

# Candidate experience

Candidates can use the terminal to perform the tasks described in the question.

![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1771231528456-image.png?Expires=253370764800&Signature=cPgCCdEEuiTiACHm0~pRaL8BCXvUVAIj~~mLuEqOkHuY6CwB3SVwGSJMWiHxkbyFV5f3~ooJ29hWP5pqy8t5LZTY4btwcOto~bMG-ApGPJVPUtON99B7KE14m7sE11Xx~HLVeU~NAK1fp097b5eOi1b~g122socaTLguh9vDkSc50KZn6ySSDl~8WZLUjiu~6Ss77p2il54lH5r9hIecUf2zMQqqW~EZxpzS~i6-bPDcB9IRBpkAhFrbmV6BQb~NRRgqaTbQwYTl37RhnblxGCg4iT2~22GbL0hHCpzuLP-rF4tqBPrry7KJJ0arBYttw-rOY-QEgus0nUIVTlHKMw__&Key-Pair-Id=K3NV4LZ47N8M46)

# Scoring a DevOps question in tests

DevOps questions use automatic evaluation. The platform runs a Bash scoring script to validate tasks and assign scores.

The scoring script determines whether the candidate receives full credit, partial credit, or no credit, based on its output and exit status.

## Partial credit logic

If the scoring script prints one or more lines in the following format:

```
Partial Credit: <value>%
```

The system calculates the score as follows:

- The system adds all printed percentage values to calculate a total percentage score (x%).

- The candidate receives x% of the maximum score assigned to the question.

- If the percentage symbol (`%`) is missing, the system treats the value as a percentage.

  - Example: `Partial Credit: 50` is equivalent to `Partial Credit: 50%`.

- If a printed value is less than 0%, the system ignores it.

- If a printed value is greater than 100%, the system treats it as 100%.

## Scoring based on script exit status

If the scoring script does not print any lines in the `Partial Credit: <value>%` format, the system assigns the score based on the script’s exit code:

- **Exit code 0:** The candidate receives 100% of the maximum score.

- **Non-zero exit code:** The candidate receives 0 points.

\

\
