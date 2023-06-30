from adminQueries import AdminQuery
from constant import Constant, InitData, AdminData
from queries import Query
from utils import *
import uuid

def init_users(num=10000):
    admin_query = AdminQuery(Constant.ts_address)
    admin_query.login(Constant.admin_username, Constant.admin_pwd)
    
    f = open(Constant.userfile, 'w')
    
    for i in range(num):
        new_username = uuid.uuid4().hex
        res = admin_query.admin_add_user("1", "5599488099312X", "ts@fd1.edu.cn", "111111", new_username, "1")
        
        f.write("%s\n"%new_username)
        
        print(f"[new user] : userId : {res.get('userId')} , username : {res.get('userName')} , pwd : {res.get('password')}")
        
    f.close()
    
if __name__ == '__main__':
    init_users()
    