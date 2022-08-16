endereco = "João Luiz 505, Jardim São Lourenzo, Sorocaba, SP, 18076-310"

import re # regular expression - RegEx

# 5 dígitos + hífen (opcional) + 3 dígitos

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco) #match
if busca:
    cep = busca.group()
    print(cep)