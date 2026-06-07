# Design to Frontend Workflow

一套面向 AI 编程代理的端到端 UI 工作流 Skill，用于把产品方向、视觉探索、Figma 设计、前端实现和浏览器验收串成一条可追踪、可复查的交付链路。

它不把 Stitch 或其他生成式 UI 工具的结果直接视为生产代码，而是通过明确的阶段、产物和审批关卡，让产品意图、正式设计、代码实现与运行效果保持一致。

## 适用场景

- 从零设计 Web、移动端 Web 或应用界面。
- 对现有产品进行较大范围的 UI/UX 重设计。
- 将已有 Figma 设计实现为前端页面。
- 从 Stitch、静态稿或视觉参考过渡到正式设计和代码。
- 改进已有组件的交互、状态、响应式或可访问性。
- 对实现结果进行桌面端和移动端视觉验收。

## 核心原则

1. **先明确产品方向，再开始画界面**
2. **每个阶段都有明确产物和完成条件**
3. **Stitch 用于探索，不是最终设计真源**
4. **Figma 或屏幕规格负责定义正式设计**
5. **前端代码负责运行行为**
6. **浏览器验收负责证明视觉与交互质量**
7. **从当前未完成阶段继续，不重复已经完成的工作**

## 工作流

```text
产品方向
   ↓
设计系统
   ↓
视觉探索
   ↓
正式设计
   ↓
前端实现
   ↓
浏览器运行验收
```

### 1. 产品方向

明确以下内容：

- 核心用户
- 主要任务
- 产品身份与情绪基调
- 信息密度
- 目标设备
- 必要页面和核心流程

应提供 2 至 3 个真正不同的方向，而不是只更换颜色。

**产物：**

- `design/UI-BRIEF.md`
- `design/decisions/YYYY-MM-DD-<decision>.md`

**完成条件：** 用户明确批准一个方向。

### 2. 设计系统

根据批准的方向定义：

- 色彩角色和设计 Token
- 字体与排版
- 间距、网格和内容宽度
- 表面、边框、圆角与阴影
- 图标规范
- 动效与减少动态效果
- 桌面端和移动端响应式规则
- 加载、空状态、错误、禁用、聚焦和危险操作状态
- 明确禁止的视觉与交互模式

**产物：** `design/DESIGN.md`

**完成条件：** 两个不同页面遵循这些规则时，能够明显属于同一产品。

### 3. 视觉探索

在需要较广视觉探索时，可使用 Stitch 生成 2 至 3 个高保真方案。所有方案必须使用相同的产品需求和设计系统，只改变构图、重点或交互表达。

如果不使用 Stitch，也可以使用：

- Figma
- Visual Companion
- 静态 Mockup
- 屏幕规格文档

**完成条件：** 选定一个构图方向，并记录保留、拒绝和合并的设计内容。

### 4. 正式设计

使用 Figma 将批准的方向整理为可维护设计：

- 颜色、字体和间距变量
- 可复用组件及其变体
- 桌面端与移动端 Frame
- 组件完整状态
- 必要的交互原型

如果项目明确跳过 Figma，则屏幕规格必须成为正式设计真源，完整描述布局、Token、状态和响应式行为。

**产物：**

- Figma 文件，或
- `design/screens/<screen-name>.md`

### 5. 前端实现

实现前先检查现有代码库：

- 技术栈与依赖
- 组件约定
- Design Token
- 图标库
- 路由、状态管理和数据获取模式

先实现共享基础组件，再实现页面构图、交互状态和响应式行为。

不要未经架构审查就把 Stitch 生成的 HTML 直接复制进生产项目。

**完成条件：**

- 构建通过
- 类型检查通过
- 相关测试通过
- 必要状态均已实现

### 6. 浏览器运行验收

使用真实浏览器打开实现结果，在代表性的桌面端和移动端尺寸下，与批准的 Figma 或屏幕规格进行对比。

重点检查：

- 视觉层级
- 对齐与间距
- 字体和颜色
- 图标一致性
- 加载、空状态、错误和禁用状态
- Hover、Active、Focus 和键盘操作
- 响应式布局
- 横向溢出与内容裁切
- 对比度与减少动态效果

**产物：** `design/visual-qa/<screen-name>.md`

**完成条件：** 没有未解决的高影响视觉、交互、响应式或可访问性问题。

## 推荐项目结构

```text
design/
├── UI-BRIEF.md
├── DESIGN.md
├── screens/
│   └── <screen-name>.md
├── decisions/
│   └── YYYY-MM-DD-<decision>.md
└── visual-qa/
    └── <screen-name>.md
```

## 真源层级

| 关注点 | 真源 |
|---|---|
| 产品意图与范围 | `design/UI-BRIEF.md` |
| 视觉语言与 Token | `design/DESIGN.md` |
| 页面构图 | Figma，或明确跳过 Figma 时的屏幕规格 |
| 运行行为 | 前端代码 |
| 视觉与响应式证据 | `design/visual-qa/` |

## 安装

将整个目录放入 Agent 的 Skills 目录：

```bash
mkdir -p ~/.agents/skills
cp -R design-to-frontend-workflow ~/.agents/skills/
```

最终路径应为：

```text
~/.agents/skills/design-to-frontend-workflow/SKILL.md
```

## 使用

在支持 Skills 的 AI 编程代理中明确调用：

```text
使用 design-to-frontend-workflow，帮我把这个管理后台从产品方向推进到前端实现和浏览器验收。
```

已有 Figma 时：

```text
使用 design-to-frontend-workflow，实现这个已经批准的 Figma 页面，并完成桌面端和移动端视觉验收。
```

小范围组件改进时：

```text
使用 design-to-frontend-workflow，改进聊天输入框的 Focus、错误和移动端状态。
```

## 配套能力

工作流会根据任务阶段选择所需能力，不要求一次加载所有视觉 Skill：

- `brainstorming`：产品方向和需求澄清
- `stitch-design-taste`：Stitch 输入与视觉探索
- `design-taste-frontend`：前端实现
- Figma MCP：正式设计与设计到代码交接
- Browser：运行时、响应式和视觉验收

## 目录说明

```text
design-to-frontend-workflow/
├── SKILL.md
├── README_ZH.md
├── agents/
│   └── openai.yaml
├── assets/
│   ├── UI-BRIEF.template.md
│   ├── DESIGN.template.md
│   ├── SCREEN.template.md
│   └── VISUAL-QA.template.md
└── references/
    ├── acceptance-scenarios.md
    └── tool-handoffs.md
```

## 范围控制

- 小组件修改只运行受影响的阶段。
- 新产品或大型重设计使用完整流程。
- 用户明确不使用 Stitch 或 Figma 时应尊重该决定。
- 不能仅凭“打算完成”判定阶段结束，必须有实际产物或运行证据。
- 产品方向和正式设计需要用户批准；机械实现步骤不需要反复打断用户。

## 验收场景

仓库内的 `references/acceptance-scenarios.md` 提供了以下测试场景：

- 从零创建产品
- 实现已有 Figma
- 小范围组件修改
- Stitch 不可用
- 用户跳过 Figma
- 生成式 UI 漂亮但不完整

修改 Skill 后，可以使用这些场景检查工作流是否仍然遵守预期边界。

## License

当前目录未附带独立许可证。公开发布或允许他人复用前，建议根据实际需求补充 `LICENSE`。
