from pages.base_page import BasePage


class OptionalPage(BasePage):
    _content_recycler = {'resourceIdMatches': '.+content_recycler'}
    _search = {"resourceId": "com.xueqiu.android:id/action_search"}
    _stock_list = {'resourceId': 'com.xueqiu.android:id/row_layout'}
    _stock_code = {"resourceIdMatches": ".+portfolio_stockCode"}
    _stock_name = {"resourceIdMatches": ".+portfolio_stockName"}
    _current_price = {"resourceIdMatches": ".+item_layout"}

    def go_to_search(self):
        self.find(self._search).click()

    def get_stock_list_info(self):
        self.find_by_exists(self._stock_code, 3)
        stock_list = []
        info_list = self.find(self._content_recycler).child(**self._stock_list)
        index = 1
        for info in info_list:
            stock_dict = {}
            stock_dict['index'] = index
            stock_dict['name'] = info.child(**self._stock_name).get_text()
            stock_dict['code'] = info.child(**self._stock_code).get_text()
            stock_dict['currentPrice'] = info.child(**self._current_price).get_text()
            index = index + 1
            stock_list.append(stock_dict)
        return stock_list
