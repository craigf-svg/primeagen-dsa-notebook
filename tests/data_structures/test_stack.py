from data_structures.stack import Stack

# Two analogies for stacks are a pile of plates and a deck of cards
def test_stack_plates():
    pile_of_plates = Stack()
    pile_of_plates.push("Dinner Plate")
    pile_of_plates.push("Dessert Plate")
    errors = []
    try:
        assert pile_of_plates.to_string() == "Dessert Plate -> Dinner Plate -> None"
    except AssertionError:
        errors.append(
            "pile_of_plates.to_string() didn't return Dessert Plate -> Dinner Plate -> None")

    # Time to have some dessert 🍰
    try:
        assert pile_of_plates.pop() == "Dessert Plate"
    except AssertionError:
        errors.append("pile_of_plates.pop() didn't return Dessert Plate")

    try:
        assert pile_of_plates.to_string() == "Dinner Plate -> None"
    except AssertionError:
        errors.append(
            "pile_of_plates.to_string() didn't return Dinner Plate -> None")

    assert not errors, "Errors: " + ",".join(errors)


def test_stack_cards():
    deck_of_cards = Stack()
    deck_of_cards.push("2♥")
    deck_of_cards.push("7♠")
    errors = []
    try:
        assert deck_of_cards.pop() == "7♠"
    except AssertionError:
        errors.append("deck_of_cards.pop() didn't return 7♠")

    try:
        assert deck_of_cards.to_string() == "2♥ -> None"
    except AssertionError:
        errors.append("deck_of_cards.to_string() didn't return 2♥ -> None")

    try:
        assert deck_of_cards.pop() == "2♥"
    except AssertionError:
        errors.append("deck_of_cards.pop() didn't return 2♥")

    try:
        assert deck_of_cards.to_string() == "None"
    except AssertionError:
        errors.append("deck_of_cards.to_string() didn't return None")

    try:
        assert deck_of_cards.pop() is None
    except AssertionError:
        errors.append("deck_of_cards.pop() didn't return None")

    try:
        assert deck_of_cards.to_string() == "None"
    except AssertionError:
        errors.append("deck_of_cards.to_string() didn't return None")

    assert not errors, "Errors: " + ",".join(errors)
