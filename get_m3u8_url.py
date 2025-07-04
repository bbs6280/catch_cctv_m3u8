import sys
import os
from playwright.sync_api import sync_playwright

def extract_title_and_m3u8_urls(url):
    m3u8_urls = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        def handle_request(request):
            if request.url.endswith('.m3u8') or ".m3u8?" in request.url:
                m3u8_urls.append(request.url)

        def handle_response(response):
            if response.url.endswith('.m3u8') or ".m3u8?" in response.url:
                m3u8_urls.append(response.url)

        page.on("request", handle_request)
        page.on("response", handle_response)

        # 访问页面
        page.goto(url, timeout=30000)
        page.wait_for_timeout(8000)

        # 提取标题
        title = page.title()

        browser.close()

    unique_m3u8 = list(set(m3u8_urls))

    # 处理标题：去除首尾空白，内部空格替换为下划线
    clean_title = title.strip()
    # clean_title = title.strip().replace(' ', '_')

    # 追加写入文件
    list_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "list.txt")
    with open(list_path, 'a', encoding='utf-8') as f:
        for m3u8_url in unique_m3u8:
            f.write(f"{m3u8_url}|{clean_title}\n")

    print(f"网页标题：{title}")
    print(f"捕获到 {len(unique_m3u8)} 个 .m3u8 请求，已追加到 list.txt 文件")

# === 主程序入口 ===
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ 用法：python get_m3u8_url.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    extract_title_and_m3u8_urls(url)
