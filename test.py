import pandas as pd

mail_info=pd.DataFrame(data=[(1,2,3,4,5)],columns=["邮件主题","发件人","时间","邮件内容","是否有附件"])
print(mail_info)
mail_info2=pd.DataFrame(data=[(1,2,3,4,5)],columns=["邮件主题","发件人","时间","邮件内容","是否有附件"])
mail_info2=mail_info.append({"邮件主题":1,"发件人":2,"时间":3,"邮件内容":4,"是否有附件":5},ignore_index=True)
print(mail_info2)
# writer = pd.ExcelWriter(r'D:\selenium\mail.xlsx', engine='xlsxwriter')
mail_info.to_excel(r'D:\selenium\mail.xlsx', sheet_name='Sheet1', index=False)
# sheet1 = pd.read_excel(r'./mail.xlsx', sheet_name='Sheet1',names=["1","2","3","4sdf"])
# sheet1.head()
print(type(mail_info),"\n",mail_info)