#! usr/bin/python
# coding=utf-8

from Web.models import Menu
import json


class MenuService:
    def __init__(self):
        pass

    def get_menus_to_json(self):
        menus = Menu.query.all()
        data = []
        for m in menus:
            param = {}
            if m.pid == 0:
                param["id"] = m.id
                param["name"] = m.name
                sub = self.get_sub_menus(m.id, menus)
                if len(sub) > 0:
                    param["submenu"] = sub
                data.append(param)
        return json.dumps(data, ensure_ascii=False)

    def get_sub_menus(self, pid, menus):

        submenus = []
        for m in menus:
            param = {}
            if m.pid == pid:
                param["id"] = m.id
                param["name"] = m.name
                param["url"] = m.url
                sub = self.get_sub_menus(m.id, menus)
                if len(sub) > 0:
                    param["submenu"] = sub
                submenus.append(param)

        return submenus
