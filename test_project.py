from project import write_to_leaderboard, get_userscore, fetch_leaderboard


def test_writing(tmpdir):
    file = tmpdir.join("leaderboard.txt")
    write_to_leaderboard(10, "Johnny", file)  # or use str(file)
    assert file.read() == "Johnny: 10\n"
    write_to_leaderboard(12, "Johnita", file)
    assert file.read() == "Johnny: 10\nJohnita: 12\n"


def test_userscore(tmpdir):
    file = tmpdir.join("leaderboard.txt")
    write_to_leaderboard(10, "Johnny", file)
    write_to_leaderboard(12, "Johnita", file)

    assert get_userscore("Johnny", file) == 10
    assert get_userscore("Melanie", file) == None


def test_fetch(tmpdir, capsys):
    file = tmpdir.join("leaderboard.txt")
    write_to_leaderboard(10, "Johnny", file)
    write_to_leaderboard(12, "Johnita", file)
    fetch_leaderboard(file)
    captured = capsys.readouterr()

    assert captured.out == "Johnny: 10\n\nJohnita: 12\n\n"
