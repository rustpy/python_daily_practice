import pandas as pd
import win32com.client as win32
import time


def search_by_name(worker_name):
    data = pd.read_excel('team-roster.xlsx')
    data_li = data.values.tolist()
    result = []
    name_li = []
    for first_list in data_li:
        if worker_name in first_list:
            name_li.append(first_list)
        else:
            result.append(first_list[0])
    if len(result) == len(data_li):
        print('查无此人')
    else:
        return name_li


# 使用.()split('(')[0]).rstrip函数可以节约时间(列表切片)
def get_email_address(name):
    email_list = []
    name_li = search_by_name(name)
    basic_info = name_li[0]
    worker_email = basic_info[3]
    leader_info = basic_info[2].split()
    leader_name = leader_info[0] + ' ' + leader_info[1]
    name_li = search_by_name(leader_name)
    basic_info = name_li[0]
    leader_email = basic_info[3]
    email_list.append(worker_email)
    email_list.append(leader_email)
    return email_list


def send_email(address):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = address
    mail.Subject = 'This is a test email'
    mail.Body = 'Time and Date: ' + time.strftime('%Y-%m-%d %H:%M  %A', time.localtime(time.time()))
    # mail.HTMLBody = '<h2>HTML Message body</h2>' #this field is optional
    # To attach a file to the email (optional):
    # attachment  = "Path to the attachment"
    # mail.Attachments.Add(attachment)
    mail.Send()


if __name__ == '__main__':
    name = input('请输入姓名(例如Tom, Rust): ')
    email_address = get_email_address(name)
    send_email(email_address)
