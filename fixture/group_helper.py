import time
import pywinauto


class GroupHelper:

    def __init__(self, app):
        self.pywinauto = pywinauto
        self.app = app

    def get_group_list(self):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        group_list = [node.text() for node in root.children()]
        self.close_group_editor()
        return group_list

    def add_new_group(self, group):
        self.open_group_editor()
        self.group_editor.window(auto_id="uxNewAddressButton").click()
        input = self.group_editor.window(class_name="Edit")
        input.set_text(group)
        input.type_keys("\n")
        self.close_group_editor()

    def open_group_editor(self):
        self.app.main_window.window(auto_id="groupButton").click()
        self.group_editor = self.app.application.window(title="Group editor")
        self.group_editor.wait("visible")

    def close_group_editor(self):
        self.group_editor.close()

    def delete_group(self):
        self.open_group_editor()

        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        item = root.children()[1]
        item.click()
        self.group_editor.window(auto_id="uxDeleteAddressButton").click()
        self.delete_group = self.app.application.window(title="Delete group")
        self.delete_group.window(auto_id="uxDeleteAllRadioButton").click()
        self.delete_group.window(auto_id="uxOKAddressButton").click()

        # for item in root.children():
        #     if item.text() != "Contact groups":
        #         item.click()
        #         time.sleep(1)
        #         self.group_editor.window(auto_id="uxDeleteAddressButton").click()
        #         self.delete_group = self.app.application.window(title="Delete group")
        #         self.delete_group.window(auto_id="uxDeleteAllRadioButton").click()
        #         self.delete_group.window(auto_id="uxOKAddressButton").click()
        #     else:
        #         pass


