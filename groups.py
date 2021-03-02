class Group():

    def __init__(self, name, privs, del_pr, sel_pr):
        self.name = name
        self.privileges = privs
        self.tbls_del = del_pr
        self.tbls_sel = sel_pr
        self.users = set()

    def add_user(self, user):
        self.users.add(user)
        user.privileges.update(self.privileges)
        for priv in self.tbls_del:
            user.tbls_del.add(priv)
        for priv in self.tbls_sel:
            user.tbls_sel.add(priv)

    def update_privs(self, privs):
        for priv in privs:
            self.privileges.update({priv: True})
            for user in self.users:
                user.privileges.update({priv: True})

    def update_select_privs(self, privs):
        print(privs)
        self.tbls_sel.add(privs)
        for user in self.users:
            user.tbls_sel.add(privs)

    def update_delete_privs(self, privs):
        print(privs)
        self.tbls_del.add(privs)
        for user in self.users:
            user.tbls_del.add(privs)