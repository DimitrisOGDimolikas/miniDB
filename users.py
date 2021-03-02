class User():

    def __init__(self, usrname, pwd, priv, del_privs, sel_privs):
        self.username = usrname
        self.password = pwd
        self.privileges = priv
        self.tbls_del = del_privs
        self.tbls_sel = sel_privs


    def can_create(self):
        if self.privileges.get('Create_User') == True:
            return True
        return False

    def can_delete(self):
        if self.privileges.get('Delete_Tbl') == True:
            return True
        return False

    def can_del_tbl(self, table):
        print("Can delete rows from ", table, " as ", self.username)
        if table in self.tbls_del:
            return True
        return False

    def can_sel_tbl(self, table):
        print("Can select ", table, " as ", self.username)
        if table in self.tbls_sel:
            return True
        return False