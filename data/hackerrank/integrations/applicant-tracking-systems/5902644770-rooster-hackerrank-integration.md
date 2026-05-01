---
title: "Rooster - HackerRank integration"
title_slug: "rooster-hackerrank-integration"
source_url: "https://support.hackerrank.com/articles/5902644770-rooster-hackerrank-integration"
article_slug: "5902644770-rooster-hackerrank-integration"
last_updated_exact: "Jan 22, 2025, 10:38 AM"
last_updated_relative: "Last updated 1 year ago"
breadcrumbs:
  - "Integrations"
  - "Applicant Tracking Systems"
---

# Rooster - HackerRank integration

_Last updated: Jan 22, 2025, 10:38 AM (Last updated 1 year ago)_

### **HackerRank Side**

#### **1. Generate an API Token for Rooster**

- Use the partner header provided for this configuration.

<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F6d74b9ea-6f3b-4548-87ab-8a07b1bbcaec-AD_4nXeZj6AW_L-1LYetczc1OGjB2T9iV5MvOYiECD3qP4b5Mov4JA081ziL9d6SDDsD2coVFFqY81KB20elMTil3ukpvnjouAyjjCenTY1cN_49aUr1ArbsJyhiUZ1byyHeavkdIaHP2w-155f0370-d235-4379-933c-1410e800a697?Expires=253370764800&amp;Signature=b1X-I8y-5i78MI88tiJPR5H2aG7GWK-MX8WHEialbnKxRqruUVBfctTn3Cb3sQHbccIg8ee0hn8OtKT-3kIgkRwBw7qfdaeWd9iv8KC90nz732hg-q4LbDRD6-Ks93tCe5j6eK~C570OdwVmNCg1ekOTW-3~VVDOtdGDSKEf0FsvV3TzdOstlU4dEm3llMy9gWasxIyoeGP89bVAwt4ZWrLS5jZO7ozCPcA5h7ojisUgJQGgzhtVZX6k9if~LlImwkOhfqDK0rWAZxXL4MxODTv8l3jtRCWSA8JTwhFvR51HVv3ZtytpYgnNAmUEeeoRYKtRPoIcYZsIO-5fa6RuhA__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

#### **2. Configure Workday-Specific Credentials**

- **Username and Password**: Use the credentials for the **Integration System User** created in Workday.

- **Endpoint Configuration**:

  1.  Locate the **Public Web Services** report in your Workday tenant.

  2.  Navigate to the **Recruiting (Public) Web Service**.

  3.  Perform the following:

      - Click the Related Actions menu.

      - Navigate to **Web Service \> View WSDL**.

      - Identify the URL under the soapbind:address tag.

<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F0a34c13d-1d65-4d93-9f74-ad83061c3cf1-AD_4nXea6nvuM5BgOlSOxPqC9jesSm-K81eL_VHwVXe0rNORz-OgRZRIC7uLaCQ2dh42HuauPVSukgYe3kFJXbPjgqV1Pek5neDWXaDBW3gCpjGkPD1wzSPbq-C1zD_Rk8pZ2nrj7db1-74f42d13-b93c-4bb0-857c-879ae654e7ea?Expires=253370764800&amp;Signature=DqUu-RgJKWfyuo-BYXlr5jfCBRjh8hxUW4dBGoGAdNSDmIFF1Z3-akSy0hf06WgXgJEwwoRff20ddsUstivsEE7gg4gRbjGz6UtqN8AKl1yB5TJqhXJV7kCTjIJd2jBAx2YEkv3LPPh9-lXtCqJ3h5eVaGhkECJ5dgWG-fiFBtmv5bpkyK3p6tBq2DqMwp94oXCH-LzP~0SQTFMiv0ssKWVMagwwCidlGP-Eqbj9~dPZ7qvTka5rSfs3ENP5WLUg6benJTpE3N3uBDhZG1AbWb~YsXwbcUF5ExluHKFCDpG7aRylEzfTVdhl~9ZQAyE9gonqJi78bB6u6~AmffdwRQ__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

#### **3. Configure Interview Ratings**

- Obtain **Interview Rating IDs** from Workday that correspond to:

  - **Pass**

  - **Fail**

- To configure ratings initially:

  - Use the **Maintain Interview Feedback Ratings** task.

  - Later, use the same task to update feedback descriptions if needed.

- To manage reference IDs for the **Interview Feedback Rating** business object:

  - Access the **Maintain Reference IDs** task.

**Note:** If your Workday tenant changes, update your credentials with the HackerRank team to avoid disruptions.

### **Workday Side**

#### **1. Integration System User Configuration**

1.  Access the **Create Integration System User** task.

2.  Configure a new user account:

    - **Name**: HackerRank_Interview_Integration_Rooster

    - **Password**: Create and securely store it.

    - Set **Session Timeout Minutes** to 0.

    - Enable **Do Not Allow UI Sessions**.

<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2Fd567e180-706c-49e0-8dde-cf5ca40f07ef-AD_4nXcj8uayf273r395APTkKD8iNJx2nMum4Ec2HqwOHgo_oTmGwXh5OM0eIdGUBl_3D7SsZriBgQVJBoZCtf2IhjH-xhkKMAe2Qf5_sTF1AUXeVZoeYjsiMX2q-jhYMLyyKY9BSAkL-20ff9db0-fab5-4caf-b862-b5d6d59b7626?Expires=253370764800&amp;Signature=DZdgHOGUudDH1Zrv3RVwmjAm94MYga8xewL~ggWvJnsXggpf823eY3S8Iz1PdN9~YfW-i12EyIiKQ4qh~Ad334tQla5YaLAG7WlZ8N9b8qGPP3tZ-vocLkyVGwd6Mx1h3lnHoAie9Ji7ijX88DtxTdmLeqh~7IGDDezVGfyKgC-FoWUwlC4tJq2-WJoSdLGS7-COVSKhZrs7OofWb78xGeFK1zOuoF5xykM3P2IwL4Ck5xKrYOlwH~srM2yJ-3SBk88XoflirnqgW7hoda9Z~lO50Dur5cJfl4~qMQJsFltZ6ZZ0-KqPaSvj4w4zI0YlWAPjeSaOPm6N21Z8NxxoTQ__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

#### **2. Create Integration System Security Groups**

1.  Access the **Create Security Group** task.

2.  Create an **Integration System Security Group (Unconstrained)**:

    - **Name**: ISSG_HackerRank_Interview_Integration_Rooster

    - Assign the previously created Integration System User.

<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2Fd244f26c-deac-4df5-945a-71755b29508c-AD_4nXdsIFcUn_xAdWgSSeF_QrbnoDMDhmN-ocAouafv_64P4tovr26t9pZIJwqXUoXg9f95uBFuV18pSyitaAf-a5gqkHPvZMOIWXYDY-Yn2n3j-Z6zcqGvAVeCg6k3IUZ_uflzW9Nk-6285fa87-3b26-4690-b658-2d8d3581566e?Expires=253370764800&amp;Signature=p5J4z3e8brd9Uao6bmFXLiEMv0K8oD-Wymi8urugUe0w3pxmtfmnHAWf7~RUSMMmsLjGVKZ8BERrpTCUb-O7ryKKNaQeDOcRKFsQ6UDbsNdLJ1LvbdDFmewIzaODd0DCG-RTPAMFpIwe0~u2XmVZIlyNrbWIWIxAK~dEdhcBJ~aBbSi8fC7aYLYR6L7pzqXCXDj4hos0pmpcz0kqrh1paoZREhh44C7nBoWp9eV2X7sRULChbjE9H-~Ed62E2WISag7iX52MKYtrmesFFf7B~LR4bZ0jiiwCwTR97Yafkv-DSaIPHadAGM3bOwfIv3vWG6mrrfGCXih-G1zHksVBcA__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

#### **3. Edit Domain Security Policies**

1.  Grant required access to the following domains:

    - **Interview Integrations**

    - **Candidate Data: Interview Schedule**

    - **Candidate Data: Interview Feedback Results**

    - **Worker Data: Public Worker Reports**

    - **Person Data: Work Contact Information**

2.  Steps:

    - Access the **View Domain** report.

    - Perform a Related Action on the domain:

      - Select **Domain \> Edit Security Policy Permissions**.

      - Add the Security Group to the necessary permissions.

      - Assign Get, Put, View, and/or Modify permissions as applicable.

3.  Activate the changes:

    - Use the **Activate Pending Security Policy Changes** task.

    - Provide a comment and confirm activation.

<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F5ee5917f-3a65-4867-98a4-ee859b928a41-AD_4nXdmP2EOzrOCp-NDd_JWkO7zxAwG6BIC2m2qNFF1wgIopolGud6z_r-UdB5QYr-0LCLvC81IfJU4hmb-ym_LwYQvvxT0EcBPpXAWP8MKmKhmiKkZQ7OT6mfhCj-uIjIlxN7kg6NL_w-55438acb-c74e-4f6b-88fe-c21f3becb681?Expires=253370764800&amp;Signature=noDMvAWh5mIGksQLmYhbbxkPxkzT7Z4bNIz5IxMbf145XQ5HSPQ13mUVp50hb9OQKMxiOQzQqUAyktmbsTiFWpa3fwo2nScHdtbyb3IRjnm3qMKEMHdzzU7o4b0VQpWQH8HPYgs6VwmU82fVCge00KSaJxGSYuVQRnzm5D6tDi6jw-CYGvOAQXVFmHeD0ZxrFkfug3XTTXV0kqbX-eKd-h6Ylghm102~S8Up1GXIGyHurvPwnqZHf51gY60~bsBsmyPXEDHwqvU~mFRFkSAuuWJy5OcaD-zb3~hlYnwbw-1H3rkO-ZDeVvXUnbM6tLX2SFJANkjHlpeCvLMibAGGhQ__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" /><img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F7185a3b4-49f9-40d2-bdd5-fe29ab9be4b3-AD_4nXdVANHHEseQMUFNMX3Vs2VKZH1wkDLEzrtYLX0SirLs9IxAHnlIyqht3QSeFACIcZPaS5ny_fzAMWzDzqx-88bgKPdLWCwEzHmFc6ZVPbWOlfmCQ5hkHGvBRvy4aMB8cmbTmIsjsQ-e610d017-aa03-4c80-bfef-a076c2bdd69a?Expires=253370764800&amp;Signature=D05kFa2~rqz5wAc0iDp5z6BnnmCcZFdHkMNySAsKtgPh3yY6y2Nwb2oVoHYig~mXS0UBiFE4IZ4wHVuMUNbvSV8JJcwlWwaDs4HiPsPNjyc7jgKd6NiEhOZd0T3iF2oP~xC9JJp4utzsTMOrI6jxYIKV7L5gEH3EBrjvlD3W25Z8CCltIOPYUlnOh4NcIVWW8W~cyzmmIpNpqD~YeDowSOmDc-HHOUfwvsnqLatqCNY6fVwPBEHJrtZKJgNvO4XBpYKWsxLETnRMgNUlpktDpsHOol9efl0ra3BYRn3zZntikWG-fENJ043l4edMxVnjMj4g2-j9gxDomNQWgNjPxg__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

#### **4. Manage Password Rules**

- Access the **Maintain Password Rules** task.

- Add the Integration System User to the **System Users Exempt from Password Expiration** field.

#### **5. Manage Authentication Policies for API Access**

1.  Navigate to the **Manage Authentication Policies** task.

2.  Edit the authentication policy for the current environment:

    - Create a new **Authentication Ruleset**.

    - Specify:

      - **Rule Name**

      - **Security Group**: The group was created earlier.

      - **Authentication Condition Name**

      - Allowed Authentication Type: User Name Password

3.  Activate all pending authentication policy changes.

#### **Troubleshooting**

- If authentication issues occur, use the **Signons and Attempted Signons** report to identify and resolve failed sign-on attempts.

\
\
