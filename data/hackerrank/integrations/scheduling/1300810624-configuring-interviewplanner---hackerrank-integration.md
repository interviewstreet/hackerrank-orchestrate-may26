---
title: "Configuring InterviewPlanner - HackerRank Integration"
title_slug: "configuring-interviewplanner-hackerrank-integration"
source_url: "https://support.hackerrank.com/articles/1300810624-configuring-interviewplanner---hackerrank-integration"
article_slug: "1300810624-configuring-interviewplanner---hackerrank-integration"
last_updated_exact: "Dec 13, 2024, 5:22 PM"
last_updated_relative: "Last updated 1 year ago"
breadcrumbs:
  - "Integrations"
  - "Scheduling"
---

# Configuring InterviewPlanner - HackerRank Integration

_Last updated: Dec 13, 2024, 5:22 PM (Last updated 1 year ago)_

## Overview

HackerRank's Interviews integrate with InterviewPlanner to facilitate a seamless and efficient Candidate screening process for recruiters. As part of their interview workflow, InterviewPlanner users can directly send HackerRank Interview invites to Candidates.\
\

This article provides you with detailed configuration steps on HackerRank and InterviewPlanner.\
\

### Prerequisites

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td data-colspan="1" data-rowspan="1" style="background-color: #eafcef; width: 436px"><p><strong>In HackerRank for Work</strong></p></td>
<td data-colspan="1" data-rowspan="1" style="background-color: #eafcef; width: 447.139px"><p><strong>In InterviewPlanner</strong><br />
<br />
</p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 436px"><ul>
<li><p>You must own an Enterprise plan with a Recruiter license.</p></li>
<li><p>You must have an activated <strong>Recruiter-type</strong> user account with <strong>Company Admin</strong> permissions. This user account must belong to any team.</p></li>
<li><p>Log in with this user account to:  </p>
<ul>
<li><p>Generate the InterviewPlanner API key<br />
<br />
</p></li>
</ul></li>
</ul></td>
<td data-colspan="1" data-rowspan="1" style="width: 447.139px"><ul>
<li><p>Log in using the InterviewPlanner account which has the same email address as the <strong>HackerRank for Work Company Admin</strong> user account. This is important for sending HackerRank Interview invites and generating interview links in InterviewPlanner.</p></li>
</ul>
<p><em>Example: If the email address in HackerRank for Work is </em>[jackpeters@hackerrank.com,](mailto:jackpeters@hackerrank.com,) <em>the InterviewPlanner user account must also include the same email address.</em></p>
<ul>
<li><p>You must have relevant administrative permissions to the <strong>Integrations</strong> page.</p></li>
</ul></td>
</tr>
</tbody>
</table>

## Configuring InterviewPlanner Integration with HackerRank

When configuring the InterviewPlanner integration with HackerRank, the administrator generates an API key that the admin must keep a record of.

#### **Generating an API Key from HackerRank**

1.  Log in to HackerRank for Work with the Company Admin user account.  

2.  On the home page, click the drop-down next to the user icon in the top right corner.

3.  Click **Settings**.

    ![settings.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046899688-?Expires=253370764800&Signature=UNFvrwSNKTojz3SOzJXn5PMD6eNE5CQSMAgXwyVmx41ctELjTylM53ivrOpIxyJLtDUfVnWbKX915lsw7XF9DfayNC8pzftNItTHUMAyd6YoenYxEKf8GqE-~CFtc2AZZqz-RLqcMzFiBJ1yakJTQOL5Fy7dwK3jXx8DaQgg19LZS6gxgSbhrJcbTYoZQDTHb4-ghVwl-YbbHtnBDjRuEVM~izDq5ULtgutW7ikn7jotyIFg-eKwGadY3jI7ri9uqOz08P3j9c54zqxWSGYNEQqnkGpceQmwiD9YxL8uRDdXN3e6JbMGY9ezWj1k3LdZCuR~S8VmGLXp11rqEVdHaA__&Key-Pair-Id=K3NV4LZ47N8M46)

4.  On the left pane, click **Integrations.** The **Integrations** page is displayed. Scroll down and click **Configure** on the **InterviewPlanner** option. You can also search the Integration from the Search bar.

    ![integ_interview_planner.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046900550-?Expires=253370764800&Signature=a678CPX92laMOglVeTZtsv7C0RLbihRi1QK2CNYgrOdjgBR2B2aBPIlG~CqXEA~3baLFJpgTubnYVpMEoTuzfenUvNSB8MiTdCUf1MZChFIpHuy8siYC79wYMkbHZtzo~TO7Z6DqI9WPcZu9ADdzGqcBe9a5c2e7dKwe17GTwLT74sdShwB8C5C3NlLCt5Rv8mQH6MvvyDVg-BNl-yi-SVacZseBrZjAhJnp6oiwd4RWjg7rRpP8MRixhlgdY~iOiJmN7vGW1tszE0a-s3-xOVAk-lYgNVZ8K-kwhXBzT9g9ZeP2fC40XpqbOi~SiyMV~DLpTvfaciszZ-sWgy9TyQ__&Key-Pair-Id=K3NV4LZ47N8M46)

5.  Click **Generate API Token** to generate the API token.

    ![integ_interview_planner1.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046900909-?Expires=253370764800&Signature=Hk2WvjMaXlkuFE4waxWX5g85fIbbM398153Vj1BcbhiDp6HyrrAlRjt0tzSZvulthfaz5rZp1Vaumc1g~lU6eZnIukSIKGwavZczjpqRHixSe5sssY4djHAOtfpIlcgQwXwcH6RB66vvHpMADvSsDp-QWh7uEPg-1fkschHiCxYw60AS3VlE1IQjyERwm~HqozTJSLggls8lw~nHLy9K7CHxXbSwNRt2Tlyr4WivD3AAd9CN7ZzKkUUPrLhvXmT6BCVJW8h7yqX9reBoMnJGzBckq1xb1hO0wdJ0UEaMHUeiDVyf65ZjY-lQd-KYyLUhSz6fcNM3naHoCXzLh8X4Yw__&Key-Pair-Id=K3NV4LZ47N8M46)

    A unique API Key is displayed.

    ![integ_interview_planner2.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046901316-?Expires=253370764800&Signature=A1tceNI77iDHvUZI~33z~8Gb1HYbs3tD4HyaPvNneHGtIlVm~bGfIKEgL7GJYzR~2f52p3DW9k1alz-U8joh0GEbQyawKCw9UGI2cQlNZb3tTLKC1mWZt-9BtwdvK6Wzclp96wUiAUzatnQgJU0-taMj8dXjRPFeLQ-Jpf-OJ5T8gbcTYRln754l3naPxLOXYwsxYTCkKew2oWsZi73PgCuGSTf9j16fTlqkUmQ7DVGL2tlQf8jIscwRbIzd91DZI3b95yNW7kOuAo9z7XG4byPkOMpR50-NYkAzWSowFAfCLJDDnROfq4RTl-Nwb2H8kwxYSferiX495MZjWCsdjg__&Key-Pair-Id=K3NV4LZ47N8M46)

6.  Copy this key. You will need to add this key to the Greenhouse account to establish the integration.

**Note**: Ensure to store the API key safely. Once the popup is closed, you cannot retrieve the key again.

#### **Adding the API Key in InterviewPlanner**\
\

1.  Log in to **InterviewPlanner.**

2.  Under **Settings**, click **Account \> Integrations** on the left navigation pane.

    ![intrvwplanner_login.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046901736-?Expires=253370764800&Signature=BJS6PcwSVBQlfi31l~Fr~zhPpZGtbNai~B~iG1eXqZnAsNzOvnA1ZeD22RpaGu~gaOyKbRssbLSdbzOYeKWx3hKtR8PaXxxidcFoGfoV2C-In9s24TDmL5w-7zJjm0tMKjWZwJpjg02dHIKwPBIo~fE660gWpbXKJosJ3Y~d1dHuljHMgpCSh5eFsAtnhe8d3Cj9PzErd8lsoQmtI-zzdmdJFTm02pEZHHlzU2sVYyjSITAHeNoN2KHkqoYKNAZcEeVzvHWyoVndP~sbED9JuRyDxvLPsPGvKGAk6twxXZ~LmYjhNL-9DkqFbNOm5pWEkBz5s-HsCnu10hNpYqpb8A__&Key-Pair-Id=K3NV4LZ47N8M46)

3.  Scroll down to the Live Coding section and click Edit. 

4.  In the Live Coding Type drop-down, select HackerRank.

    ![live_coding.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046902068-?Expires=253370764800&Signature=QBCIxMfmaxBW29vPhiSiZ3sLnELfQAThdLsBUPDVc0SXGirEgDZiHNtBmctvRg3WCz6BniA5cjn4a6Dx6BotYEid0yVti9VVPA474Il8BirsJycBXs2WjQOgdiSZGCn-8PDfEaTpF19fAr5R8-hv87axBpIV~AeWZd2GIp47ZigNpg9U6he2b4gKRQey4vEZlCxEqvJ8JU~6WP8hbOIYhGDQYXAr7TSO1k2oyagAK7Pk8x9XdTh2t5RISxoNlAlfTtXHFFYSI3xgN1MwYQnsdJZQd86qgcaPOynLJ8dIP8k9GdxAiBo3wpPZUf1v3fhXkLAwlNhmVOJfs~It31CwPA__&Key-Pair-Id=K3NV4LZ47N8M46)

5.  Enter the API Key that you generated from HackerRank.

6.  Click **Save.** The API Key is added and the InterviewPlanner integration with HackerRank is completed.

\
