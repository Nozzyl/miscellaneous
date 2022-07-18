from textwrap import wrap


def symmetric_enc(inp, pw, enc):
    char_dict = {
        """a""": """0001""",
        """b""": """0002""",
        """c""": """0003""",
        """d""": """0004""",
        """e""": """0005""",
        """f""": """0006""",
        """g""": """0007""",
        """h""": """0008""",
        """i""": """0009""",
        """k""": """0010""",
        """l""": """0011""",
        """m""": """0012""",
        """n""": """0013""",
        """o""": """0014""",
        """p""": """0015""",
        """q""": """0016""",
        """r""": """0017""",
        """s""": """0018""",
        """t""": """0019""",
        """u""": """0020""",
        """v""": """0021""",
        """w""": """0022""",
        """x""": """0023""",
        """y""": """0024""",
        """z""": """0025""",
        """,""": """0026""",
        """.""": """0027""",
        """'""": """0028""",
        '''"''': """0029""",
        """ """: """0030""",
        """!""": """0031""",
        """1""": """0032""",
        """2""": """0033""",
        """3""": """0034""",
        """4""": """0035""",
        """5""": """0036""",
        """6""": """0037""",
        """7""": """0038""",
        """8""": """0039""",
        """9""": """0040""",
        """0""": """0041""",
        """A""": """0042""",
        """B""": """0043""",
        """C""": """0044""",
        """D""": """0045""",
        """E""": """0046""",
        """F""": """0047""",
        """G""": """0048""",
        """H""": """0049""",
        """I""": """0050""",
        """J""": """0051""",
        """K""": """0052""",
        """L""": """0053""",
        """M""": """0054""",
        """N""": """0055""",
        """O""": """0056""",
        """P""": """0057""",
        """Q""": """0058""",
        """R""": """0059""",
        """S""": """0060""",
        """T""": """0061""",
        """U""": """0062""",
        """V""": """0063""",
        """W""": """0064""",
        """X""": """0065""",
        """Y""": """0066""",
        """Z""": """0067""",
        """?""": """0068""",
        """j""": """0069"""
    }
    char_dict_reversed = {
        '''0001''': '''a''',
        '''0002''': '''b''',
        '''0003''': '''c''',
        '''0004''': '''d''',
        '''0005''': '''e''',
        '''0006''': '''f''',
        '''0007''': '''g''',
        '''0008''': '''h''',
        '''0009''': '''i''',
        '''0010''': '''k''',
        '''0011''': '''l''',
        '''0012''': '''m''',
        '''0013''': '''n''',
        '''0014''': '''o''',
        '''0015''': '''p''',
        '''0016''': '''q''',
        '''0017''': '''r''',
        '''0018''': '''s''',
        '''0019''': '''t''',
        '''0020''': '''u''',
        '''0021''': '''v''',
        '''0022''': '''w''',
        '''0023''': '''x''',
        '''0024''': '''y''',
        '''0025''': '''z''',
        '''0026''': ''',''',
        '''0027''': '''.''',
        '''0028''': """'""",
        '''0029''': '''"''',
        '''0030''': ''' ''',
        '''0031''': '''!''',
        '''0032''': '''1''',
        '''0033''': '''2''',
        '''0034''': '''3''',
        '''0035''': '''4''',
        '''0036''': '''5''',
        '''0037''': '''6''',
        '''0038''': '''7''',
        '''0039''': '''8''',
        '''0040''': '''9''',
        '''0041''': '''0''',
        '''0042''': '''A''',
        '''0043''': '''B''',
        '''0044''': '''C''',
        '''0045''': '''D''',
        '''0046''': '''E''',
        '''0047''': '''F''',
        '''0048''': '''G''',
        '''0049''': '''H''',
        '''0050''': '''I''',
        '''0051''': '''J''',
        '''0052''': '''K''',
        '''0053''': '''L''',
        '''0054''': '''M''',
        '''0055''': '''N''',
        '''0056''': '''O''',
        '''0057''': '''P''',
        '''0058''': '''Q''',
        '''0059''': '''R''',
        '''0060''': '''S''',
        '''0061''': '''T''',
        '''0062''': '''U''',
        '''0063''': '''V''',
        '''0064''': '''W''',
        '''0065''': '''X''',
        '''0066''': '''Y''',
        '''0067''': '''Z''',
        '''0068''': '''?''',
        '''0069''': '''j'''
    }

    def turn_to_number(string):
        output = '9'
        for char in str(string):
            output += (char_dict[char])
        return int(output)

    def turn_to_string(number):
        num = str(number).replace('9', '', 1)
        out = ''
        for character in wrap(num, 4):
            out += char_dict_reversed[character]
        return out

    def password_encryptor(string_in, password_to_encrypt):
        return turn_to_number(string_in) ^ turn_to_number(password_to_encrypt)

    def password_decrypter(number, password_to_decrypt):
        return turn_to_string(int(int(number) ^ turn_to_number(password_to_decrypt)))

    try:
        if enc == 1:
            return password_encryptor(inp, pw)
        elif enc == 0:
            return password_decrypter(inp, pw)
        else:
            return 'invalid input error 1'
    except IndexError or ValueError:
        return 'invalid input error 2'


print('PASSWORD PROTECTED MESSAGE ENCRYPTING AND DECRYPTING SOFTWARE')
while True:
    whether_to_encrypt = input('Encrypt or decrypt: ')
    if whether_to_encrypt == 'encrypt':
        message = input('Message: ')
        password = input("Password to encrypt: ")
        print(symmetric_enc(message, password, 1))
    elif whether_to_encrypt == 'decrypt':
        message = input('Encrypted message: ')
        password = input('Password to decrypt: ')
        print(symmetric_enc(message, password, 0))
    elif whether_to_encrypt == 'quit':
        while True:
            whether_sure = input('''Are you sure you want to quit (type 'yes' or 'no')? 
> ''')
            if whether_sure == 'yes':
                sure_to_break = True
                break
            elif whether_sure == 'no':
                sure_to_break = False
                break
            else:
                print("please type 'yes' or 'no'")
                continue
        if sure_to_break:
            break
    else:
        print("please type 'encrypt' or 'decrypt', to close the program, type 'quit'")
