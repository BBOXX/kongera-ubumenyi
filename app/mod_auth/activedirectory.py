from ldap3 import Server, Connection, ALL, NTLM, SUBTREE, ALL_ATTRIBUTES

class ActiveDirectory():

    def __init__(self, host, port, username, password, base_dn=""):
        self.user = username
        self.base_dn = base_dn
        self.server = Server(host, port=port, get_info=True)
        self.conn = Connection(
            self.server,
            user=username,
            password=password,
            authentication=NTLM
        )

    def bind(self):
        return self.conn.bind()

    def get_schema(self):
        return self.server.schema

    def __get_user(self, search_key, search_value):
        search_filter = "(&(objectclass=user)("+search_key+"="+search_value+"*))"
    
        #Search AD
        self.conn.search(search_base=self.base_dn, 
                search_filter=search_filter, 
                search_scope=SUBTREE, 
                attributes = ALL_ATTRIBUTES, 
                size_limit=0
            )

        return self.conn.entries

    def get_user_by_name(self, name):
        return self.__get_user("cn", name)

    def get_user_by_email(self, email):
        return self.__get_user("mail", email)

    def get_user_by_guid(self, guid):
        return self.__get_user("objectGUID", guid)

