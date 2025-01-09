from core.api.gorest.dto_user import UserSchema
from core.api.gorest.gorest_ctrl import GorestCtrl
import time  # time.time() - повертає поточний час в секундах


def test_create_user():
    user_data = {"name": "Tenali Ramakrishna",
                 "gender": "male",
                 "email": f"tenali.ramakrishna@{time.time()}.com",
                 "status": "active"}

    # res = GorestCtrl().create_user(data=user_data)
    res = [{"name": "Tenali Ramakrishna",
                 "gender": "asd",
                 "email": f"tenali.ramakrishna@{time.time()}.com",
                 "status": 2,
           "id": 5877}, {"name": "Tenali Ramakrishna",
                 "gender": "asd",
                 "email": f"tenali.ramakrishna@{time.time()}.com",
                 "status": 2,
           "id": 5877}]

    validated_data = UserSchema().load(res, many=True)

    pass


def test_create_user_auth_problem():
    user_data = {"name": "Tenali Ramakrishna",
                 "gender": "male",
                 "email": f"tenali.ramakrishna@{time.time()}.com",
                 "status": "active"}

    GorestCtrl().create_user(data=user_data, token='asd', status_code=401)
