# Quality Rules

Score questions to select the best study prompts.

## High-Quality Signals

Add weight for:

- Scenario/system design: 秒杀, 订单超时, 支付, 限流, 日志, 定时任务, 海量数据, 文件交集, 浏览器前进后退, cd/pwd path simulation.
- Project deep dive: request lifecycle, login system, cache/database consistency, service splitting, data model, bottleneck, business flow.
- Backend fundamentals with depth: TCP state machine, MVCC, index optimization, Redis persistence/eviction/cache breakdown, thread pool internals, lock/CAS, IPC, STL invalidation.
- Distributed systems: service discovery, Raft, microservice calls, multi-level cache, distributed transactions, scheduler design.
- AI backend/Agent: Agent timeout/failure handling, RAG/knowledge-base fallback, SSE high concurrency, model API rate limit, context management, MCP/Skill design, AI coding workflow.
- Constraints: explicit scale or limits such as 1000 万 tasks, 100 亿 ints, 256MB memory, 5000 万 UUID strings, 100 concurrent LLM requests.

## Low-Quality Signals

Drop or de-prioritize:

- 自我介绍
- 反问
- 能不能实习/实习多久
- 你有什么优势
- 你最近学什么
- Generic "讲一下项目" without follow-up details
- Generic "线程池是什么" unless paired with internals or scenario
- Generic "Redis 是什么" or "MySQL 是什么"
- Single short algorithm names with no context, unless the post has too few alternatives

## Selection Procedure

1. Extract all candidate questions from a post.
2. Merge duplicate or highly overlapping questions.
3. Prefer questions that can be practiced as standalone prompts.
4. Select exactly 3 questions per post by default.
5. Rewrite lightly into clear study questions. Preserve concrete constraints and scenario details.
6. Add 2-4 terse `考察点` tags per question.

## Post Ranking

When choosing final posts, prefer:

1. Explicit target company + explicit backend/platform role.
2. Recent or latest in feed order.
3. Detailed questions with constraints and context.
4. Diversity across companies if possible.
5. Diversity across topics: system design, database/cache, network/concurrency, AI backend/Agent.
