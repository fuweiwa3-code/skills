---
name: nowcoder-backend-interview-digest
description: Crawl and summarize Nowcoder interview-experience posts for big-tech backend, server-side, AI backend, Agent development, and platform development roles, then send the digest to Feishu using this skill's bundled webhook sender. Use when Codex needs one integrated workflow to collect latest Nowcoder posts, filter Alibaba/Tencent/ByteDance/Baidu/Meituan/JD/PDD/Kuaishou/NetEase/Xiaomi/Ant backend interview questions, choose high-quality questions, and deliver the Feishu notification.
---

# Nowcoder Backend Interview Digest

## Overview

Collect recent Nowcoder interview-experience posts in time order, keep big-tech backend/platform/AI-backend candidates, select high-signal questions, and send a Feishu study digest when a webhook is available.

This skill is a workflow skill. It coordinates with `web-access` for browsing Nowcoder and uses its bundled `scripts/send_feishu_message.py` for delivery. Treat "crawl/summarize interview questions" and "send to Feishu" as one synchronous workflow unless the user explicitly says not to send.

## References

Load these only when needed:

- `references/company-keywords.md`: company names, aliases, and business-group hints.
- `references/role-keywords.md`: included and excluded role keywords.
- `references/quality-rules.md`: question scoring and filtering rules.
- `references/feishu-template.md`: final message format.
- `scripts/send_feishu_message.py`: bundled Feishu/Lark webhook sender.

## Default Output Target

Unless the user overrides it:

- Select `3` posts.
- Select `3` questions from each post.
- Produce `9` questions total.
- Send the digest to Feishu if a webhook is supplied, configured, or known from the current conversation.
- If no webhook is available, output the Feishu-ready text and clearly state that delivery is pending webhook configuration.
- Only skip Feishu delivery when the user explicitly says "不要发送", "只输出", or equivalent.

## Workflow

1. Use `web-access` before any Nowcoder network or browser operation.
2. Open Nowcoder's interview center or search results while preserving the user's logged-in browser state when available.
3. Prefer the latest/time-sorted interview feed. Scan in displayed time order.
4. For each list item, use company aliases plus role keywords to decide whether to add it to the candidate pool.
5. Open candidate posts one at a time. Extract:
   - company name
   - role/direction
   - interview round
   - interview date or timeline
   - post publish time
   - source URL
   - question list
6. Keep scanning until there are enough strong candidates for the requested output. For the default `3 x 3`, collect at least `5-8` candidates if available, then choose the best `3`.
7. Score questions with `references/quality-rules.md`.
8. For each selected post, pick the top `3` questions. Rewrite lightly for clarity, but do not invent details.
9. Format the result with `references/feishu-template.md`.
10. Immediately invoke this skill's bundled `scripts/send_feishu_message.py` when a webhook is available. This is part of the normal completion path, not a separate follow-up task.
11. Close any browser tabs created for the task.
12. Report the selected post count, question count, and Feishu delivery status. Avoid echoing full webhook URLs.

## Candidate Selection

Prefer candidates that have:

- A target company from `company-keywords.md`.
- A backend/server/platform/AI-backend role from `role-keywords.md`.
- Explicit interview date, timeline, or publish time.
- Multiple concrete technical questions.
- Scenario, system design, project deep-dive, high-concurrency, data, network, distributed systems, AI backend, or Agent questions.

Reject or de-prioritize:

- Posts with only timeline, emotional notes, or offer discussion.
- Pure HR interviews.
- Frontend/product/operations/client/testing-only roles unless the post clearly contains backend/platform questions.
- Posts that only contain generic prompts such as "self introduction" or "talk about project" without technical detail.

## Time Handling

When Nowcoder uses relative dates such as "yesterday" or "today", convert them using the current local date if known. If exact interview time is missing, write `面试时间：未注明，帖子发布于 ...`.

Do not pretend a publish time is the interview time. Keep them distinct.

## Copyright-Safe Summarization

Do not copy full posts. Extract only short question descriptions and paraphrase into study prompts. Keep source links so the user can inspect originals.

## Feishu Integration

Default behavior:

1. Generate the final message text first.
2. Use this skill's bundled sender:

   ```bash
   python3 /Users/awei/.codex/skills/nowcoder-backend-interview-digest/scripts/send_feishu_message.py \
     --webhook "$FEISHU_WEBHOOK_URL" \
     --text "$DIGEST_TEXT"
   ```

   The sender also accepts `FEISHU_WEBHOOK_URL` and optional `FEISHU_WEBHOOK_SECRET` environment variables.

3. Send one concise text message unless the message would be too long; if too long, split by company/post.
4. Confirm Feishu API success before claiming delivery.
5. If delivery fails, return the error summary and keep the generated digest in the response so the user can retry.
