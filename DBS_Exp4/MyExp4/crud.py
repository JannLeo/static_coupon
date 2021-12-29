# CRUD， add, delete, change, search
from MyExp4 import models
from MyExp4.database import db_session

'''
new_coupon = models.CouponsForm()
new_customer = models.CustomerForm()
new_sign = models.Sign()
'''


# sign_up表
def SignInsert(customer, signup, deal):
    session = db_session()
    # 创建新Sign对象:
    new_sign = models.Sign(customer_number=customer, sign_up_number=signup, deal_number=deal)
    # 添加到session:
    session.add(new_sign)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()


def SignSearch(signup):
    # 查询操作
    # 创建Session
    session = db_session()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    user = session.query(models.Sign).filter(models.Sign.sign_up_number == signup).one()
    if user:
        print('SignUpNumber:', user.sign_up_number)
        print('CustomerNumber:', user.customer_number)
        print('DealNumber:', user.deal_number)
    else:
        print("未找到指定结果！")
    session.close()  # 关闭Session


def SignDelete(signup):
    # 删除操作
    session = db_session()  # 创建会话
    delete_users = session.query(models.Sign).filter(models.Sign.sign_up__number == signup).first()
    if delete_users:
        session.delete(delete_users)
        session.commit()
    session.close()  # 关闭会话


def CouponsInsert(deal_number, description, location, deal_price, original_price, available_date, ending_date):
    session = db_session()
    # 创建新Sign对象:
    new_coupon = models.CouponsForm(deal_number=deal_number, description=description,
                                    location=location, deal_price=deal_price,
                                    original_price=original_price,
                                    available_date=available_date,
                                    ending_date=ending_date)
    # 添加到session:
    session.add(new_coupon)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()


def CouponsSearch(deal_number):
    # 查询操作
    # 创建Session
    session = db_session()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    user = session.query(models.CouponsForm).filter(models.CouponsForm.deal_number == deal_number).one()
    if user:
        # deal_number, description, location, deal_price, original_price, available_date, ending_dates
        print('DealNumber:', user.deal_number)
        print('Description:', user.description)
        print('Location:', user.location)
        print('Deal price:', user.deal_price)
        print('Original Price:', user.original_price)
        print('Available Date:', user.available_date)
        print('Ending Dates:', user.ending_dates)

    else:
        print("未找到指定结果！")
    session.close()  # 关闭Session


def CouponsChange(deal_number, description, location, deal_price, original_price, available_date, ending_date):
    # 更新操作
    session = db_session()  # 创建会话
    users = session.query(models.CouponsForm).filter_by(deal_number=deal_number).first()  # 查询条件
    users.description = description  # 更新操作
    users.location = location  # 更新操作
    users.deal_price = deal_price  # 更新操作
    users.original_price = original_price  # 更新操作
    users.available_date = available_date  # 更新操作
    users.ending_date = ending_date  # 更新操作
    session.add(users)  # 添加到会话
    session.commit()  # 提交即保存到数据库
    session.close()  # 关闭会话


def CouponsDelete(deal_number):
    session = db_session()  # 创建会话
    delete_users = session.query(models.CouponsForm).filter(models.CouponsForm.deal_number == deal_number).first()
    if delete_users:
        session.delete(delete_users)
        session.commit()
    session.close()  # 关闭会话


def CustomerInsert(customer_number, name, email):
    session = db_session()
    # 创建新Sign对象:
    new_customer = models.CustomerForm(name=name, customer_number=customer_number, email=email)
    # 添加到session:
    session.add(new_customer)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()


def CustomerSearch(customer_number):
    # 查询操作
    # 创建Session
    session = db_session()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    user = session.query(models.CustomerForm).filter(models.CustomerForm.customer_number == customer_number).one()
    if user:
        # customer_number, name, email
        print('Customer Number:', user.customer_number)
        print('Name:', user.name)
        print('Email:', user.email)
    else:
        print("未找到指定结果！")
    session.close()  # 关闭Session


def CustomerChange(customer_number, name, email):
    # 更新操作
    session = db_session()  # 创建会话
    users = session.query(models.CustomerForm).filter_by(customer_number=customer_number).first()  # 查询条件
    users.name = name  # 更新操作
    users.email = email  # 更新操作
    session.add(users)  # 添加到会话
    session.commit()  # 提交即保存到数据库
    session.close()  # 关闭会话


def CustomerDelete(customer_number):
    session = db_session()  # 创建会话
    delete_users = session.query(models.CustomerForm).filter(models.CouponsForm.customer == customer_number).first()
    if delete_users:
        session.delete(delete_users)
        session.commit()
    session.close()  # 关闭会话
