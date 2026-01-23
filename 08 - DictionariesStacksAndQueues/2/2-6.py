# W systemie operacyjnym każdy użytkownik posiada pewne uprawnienia. Użytkownik chce wykonać pewną akcję, która wymaga określonych uprawnień. Napisz program, który sprawdza, czy użytkownik posiada wymagane uprawnienia.

required_permissions = {"read", "write", "execute"}
user_permissions = {"read", "write"}

has_permissions = set(required_permissions).issubset(set(user_permissions))  # subset
print(has_permissions)  # Will return False because "execute" is missing.