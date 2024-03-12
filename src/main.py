from utils import get_info
from utils import get_info_filter
from utils import get_sorted_list
from utils import format_operation

executed_count = 5
filter = "EXECUTED"
data = 'operations.json'

sorted_list = get_sorted_list(get_info_filter(get_info(data), filter), executed_count)

for i in sorted_list:
    print(format_operation(i))
