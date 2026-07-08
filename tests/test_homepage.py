from pages.home_page import Homepage

def test_item_count(authed_driver, authed_driver_wait):
    homepage = Homepage(authed_driver, authed_driver_wait)
    assert homepage.get_count_of_items() == 6