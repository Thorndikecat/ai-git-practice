# AI Git Practice

本仓库用于完成 2026 年春季读书实践周的 Git 与代码版本管理必做任务。

项目主题：人工智能基础实践，使用 Python 编写一个简单的感知机分类示例。

## 一、项目简介

本项目通过一个简单的感知机模型学习 AND 逻辑门，展示人工智能中“模型训练、预测、误差修正”的基本思想。

代码文件：

- `perceptron_demo.py`：感知机训练与预测示例。
- `.gitignore`：忽略 Python 缓存、虚拟环境和编辑器配置文件。

运行方式：

```powershell
python perceptron_demo.py
```

## 二、学习资料来源

- Git 官方文档：https://git-scm.com/doc
- GitHub Docs：https://docs.github.com/
- 菜鸟教程 Git 教程：https://www.runoob.com/git/git-tutorial.html

## 三、实践流程

1. 检查 Git 环境，确认本机已经安装 Git。
2. 配置 Git 用户名和邮箱，用于记录提交作者信息。
3. 创建 `ai-git-practice` 项目文件夹。
4. 使用 `git init` 初始化本地仓库。
5. 编写人工智能实践代码和项目说明。
6. 使用 `git add` 将文件加入暂存区。
7. 使用 `git commit` 完成本地版本提交。
8. 后续创建公开远程仓库，并使用 `git remote add origin` 和 `git push` 上传代码。

## 四、提交记录说明

本项目规划并完成不少于 3 次有效提交：

1. `初始化人工智能实践项目`：创建项目基础结构，添加 `.gitignore` 和初始 `README.md`。
2. `添加感知机分类示例代码`：添加 `perceptron_demo.py`，实现简单感知机训练与预测。
3. `完善Git实践学习笔记`：补充学习资料来源、实践流程、问题解决方法和学习心得。

## 五、遇到的问题及解决方法

### 问题 1：当前文件夹不是 Git 仓库

现象：执行 `git status` 时提示 `fatal: not a git repository`。

解决方法：进入项目文件夹后执行：

```powershell
git init
```

初始化完成后，当前文件夹就可以使用 Git 进行版本管理。

### 问题 2：远程仓库和本地仓库没有关联

现象：本地可以提交，但无法直接 `git push` 到 GitHub 或 Gitee。

解决方法：先在 GitHub 或 Gitee 创建公开仓库，再执行：

```powershell
git remote add origin 远程仓库地址
git branch -M main
git push -u origin main
```

之后再提交新版本时，只需要执行 `git push`。

## 六、Git 学习心得

通过本次实践，我了解了 Git 的基本工作流程，包括初始化仓库、暂存文件、提交版本、查看状态和关联远程仓库。Git 能够记录项目的每一次变化，使代码修改过程更加清晰，也方便在出现问题时回看历史版本。

作为人工智能专业学生，后续在模型训练、实验代码管理、数据处理脚本维护和课程项目协作中，Git 都是非常重要的工具。合理使用 Git 可以让实验过程更可追踪，也能帮助团队成员更高效地协作。
