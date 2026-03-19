# -*- coding: utf-8 -*-
"""
从 爬取的内容.html 中提取正文内容的脚本
"""

from pathlib import Path

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("请先安装 beautifulsoup4: pip install beautifulsoup4")
    exit(1)


def extract_main_content(html: str, output_path: str = None) -> str:
    """
    从 HTML 文件中提取正文内容。
    正文位于 class 包含 post-body 和 ql-view 的 div 中。
    """
    # html_path = Path(html_path)
    # if not html_path.exists():
    #     raise FileNotFoundError(f"文件不存在: {html_path}")
    # 
    # with open(html_path, "r", encoding="utf-8") as f:
    #     html = f.read()

    soup = BeautifulSoup(html, "html.parser")

    # 定位正文区域：用 CSS 选择器或 class 列表查找
    post_body = soup.select_one("div.post-body")
    if not post_body:
        for div in soup.find_all("div", class_=True):
            if "post-body" in div.get("class", []):
                post_body = div
                break

    if not post_body:
        return "未找到正文区域（post-body）。"

    # 标题：class 含 text-darker 的 div
    title = ""
    for d in post_body.find_all("div", class_=True):
        if "text-darker" in d.get("class", []):
            title = d.get_text(strip=True)
            break

    # 正文容器：class 含 ql-view 且内有 <p> 的 div
    content_div = None
    for d in post_body.find_all("div", class_=True):
        if "ql-view" in d.get("class", []) and d.find("p"):
            content_div = d
            break

    # 备用：通过正文特征句「今天的头条」定位
    if not content_div:
        for d in soup.find_all("div", class_=True):
            if d.find("p") and "今天的头条" in d.get_text():
                content_div = d
                break

    if not content_div:
        return "未找到正文区域（ql-view 或含「今天的头条」的 div）。"

    # 按顺序提取所有 <p> 的文本
    lines = []
    if title:
        lines.append(title)
        lines.append("")
    for p in content_div.find_all("p"):
        text = p.get_text(separator=" ", strip=True)
        if text:
            lines.append(text)

    result = "\n".join(lines).strip()

    if output_path:
        out = Path(output_path)
        out.write_text(result, encoding="utf-8")
        print(f"正文已保存到: {out}")

    return result


if __name__ == "__main__":
    base = Path(__file__).parent
    html_file = base / "爬取的内容.html"
    out_file = base / "正文内容.txt"

    text = extract_main_content(str(html_file), str(out_file))
    if not text or text.startswith("未找到"):
        print("提取失败:", text)
    else:
        print("\n--- 提取的正文（前 1500 字）---\n")
        print(text[:1500])
        if len(text) > 1500:
            print("\n... (后续内容已写入文件)")
        print("\n总字数:", len(text))
