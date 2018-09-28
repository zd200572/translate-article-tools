from drop_enter import *
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException 
from tencentcloud.tmt.v20180321 import tmt_client, models 

dic ={}
paragraph = drop_enter("fin.txt")
try: 
    cred = credential.Credential("", "") 
    httpProfile = HttpProfile()
    httpProfile.endpoint = "tmt.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = tmt_client.TmtClient(cred, "ap-shanghai", clientProfile) 

    req = models.TextTranslateRequest()
    params = '{"SourceText":"%s","Source":"en","Target":"zh","ProjectId":"1"}' % paragraph
    req.from_json_string(params)

    resp = client.TextTranslate(req) 
    dic = resp.to_json_string()

    print(dic[32:][:-71]) 
    print('\n\n')

except TencentCloudSDKException as err: 
    print(err) 