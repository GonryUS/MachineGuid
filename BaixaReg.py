import streamlit as st
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


@st.cache
def convert_reg(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_txt().encode('utf-8')

reg = convert_reg(regedit)

st.download_button(
    label="Baixe seu MachineGuid AQUI",
    data=reg,
    file_name="MachineGuid - "+ str(myuuid)+".reg",
    mime='text/reg',
)
