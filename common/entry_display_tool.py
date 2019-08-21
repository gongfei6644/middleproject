
def entry_display_tool(num, entry_name, entry_value, default_value, flag=0):
    if num % 2 == 0:
        if flag:
            entry_name['show'] = '*'
        if entry_value.get() == default_value:
            entry_name.delete(0, 'end')
    else:
        if entry_value.get() == '':
            if flag:
                entry_name['show'] = ''
            entry_name.insert(10, default_value)
    return True