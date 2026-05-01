---
title: "Hidden Test Cases for Front-End, Back-End and Full Stack Questions"
title_slug: "hidden-test-cases-for-front-end-back-end-and-full-stack-questions"
source_url: "https://support.hackerrank.com/articles/1626384486-hidden-test-cases-for-front-end%2C-back-end-and-full-stack-questions"
article_slug: "1626384486-hidden-test-cases-for-front-end%2C-back-end-and-full-stack-questions"
last_updated_exact: "Dec 24, 2024, 4:52 AM"
last_updated_relative: "Last updated 1 year ago"
breadcrumbs:
  - "Library"
  - "Additional Resources"
  - "Project Questions"
---

# Hidden Test Cases for Front-End, Back-End and Full Stack Questions

_Last updated: Dec 24, 2024, 4:52 AM (Last updated 1 year ago)_

## Overview

HackerRank Tests allows you to hide your test cases for the Front end, Back End, and Full Stack question types. This article will walk you through the process of adding Hidden Test Cases to your project file.  

## Steps to Add Hidden Test Cases

- In the “Setup Project” step of question creation, you can add test case files you intend to hide from the candidate inside the project and declare its path inside the Hackerrank.yml file.

![image3.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046494326-?Expires=253370764800&Signature=GQY-R2iM3PIleoLTVT-wLpjo~B0J2vGH8-iLLkcOoPzPsiaCSjNWjWKIuVpfX~c~8u2eWN5se119vTw10pEzh3VlLi2cvRBQ4wETJDEtrzpNfQyDeez0SP22c8Db-lnfZK3T58TAi~jqE3lBM1k1W8VpUlEz1GYDHdNrK~hpZCM2ZfU6IOEdDIZY~N2jEM6pIqflKptzF1oZWOSbLCXMgU3tP8E-8gE753Fn5N8tl7r9gk-ENsaOcbqanydE88C7bIuHrhnzBKEy6xqdE07aN1FrMlNB-gl4nZG054nduFsh~Gu37SsVEkpDWJR23qxqAxwWTun05OtUir9Y2HO6Nw__&Key-Pair-Id=K3NV4LZ47N8M46)

- On clicking the “Validate and save” button, the question will be validated for any discrepancies in the hidden test case declaration.

![image5.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046494743-?Expires=253370764800&Signature=ANcpk96SAacYTML2VyQYIxcsUSbH7PZijDCY2pexh3Ku~tpYPH~GUMN98IlLPoCh8fX-LxsoGw8dyZF0eUSgniE-5ui2ca~b7NcsQnd-ch0MODkXlxD~eWCvNKowSEK~qVBgv59JZAp9Rg4YBvSaj9ac7dLNIy2CgJhyWLTqvX2FLUXwxCqpi9UDnM8mOy0z9GuRxSIa~3ywsByHKYVRCaxeyPV23fSX3mEorprUh2kwx9BWwLDhmNJJ5m98xq2A4IwabE0FaERLWarCdeL2VMPY1zWtDiiCUL77FgHxh~4BXT2gtDkDW5ydxIe9LW7so0OR0VZFfzCidcA8SFQSIA__&Key-Pair-Id=K3NV4LZ47N8M46)

- If the read-only files or hidden files are detected in the project, the candidate will see an instruction file PROJECT_FILES_INSTRUCTIONS.md which would read:

  - **Read-only Files**

  The following files are marked read-only. You cannot edit these files in the editor; however, it is possible from the terminal. You must not modify or delete these files because doing so results in a zero score.

  \* src/App.test.js

  - **Hidden Files**

  The following files are not part of the project while attempting, and we add these files when scoring your submissions. You must not create new files with the same name because we will overwrite your changes.

  \* src/App.hidden.test.js

- During a candidate session, the hidden test cases files will not be downloaded into the IDE to ensure candidates are not able to access the files. “Run test” by the candidate will not display if the hidden test cases passed or not to the candidate.

![image1.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046495180-?Expires=253370764800&Signature=TRjIxFXrdETahP3IGs~RHcfKHpVgAEk2kMHb4KQX0EvSTG0GPqlLm3tywbu0OuuhMZk40w0VXm6hIOnzQhjJPnVyUfDXHwD66LmdT5thZX4BGNFiqsd4Kg7GMGLUz-BYIQrDeZLQfFrspCijasgCn0qYIdUTzOR9TybVzSVHc3tRzjYWI2zSLx0~OwRxw4jJ0GQ8qUJPr1ChsockgH8EUUnZ62MXdaP8y7LDWlPdaDYqZM9lcZAw~D7xA3R2y1wchKj9oe-GWDk2OZPsBzV1pGHjvbTapKD7RzdbDbCW7D8YAg9xFZdC1CFUvTSzR9EFtsOVAE0zTE~k9V91s~Yg6g__&Key-Pair-Id=K3NV4LZ47N8M46)

- After the candidate submits the attempt, the scoring will include these hidden files for evaluation.

<!-- -->

- When an evaluator checks the candidate report, all the test cases will be displayed, including hidden test cases.

![image4.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046495563-?Expires=253370764800&Signature=EiLYtWEPXoz49PiyPhxDlp6GpB82eCV1GVOz2AjarzF7W9D3QDdU4PrfcFEcaAS6U-w4xywbr4d9yMLtaUdIXNqkMIdvzWVqO1UmEW07QfSZ0m6eIHiM4xUjBK~eLnmG~F2sAmhcgw8bU7gYOlPEdwb3yf8lKi6UPmnAZhUI4iVgJ9XguGksw-E8iJvSnvDaUYO7ykyoqOBBqSSlObtUy9nQpAPDYgM0Ox4dQJg2XS76oDAs44uL0PKcz9axHG1LKcLd1c1uuqu7fi-vDCVq7c6oOZklskgTQtUCxRWhV3ba44mYMFWfArq8De8rOZgtLqz~uFpBM~YeTHJ7AFN2yg__&Key-Pair-Id=K3NV4LZ47N8M46)

- If the evaluators decide to review the candidate submission in the IDE, the hidden test cases would be present in the IDE, and “**Run Test**” will show if the solution passed all test cases, including the hidden test cases.

![image2.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046496002-?Expires=253370764800&Signature=kxtz9ktbTnxCwRkRl8hYcU71Qi6MjB6bXuU7lDqCwrcM7eyGa4MRH6Cku2G0WQsjTTQr5HDodJAJOhHy2cSchC4LnWl1xeqcDDeF9EP2B60EOhY7dHoCAsScMcuofNRBkDZrwo2D7WEe8yxno5hgpJB29wA7Xga4dfjOsGfp26odKy~h6ZUx8KrzO~NGQsaiB0ueIQLhnmNGIa0OP7mpOXQYgdvGtE1an2gpcHdELbF9E1NhgtmZtttOUD9i55A1rlYrQlU~zYXBnUF8UlduTvKZprzaBxxf0l7AKPZYHznZXuGCz4QpR6o4xwKlTZwfLZBxiObzmCQhc6jNEx5fmg__&Key-Pair-Id=K3NV4LZ47N8M46)

\
