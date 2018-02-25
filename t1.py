
start_symbols_for_level = {0: "", 1: "", 2: '|'}
shift_sumbol = '+-- '
filling_symbol = {0: '', 1: '', 2: ' '}
backspace = '\n'
list_separator = ' '
service_symbols =  '() '

    
def ascii_tree_sax(symbol):
    
    def make_line_preffix(level):
        line_to_print = ''
        if ascii_tree_sax.prev_symbol is not None:
            line_to_print += backspace
        line_to_print += start_symbols_for_level[level if level < 2 else 2]
        line_to_print += filling_symbol[level if level < 2 else 2] * (len(shift_sumbol) * (level - 1) - len(start_symbols_for_level[level if level < 2 else 2])) 
        line_to_print += shift_sumbol if  level > 0  else ""
        return line_to_print
    
    line_to_print =  ''
    try:
        getattr(ascii_tree_sax, 'current_level')
    except AttributeError:
        ascii_tree_sax.list_print_mode = False
        ascii_tree_sax.prev_symbol = None
        ascii_tree_sax.is_list_print_mode_possible = False
        ascii_tree_sax.current_level = -1
    
    if  symbol == '(':
        ascii_tree_sax.current_level += 1
        line_to_print += make_line_preffix(ascii_tree_sax.current_level)
        ascii_tree_sax.is_list_print_mode_possible = False
    elif symbol == ')':
        if  ascii_tree_sax.list_print_mode:
            ascii_tree_sax.current_level -= 2
        else:
            ascii_tree_sax.current_level -= 1
        ascii_tree_sax.list_print_mode = False
        ascii_tree_sax.is_list_print_mode_possible = False
    elif symbol == list_separator:
        pass
    elif symbol.isprintable():
        if ascii_tree_sax.prev_symbol == list_separator:
            if not ascii_tree_sax.list_print_mode and ascii_tree_sax.is_list_print_mode_possible:
                ascii_tree_sax.current_level += 1
                ascii_tree_sax.list_print_mode = True
            line_to_print += make_line_preffix(ascii_tree_sax.current_level)
        line_to_print += symbol
        ascii_tree_sax.is_list_print_mode_possible = True
    else:
        pass
    ascii_tree_sax.prev_symbol = symbol

    return line_to_print

line = "(asciitree (sometimes you) (just (want to draw)) trees (in (your     terminal)))"
result =  "".join([ascii_tree_sax(symbol) for symbol in line])
print(result)

"""
https://github.com/mbr/asciitree
the word 'trees' is in the parensis
"""
line = "(asciitree (sometimes you) (just (want to draw)) (trees) (in (your   terminal )))"
result =  "".join([ascii_tree_sax(symbol) for symbol in line])
print(result)
