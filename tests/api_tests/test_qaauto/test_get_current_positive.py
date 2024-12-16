def test_get_current_positive(qa_auto_ctrl):
    # session = requests.Session()
    # response_sign_in = session.post(url=url_signin, json=body)  # запусуємо cookeis в session
    # print(session.get(url=url_get_current).json())

    # session.cookies.clear()  # чистити кукі
    # response_current = requests.get(url=url_get_current, cookies=get_cookie()).json()

    response_current = qa_auto_ctrl.get_current().json()



    assert response_current['status'] == 'ok'

