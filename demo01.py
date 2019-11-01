url = 'href="/wap/activities/2461132139?activity_log_id=878965&customer_id=71&from=index&user_id=24492"'

import re

print(re.search('activities/([0-9]+)\?', url).group(1))