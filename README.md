# Idea to Production VibeCoding

**Author:** Neil Bauman / Catnip 薄荷猫

这是一个把“模糊想法”转化为“可施工、可测试、可回滚、可接力的软件项目”的 Agent Skill。

它适合在以下 CLI Agent 中使用：

- Codex CLI
- Claude Code CLI
- 其他支持标准 `SKILL.md` 的 Agent

## 它会做什么

使用后，Agent 会按下面的顺序工作：

1. 追问并澄清 idea；
2. 区分核心产品与辅助功能；
3. 固化产品需求和非目标；
4. 设计架构与层级边界；
5. 创建施工文档体系；
6. 检查仓库和 Git 状态；
7. 创建远端备份分支；
8. 按 Phase 小步施工；
9. 一步一测试；
10. 保存失败、修复、复测记录；
11. 修正文档漂移；
12. 更新接力文档；
13. 提交并推送；
14. 汇报真实状态。

## 推荐触发方式

安装后，在 Agent 对话中输入：

```text
请使用 idea-to-production-vibecoding Skill。

我有一个产品 idea，请先进入 Discovery Mode。持续向我提问并总结，直到产品核心对象、目标用户、第一版边界、用户路径和成功标准都明确。

在我确认产品定义之前，不要开始写代码。
```

已有仓库时：

```text
请使用 idea-to-production-vibecoding Skill，以 Resume Mode 接管当前仓库。

先读取 AGENTS.md 和 docs 中的施工文档，检查 Git、分支、未提交改动、远端和测试基线。不要覆盖任何未知修改。先告诉我当前项目真实状态，再制定本轮施工计划。
```

准备开始完整建设时：

```text
请使用 idea-to-production-vibecoding Skill，进入 Full Construction Mode。

从产品澄清开始，完成产品文档、施工文档、Git 备份、阶段计划、逐步开发、测试、漂移修正、接力记录、提交与推送。每轮只做当前 Phase，不得越界。
```

## 文件结构

```text
idea-to-production-vibecoding/
├── SKILL.md
├── README.md
├── references/
│   ├── QUESTIONNAIRE.md
│   ├── CONSTRUCTION_DOCS.md
│   ├── GIT_SAFETY.md
│   ├── TESTING_AND_HANDOFF.md
│   └── OUTPUT_TEMPLATES.md
└── scripts/
    └── bootstrap_construction_docs.py
```

## 脚手架脚本

可在项目根目录运行：

```bash
python path/to/idea-to-production-vibecoding/scripts/bootstrap_construction_docs.py \
  --project-name "My Product" \
  --owner "Your Name" \
  --brand "Your Brand"
```

脚本默认不会覆盖已有文件。

## 设计原则

这不是“让 AI 快速堆代码”的 Skill。

它的目标是：

> 用施工文档、阶段边界、Git 回滚、测试闭环和 Agent 接力，把 AI 的高产出能力约束成稳定的软件工程能力。
