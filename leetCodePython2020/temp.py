import re
import functools


@functools.lru_cache(None)
def foo(n):
    return 1


s = "(N42)24(OB40Li30CHe3O48LiNN26)"

current_search = re.search(r'\((.)*?\)\d*',s)
# current_search = re.search(r'(?<=\()(.)*(?=\))\d*',s)


print(current_search)

print(current_search.span())
print(current_search.group())
print(current_search.group(1))

print(current_search.groups())


current_search = re.search(r'\((.)*\)\d*',s)
ignore_range = current_search.span()
s_parameter = re.search(r'(?<=\()(.)*(?=\))',current_search.group()).group()
ratio_parameter=re.search(r'(?<=(.))\d*$',s).group()

print(ignore_range)
print(s_parameter)
print(type(ratio_parameter))