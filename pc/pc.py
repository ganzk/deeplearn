from playwright.sync_api import sync_playwright  # 正确写法
import time
import AnalysisHtml
import  agent

# 安装浏览器驱动
# 注意：首次使用前需安装 Chromium 浏览器驱动
# playwright install chromium

# 定义核心参数（替换成你自己的）
LOGIN_URL = "https://www.red-ring.cn/"  # 比如：https://xxx.com/login
TARGET_URL = "https://www.red-ring.cn/group/27593"  # 比如：https://xxx.com/post/12345
USERNAME = "18754264575"
PASSWORD = "141425gan"

def login_and_crawl():
    # 启动 Playwright 并打开浏览器
    with sync_playwright() as p:
        # 1. 启动浏览器（headless=False 显示浏览器窗口，方便调试；True 则后台运行）
        browser = p.chromium.launch(headless=False, slow_mo=500)  # slow_mo 放慢操作速度，避免被反爬
        # 2. 新建浏览器标签页
        page = browser.new_page()

        print("启动浏览器，准备加载")

        try:
            # 3. 访问登录页面
            page.goto(LOGIN_URL)
            # 等待页面加载完成（可选，根据网站调整）
            page.wait_for_load_state("networkidle")

            print("启动浏览器，准备加载")
            page.click('button[type="button"]')
            # login_tab_locator = page.locator('//div[text()="帐号密码登录"]')
            # page.click('button[type="button"]')

            # 3. 等待登录弹窗出现，然后点击「帐号密码登录」
            print("🔍 正在点击弹窗中的「帐号密码登录」...")
            # 等待弹窗加载 + 定位「帐号密码登录」选项
            account_login_tab = page.locator('text=帐号密码登录')
            account_login_tab.wait_for(state="visible", timeout=10000)
            account_login_tab.click()

            # 4. 定位并输入账号（关键：用开发者工具找账号输入框的选择器）
            # 常见选择器：input[name="username"]、input[id="phone"]、//input[@placeholder="请输入账号"]
            print("🔍 正在输入手机号")
            page.fill('input[name="mobile"]', USERNAME)  # 替换成目标网站的账号输入框选择器
            # 5. 定位并输入密码
            print("🔍 正在输入密码")
            # page.fill('input[name="password"]', PASSWORD)  # 替换成密码输入框选择器
            print("🔍 输入密码...")
            password_input = page.locator('input[placeholder="请输入密码"]')
            password_input.wait_for(state="visible", timeout=5000)
            password_input.fill(PASSWORD)

            print("🔍 输入密码完成")

            # 6. 点击登录按钮（替换成登录按钮的选择器）
            # 常见选择器：button[type="submit"]、//button[text()="登录"]、.login-btn
            page.click('button[type="submit"]')

            print("🔍 点击登录按钮...")
            account_login_tab = page.locator('text=进入圈子').nth(0)
            account_login_tab.wait_for(state="visible", timeout=10000)
            account_login_tab.click()

            # 7. 等待登录完成（可根据场景调整：比如等待跳转、等待特定元素出现）
            # 方式1：等待页面跳转（登录后一般会跳首页/个人中心）
            page.wait_for_url("https://www.red-ring.cn/group/27593")  # 替换成登录后的跳转URL
            # 方式2：等待登录后的标志性元素（比如个人头像）
            # page.wait_for_selector('.avatar', timeout=10000)

            print("✅ 登录成功！开始爬取目标页面...")

            # 8. 访问需要登录的目标页面
            page.goto(TARGET_URL)
            page.wait_for_load_state("networkidle")

            #  2026年3月3日
            # account_login_tab = page.locator('text= 2026年3月10日财经早餐 ').nth(0)
            # account_login_tab = page.locator('.panel.my-10.por').nth(1)
            account_login_tab = page.locator('.fz-lg.mb-7.c-0.fwm.text-darker.cup').nth(0)
            # account_login_tab = page.locator('fz-lg mb-7 c-0 fwm text-darker cup').nth(0)
            account_login_tab.wait_for(state="visible", timeout=10000)
            account_login_tab.click()

            # 等待5秒钟，等待页面加载完成
            time.sleep(5)

            # 9. 提取页面内容（根据你的需求调整）
            # 提取整个页面HTML
            page_html = page.content()
            # 提取特定元素的文本（比如你之前要的文章内容）
            # article_content = page.inner_text('.post-body')  # 替换成目标内容的选择器

            text = AnalysisHtml.extract_main_content(html = page_html)

            content = agent.King_agent(text)

            # 10. 保存/输出内容
            with open("King解读内容.md", "w", encoding="utf-8") as f:
                f.write(content)
            print("📝 内容已保存！")
            # print("📝 内容已保存！核心内容预览：")
            # print(text[:500] + "...")  # 打印前500字预览

        except Exception as e:
            print(f"❌ 操作出错：{e}")
            # 出错时截图，方便调试
            page.screenshot(path="error_screenshot.png")
        finally:
            # 11. 关闭浏览器（可选：也可以留着，方便手动检查）
            time.sleep(5)  # 停留5秒，方便查看结果
            browser.close()


if __name__ == "__main__":
    login_and_crawl()