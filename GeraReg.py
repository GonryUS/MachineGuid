import uuid

myuuid = uuid.uuid4()

regedit = (f"Windows Registry Editor Version 5.00\n\n"
"[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography]\n"
'"MachineGuid"="'
    + str(myuuid)
    +'"')
arquivo = open("MachineGuid - "+ str(myuuid)+".reg", 'w+')
texto = arquivo.readlines()
texto.append(regedit)
arquivo.writelines(texto)
arquivo.close()
