
from python_aternos import Client, atserver
from python_aternos import Client
def ServerStarted():

    user = "M0BL0L"
    pswd = "89001360608Zz"

    atclient = Client()
    aternos = atclient.account
    atclient.login(user, pswd)

    srvs = aternos.list_servers()
    print(srvs)



    s = srvs[1]
    s.eula()
    s.start()


def info():
    data = []
    user = "M0BL0L"
    pswd = "89001360608Zz"

    atclient = Client()
    aternos = atclient.account
    atclient.login(user, pswd)

    srvs = aternos.list_servers()

    srv = srvs[1]

    print()
    data.append(f"-=*** {srv.servid} ***=-")
    print('***', srv.servid, '***')
    srv.fetch()
    data.append(srv.domain)
    print(srv.domain)
    data.append(srv.motd)
    print(srv.motd)
    data.append(f"*** Status: {srv.status}")
    print('*** Status:', srv.status)
    data.append(f"*** Full address: {srv.address}")
    print('*** Full address:', srv.address)
    data.append(f"*** Port: {srv.port}")
    print('*** Port:', srv.port)
    data.append(f"*** Name: {srv.subdomain}")
    print('*** Name:', srv.subdomain)
    data.append(f"*** Minecraft: {srv.software, srv.version}")
    print('*** Minecraft:', srv.software, srv.version)
    data.append(f"*** IsBedrock: {srv.edition == atserver.Edition.bedrock}")
    print('*** IsBedrock:', srv.edition == atserver.Edition.bedrock)
    data.append(f"*** IsJava: {srv.edition == atserver.Edition.java}")
    print('*** IsJava:', srv.edition == atserver.Edition.java)

    print()
    return data