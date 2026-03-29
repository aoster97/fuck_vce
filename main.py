import json
import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from pydantic import BaseModel

app = FastAPI()

# 允许跨域访问，确保与前端 index_v2.html 兼容
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 读取题库
# 假设 questions.json 是一个包含多个题目对象的列表
try:
    with open("questions.json", "r", encoding="utf-8") as f:
        QUESTIONS = json.load(f)
except FileNotFoundError:
    QUESTIONS = []
    print("错误：未找到 questions.json 文件")


@app.get("/questions")
def get_questions(count: int = 10):
    """
    按照 JSON 顺序抽取前 count 道题。
    不再在后端打乱，交由前端进行乱序显示，以保证逻辑可控。
    """
    # 1. 按照 JSON 原始顺序截取前 count 题
    selected = QUESTIONS[:min(count, len(QUESTIONS))]

    # 2. 直接返回原始题目（包含正确选项顺序）
    # 前端接收后会自行通过 shuffleArray 进行打乱显示
    return selected


@app.post("/submit")
def submit(answers: List[dict]):
    """
    提交接口，兼容前端发送的 [{id: 1, answer: "ABC"}] 格式
    """
    score = 0
    total = len(answers)

    # 构建 ID 到正确答案的映射表
    correct_map = {q["id"]: q.get("answer", "") for q in QUESTIONS}

    result_detail = []

    for a in answers:
        qid = a.get("id")
        user_ans = a.get("answer", "")
        correct_ans = correct_map.get(qid)

        # 判定对错（注意：前端已对用户选项进行了字母排序拼接）
        is_right = (user_ans == correct_ans)
        if is_right:
            score += 1

        result_detail.append({
            "id": qid,
            "your": user_ans,
            "correct": correct_ans,
            "is_right": is_right
        })

    return {
        "score": score,
        "total": total,
        "detail": result_detail
    }


if __name__ == "__main__":
    import uvicorn

    # 启动命令：python main.py
    uvicorn.run(app, host="127.0.0.1", port=8000)