from page.app import App


class TestContact:
    def setup_class(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def test_contact(self):
        name = 'abc'
        sex = '男'
        phone = '13069856458'
        self.main.goto_contactlist().addcontact().add_menual().set_name(name).set_gender(sex).set_phonnum(
            phone).click_save()
