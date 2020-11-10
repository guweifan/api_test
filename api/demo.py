import random
from walnuts import RequestMapping, Method, Requester
from api.identity import IdNumber
from api.randstr import get_name,generate_random_num,get_tel,generate_random_str,get_time



# 招联授信加密
@RequestMapping(path='{app.encrvption}', method=Method.POST)
class Encrvption:

    @RequestMapping(method=Method.POST)
    def creditApply_encrvption(self):
        '''授信申请接口加密'''
        applyno = generate_random_num(11)
        custName = get_name()
        mobileNo = get_tel()
        custNo = "test" + generate_random_num(11)
        openId = generate_random_str(10)
        random_sex = random.randint(0, 1)
        applyTime = "20200605"
        idNo = IdNumber.generate_id(random_sex)
        data = {
                "bizContent":{
                "applyNo":applyno,
                "idNo":idNo,
                "mobileNo":mobileNo,
                "custNo":custNo,
                "openId":openId,
                "occupation":"其他",
                "nation":"汉",
                "residentAddr":"",
                "ipAddr":"",
                "gpsAddr":"116,40",
                "trustId":"000000000",
                "workCity":"",
                "certValidDate":"20000801-20300801",
                "addr":"中国台湾台北市",
                "applyTime":applyTime,
                "channelCode":"MUCF",
                "address":"中国台湾",
                "workAddr":"上海市",
                "suggestLimit":"900",
                "custName":custName,
                "extendInfo": "{\"cardLmtNear6mUsed\":\"0\",\"card24mHstrOvdMax\":\"000000000000000000000000\",\"class5StateGuaLoan\":\"否\",\"cardOvdAmtTot\":\"0\",\"loanOvdAmtTot\":\"0\",\"loan24mHstrOvdCnt\":\"000000000000000000000000\",\"loanQueryOrgCnt1m\":\"0\",\"selfQueryCnt1m\":\"0\",\"badDebtRecords\":\"否\",\"loanBalance\":\"0\",\"loanAbnormalCnt\":\"0\",\"houseFundBase\":\"5\",\"ovdMonthMax\":\"0\",\"houseLoanPrcp\":\"0\",\"reportCreateTime\":\"0\",\"cardLmtUsed\":\"\",\"cardAbnormalCnt\":\"0\",\"loanOrgCnt\":\"0\",\"cardTotLmt\":\"0\",\"cardUsingHstrAvg\":\"0\",\"card24mHstrOvdCnt\":\"000000000000000000000000\",\"cardQueryOrgCnt1m\":\"0\",\"loan24mHstrOvdMax\":\"000000000000000000000000\",\"monthIncome\":\"10000\",\"loanPayAmt1m\":\"0\"}",
                "workCompany":"",
                "residentCity":"",
                "bioCompareRs":"true",
                "merchantNo":"000000000"
            },
            "appId": "merchCreditApply",
            "channelCode":"MUCF",
            "encoding":"UTF-8",
            "encryptKey":"cAzHFcdZaSbNaV57dCCr4n+Y+4rh0K3AZdcFwP/0GUukI3ZjpG3XqZgANWe9j8QRd4nXeVPnS2W2Vh7hb3ykTa6jeSTKRJYhe8ZWWrSwJqYriTSleoUwRBNBLoR9XI5a22PsjrTJBa6AKtaBmo4kS9NXEe3j13ka5SOg7zeeVSU=",
            "encryptType":"AES",
            "flowNo":"000006",
            "merchantId":"000000",
            "reqDateTime":"2020-10-15 01:35:22",
            "reqServiceId":"merchCreditApply",
            "sign":"JMvAl1F472juRss0SBm5Md7mA4VsKt4ZGLtLPqnli07ERfl91GUyOtB2/p9OouuyBdD0fvHlPbTU3Et+lCnYgHdMOV0bhIRQFLpCA4lExjmfDQWuu0HSMBN+kiUoemHJBDVFJ8RAODIFeDRxSQGCjMwZTJrZKwez+XnIXvhIHcI=",
            "subMerchantId":"000000"
}

        return Requester(json=data)

# 招联授信
@RequestMapping(path='{app.url}', method=Method.POST)
class CreditApply:

    @RequestMapping(method=Method.POST)
    def creditApply(self):
        '''授信申请接口'''
        fun = Encrvption()
        data = fun.creditApply_encrvption().text()
        return Requester(json=data)
















# if __name__ == '__main__':
    # http_bin = vip_encryption()
    # http_bin.add_header_to_all()
    # http_bin.post_form().json()
    # print(http_bin.vip_encryption())
    # http_bin.path_var().json()
    # post_json()

