from pages.base_page import BasePage


class UserProfilePage(BasePage):
    _phone = {"resourceId": "com.xueqiu.android:id/iv_login_phone"}
    _wechat = {"resourceId": "com.xueqiu.android:id/iv_login_phone"}
    _weibo = {"resourceId": "com.xueqiu.android:id/iv_login_phone"}
    _qq = {"resourceId": "com.xueqiu.android:id/iv_login_phone"}

    def go_to_phone_login(self):
        self.find(self._phone).click()

    def wechat_login(self):
        self.find(self._wechat).click()

    def weibo_login(self):
        self.find(self._weibo).click()
