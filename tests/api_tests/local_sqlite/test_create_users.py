from core.api.local_sqlite.sqlite_ctrl import SqLiteCtrl
from datetime import datetime, UTC
import time

from core.api.local_sqlite.user_utils import get_user_created_time_dt
from utils.data_time_utils import DataTimeUtils


def test_get_students():
    stat_time = time.time()  # коли почався тест

    current_time_dt = datetime.now(UTC)

    response = SqLiteCtrl().crate_student({'name': 'Alex x', 'score': 78})

    end_time = time.time()  # коли юзер вже ствоерний

    updated_date_of_user_dt = get_user_created_time_dt(response.json())
    DataTimeUtils.check_diff_between_dt(updated_date_of_user_dt, current_time_dt, end_time - stat_time)