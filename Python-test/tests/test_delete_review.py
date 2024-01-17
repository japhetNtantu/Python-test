from restaurant_reviews import RestaurantReviews

def test_delete_existing_review():
    rr = RestaurantReviews()
    rr.add_review("Italian Delight", "Amazing pasta dishes.", 4)
    delete_result = rr.delete_review("Italian Delight")
    get_result = rr.get_review("Italian Delight")
    assert delete_result == "Review deleted for Italian Delight."
    assert get_result == "Review not found."

def test_delete_non_existent_review():
    rr = RestaurantReviews()
    result = rr.delete_review("Mexican Fiesta")
    assert result == "Review not found."
