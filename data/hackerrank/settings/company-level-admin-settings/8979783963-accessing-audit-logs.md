---
title: "Accessing Audit Logs"
title_slug: "accessing-audit-logs"
source_url: "https://support.hackerrank.com/articles/8979783963-accessing-audit-logs"
article_slug: "8979783963-accessing-audit-logs"
last_updated_exact: "Feb 13, 2025, 4:42 PM"
last_updated_relative: "Last updated 1 year ago"
breadcrumbs:
  - "Settings"
  - "Company Level Admin Settings"
---

# Accessing Audit Logs

_Last updated: Feb 13, 2025, 4:42 PM (Last updated 1 year ago)_

HackerRank provides a comprehensive audit trail for all user events, allowing admins to quickly identify who made changes, what the changes were, and when they occurred. This feature ensures efficient and transparent data investigation.

## Accessing Audit Logs

**Prerequisite**

- **Company Admin** user access.

**Steps**

1\. In the top right-hand corner of the homepage, click on the arrow next to the user icon. Then, select the **Settings** option from the drop-down menu.

2\. From the left pane, click on the **Audit Logs** option under the **Company** section.

<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046671584-?Expires=253370764800&amp;Signature=hkzFvxlnmYQb49rOoPehcS-uLuot~aGRMvy9lOYWa9BR1q9J7NMs3eGOq-Aw5e8omWHvGBVSW7Q6ZFPAppaIgSrUHBjNvQHhx4jzoG3dOSNv8xfZZguqTEI~MaWwVT6jNyv74A8Ng8WxUd2l-5MG-flK~~gVERDpmwc94THUUeAel-xC5WuBuvo5TO0kNLRI-CmqxxWzcZ0wRTAsmZunKYivzOMy--6iFYEOuAOB5z3zrymOPMD~EDLBABoUhO9RSd8mAVPig0j-8hVs4Xymhb3ncSPGhvtl37MONJVq3LHND8o0Cxs~1ozsMxzapA6NwjGHhaYx2achV156k9rEqg__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

3\. Select details such as **Company**, **Test**, **Attempt**, etc. from the drop-down under **Filter by Object** for which you would like to view the audit trail. Each object selected will have details such as:  

- **User** - The name of the user who made the change. 

- **Action** - The kind of change done to the particular object. There are three kinds of actions:

  - **Create** is when a specific object or an attribute in it is created

    1.  **Update** is when a specific object or an attribute is updated

    2.  **Delete** is when a specific object or attribute is deleted

- **Object** - Indicates the source that is modified. For example, interviews, tests, questions, library, etc. 

- **Object Id** - A unique ID allotted to each object. 

- **Timestamp** - The exact date and time when the changes were made. 

- **Modified Fields** - List of the fields that are modified.

- **View** - Modified field information and IP address.

<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2Fab64843e-585c-4a59-a510-31c160449d44-1734046671941--51bfb268-716c-4eee-a337-3ab099c84899?Expires=253370764800&amp;Signature=AcVcJnDB-CCpl6FCDlIlpUmFCh4jE5UGaOZoZVMvlwRwAvwqYd8YJQB9lXFS69Yye1Mo9aNFXkfNjQQ5duJtlvB1aE6Iecfpe6IS0Rd4uMV~RiJsvloaF~yMacNWMkQ46lPyacbf3ouHhTwktVOzd3Z4SF2YjUsYZC73WjPUSJ8Nm0QPyxfT~PL3kol6Kwyu2O7KxCwdjqbEKYQFF35YF9dWupUDSGGRAJrizg5SH9BYqe2XXKatv13GDSqrFZXGBV5LnGgtjSNHTPWWuJhMklQM0i09VfIvuSber2ltTj9QW~Rz0lRIC--i3uy7k2kVCbmUXw6GhM5sptEtR50ztQ__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

**Notes**:

- HackerRank retains only the last three years of audit logs**.**

- Seeing **HackerRank** in the audit log means that HackerRank's customer support team acted on the customer's behalf.

## Examples of Retrieving Object IDs for Tests, Interviews, and Questions

**Tests:** Click on the required test from the **Tests** tab and note the 7-digit number in the URL, which is the test ID.

<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046672363-?Expires=253370764800&amp;Signature=t20rbMg6UVc17petqOujiDDGTR9wurICMN~G1OuUg49YaPXEdnYmMwJMt3L2PeETu7e7iuJh6wRpQ2zOWDY4aYnZnMEk3MBi-vetCBuI9d-Tqk4XBQkxlFZZVXA31LnMTqjedmu6zhdbNA9-VHU5aefjQlfTijuzQwOXwLlIz9FaQtOIhWbGEnYJuDsKrATlTD~jtBN8-JEY4mfHw457o3U-glA8JntCNZRXNKKG7UqiAJENkUeLbdBW~guJtZqwJTwZ9Bo47Wu-v91utiNDDQGllpQFz8HG~oXgDh2iOAbgS~s9b-i-YEEU7dAn1PLnc1UX9JpLTkoBXsrgOPJGkA__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

**Interviews:** Click on the required interview from the **Interviews** tab and note the 7-digit number in the URL, the interview ID. 

<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046672842-?Expires=253370764800&amp;Signature=MADo5lFelfg0Kwa~U8odOQPaDveSYnQ7nqLjGR07Pjx4wcgS0K3O1weEu~qxqS7VAYeAVj~MqC84LOihFZoN4bMFs5-ZBXn-H0j02AVy4h78tPWMJsrtHu0Qcn79ahdaaEcNjoLxmd9Lyt4nQ6FULF4NB23wcdJaqobci9hWvSVwmk3qefEqeWJBOO4jba2HJUN3IIVUm2c~cPSeUfUZSBg56QVxV8UH2DL-nlnH~ev6Tn9X9Pa~qJ-BYHmcWmWXRw-U0zutgoxxKFFsaySciLVGygdF9i2TZ~LuetXZqfKq0FT7qrk~EC~szFOLtCcoSZGIWxTL-wvi4cL0FJHLBA__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

**Question:** Click on the required question from the **Library** tab and note the 7-digit number in the URL, which is the question ID.

<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046673451-?Expires=253370764800&amp;Signature=Qj9PbfryeNXC7mSuTrPTJWsDFIJCXsd3qFlrmp6MEEoYbp-f6-11XE0TvV58xumxvq~9TevR~PHjKAwopB8Dix0kZ52uLn71COG8HRmSL87CphQa7qqMrDp~7TBk-4rdnnsVKZoWaqUQUWHBf216sAArhlm5LGfO7FgekSS8qAFJ5ahl3M2qiysVGzR5o0HqJXZYxfaQrRBcDCEgpsTHdsnfVP5KLColMPthGnWjpK8XYHJHo79Q4cz19i2dOQ4pRIHhrCx6vGZ1Wjh-Q4x8udyAmwIXKaOGKv6DoDdGBv7ubFrtn-wxVKFudLalGjRsjeth6~RPiCCzz5biD3bgjA__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

Question ID can also be retrieved from a test. In the **Questions** tab of a test, click on the three dots icon for a particular question and select **Try Question**. The question will open in a new tab, and you can find the question ID in the URL. The test ID comes first in the URL, followed by the question ID.

<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046673900-?Expires=253370764800&amp;Signature=TNTXqB-anvwn08d2rRhGPnJmgaeslL6gqP1uKbtIGu7iPUdTqC9gicwW8QPXfHluPAJrZ4SXAG52IHB1t45cnQ6a16cYz4y1BXvFcoctk83tM~HPNCGTj29-YYYL3cc~-4vRSGL3JOwbd5ij5WSkP9FRg3WJPuxYqIKnGbLf-ZZTzutlCiAnRt6I4Wn1QWDu24qZasNrKVkJ--XGzQiqMvTa~3GQqdxWnxhKZtQnzCLpIsSyo8n4FrtSOADsariHWMdsGQvPosTZAQKAPKgL6agQaRCMdaSlXAGvx140Lrv3AvJwsRKCyvwI7z6Mkjgb3U9KYo0V~S2Krne-WC8PQw__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

\
