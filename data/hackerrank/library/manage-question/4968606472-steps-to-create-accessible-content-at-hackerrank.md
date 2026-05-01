---
title: "Steps to Create Accessible Content at HackerRank"
title_slug: "steps-to-create-accessible-content-at-hackerrank"
source_url: "https://support.hackerrank.com/articles/4968606472-steps-to-create-accessible-content-at-hackerrank"
article_slug: "4968606472-steps-to-create-accessible-content-at-hackerrank"
last_updated_exact: "Dec 24, 2024, 3:10 AM"
last_updated_relative: "Last updated 1 year ago"
breadcrumbs:
  - "Library"
  - "Manage Question"
---

# Steps to Create Accessible Content at HackerRank

_Last updated: Dec 24, 2024, 3:10 AM (Last updated 1 year ago)_

## Overview

The candidate site is now Accessible as per [WCAG 2.1( Level AA)](https://www.w3.org/TR/WCAG21/)**.** Thus it becomes imperative that the questions are also accessible so that *accessibility* is not impacted.

If you are a recruiter trying to create a question for your assessment, below are the steps that will help in creating accessible questions. 

- After you have created an assessment, head over to the ‘Questions’ tab and open a question in view mode.

  ![image4.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046680234-?Expires=253370764800&Signature=CmOMuuIvZ8xgK9~BwoP9bwVt2gVfUNcf-411D1-2AI7eNHgKwam~nL-Nvb6rAucZ2qe7LExnmFhW1Pzj4SYLbienKXhcVg9GWxb-4RiqLXOgenn1mbhfNS7mA7CKvaCQjUkMpi~Ujto0n2s1lStJbmmoLs6EFkuSKXF8UYBZMeOlNhClm6KvZICeT7kP5Obu0~cfc6V2M2ZsSGVITc4npLbeDn0eLZDLsbTyFKbLsrBrpb-GOlu0JXtdGLf8laKj0BQmi4ZpdJ4Ttfj~CZdShwJ1QSy2I452TQumCsrqKgvFEFD9ywvc~9WQvjuthHBzW9-kpJY9j~YmwWD35Iv47A__&Key-Pair-Id=K3NV4LZ47N8M46)

  In case you are the owner of the question you would be able to open the question in edit mode and update the endpoint to view mode as shown below.

  ![image5.gif](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046680782-?Expires=253370764800&Signature=AvmPKlNhVQy3shqh4XmpP6vc7jbXfkF-BI-lhOsPMvvx3YYEiTnm457eFTyQK5AqMb5cOo0vhPWeElR9-0TdFuEqSIWMIOJZHZmMcbDdJArWwG5Eu7n99kl3x6QVK7ujFBhp3EXCu8LVLD8tG~9zz1t0pYlfCk3gNhBckBjBPlUorOjrYHj-SvO4icQ2lZmlyU1fWdi0flKukG-CZ-Ejj54ie-lXyVJ1dX8DL5d9zF6GDPZH0x2jbfS7S58b-gwg7DIAKJYoIGL4eYv1keir0PXKwk55LH23d-ywNoWcmmM~DbyviTYiXkl-kuXi2VE9ZoSQe4BIHixtHlJVsclpNg__&Key-Pair-Id=K3NV4LZ47N8M46)

- Run this question through [axe](https://chrome.google.com/webstore/detail/axe-devtools-web-accessib/lhdoppojpmngadmnindnejefpokejbdd). You can install this extension and run it to fix the violations if any. This will catch most of the violations.  The below steps highlight how to use this tool to identify the issues and fix them.

####     Steps to Run axe:

1.  Install the [Axe extension](https://chrome.google.com/webstore/detail/axe-devtools-web-accessib/lhdoppojpmngadmnindnejefpokejbdd).

2.  Once you install the extension, you will need to restart the browser.

3.  Open the dev tools by clicking on inspect in the context menu. You can open the context menu by right-click.

    ![image9.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046681206-?Expires=253370764800&Signature=SVg0TCSQ7b~QfShwckEhwHrV385cwAyrB~IPlIGhgAB7KpHAQBGnvh4dBx8HiGHPCB8PasBB5xg1aCpguj-2864KG9FIgENPYnuL7Wqt8D~JsWl~bOsNs7Oa3zB2OpV8MkNXf5V0pNORJs0kSE5G76zawtcFB5e4R5gGEOp504KtQpA4zYKBikKaW1Hhyz5V9CnIXClitayMYyPzFqHFqyt23wRyPUTdL5p87iYc0umnL0J5IQCmnS6Kg7Ccs~b5KybYaUo7CyXQBNY0wKR1TTnv4acq8LDCo0o1-qWEtGY9bOY-nHtnmbMsYjtrVydeMpyTZ8sEvFb0nKjKsn108Q__&Key-Pair-Id=K3NV4LZ47N8M46)

4.  Now you should be able to see *axe dev tools* in the developer menu.

    ![image8.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046681808-?Expires=253370764800&Signature=Rs7TCeMWmOaEeVVPBRc5Iso5lMRGjm7GaM5rzto6t0DTjdZ10PjUcse~6CfNvRVYjN2RU7xowb7g4QsCBiPsAcWuLRux7aaqAS5Cp~RzbebV-HG34uStda9xJYKG91Jhde7M984KuS-qhrdpd1dB28WaEPwvJdjBFJZJ8K2hgGlmxMAww98dGdGtedRpLHvV6kLJrgTTwLJOaNMKYfXz4wuAcfbUcxEM8CPKyfhHw6xmoH5IhMAhBP8-st9CqTPWGVnf04ijET2sJF-T2lc6dlFNfGZWZk-hiHwVn-6cbVAAKJRU7DdA7Bh2xSds6WCtaF6ZhZu5V5ryNQ4V0P67vg__&Key-Pair-Id=K3NV4LZ47N8M46)

5.  Click on ‘Scan’ in the left panel to run the *axe Dev tools*.  

    ![image3.gif](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046682458-?Expires=253370764800&Signature=fUz~G7DPBxEQ9SecTXl1j1mfEKcW0~ZawIpqW-VOV8iX4kCA5UiZNVW7p6sebiFvS72bu6FPpqpkKUARss3kFHRQ-3DPXout4YFn6AHmU2MJZ7IsP~zl7PUulpz5YGa0ULueKs~JCB~OFHENECPQWEP8QUNbNL8d53VpuAoViDlpxIIi66VPo5dnda3etF6NdwGMamw-mn2CDdeckW5S61v4C83Yf7C28Y72kYwJU~Yp9R4nWecZVmVDMTGQkZV5RQpux~vX7eV5ii-WokiZ3OubOfCAnaux3sTvDEa4h6kr9tXL4bb1VQVW5E1CiABkwrKJv8yevp8bntCanKNy~Q__&Key-Pair-Id=K3NV4LZ47N8M46)

**Note**: By default, the axe will scan the whole page so you can ignore the other issues outside the problem description.

- Axe will report all the violations along with the suggested fix. Once the violations are fixed, rerun the scan and the question is accessible now.

  ![image1.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046682850-?Expires=253370764800&Signature=KuJbRRjAglPVIiUBSJIzyorJtDRf5iiZgCeNadvTcaCArzhisox1E~~vOkEFEMe8USJ-3zI91jfEs9WFQ4DxrlY9X3xYHHfIBJcBWeaeHXR6ln5e8MHL5wp~0RSuHCJo5QQysRgvCylDf4Y8VumQJoS8XObattGM~C7RGxVBECXbAHQRnH5pUjxCn-fApwwJfWG59iyAe9JM8iUFgoevHuGJHcHLVOFpfR8V8ZC9Z~GoJK-ArQq4XIBy3Ba6yZY-uSfd-SpT68rCNPAdTCkKP78oBcdQoWuelMLxTjZmyyLvwGZRP-w9djBL-ZN7nlaEZqZIcDLDm6zyu7FrKn5pMA__&Key-Pair-Id=K3NV4LZ47N8M46)

## Dealing with Images

#### Why is alt text (alternative text) needed?

Sometimes you might want to add images to problem descriptions and these images might not be perceived by every user. In such cases, it becomes very important to have an option to make these images accessible to every user. Thus the need to have an alternative text (alt-text) to describe the image in question.

Below cases are where an *alt text* (alternative text) needs to be added.

1.  For screen reader users, images will not convey the information.

2.  For users with cognitive disabilities who do not understand images.

3.  Sometimes users might turn off images to prevent distraction.

Hence an *alt text* is recommended so that there is no loss of information for the aforementioned users.

## How to add an alt text?

In the problem creation flow, you can add an image in the problem description by clicking on the ‘Image’ icon (screenshot below). This opens the ‘Image Properties’ pop-up with a *Text Display* field. Set an appropriate value in the *Text Display* field and this will be used as an *alternative text* (alt text) to the image.

![image6.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734990002231-image6.png-1504db9b-6ab0-4448-b71c-a5fc37f45736?Expires=253370764800&Signature=rMDLpG0hn~sLZEzwVMSGuisp6SLW6juUusE8gnemzHCkCO1g3uvPRtjLtrWqk-n341Qk~fG7LG63jciRjh3fC6dk9GvqFEDNR1qdlJ4ogG7L3j4h8nJNj3MJUMvK6kBM0Oe4AfZxgefEcZ1OlKRCUZbssoa1KSUfd8JUdAaW5IRp42AqBkjmv--Y0SWUp5C-aKNkxZIdbov~Izr4OCXcKe-fAuBS1a0i0yyQ9bqTpkH5OMWfeLta79v021HYPXr47WwP0tFcWbOb9Jm~o06qp54bduEgItuxy4qWVGBdxj59~-KJZ~XGkCog1dzs7AhCq9DEtFkS-9WqQl9BolfJKw__&Key-Pair-Id=K3NV4LZ47N8M46)![image2.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734989996628-image2.png-5ed83856-2413-42d7-a456-a42e5f8f27ee?Expires=253370764800&Signature=dJQBUIRWlrC257lTOww15GLD7RmAxGfJqIJ8-xQVs73BV8T~44DAleluP00PiXB5lxk6PUPtpOAEmUeUJ6cJs2y0njoRnz4TuS6VBZOdo67T1Gf-xXanC-rElyF8KzVG8yvuQkbY2EyEWz6OJosxsJmz5rLd9iQwWEoKyneLuMKMVbrdSOpXNT3SDyv0gGmuQ1Jpa3zaaxxvOQcAGNjgeNg8ci52CZ8BwZ1FCdBUnioQI~JRFvvJsBdpKmu6X1pK4nAsT0wNrhgAnsHk1bT~Z7YRW~lysjQI3g~3-oXqr9bIgYHuDyO~E8cxXw0nmu27fVUFTPEGt0tGYVL2zMXc7g__&Key-Pair-Id=K3NV4LZ47N8M46)

### Does every image need an alt text (alternative text)?

Not every image needs to have *alt text*. Most of the time, the images used will be solely for decorative purposes or some text in the problem description might already convey the purpose of the image. In such cases, adding an empty *alt text* is completely fine as the description contains information about the image, as shown below.

![image7.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734990014004-image7.png-b7313688-27b0-41f0-a760-e7cd3305af3e?Expires=253370764800&Signature=N469lpZUwyBwaDr27oXN6CpFV8CrcNgQBWcrv5HK8h2oB7DETEbd0g3MLr8FyWMlvSJHoQDNKg6N1iuB26IfjIx940aPjLqr8AGxZKb944fn5o~HErEWpDa50GtvEbhcHVT5w4ZWPBKrsxGpxwCN8Bc~Xw07GxBmEOKZxBwZS6e9lITaIEShVWT0xIly2uwXH3hHFW2bFEpa3jurliE91~5sVANJdl8xH5RpvvFvULTLXc7sg2xA~wt3jTU~fxa9XOWZ4e8kFOk1PsVtCzJ97iWi93loq1wTZAJQXgvtL1u459VAvjkt4pn3wT6pY06Xs2C2wkWlKHkG9fsGumdvkQ__&Key-Pair-Id=K3NV4LZ47N8M46)

### When is alt text (alternative text) mandatory?

A descriptive alt text will be needed in the below scenarios

1.  Images act as navigation elements for example links.

2.  Images contain text

**Note**: It is recommended to use images (if used) solely for decorative purposes in the problem description so that it is easily perceivable by all. 

\
