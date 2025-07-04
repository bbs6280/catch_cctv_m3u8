

# 📺 catch\_cctv\_m3u8

`catch_cctv_m3u8` 是一个用于抓取央视网（CCTV）视频播放页面中 `.m3u8` 视频资源地址的工具。支持：

* 抓取当前播放页面的视频 `.m3u8` 地址
* 抓取带有剧集播放列表页面中，**右侧所有剧集的 `.m3u8` 地址**
* 抓取结果统一保存在 `list.txt` 文件中，可与 [cctv\_downloader](https://github.com/bbs6280/cctv_downloader) 配合使用，批量下载央视资源。

---

## 🧰 环境要求

* Python 3.7+
* [Playwright](https://playwright.dev/python/) 无头浏览器支持

### 安装依赖

```bash
pip install -r requirements.txt
pip install playwright
playwright install
```

---

## 🚀 快速使用

### 1️⃣ 获取某个播放页面的 m3u8 地址

```bash
python get_m3u8_url.py "https://tv.cctv.com/your_video_page_url"
```

此命令会提取页面中当前剧集的视频地址，输出并写入 `list.txt`。

---

### 2️⃣ 批量获取剧集播放列表中的所有 m3u8 地址

打开 `start.py` 文件，修改其中的调用：

```python
page.go("https://tv.cctv.com/your_video_page_url")
```

将括号内替换为**任意一集**的播放页面链接（该页面需包含右侧剧集播放列表）。

然后执行：

```bash
python start.py
```

程序会抓取所有剧集对应的 `.m3u8` 地址并保存至当前目录下的 `list.txt` 文件。

---

## 📁 项目结构

```
catch_cctv_m3u8/
├── get_m3u8_url.py       # 获取单个页面的 m3u8 地址
├── list.txt              # 抓取结果，包含所有 m3u8 地址
├── start.py              # 抓取剧集列表所有 m3u8 地址
├── requirements.txt      # Python 依赖库
└── README.md             # 使用说明与项目文档
```

---

## 🧩 推荐搭配工具

你可以将本项目输出的 `list.txt` 文件作为输入，搭配另一个工具项目 [`cctv_downloader`](https://github.com/你的用户名/cctv_downloader) 使用，实现一键批量下载所有剧集资源。

---

## ⚠️ 免责声明

本项目仅供学习、研究与技术交流使用。

* 所抓取的内容版权均归属央视网及其内容版权所有方。
* 请勿将本项目用于任何商业用途或违反版权法规的行为。
* 使用本项目下载内容的行为应遵守国家法律法规及网站相关政策，任何因使用本工具产生的法律责任由使用者自行承担。
* 开发者不对任何滥用或非法使用本项目的行为承担任何责任。

---

## 📬 反馈建议

如有功能建议或 bug 反馈，欢迎在 Issues 区提交，也欢迎 PR。

---

🎉 项目致力于简单、快速、安全地辅助抓取公开网页资源地址，感谢支持！

---
