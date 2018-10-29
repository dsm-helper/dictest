import sys
sys.path.insert(0, sys.path[0]+'/../dictest')

def test_get_words_by_info():
    import main
    import json

    words = main.get_words_by_info("2017", "2nd", "01")
    with open('../data/dsm2017/2nd/01.json', 'r', encoding="UTF8") as f:
        real_datas = json.load(f)
    assert words == real_datas