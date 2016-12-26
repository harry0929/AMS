#!/usr/bin/python
# -*- coding:utf-8 -*-

from Web import db
import hashlib
from datetime import datetime
from Web.models import *
from decimal import *
import xlrd


if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    # 系统菜单
    # m = Menu(name='用户管理',link='#',url='',pid=1,published=True,order=0)
    menus = [
        Menu(name='系统管理', link='fa fa-th-larg', url='#', pid=0, published=True, order=0),
        Menu(name='用户管理', link='', url='/user', pid=1, published=True, order=0),
        Menu(name='角色管理', link='', url='#', pid=1, published=True, order=0),
        Menu(name='菜单管理', link='', url='#', pid=1, published=True, order=0),
        Menu(name='权限管理', link='', url='#', pid=1, published=True, order=0),
        Menu(name='会员管理', link='fa', url='#', pid=0, published=True, order=0),
        Menu(name='人力资源', link='', url='#', pid=1, published=True, order=0)
    ]
    for m in menus:
        db.session.add(m)


    # 系统用户
    u = User(name='admin', email='@', nickname='管理员', password=hashlib.new("md5", "admin".encode("utf-8")).hexdigest(),
             reg_time=datetime.now(), status=0, deleted=False)
    db.session.add(u)

    #
    Categorys = [
        AssetCategory(name='医疗设备',code='01'),
        AssetCategory(name='医疗家具',code='02'),
        AssetCategory(name='办公家具',code='03'),
        AssetCategory(name='电子及办公设备',code='04'),
        AssetCategory(name='办公车辆',code='05')
    ]
    for c in Categorys:
        db.session.add(c)

    db.session.commit()


    types = [
        ManagerType(name='在帐资产'),
        ManagerType(name='在帐资产（行政）'),
        ManagerType(name='报废资产'),
        ManagerType(name='暂存资产'),
        ManagerType(name='实物资产'),
        ManagerType(name='临时资产'),
        ManagerType(name='实物报废')

    ]
    for t in types:
        db.session.add(t)
    db.session.commit()

    excel = xlrd.open_workbook(u"资产清单.xls")

    sheetDepartment = excel.sheet_by_name(u"部门")
    sheetSupplier = excel.sheet_by_name(u"供货商")
    sheetDetail = excel.sheet_by_name(u"固定资产清单")

    for iRow in range(sheetDepartment.nrows):
        d = Department(name=sheetDepartment.cell(iRow,0).value)
        db.session.add(d)
    db.session.commit()

    for iRow in range(sheetSupplier.nrows):
        c = Supplier(name=sheetSupplier.cell(iRow,0).value)
        db.session.add(c)

    for iRow in range(4, sheetDetail.nrows):

        if sheetDetail.cell(iRow, 1).ctype == 0:
            print(sheetDetail.cell(iRow, 0).value)
            break
        supplier = Supplier.query.filter(Supplier.name == sheetDetail.cell(iRow, 2).value).first()
        print(sheetDetail.cell(iRow, 1).ctype)
        # print None if supplier is None else supplier.id
        print(iRow)
        asset = Asset(code=sheetDetail.cell(iRow, 1).value,
                      name=sheetDetail.cell(iRow, 5).value,
                      supplier_id=None if supplier is None else supplier.id,
                      manager_type_id=ManagerType.query.filter(
                          ManagerType.name == sheetDetail.cell(iRow, 3).value).first().id,
                      asset_category_id=AssetCategory.query.filter(
                          AssetCategory.name == sheetDetail.cell(iRow, 4).value).first().id,
                      purchase_date=xlrd.xldate.xldate_as_datetime(sheetDetail.cell(iRow, 7).value, 0).date(),
                      original_value=Decimal(sheetDetail.cell(iRow, 8).value),
                      depreciation_year=int(sheetDetail.cell(iRow, 9).value),
                      department_id=Department.query.filter(
                          Department.name == sheetDetail.cell(iRow, 10).value).first().id,
                      position=sheetDetail.cell(iRow, 11).value,
                      remark=sheetDetail.cell(iRow, 12).value
                      )

        db.session.add(asset)
        # print Supplier.query.filter(Supplier.name == sheetDetail.cell(iRow, 2).value).first().id
        # print xlrd.xldate.xldate_as_datetime(sheetDetail.cell(iRow, 7).value, 0).date()

    db.session.commit()
