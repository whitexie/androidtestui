from pages.base_page import BasePage


class MainPages(BasePage):
    # 微信会话列表页面
    _search_button = {'resourceId': 'com.tencent.mm:id/qi'}


    # 搜索页面
    _search_input = {'resourceId': 'com.tencent.mm:id/li'}
    _search_result = {'resourceId': 'com.tencent.mm:id/rd', 'text': '全员裂变通'}

    # 公众号会话页面
    # 全员裂变菜单
    _qylb_button = {'resourceId': 'com.tencent.mm:id/ap4', 'text': '全员裂变通'}

    def go_to_qylbt(self):
        self.find(**self._search_button).click()
        self.find(**self._search_input).send_keys('全员裂变通', clear=True)
        self.find(**self._search_result).click()

        self.find()

