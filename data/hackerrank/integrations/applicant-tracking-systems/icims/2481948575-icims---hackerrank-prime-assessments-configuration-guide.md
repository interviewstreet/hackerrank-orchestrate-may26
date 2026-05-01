---
title: "iCIMS - HackerRank Prime Assessments Configuration Guide"
title_slug: "icims-hackerrank-prime-assessments-configuration-guide"
source_url: "https://support.hackerrank.com/articles/2481948575-icims---hackerrank-prime-assessments-configuration-guide"
article_slug: "2481948575-icims---hackerrank-prime-assessments-configuration-guide"
last_updated_exact: "Dec 27, 2024, 5:57 AM"
last_updated_relative: "Last updated 1 year ago"
breadcrumbs:
  - "Integrations"
  - "Applicant Tracking Systems"
  - "iCIMS"
---

# iCIMS - HackerRank Prime Assessments Configuration Guide

_Last updated: Dec 27, 2024, 5:57 AM (Last updated 1 year ago)_

## Overview

HackerRank's Tests integrate with iCIMS Prime Assessments to facilitate an efficient candidate screening process for Recruiters. As part of their interview workflow, iCIMS Prime Assessments users can send HackerRank Test invites to candidates and obtain the Test report for further evaluation.

This article provides detailed configuration steps on HackerRank and iCIMS Prime Assessments.

### Prerequisites

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td data-colspan="1" data-rowspan="1" style="background-color: #eafcef; width: 436px"><p><strong>In HackerRank for Work</strong></p></td>
<td data-colspan="1" data-rowspan="1" style="background-color: #eafcef; width: 447.139px"><p><strong>In iCIMS Prime Assessments</strong><br />
<br />
</p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 436px"><ul>
<li><p>You must own an Enterprise plan with a Recruiter license.</p></li>
<li><p>You must have an activated <strong>Recruiter-type</strong> user account with <strong>Company Admin</strong> permissions.</p></li>
<li><p>Log in with this user account.</p></li>
</ul></td>
<td data-colspan="1" data-rowspan="1" style="width: 447.139px"><ul>
<li><p>Log in using the iCIMS Prime Assessments account. The Recruiter email address on the iCIMS job should match the HackerRank email address.</p></li>
</ul>
<p><em>Example: If the email address in HackerRank for Work is </em>[jackpeters@hackerrank.com,](mailto:jackpeters@hackerrank.com,) <em>the iCIMS Prime Assessments user account must also include the same email address.</em></p>
<ul>
<li><p>You must have relevant administrative permissions to the <strong>Integrations</strong> page.</p></li>
</ul></td>
</tr>
</tbody>
</table>

## Configuring iCIMS Prime Assessments Integration With HackerRank

1.  Log in to HackerRank for Work with the Company Admin user account.  

2.  On the home page, click the drop-down next to the user icon in the top right corner.

3.  Click **Settings**.

    ![settings.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046183582-?Expires=253370764800&Signature=OeOqHWWGZTPgy9dZ~fqaT-Uvj-ghyJGzS5yYTzgdHuOsFNq40AHgayya7dqw-0PE4rxP5OIUCBhlNbIHJdgV8oT1cSGw~wbO4VbTf0h2~eKnCRU6dLxSJja40cmhQvM8TJQCreoAgRQhTCGx1fyv4rOASzvcoLwILQ8cZmw0PSd0dcaV53YFZT0344KbHHlFeK-Ya31Dhtg4xkMultjZ2T1PUSVvP2XQiItCB141EzF1rsJlrDe9xAmvXYXwofLQJqxArY69rWt9EBH6aNJi1tbfVSjlXCh0QoQHfpObFnqqn5jqMAvE7YlbWil~27hPpyIS3MPdg~xhIORnZSbjRQ__&Key-Pair-Id=K3NV4LZ47N8M46)

4.  On the left pane, click **Integrations.** The **Integrations** page is displayed. Scroll down and click **Configure** on the **iCIMS Prime Assessments** option. You can also search the Integration from the Search bar.

    ![icims_integ.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046183990-?Expires=253370764800&Signature=RjBl8EtN117m3l2QFuuQj6hwg1aWlyQQi7GT-LSKOFHhUN5jp~Uuqa9CNhggkBcn2xEEsFUOTuzaqs9NFKjO9z168ZCqUIlIFQMSXYw0AHryO1VuH-bDm5kFofUJCDrluELIILA4keYwOx9ywqndUyfpkwZ8Of8s35cgBpcZdbd23-LINaoIlUQsI0wY3CNa0XTULFbTInaeBWKA3WgrjKgvdjygnrYqP0TGd1EC15z0BCHgRoIsZln95UYQV4XclOqMAGRTTJMOLHUQezguB6ZpJZEz6hYxc5vWfOwYovH4rXrmJ8IA1ioYI57FNK80R~gaesV4nOazs8Bo2HFt9w__&Key-Pair-Id=K3NV4LZ47N8M46)

5.  On the **Integration Setup** page, specify the iCIMS Customer ID, provided by the iCIMS team.

6.  Specify a validity period for the assessments in **Set Validity Period**. This is a period in which a test taken by a candidate is valid. If a Recruiter sends an invite to take the same test within the validity period, then HackerRank does not send an invite. In place, HackerRank will send back the last Test results.

    ![icims_id_name.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046184364-?Expires=253370764800&Signature=e3R4c5B5yc-MRJ~PSTK-9DlzU-7fsqSRWpnIiQSWdwLkQ3EBt72iKO4oEwslG38nDe4u-m1DprD1IKSCnNjRNOl3EogIiC30Ap6gHWLZ8HeBki2ji0XDVuMNt2yt4x4mPxzn2Ia1~YlE92o8Kr25OBlTfr-TuIcubw2s0wiSujZAbDH7y8ws54ifolPtyM3rJov3HJde7XkdflKl9FBAb8lGAaLyJHuY3vZdajaFziIqOxiV8UiYxRcPEXtOn-amvmCBvSB1ywX4rl12RvWPmfhBBEsfmO514ebm1yzx96dPsPoZOHT2lWAvMt1QU0NNbFOvyMKFvn3JbFSD4fVxuQ__&Key-Pair-Id=K3NV4LZ47N8M46)

7.  Click **Save**. The iCIMS integration with HackerRank has been established.

Related Articles:

[📄 iCIMS - HackerRank Integration Guide](/articles/9631673147)

\
