# LLM Call Analysis for the 10 Sample Tickets

This run was executed after fixing CSV header handling and ingesting the corpus into the local embeddings store. In this pipeline, the LLM can be called in two places:

1. **Router fallback LLM**: only when the company field is missing or unusable and keyword scoring is not confident enough.
2. **Response LLM**: after routing, retrieval, grounding, and post-safety checks pass.

For the refreshed sample run, all 10 tickets reached the response-generation LLM, and 3 tickets also triggered the router fallback LLM.

## Test Case 1
- **Query:** Test Active in the system
- **Company:** HackerRank
- **Router LLM called:** No
- **Response LLM called:** Yes
- **Why:** Company field routed directly to `hackerrank`, retrieval found relevant context, grounding passed, and the response LLM generated the final answer.

## Test Case 2
- **Query:** site is down & none of the pages are accessible
- **Company:** blank
- **Router LLM called:** Yes
- **Response LLM called:** Yes
- **Why:** No company field was present, so the router used the fallback LLM to classify the ticket as `hackerrank`. After that, retrieval and grounding passed, and the response LLM was called.

## Test Case 3
- **Query:** When should I create a variant versus have a different test?
- **Company:** HackerRank
- **Router LLM called:** No
- **Response LLM called:** Yes
- **Why:** Company field routed directly to `hackerrank`, retrieval found the test-variants article, and the response LLM produced the answer.

## Test Case 4
- **Query:** How to reinvite candidate to Hackerrank assessment and add extra time
- **Company:** HackerRank
- **Router LLM called:** No
- **Response LLM called:** Yes
- **Why:** Company field routed directly to `hackerrank`, retrieval found the extra-time article, grounding passed, and the response LLM was called.

## Test Case 5
- **Query:** please delete my account
- **Company:** HackerRank
- **Router LLM called:** No
- **Response LLM called:** Yes
- **Why:** Company field routed directly to `hackerrank`, retrieval found the delete-account article, and the response LLM generated the reply.

## Test Case 6
- **Query:** One of my claude conversations has some private info ... delete etc?
- **Company:** Claude
- **Router LLM called:** No
- **Response LLM called:** Yes
- **Why:** Company field routed directly to `claude`, retrieval found a Claude privacy-related article, grounding passed, and the response LLM was called.

## Test Case 7
- **Query:** What is the name of the actor in Iron Man?
- **Company:** None
- **Router LLM called:** Yes
- **Response LLM called:** Yes
- **Why:** The router had no usable company field, so it used the fallback LLM and classified the ticket as `claude`. The ticket then reached the response LLM after retrieval and grounding.

## Test Case 8
- **Query:** I bought Visa Traveller's Cheques from Citicorp and they were stolen in Lisbon last night. What do I do?
- **Company:** Visa
- **Router LLM called:** No
- **Response LLM called:** Yes
- **Why:** Company field routed directly to `visa`, retrieval found the traveller's cheques article, and the response LLM was called.

## Test Case 9
- **Query:** Where can I report a lost or stolen Visa card from India?
- **Company:** Visa
- **Router LLM called:** No
- **Response LLM called:** Yes
- **Why:** Company field routed directly to `visa`, retrieval found the Visa support article, grounding passed, and the response LLM was called.

## Test Case 10
- **Query:** Thank you for helping me
- **Company:** blank
- **Router LLM called:** Yes
- **Response LLM called:** Yes
- **Why:** No company field was available, so the router used the fallback LLM and classified the ticket as `claude`. The ticket then reached the response LLM after retrieval and grounding.

## Summary
- **Tickets that called the router fallback LLM:** 2, 7, 10
- **Tickets that called the response LLM:** all 10 tickets
- **Tickets stopped before the response LLM:** none in this fresh run
