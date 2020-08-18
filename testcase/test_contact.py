import pytest
import yaml

from page.app import App


class TestContact:
    def setup_class(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    with open('../data/data.yaml', encoding='UTF-8') as f:
        data = yaml.safe_load(f)
    @pytest.mark.parametrize('name,sex,phone',data)
    def test_contact(self,name,sex,phone):
        reslut=self.main.goto_contactlist().addcontact().add_menual().set_name(name).set_gender(sex).set_phonnum(
            phone).click_save().get_toast()
        assert '添加成功' in reslut

