from api.channel.LXIN import LXIN


class TestLxin:



    def test_PATSCMSS5005(self):
        '''乐信授信申请'''
        app = LXIN()
        res = app.PATSCMSS5005().text()
        assert 'SUCCESS' in res


    def test_PATSCMSS5006(self):
        """乐信授信结果查询"""
        app = LXIN()
        applyNo = "777496058584918652"
        res = app.PATSCMSS5006(applyNo=applyNo).json()
        # assert 'SUCCESS' in res
        assert res["sys"]['erortx'] == "SUCCESS"