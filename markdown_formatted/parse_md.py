import re
import json


def parse_ocp_md(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace("==","")
    # 按题目切分
    blocks = re.split(r'\n(?=###\s+Q\d+|\*\*Q\d+\.\*\*)', content)
    results = []

    for block in blocks:
        block = block.strip()
        if not block: continue

        # 1. 提取原始答案字母 (例如: ABD)
        ans_match = re.search(r'Answer:\s*([A-G]+)', block, re.IGNORECASE)
        ans_letters = ans_match.group(1).upper() if ans_match else ""

        # 2. 提取并清理选项
        # 正则匹配 A) 或 A. 开头的行
        opt_lines = re.findall(r'([A-G][\).].+)', block)

        # 建立 字母 -> 纯文本 的映射
        temp_opt_map = {}
        for line in opt_lines:
            # 剥离前缀，例如把 "A) text" 变成 "text"
            clean_text = re.sub(r'^[A-G][\).]\s*', '', line).replace('==', '').strip()
            letter = line[0].upper()
            temp_opt_map[letter] = clean_text

        # 3. 将答案字母转换为对应的文本列表
        # 如果是多选 ABD，则答案存为数组或拼接的文本
        correct_texts = [temp_opt_map[l] for l in ans_letters if l in temp_opt_map]

        # 4. 提取题干 (去掉题目编号和选项部分)
        q_text = re.split(r'\n[A-G][\).]', block)[0]
        q_text = re.sub(r'^(###\s+Q\d+|预览\s+Q\d+|\*\*Q\d+\.\*\*)\s*', '', q_text).strip()

        results.append({
            "id": len(results) + 1,
            "question": q_text,
            "options": list(temp_opt_map.values()),  # 纯文本列表
            "answer": "||".join(correct_texts)  # 使用特殊分隔符存储正确文本
        })

    with open("questions.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)


parse_ocp_md("mysql_ocp.md")