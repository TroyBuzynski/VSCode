import cx_Oracle

def diff(lst1,lst2):
    s = set(lst2)
    lst3 = [value for value in lst1 if value not in s]
    return lst3

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


dsn_tns_IMGDEV = cx_Oracle.makedsn('devdb1.imaging.uni.edu', '1521', service_name='IMGDEV') 
conn_IMGDEV = cx_Oracle.connect(user=r'HSI', password='wstinol', dsn=dsn_tns_IMGDEV) 

dsn_tns_PRD = cx_Oracle.makedsn('prddb1.ebiz.uni.edu', '1521', service_name='PRD') 
conn_PRD = cx_Oracle.connect(user=r'READONLY', password='panth3rs', dsn=dsn_tns_PRD) 

IMGDEV_dataset = conn_IMGDEV.cursor()
IMGDEV_dataset.execute('''  SELECT  TRIM(USERNAME)
                                    --TRIM(REALNAME),
                                    --LASTLOGON,
                                    --TRIM(EMAILADDRESS),
                                    --DISABLELOGIN
                                FROM HSI.USERACCOUNT
                                WHERE DISABLELOGIN = 0
                            ORDER BY USERNAME'''    ) 

curr_OnBase_users = []
for row in IMGDEV_dataset:
    curr_OnBase_users.append(row[0].lower())
conn_IMGDEV.close()





PRD_dataset = conn_PRD.cursor()
PRD_dataset.execute(''' SELECT DISTINCT sumv.user_name --The set of users that have had or do have a Document Imaging role in SRS
                            FROM APPS.SRS_USER_ROLE ur
                                JOIN APPS.SRS_ROLE r ON ur.role_id = r.role_id
                                JOIN APPS.SRS_SYSTEM s ON s.system_id = r.system_id
                                JOIN APPS.SSO_USER_MV sumv ON sumv.sso_id = ur.owned_by_sso_id
                            WHERE     s.NAME = 'Document Imaging'
                                AND USER_NAME NOT IN --The set of users that have an active Document Imaging role in SRS
                                    (SELECT DISTINCT sumv.user_name
                                        FROM APPS.SRS_USER_ROLE ur
                                            JOIN APPS.SRS_ROLE r ON ur.role_id = r.role_id
                                            JOIN APPS.SRS_SYSTEM s ON s.system_id = r.system_id
                                            JOIN APPS.SSO_USER_MV sumv
                                                ON sumv.sso_id = ur.owned_by_sso_id
                                        WHERE     s.NAME = 'Document Imaging'
                                            AND ur.EFFECTIVE_END_DATE IS NULL)
                                --AND r.ROLE_NAME NOT IN ('UNI OnBase Student', 'UNI OnBase Employee')
ORDER BY user_name ''')

no_active_SRS_roles = []
for row in PRD_dataset:
   no_active_SRS_roles.append(row[0])
print(len(no_active_SRS_roles))
   
PRD_dataset.execute('''   SELECT DISTINCT sumv.USER_NAME
    FROM APPS.SRS_USER_ROLE ur
         JOIN APPS.SRS_ROLE r ON ur.role_id = r.role_id
         JOIN APPS.SRS_SYSTEM s ON s.system_id = r.system_id
         JOIN APPS.SSO_USER_MV sumv ON sumv.sso_id = ur.owned_by_sso_id
   WHERE     s.NAME = 'Document Imaging'
         AND ur.EFFECTIVE_END_DATE IS NULL
         AND r.ROLE_NAME NOT IN ('UNI OnBase Student', 'UNI OnBase Employee')
         --AND sumv.EMAIL_ADDRESS != 'troy.buzynski@uni.edu'
ORDER BY sumv.USER_NAME ''')
   
active_SRS_roles = []
for row in PRD_dataset:
   active_SRS_roles.append(row[0])  
   
conn_PRD.close()


# li = [value for value in curr_OnBase_users if value.lower() in no_active_SRS_roles[0]]
# li=[]
# for user in curr_OnBase_users:
#     if user.lower() in active_SRS_roles:
#         li.append(user)


# print(len(li))
# for user in li:
#     print(user)

li = intersection(curr_OnBase_users,no_active_SRS_roles)
print(len(li))
for user in li:
    print(user)