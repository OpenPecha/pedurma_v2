from pg_num_to_img_num import convert_pg_no_to_img_num

def test_pg_num_converter():
    vol_text = """
[𰵀1a]
༄༅
:
:
[𰵁1b]


[𰵌7a]
དེབ་དང་པོའི་དཀར་ཆག
༥
དང་པོ། བསྟོད་ཚོགས། ༼ཀ༽
[𰵍7b]
བསྡུར་མཆན།(༡༠༤） བསྡུར་འབྲས་རེའུ་མིག(༡༡༢）
༠༠༠༣ ཐམས་ཅད་མཁྱེན་པ་དབང་ཕྱུག་ཆེན་པོའི་བསྟོད་པ། ....
"""
    new_vol_text = convert_pg_no_to_img_num(vol_text)
    expected_vol_text = """
[1]
༄༅
:
:
[2]


[13]
དེབ་དང་པོའི་དཀར་ཆག
༥
དང་པོ། བསྟོད་ཚོགས། ༼ཀ༽
[14]
བསྡུར་མཆན།(༡༠༤） བསྡུར་འབྲས་རེའུ་མིག(༡༡༢）
༠༠༠༣ ཐམས་ཅད་མཁྱེན་པ་དབང་ཕྱུག་ཆེན་པོའི་བསྟོད་པ། ....
"""
    assert expected_vol_text == new_vol_text


if __name__ == "__main__":
    test_pg_num_converter()