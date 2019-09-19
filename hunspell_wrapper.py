from hunspell import Hunspell

h = Hunspell('fa-IR', hunspell_data_dir='data/dict')


def tests():
    print('Tests started ...')
    assert h.spell('سلام')
    assert h.spell('سلوم') is False
    print('Tests finished.')


tests()
