# 自动化刷题系统

基于 **FastAPI** + **Vanilla JS** 开发的轻量级模拟考试系统，专为刷题而生。

## ✨ 功能特性
- **顺序抽取**：严格按照 `questions.json` 中的顺序抽取前 N 道题。
- **内部乱序**：在选定的题目范围内，前端自动进行随机洗牌（Shuffle），防止死记硬背。
- **即时评分**：提交后立即显示红绿灯标记，支持查看正确答案。
- **代码支持**：支持语法高亮，完美呈现技术细节。

## 🚀 快速开始
```bash
pip install -r requirements.txt
```
直接点击bat就可以启动后端service

### 1. 克隆项目
```bash
git clone https://github.com/aoster97/fuck_vce.git
```

🖕 FuckVCE: The Lightweight Quiz Simulator
A lightweight, local-first exam simulator built with FastAPI + Vanilla JS. 
Designed for those who just want to study without being robbed.

😤 Why does this exist?
Let’s be real: paying $99/month for a VCE subscription is absolutely unhinged. 
It’s a quiz player, not a Tier-3 Data Center. 
I also didn't want to go through the headache of installing a PHP environment (XAMPP/WAMP) just to run a simple web-based quiz tool.
FuckVCE is the "keep it simple" solution: No subscriptions, no PHP, just Python and a browser.

✨ Features
* Sequential Extraction: Strictly pulls the first $N$ questions from questions.json in order.
* Internal Shuffling: Automatically shuffles the selected pool on the frontend to prevent "positional muscle memory.
* "Instant Scoring: "Traffic Light" system—get immediate feedback with red/green markers and correct answers upon submission.
* Code Support: Beautiful syntax highlighting for SQL, Python, and more, powered by Highlight.js.

🚀 Quick Start
1. Clone the Repo
2. Install Dependencies
3. Launch
No complex commands required. Just double-click the .bat file to fire up the backend service.

📂 Question Configuration
Edit backend/questions.json to add your own material.
ID: Unique question number.
Options: Array of choices.
Answer: The correct string (e.g., "B" or "ACD").


