Jenkins Pipeline: OWASP ZAP 
===
Como preparar o pipeline para trabalhar com ferramenta OWASP Zed Attack Proxy

# Índice
1. [Download](#download)
   1. [Linux/Mac](#linuxmac)
   2. [Windows](#windows)
2. [Iniciar servidor](#iniciar-servidor)

# Download
> Utilizar sempre a última versão estável da aplicação

## Linux/Mac
Utilizar o comando:
```bash
wget https://github.com/zaproxy/zaproxy/releases/ZAP_2.7.0_Crossplatform.zip && \
unzip ZAP_2.7.0_Crossplatform.zip
```

## Windows
Efetuar o donwload através do navegador: https://github.com/zaproxy/zaproxy/releases/ZAP_2.7.0_Crossplatform.zip

# Iniciar servidor
Antes de iniciar o OWASP ZAP como servidor, primeiramente precisamos conhecer alguns parâmetros utilizados pela ferramenta: 
- **daemon**<br/> Inicializa o ZAP no modo daemon, sem GUI
- **host**<br/> Define o ip do servidr ZAP
- **port**<br/> Define a porta do servidr ZAP
- **config**<br/> Define/Sobrepõe as configurações do servidor, onde é definido através do formato CHAVE=VALOR, exemplo: *-config A=1 -config B=2*

Abaixo, algumas chaves de configuração:
- *connection.proxyChain.enable* <br/> Habilita/Desabilita o servidor de proxy
- *connection.proxyChain.hostName* <br/> IP ou endereço do servidor de proxy
- *connection.proxyChain.port* <br/> Porta do servidor de proxy
- *proxyChain.userName* <br/> Usuário de acesso ao servidor de proxy
- *proxyChain.password* <br/> Senha de acesso ao servidor de proxy
- *api.key* <br/> Define chave de segurança
- *api.disablekey* <br/> Remove a necessidade de utilizar a chave de segurança

Para iniciar o servidor, basta executar o comando:

```bash
cd <OWASP_ZAP_HOME> & \
java -jar zap-2.7.0.jar -daemon -host 127.0.0.1 -port 9999 -config api.key=abc123
```
Iniciando o servidor em uma rede com proxy corporativo
```bash
cd <OWASP_ZAP_HOME> & \
java -jar zap-2.7.0.jar -daemon -host 127.0.0.1 -port 9999 -config api.key=abc123 -config connection.proxyChain.enable=true -config connection.proxyChain.hostName=123.123.123.123 -config connection.proxyChain.port=8888
```


# Executando script

## Python
Acesse o projeto [Python](#/python) para ter ao código.

Instalar a biblioteca **"python-owasp-zap"**
```bash
pip install python-owasp-zap-v2.4
```
 
> Para mais informações, acesse o [github](https://github.com/zaproxy/zap-api-python) do projeto


