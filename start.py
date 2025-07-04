import sys
import asyncio
import json
import subprocess
from playwright.async_api import async_playwright

# 存储去重后的播放页链接
play_page_urls = set()

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        async def handle_response(response):
            if "getVideoStreamByAlbumId" in response.url:
                try:
                    text = await response.text()
                    json_str = text.strip()

                    # 处理 JSONP
                    if json_str.startswith("Callback"):
                        start = json_str.find("(")
                        end = json_str.rfind(")")
                        if start != -1 and end != -1:
                            json_str = json_str[start+1:end]
                        else:
                            print("⚠️ JSONP 格式异常，跳过")
                            return

                    data = json.loads(json_str)
                    video_list = data.get("data", {}).get("list", [])

                    for item in video_list:
                        url = item.get("url")
                        if url:
                            play_page_urls.add(url)
                            print(f"✅ 收集到播放页: {item.get('title')} ➡ {url}")

                except Exception as e:
                    print("解析失败:", e)

        # 绑定响应拦截器
        page.on("response", handle_response)

        # 打开起始页面
        await page.goto("https://tv.cctv.com/2019/12/26/VIDEeiI6VzMKKVJSAXsVXfka191226.shtml")

        # 等待 JS 动态请求加载
        await page.wait_for_timeout(10000)

        await browser.close()

    # 所有播放页处理完毕后，调用 get_m3u8_url.py 脚本
    print("\n📦 共计播放页链接数量:", len(play_page_urls))
    for url in play_page_urls:
        print(f"🚀 正在处理: {url}")

        python_executable = sys.executable  # 当前运行start.py时的Python解释器
        # 调用时改为
        subprocess.run([python_executable, "get_m3u8_url.py", url])

# 运行主程序
asyncio.run(main())
