import time
import re
import uiautomator2 as u2
from chromedriver.chromedriver import ChromeDriver

d = u2.connect()

d.app_stop_all()
d.app_start('com.tencent.mm')
d(resourceId="com.tencent.mm:id/qi").click()
d.send_keys("全员裂变通", clear=True)
d(resourceId="com.tencent.mm:id/rd", ).click()
d(resourceId="com.tencent.mm:id/ap4", text="全员裂变").click()

driver = ChromeDriver(d).driver()
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[contains(@href, "activities")]').click()
driver.find_element_by_css_selector('span.tin.wait').click()

el = driver.find_elements_by_css_selector('div.atitem a')[0]
activity_url = el.get_attribute('href')
activity_id = re.search('activities/([0-9]+)\?', activity_url).group(1)
el.click()

time.sleep(4)
d.xpath('//android.support.v7.widget.LinearLayoutCompat').click()
d(resourceId="com.tencent.mm:id/d0", text="发送给朋友").click()
d(resourceId="com.tencent.mm:id/rd", text="幺叁叁").click()
d.screenshot('sign.png')
d(resourceId="com.tencent.mm:id/b29").click()
