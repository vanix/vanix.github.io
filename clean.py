from pathlib import Path
import shutil

import frontmatter
from markdownify import markdownify as html_to_md

POST_DIR = Path("_posts")
BACKUP_DIR = Path("_posts_backup")


def make_backup():
    """備份整個 _posts 資料夾到 _posts_backup（如果還沒備份過）"""
    if BACKUP_DIR.exists():
        print(f"[INFO] 備份資料夾 {BACKUP_DIR} 已存在，略過備份步驟。")
        return
    shutil.copytree(POST_DIR, BACKUP_DIR)
    print(f"[INFO] 已將 {POST_DIR} 備份到 {BACKUP_DIR}")


def need_convert(text: str) -> bool:
    """簡單判斷內容是否主要是 Blogger HTML，需要轉換。"""
    html_signals = [
        "<p", "<div", "<span", "<h1", "<h2", "<h3", "<ul", "<ol", "<li", "<hr", "<font"
    ]
    return any(s in text for s in html_signals)


def clean_content(html: str) -> str:
    """
    將 Blogger 風格的 HTML 轉成 Markdown。
    """
    md = html_to_md(
        html,
        heading_style="ATX",  # 用 # ## ### 這種標題
        bullets="-",          # 使用 - 當作項目符號
    )

    # 簡單後處理：合併多個空白行
    lines = [line.rstrip() for line in md.splitlines()]
    cleaned_lines = []
    empty_count = 0

    for line in lines:
        if line.strip() == "":
            empty_count += 1
            # 最多保留一行空白
            if empty_count <= 1:
                cleaned_lines.append("")
        else:
            empty_count = 0
            cleaned_lines.append(line)

    cleaned = "\n".join(cleaned_lines).strip() + "\n"
    return cleaned


def write_post_safe(path: Path, post):
    """
    安全寫入：先寫到暫存檔，再覆蓋原檔。
    同時處理 str/bytes 差異，避免 TypeError。
    """
    data = frontmatter.dumps(post)  # 可能回傳 str 或 bytes

    # 確保最後寫出去的是 bytes
    if isinstance(data, str):
        data = data.encode("utf-8")

    tmp_path = path.with_suffix(path.suffix + ".tmp")

    # 先寫入暫存檔
    with open(tmp_path, "wb") as f:
        f.write(data)

    # 寫完後再取代原檔
    tmp_path.replace(path)


def main():
    make_backup()

    md_files = sorted(POST_DIR.glob("*.md"))
    if not md_files:
        print("[WARN] _posts 資料夾裡沒有 .md 檔。")
        return

    for path in md_files:
        print(f"[INFO] 處理 {path} ...")

        # 這裡用 frontmatter.load(path)，讓它自己處理編碼，回傳 str
        post = frontmatter.load(path)

        content = post.content

        # 保險：如果內容是 bytes，就轉成 str
        if isinstance(content, bytes):
            try:
                content = content.decode("utf-8")
            except Exception:
                content = content.decode("utf-8", errors="ignore")

        if not need_convert(content):
            print("  -> 看起來不是 Blogger HTML，略過。")
            continue

        new_content = clean_content(content)

        if new_content.strip() == str(post.content).strip():
            print("  -> 轉換後內容相同，略過寫入。")
            continue

        post.content = new_content

        try:
            write_post_safe(path, post)
            print("  -> 已轉換並寫回檔案。")
        except Exception as e:
            print(f"  [ERROR] 寫入 {path} 時發生錯誤：{e}")
            print("          原始檔案已保留，請手動檢查。")

    print("\n[完成] 處理結束。原始檔案已備份在 _posts_backup 資料夾中。")


if __name__ == "__main__":
    main()
