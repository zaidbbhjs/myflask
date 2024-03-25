import os,sys
#os.system("pip install fastapi")
#os.system("pip install uvicorn")
from fastapi import Response
import requests
import os
import random
import uvicorn,time
from fastapi import Request
import json
from user_agent import generate_user_agent
from fastapi.responses import JSONResponse
from fastapi import FastAPI
import secrets
app = FastAPI()
import requests
import requests , time,random
from json import dumps
r = requests.session()
a=int(0)
from fastapi import FastAPI, UploadFile
from secrets import token_hex
import uuid,secrets
cok = token_hex(8) * 2
uuid = str(uuid.uuid4())
app = FastAPI()
@app.get('/api/gmail/{gmail}')
async def ga(gmail):
    global cok,uuid
    email=gmail
    url = 'https://accounts.google.com/_/lookup/accountlookup?hl=ar&_reqid=32589&rt=j'
	
    headers = {
		'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
		'content-length': '3911',
		'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
		'cookie': 'OGPC=422038528-2:; SID=8Ae5CNXyYLku7h3Nhd6PmjEwsqpLep9sdfcDc_QeJT1m6pf_cFdWBefOdFWBrRatzQzoTw.; __Secure-3PSID=8Ae5CNXyYLku7h3Nhd6PmjEwsqpLep9sdfcDc_QeJT1m6pf_LWBgOEuV0LWH29_CLb3l1g.; HSID=A8KaTqMCOG6xpfvsz; SSID=AtYd81IgyZuE9EbfE; APISID=E3Psm5Uangi4fH9M/AkOnPYEUZWnD-tnA_; SAPISID=iN7Q0OqbHZcyy5FL/Aerh1_4xeYlLJY4Hq; __Secure-3PAPISID=iN7Q0OqbHZcyy5FL/Aerh1_4xeYlLJY4Hq; ACCOUNT_CHOOSER=AFx_qI6QfbFWoV6PV6XKN_T6BDu29QAEvMrEZsoAl1r4bDBfnWApbNKbPlRCbFUWBfZ_IufZlpgrXPJIQyLZtlrdzhTBLG1ugbS2CJ2q9HNMMkzfgeaXgctISpVwNdXddAWu4ZnL0x6TC4OCJGrmngsaE5GSmcovCQ; LSID=o.myaccount.google.com|s.youtube:8Ae5CGkVX0iajA0zvRf3mhX7pmhByOogOBptOhnbeOOuoJS6lsMzh7eIoJ7jRz_OOQU1DQ.; SEARCH_SAMESITE=CgQImZIB; __Host-3PLSID=doritos|o.myaccount.google.com|s.youtube:8Ae5CGkVX0iajA0zvRf3mhX7pmhByOogOBptOhnbeOOuoJS6ByLMNjL9oNzA97kBg7BANg.; 1P_JAR=2021-03-29-09; NID=212=i268DCPkYi3AzR0f25yIGeJwDvI9KnX0IkpB6-jLiMgIkylu-ok0FxsNwgb77pnNf9P1dRbBa0rwmwoo3rBZLPEqBaYbIUTYOqnGXlodQyFP6PiO7x1DARyLyIg2nH_J_J208rXWq1sLL7oP_YSeJFznofwfpsHamypEYMgwPx2rU9UJJ59txYOFOliHngVgrmyLeujCj_dKNV8hrTJDFTTVfnxZG68C; __Host-GAPS=1:BWYU84SbcmvuPTxMnLb_Bw1WhSze11euoEbasRquyke84p3z6kKhM4STn2l2KqDaXmLnjmuLAu5YjxpgPYYS2MAbFJoYEA:8QsfUKnQPG8GNFFh; SIDCC=AJi4QfGikn_BfUsmrNc_AQgbrwCzKzaBTYlqHvZ_vt7pRS98qOGuitJ1M1_khzvPELS_owtDIQ; __Secure-3PSIDCC=AJi4QfH3OD5jfNAacCFyT0_heunei0GLdQymhUmRU8zPB7R7Svse8_GiuWLuXbaSblXAYlq-7bU',
		'google-accounts-xsrf': '1',
		'origin': 'https://accounts.google.com',
		'referer': 'https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fadssettings.google.com%2Fauthenticated%3Fref%3Dyt_auth%26pli%3D1&ec=GAlAmQM&flowName=GlifWebSignIn&flowEntry=AddSession',
		'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
		'sec-ch-ua-mobile': '?0',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
		'x-chrome-id-consistency-request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=eaa94017-90e6-4761-a779-143e63ce180a,sync_account_id=116486990055578668701,signin_mode=all_accounts,signout_mode=show_confirmation',
		'x-client-data': 'CJa2yQEIo7bJAQjEtskBCKmdygEIlqzKAQiIucoBCIbCygEI+MfKAQjx6soBCLGaywEI1JzLAQjjnMsBCKmdywEY4ZrLAQ==',
		'Decoded':
		'message ClientVariations {// Active client experiment variation IDs. repeated int32 variation_id = [3300118, 3300131, 3300164, 3313321, 3315222, 3316872, 3318022, 3318776, 3323249, 3329329, 3329620, 3329635, 3329705]; // Active client experiment variation IDs that trigger server-side behavior. repeated int32 trigger_variation_id = [3329377];}',
		'x-same-domain': '1' }
    foeml=gmail
    data = {
		'continue': 'https://adssettings.google.com/authenticated?ref=yt_auth&pli=1',
		'f.req': f'["{foeml}","AEThLlw6VGsyn2_pe-f86vgMSUv6HW6cl7s3ftZAG2KM59m7HtlMteSbiMd1cXodMV9ao2r-etLvEFwNOT1gmDeaWFo3pqVs2c8soJREt0Nt6O_RSxudYIUsivz-edV1f8qX-zBOsY7YMWaow-mczgAPFsOkLBibmlmgwm2DK_Mq4qKUpR1tG4YpAzApopzlBEgFAymMMus8",[],null,"US",null,null,2,false,true,[null,null,[2,1,null,1,"https://accounts.google.com/AddSession?continue=https%3A%2F%2Fadssettings.google.com%2Fauthenticated%3Fref%3Dyt_auth%26pli%3D1&ec=GAlAmQM",null,[],4,[],"GlifWebSignIn",null,[]],10,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"eaa94017-90e6-4761-a779-143e63ce180a",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,[],[]],null,null,null,null,null,null,[],null,null,null,[],[]],null,null,null,true],"{foeml}",null,null,null,true,true,[]]',
		'bgRequest': '["identifier","!XV6lXhPNAAY7smA8O7JCzxWNYzZtiS87ACkAIwj8RuOTLVLxGJigVpDhaC2z7ynSG4_C6vg2kxXAWOp26z7eH2IZogIAAAB9UgAAAB5oAQeZBBMPBNZpIQ75l0BgkmrzBFCvhfOdp8Lin14ikTnA1WsoaIfdlfYG6MYQnjc1UrPRJa74ZxDpu1BFftPI0nN7EOnM4ZS18dsZejZRwZBLtKG8QP0Q-GJEOZbq2-r2fqHe3GZb5Z7NW4rUeCLKfwsV7Tb8fuzfYlpZ_40Mw5S4Gk1C7BL4MOhtd3GE_62Qp-RuqLoqIvv5XIqMbLq6v0PjY6cUg5wg3cN4n3dF26kVWJYtS8vpVd5kBtydVCgidSNhN4ARi9Lk5TocNbPYonI5sm-7sJ0UGHI7wT4OFXJeKK_FgVxjXWI2FpFSrEPhgZahdfMB94LMNK-8eMIJKLTR-eOtu6l6TB3KVZEthoN_M0pvQHPcfAhLb0EB5tfkrcdZiMhOCGIZuCBmjzkog2_DV0Mw8Im5hMuTm8qrmX7i-lzWEmuuuYW5FGKDUraHZ0A0EmvWRaw7uMII2ScdpcXWUI6JGEjZYgGmOoTgMWVmUU0HTKuwLYkJvYxV89EdOjdtEjqfnlEl9WC21RfSxIt3mMkr9orJdP4opSk6neVuFTvvRD53NZ9iNboauX0Epe0IFa6NvidBSHLXIiaC92VUeNE08EaGEMXcy45ffg2BYsxmyu4DWRIoPcr0t1IrWdhwc1srOguxWl0mBs6QYeyLBc4CNRVglRFm3nklWlIE31g8GahYNLQnAxeljgp_WKEXda5VQm6WkDGcYGPbRf3bfxYqbJircIPhcOEYXzk8BQ9gJq9i3t3zX3qFg9U9B3skBRK4JgGKwzVWGjrw6K5G9uIOFsmXdPq7pdQE_tQ-PMPkuUPNoIZb98lu6reUbBEDHWfnpaiY6tjtTg0fcQW0kzrUN5kwJz7L47KpDYij4K3Y-hWN4vXJAFrbAHazlYZ4THHYrQDxeITF0MP6vweiyoful6H_YArrwliPX_7kswLE1MYOR_i5KwYlJEi9dMz1nSzyRynLSthBsez-zQYhlbt5Xhi8NuL3dRMxM8zRj2yw71sYdKjsX_AvNz0JX0v6W6eQSv6pVwyNAscdFsBcNt2N3xvwy0YUiFwIud5ypZe_MeWd8aByk4cce21tpZN8FDa4j6b2CGXPVpaVC7IZjCh0h_cXfFPoNONzD9roDpmOKzCrTj_q6xNPhtwY8vWdTV0CaJJbcm_ra3rp3FF0x6Hws5KZl9KpeRanphhtuiT90e-49V2AYdmbdlXgtZqJBswKwOOZhYUcw_33Q8t27ZXtiKxW2ieUv3fwvJ9Dz8l9pttsavtYUZ_mX6mN-PU4orT89JgeUDqimD91YI6Yx7KyoYlRbe7hYWNMzo0RAuuoElDr6GyTgf7pZC67XYQKm3-J3Obuja9iac7IeN7KaScI7uGcFV9gNhvP8j6evm9zws5Dlw"]',
		'at': 'AFoagUW_q8bXR45ZgAOS4A5fq9dVpQpMBQ:1617008567951',
		'azt': 'AFoagUW9q50Z3AnyfPsppwG7DjGdRvSUMQ:1617008567952',
		'cookiesDisabled': 'false',
		'deviceinfo': '[null,null,null,[],null,"US",null,null,[],"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"eaa94017-90e6-4761-a779-143e63ce180a",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,[],[]],null,null,null,null,null,null,[],null,null,null,[],[]],null,null,null,null,2,null,false]',
		'gmscoreversion': 'undefined',
		'checkConnection': 'youtube:142:0',
		'checkedDomains': 'youtube',
		'pstMsg': '1'}

    ok = r.post(url,headers=headers,data=data).text
    if "https://support.google.com/accounts/answer" in ok:
    		
    		data2={
    		"email":f"{gmail}",
    		"status":"Bad",
    		"Dev":"Marko_Bots",
    		}
    		return JSONResponse(content=data2)
    else:
    		dta={
    		"email":f"{gmail}",
    		"status":"Hit",
    		"Dev":"Marko_Bots",
    		}
    		return JSONResponse(content=dta)

#uvicorn.run(app,host='0.0.0.0',port=8080)