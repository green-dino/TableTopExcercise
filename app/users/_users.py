from ldap3 import Server, Connection, ALL, MODIFY_ADD

class ActiveDirectoryManager:
    def __init__(self, server_uri, username, password, base_dn):
        self.server_uri = server_uri
        self.username = username
        self.password = password
        self.base_dn = base_dn

    def create_user(self, user_name, description, email):
        server = Server(self.server_uri, get_info=ALL)
        connection = Connection(server, user=self.username, password=self.password, auto_bind=True)

        user_dn = f"CN={user_name},{self.base_dn}"
        user_attributes = {
            'cn': user_name,
            'sAMAccountName': user_name,
            'description': description,
            'mail': email
        }

        connection.add(user_dn, attributes=user_attributes)

    def create_security_group(self, group_name, group_description):
        server = Server(self.server_uri, get_info=ALL)
        connection = Connection(server, user=self.username, password=self.password, auto_bind=True)

        group_dn = f"CN={group_name},{self.base_dn}"
        group_attributes = {
            'cn': group_name,
            'description': group_description
        }

        connection.add(group_dn, attributes=group_attributes)

# Example usage:
if __name__ == "__main__":
    server_uri = 'ldap://your-ldap-server'
    username = 'your-username'
    password = 'your-password'
    base_dn = 'DC=example,DC=com'

    ad_manager = ActiveDirectoryManager(server_uri, username, password, base_dn)

    # Create users and security groups
    users = [
        {"name": "SEC-ARCH", "description": "Security Architect", "email": "secarch@example.com"},
        {"name": "SYS-ARCH", "description": "Systems Architect", "email": "sysarch@example.com"},
        {"name": "SOFT-DEV", "description": "Software Developer", "email": "softdev@example.com"},
        # Add more users here...
    ]

    security_groups = [
        {"name": "SG-SEC-ARCH", "description": "Security Architect"},
        {"name": "SG-SYS-ARCH", "description": "Systems Architect"},
        # Add more security groups here...
    ]

    for user_info in users:
        ad_manager.create_user(user_info["name"], user_info["description"], user_info["email"])

    for group_info in security_groups:
        ad_manager.create_security_group(group_info["name"], group_info["description"])
