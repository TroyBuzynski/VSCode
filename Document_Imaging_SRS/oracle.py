import cx_Oracle

dsn_tns = cx_Oracle.makedsn('devdb1.imaging.uni.edu', '1521', service_name='IMGDEV') # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
conn = cx_Oracle.connect(user=r'HSI', password='wstinol', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'

c = conn.cursor()
c.execute('''SELECT USERNAME,
                        REALNAME,
                        LASTLOGON,
                        EMAILADDRESS,
                        DISABLELOGIN
                FROM HSI.USERACCOUNT
                WHERE DISABLELOGIN = 0
            ORDER BY USERNAME''') # use triple quotes if you want to spread your query across multiple lines
for row in c:
    print (row[2]) # this only shows the first two columns. To add an additional column you'll need to add , '-', row[2], etc.
conn.close()