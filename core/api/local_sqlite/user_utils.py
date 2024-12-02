from datetime import datetime

def get_user_created_time_dt(user):

    return datetime.strptime(user['updated_date'], '%Y-%m-%dT%H:%M:%S%z')