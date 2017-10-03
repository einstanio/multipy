from Savoir import Savoir
from pickle import *
import wx

def creafile():
    file = open("dati.dat", "wb")
    rpcuser = input("User: ")
    rpcpasswd = input("Password: ")
    rpchost = input("Host o indirizzo IP: ")
    rpcport = input("Porta: ")
    chainname = input("Nome del chain: ")
    dump(rpcuser, file)
    dump(rpcpasswd, file)
    dump(rpchost, file)
    dump(rpcport, file)
    dump(chainname, file)
    file.close()
    configurazione = [rpcuser, rpcpasswd, rpchost, rpcport, chainname]
    return configurazione

def caricafile():
    configurazione = []
    try:
        file = open("dati.dat", "rb")
        rpcuser = load(file)
        rpcpasswd = load(file)
        rpchost = load(file)
        rpcport = load(file)
        chainname = load(file)
        configurazione = [rpcuser, rpcpasswd, rpchost, rpcport, chainname]
        return configurazione
    except FileNotFoundError:
        configurazione = creafile()
        return configurazione

configurazione = []
configurazione = caricafile()


api = Savoir(configurazione[0], configurazione[1], configurazione[2], configurazione[3], configurazione[4])

app = wx.App()
frm = wx.Frame(None, title="Hello World")
frm.Show()
app.MainLoop()

#rpcuser = 'multichainrpc'
#rpcpasswd = '7dZZjBNKMFFphjiVpMce1yVCWXWQQ6eKN6Ne6vkVudiT'
#rpchost = 'localhost'
#rpcport = '7410'
#chainname = 'trust'