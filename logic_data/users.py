class TestUser:

    name = 'Den'
    id_ = 55
    ud_data = DB.get_user_by_id(id=id_)

    def create_new_product_in_id(self, data):
        DB.insert_new_product(data)
        return self


# marshmallow @post_action