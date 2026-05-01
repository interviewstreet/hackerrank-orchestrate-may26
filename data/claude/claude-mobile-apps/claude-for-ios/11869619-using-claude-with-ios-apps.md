---
title: "Using Claude with iOS Apps"
title_slug: "using-claude-with-ios-apps"
source_url: "https://support.claude.com/en/articles/11869619-using-claude-with-ios-apps"
last_updated_iso: "2026-03-16T21:25:23Z"
article_id: "13028604"
breadcrumbs:
  - "Claude Mobile apps"
  - "Claude for iOS"
---

# Using Claude with iOS Apps

_Last updated: 2026-03-16T21:25:23Z_

Claude can now connect with your iOS device's system apps to help you take action directly from your conversations. When you chat with Claude, it can draft messages, emails, or calendar events, find locations, manage reminders, and analyze your health and fitness data — all seamlessly integrated with your mobile apps.

> This feature is supported on all Claude plans and works with iOS system apps (Messages, Mail, Calendar, Maps, Reminders, and Location Services), as well as compatible third-party apps. Health features are currently in beta, require a Pro or Max plan, and are available in the US only.

## What can Claude do with iOS apps?

Claude can help you:

- **Draft and send messages** through the Messages app or any messaging platform like WhatsApp, Slack, or Messenger.
- **Compose emails** that open directly in the Mail app or any other email platform like Gmail or Outlook with the subject and content pre-filled.
- **Access your location** to provide contextual suggestions for nearby places and services.
- **Display locations on maps** and help you navigate to restaurants, stores, and other destinations.
- **Read and manage your calendar** to check availability, create events, and schedule meetings.
- **Create and manage reminders** to help you stay organized with tasks and lists.
- **Read and analyze your health data** to help you understand fitness patterns, track progress toward goals, and visualize trends with native charts (Pro and Max plans only).

#### Limitations

- **Location:** Members of Team or Enterprise plans can’t access the location tool at this time.
- **Calendar:** Ability to edit events depends on your ownership of the event.
- **Reminders:** Claude cannot create or edit reminder lists themselves, only items within existing lists.
- **Contacts:** Claude does not have direct access to your contacts.
- **Health:** Available in beta on Pro and Max plans only. Currently limited to users in the US. Claude can read health data but cannot write or modify entries in Apple Health.

---

## How Claude helps you take action

When Claude determines that using one of these features would be helpful, it will automatically suggest it. You'll see a card or prompt within your conversation that lets you review and take action with Claude’s help.

> **Note:** Most functionality described below is not compatible with our voice mode beta feature at this time. See [Using voice mode on Claude Mobile Apps ](https://support.claude.com/en/articles/11101966-using-voice-mode-on-claude-mobile-apps)for more information.

#### Sending texts and emails with Messages and Mail

1. Ask Claude to help draft a message or email (for example: "Help me write a text to my team about tomorrow's meeting").
2. Claude will prepare the message and show you a preview.
3. Tap the message card to open your Messages app or Mail app.
  1. Third-party apps (WhatsApp, Messenger, Signal) are also supported.
4. Review the pre-filled content and make any changes if needed.
5. Send the message as you normally would.

**Example:** "Draft an email to my manager explaining that I'll be late to the morning meeting due to a doctor's appointment."

#### Using location for contextual suggestions

1. Ask Claude for location-based recommendations (for example: "What's nearby for dinner?").
2. Claude will request access to your location if not already granted.
3. Based on your location, Claude provides relevant suggestions.
4. You can view locations on a map and get navigation directions.

**Example:** "Find good restaurants near me that are open now."

#### Displaying locations with Maps

1. When Claude suggests locations, they can be displayed on an interactive map.
2. Tap on any location to see more details.
3. Select a location to open it in Apple Maps for navigation.
4. Get turn-by-turn directions directly from the map.

**Example:** "Show me coffee shops within walking distance on a map."

#### Managing your calendar

1. Ask Claude to check your schedule or create events.
2. Claude will request calendar access if not already granted.
3. For checking availability: Claude reads your calendar and identifies free slots.
4. For creating events: Claude prepares event details and adds them to your calendar.
5. You can edit or delete events as needed.

**Examples:**

- "When am I free this week for a 30-minute meeting?"
- "Schedule a dentist appointment for next Friday at 10 AM."
- "Add a weekly team standup every Monday at 9 AM."

#### Creating and managing reminders

1. Ask Claude to create reminders or add items to lists.
2. Claude will request Reminders access if not already granted.
3. Claude can add items to existing lists or create new reminders.
4. Set due dates, priorities, and notes for reminders.
5. Manage recurring reminders for regular tasks.

**Examples:**

- "Add milk and eggs to my grocery list."
- "Remind me to call the dentist tomorrow at 2 PM."
- "Create a packing list for my trip next week."

Note that when Claude uses tools to take these actions, their use is preserved in the conversation history in the same way as any tool.

---

## Accessing and analyzing your health data

> **Note:** Health features are available in beta on Pro and Max plans only, and currently limited to users in the US.

Claude can read your health and fitness data from Apple Health to help you understand patterns, track progress, and make informed decisions about your wellbeing. When you ask Claude about your health data, it can display insights using native charts that feel integrated with iOS.

> **Important:** We are not a medical device and cannot provide medical guidance. Always consult a licensed professional.

#### What health data can Claude access?

With your permission, Claude can read the following types of data from Apple Health:

- **Activity metrics:** Steps, distance, flights climbed, active calories, exercise minutes, move and stand hours.
- **Workouts:** Type (running, cycling, strength, yoga, etc.), duration, distance, heart rate data, and calories burned.
- **Vitals:** Heart rate, resting heart rate, heart rate variability (HRV), blood pressure, respiratory rate, and blood oxygen.
- **Body measurements:** Weight, height, body mass index, and body fat percentage.
- **Sleep:** Total sleep time, sleep stages, time in bed, and sleep efficiency.
- **Nutrition:** Calories consumed, macronutrients, water intake, and micronutrients (if tracked).

> **Note:** Our [memory feature](https://support.claude.com/en/articles/11817273-using-claude-s-chat-search-and-memory-to-build-on-previous-context#h_c1c0b33879) is designed to prevent Claude from using sensitive health information in future conversations.

#### How to use health features

1. Ask Claude a question about your health or fitness data (for example: "How have my runs been trending this month?" or "Show me my sleep patterns over the past two weeks").
2. Claude will request access to your health data if not already granted.
3. Review the permission prompt and select your preferred option.
4. Claude analyzes your data and provides insights, often with visual charts to help you understand trends.

#### Example prompts

- "Help me create a training plan for my upcoming half-marathon based on my recent running data."
- "Why have I been feeling tired lately? Can you look at my sleep and activity data?"
- "Show me how my resting heart rate has changed over the past three months."
- "Compare my workout consistency this month versus last month."
- "What patterns do you see in my step count throughout the week?"

#### Understanding health visualizations

Claude displays health insights using native iOS charts that appear directly in your conversation. These charts can show:

- **Bar charts** for comparing activity across days or weeks.
- **Line charts** for tracking trends over time (pace, heart rate, weight)
- **Progress indicators** for goals and milestones

Tap on chart elements to see more details about specific data points.

## Usage guidelines for optimal results

To get the best results, be specific about what you want, include relevant details like dates, times, and locations in your requests, and review content before sending or saving. Claude understands natural language, so you can make requests conversationally.

---

## What data can Claude access?

Claude only accesses the data necessary for each specific request:

- **Location:** Current location only when relevant to your request.
- **Calendar:** Event details to check availability and create/modify events.
- **Messages/Email:** Claude does not read existing messages or emails, only creates new content.
- **Reminders:** Existing lists and items to add/manage tasks.
- **Health:** Activity, workout, vital signs, body measurements, sleep, and nutrition data — only when you ask a question that requires this information and have granted permission.

Claude's connection to your iOS apps works through your device's built-in sharing and permission systems—the same secure methods you use with any iPhone app.

## Do I need to grant permission to Claude for iOS?

Permission requirements vary by feature:

- **Messages and Email:** No permissions required (uses your device’s built-in sharing system).
- **Calendar Events:** Permission required for reading calendar; writing can use system UI without permission.
- **Location and Maps:** Permission required when Claude needs to access your location.
- **Reminders:** Prompted when Claude needs to access reminder lists.
- **Health:** Permission required. Claude will request access to specific health data categories when needed.

For features requiring permissions (like location or calendar access), Claude will request permission contextually with clear explanations of why the access is needed. You’ll be prompted to approve the action with three options: Allow once, Always allow, or Don't allow.

These permissions can be managed at any time in your device settings by going to Settings > Claude. You'll see all available permissions like Location, Calendar, and Reminders and can tap on each permission to adjust access levels. You can toggle between "While Using App” and “Ask next time” to change Claude’s access, or remove permissions by choosing “Never.”

Health permissions work differently from other app permissions. When Claude requests health access, you'll see the standard iOS Health permissions screen where you can choose exactly which data types to share. You can modify these permissions at any time by going to Settings > Health > Data Access & Devices > Claude.

Claude will only request permissions if needed for specific features, and you can always choose to decline while still using other capabilities.

---

## Troubleshooting

#### Claude isn't offering to use my apps

- Make sure you're using the latest version of the Claude iOS app. See [How to update Claude for iOS](https://support.anthropic.com/en/articles/11825384-how-to-update-claude-for-ios) for instructions.
- Try being more specific in your request (refer to the examples listed above).
- Restart Claude for iOS and try again.

#### Permission prompts don't appear

- Check that the app for which Claude needs permissions is installed and set up on your phone.
- Verify iOS system permissions by navigating to Settings > Privacy & Security.
- Ensure Claude for iOS has the necessary permissions enabled.

#### Features aren't working as expected

- Your iOS mobile apps may format content slightly differently than Claude.
- You can always edit the content in the destination app before sending or saving.
- Some features may vary based on your iOS version.

#### Calendar events aren't opening correctly

- Verify you have a calendar app installed.
- Check that your preferred calendar app is set as the default for calendar events.
- Make sure the calendar app you’re trying to use is up to date.

#### Health data isn't appearing or seems incomplete

- Verify that you have a Pro or Max plan and are located in the US.
- Check that you've granted Claude access to the relevant health data types in Settings > Health > Data Access & Devices > Claude.
- Ensure your health data is being recorded. Some data types require an Apple Watch or compatible device.
- If you recently started tracking a metric, there may not be enough historical data for trend analysis.
- Try asking about a specific data type to confirm which categories Claude can access.

**Need more help?** If you're experiencing issues with these features, try restarting Claude for iOS or [updating to the latest version from the App Store](https://support.claude.com/en/articles/11825384-how-to-update-claude-for-ios).

## Related Articles
- [Installing Claude for iOS](https://support.claude.com/en/articles/9266462-installing-claude-for-ios)
- [Using Claude App Intents, Shortcuts, and Widgets on iOS](https://support.claude.com/en/articles/10263469-using-claude-app-intents-shortcuts-and-widgets-on-ios)
- [Using Claude with Android Apps](https://support.claude.com/en/articles/11869629-using-claude-with-android-apps)
- [Using the Blackbaud Connector in Claude](https://support.claude.com/en/articles/12923221-using-the-blackbaud-connector-in-claude)
- [Let Claude use your computer in Cowork](https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork)
