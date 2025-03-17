commonMPINS4digits=["1234","1111","0000","1212","7777","1004","2000","4444","2222","6969"]   #built a hashmap that can be used to search for commonly used passwords
commonMPINS6digits=["123456", "654321", "111111", "000000", "123123", "666666", "121212", "112233", "789456", "159753"  ]
def supported(n,demographics):                                                                       
    output=[]
    if len(n)!=4 and len(n)!=6:
        raise Exception("Entered MPIN is not 4 digits or 6 digits")

    if  (len(n) == 4 and n in commonMPINS4digits) or (len(n) == 6 and n in commonMPINS6digits):
        output.append("COMMONLY_USED")
        return output                             
    else:
        for i in range(len(demographics)):
            day,month,year=demographics[i].split('-')
            variations1=[day+month,month+day,year,day+year[-2:],month+year[-2:]]
            variation2=[day+year,month+year]
            if len(n)==4 and n  in variations1 or len(n)==6 and n in variation2:
                if i==0:
                    output.append('DEMOGRAPHIC_DOB_SELF')
                elif i==1:
                    output.append('DEMOGRAPHIC_DOB_SPOUSE')
                else:
                    output.append('DEMOGRAPHIC_ANNIVERSARY')

    return output


if __name__=='__main__':
    test_cases = [
    {"mpin": "1234", "demographics": []},         #will not work and bost the exception as in the function
    {"mpin": "0000", "demographics": []},
    {"mpin": "1122", "demographics": []},
    {"mpin": "2506", "demographics": ["25-06-1990"]},
    {"mpin": "1492", "demographics": ["14-08-1992"]},
    {"mpin": "0101", "demographics": ["01-01-1995"]},
    {"mpin": "9802", "demographics": ["02-02-1998"]},
    {"mpin": "6789", "demographics": []},
    {"mpin": "0195", "demographics": ["20-24-2001", "15-09-1987", "01-01-1995"]},
    {"mpin": "1985", "demographics": ["06-06-1985", "06-06-1990","01-05-2000"]},
    {"mpin": "654321", "demographics": []},
    {"mpin": "2222", "demographics": []},
    {"mpin": "2525", "demographics": []},
    {"mpin": "1587", "demographics": ["15-09-1987"]},
    {"mpin": "9090", "demographics": []},
    {"mpin": "1212", "demographics": []},
    {"mpin": "1509", "demographics": ["15-09-1990"]},
    {"mpin": "2001", "demographics": ["20-01-2000"]},
    {"mpin": "8888", "demographics": []},
    {"mpin": "4321", "demographics": []},
    {"mpin": "123456", "demographics": []},
    {"mpin": "654321", "demographics": []},
    {"mpin": "111111", "demographics": []},
    {"mpin": "000000", "demographics": []},
    {"mpin": "123123", "demographics": []},
    {"mpin": "666666", "demographics": []},
    {"mpin": "121212", "demographics": []},
    {"mpin": "112233", "demographics": []},
    {"mpin": "789456", "demographics": []},
    {"mpin": "159753", "demographics": []},
]
    for case in test_cases:
        print(supported(case["mpin"],case["demographics"]))


    
