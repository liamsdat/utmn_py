import json 
import sys
import time 

with open('visit_log.csv', 'r') as visits, \
    open('funnel.csv', 'w') as out:
    out.write('user_id,source,category\n')

    headers = visits.readline().strip().split(',')
    user_id_index = headers.index('user_id')
    source_index = headers.index('source')

    for visit in visits:
        visit_values = visit.strip().split(',') 
        visit_user_id = visit_values[user_id_index]
        visit_source = visit_values[source_index]

        with open('purchase_log.txt', 'r') as purchases:
            for purchase in purchases:
                record = json.loads(purchase)

                if record.get('user_id') == visit_user_id:
                    category = record.get('category')
                    out.write(f'{visit_user_id},{visit_source},{category}\n')
                    break