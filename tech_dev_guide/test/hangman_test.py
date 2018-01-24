import pytest

from tech_dev_guide.hangman import Game

secret = "secret"
bad_letter = 'x'
letter = 's'


@pytest.fixture
def game():
    return Game(secret)


def test_incorrect_guess(game):
    assert bad_letter not in secret
    assert not game.guess(bad_letter)


def test_correct_guess(game):
    assert letter in secret
    assert game.guess(letter)


def test_incorrect_guess_results_in_a_lost_live(game):
    lives_before_guess = game.lives

    game.guess(bad_letter)

    assert game.lives == lives_before_guess - 1


def test_double_incorrect_guess_with_same_letter_results_in_two_lost_lives(game):
    lives_before_guess = game.lives

    game.guess(bad_letter)
    game.guess(bad_letter)

    assert game.lives == lives_before_guess - 2


def test_double_correct_guess_makes_no_difference_in_lives(game):
    lives_before_guess = game.lives

    game.guess(letter)
    game.guess(letter)

    assert game.lives == lives_before_guess


def test_incorrect_guesses_lead_to_lost_game(game):
    for _ in range(Game.lives):
        assert not game.finished()
        game.guess(bad_letter)

    assert game.finished()
    assert not game.won()


def test_winning_game(game):
    for c in secret:
        assert game.guess(c)

    assert game.finished()
    assert game.won()
