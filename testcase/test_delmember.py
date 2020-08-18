import pytest
import yaml

from page.app import App


class TestContact:
    def setup_class(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    with open('../data/delData.yaml', encoding='UTF-8') as f:
        data = yaml.safe_load(f)
    @pytest.mark.parametrize('name',data)
    def test_delmember(self,name):
        sub =self.main.goto_contactlist().search_contact().search_input(name).click_del_value(name).personal_information().information_settings().edit_members_page().assert_del(name)
        assert sub ==1
