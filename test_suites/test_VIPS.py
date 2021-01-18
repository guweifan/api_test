from api.channel.VIPS import VIPS
from api.identity import IdNumber
from api.base import get_image_01_base, get_image_02_base, get_image_03_base
from api.randstr import generate_random_num



class TestVips:


    def test_pay(self):
        """唯品会授信申请"""
        app = VIPS()
        img01 = get_image_01_base()
        img02 = get_image_02_base()
        img03 = get_image_03_base()
        referno = "V" + generate_random_num(12)
        idnumber = IdNumber.generate_id(2)
        img01_res = app.PATSVPSS1004("1.jpg", img01, "1", referno, idnumber).json()
        assert img01_res["sys"]['erortx'] == "SUCCESS"     # 断言
        img02_res = app.PATSVPSS1004("2.jpg", img02, "2", referno, idnumber).json()
        assert img02_res["sys"]['erortx'] == "SUCCESS"     # 断言
        img03_res = app.PATSVPSS1004("3.jpg", img03, "3", referno, idnumber).json()
        assert img03_res["sys"]['erortx'] == "SUCCESS"     # 断言

        res = app.PATSVPSS1005(referno, idnumber).json()
        assert res["sys"]['erortx'] == "SUCCESS"  # 断言
