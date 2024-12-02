

class DataTimeUtils:

    @staticmethod
    def check_diff_between_dt(dt1, dt2, expected_diff) -> None:
        diff = (dt1 - dt2).seconds
        assert f'Expected diff in {diff}, but actual is {expected_diff}'