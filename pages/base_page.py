from uiautomator2 import Device


class BasePage:

    _blacklist = [
        {"resourceId": "com.xueqiu.android:id/snb_tip_wrapper"},
        {"resourceId": "com.xueqiu.android:id/image_cancel"}
    ]

    def __init__(self, d: Device):
        self.d = d

    def find(self, pattern):
        if isinstance(pattern, str):
            return self.d.xpath(pattern)
        elif isinstance(pattern, dict):
            return self.d(**pattern)
        else:
            raise Exception('定位参数不正确：{}'.format(pattern))

    def find_by_exists(self, pattern, timeout=3):
        if isinstance(pattern, str):
            return self.d.xpath(pattern).exists(timeout=timeout)
        elif isinstance(pattern, dict):
            return self.d(**pattern).exists(timeout=timeout)
        else:
            raise Exception('定位参数不正确：{}'.format(pattern))

    def _find_blacklist(self):
        for i in self._blacklist:
            self.find(i)
