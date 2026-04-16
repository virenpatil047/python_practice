def format_name(f_name, l_name):
    """Take first and last name & format it 
    to return the title case version of the name """
    return f_name.title(), l_name.title()
    # f_name = f_name[0].upper() + f_name[1:]
    # l_name = l_name[0].upper() + l_name[1:]
    # return f_name, l_name

f_name, l_name = format_name("viren", "patil")
print(f_name + " " + l_name)