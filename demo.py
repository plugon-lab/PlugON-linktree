from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1200)
    page = browser.new_page(viewport={"width": 480, "height": 850})

    print("페이지 열기...")
    page.goto("http://localhost:8765/index.html")
    time.sleep(2)

    print("인스타그램 버튼 hover...")
    page.hover("a[href*='instagram']")
    time.sleep(2)

    print("스레드 버튼 hover...")
    page.hover("a[href*='threads']")
    time.sleep(2)

    print("인스타그램 버튼 클릭 (새 탭)...")
    with page.context.expect_page() as new_page_info:
        page.click("a[href*='instagram']")
    new_page = new_page_info.value
    new_page.wait_for_load_state("domcontentloaded")
    print(f"이동된 URL: {new_page.url}")
    time.sleep(3)

    print("완료. 5초 후 닫힙니다.")
    time.sleep(5)
    browser.close()
