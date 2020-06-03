
import intake
from collections import Counter 
print(__name__)

  
# list of elements to calculate mode 
n_num = intake.nums
n = len(n_num) 
data = Counter(n_num) 
get_mode = dict(data) 
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]  
if len(mode) == n: 
    get_mode = "No mode found"
else: 
    get_mode = "Mode is / are: " + ', '.join(map(str, mode))      
print(get_mode) 