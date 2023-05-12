# Algoritmo de exclusão mútua de Peterson/gRPC

Disciplina: Sistemas Distribuídos

O algoritmo de exclusão mútua de Peterson é uma solução clássica para garantir a exclusão mútua em um sistema distribuído ou paralelo, permitindo que processos ou threads compartilhem recursos sem conflitos.


## Cliente/Servidor

- O servidor implementado permite que os clientes iniciem e encerrem pedidos de exclusão mútua para acessar um recurso compartilhado.

- O cliente envia um pedido de exclusão mútua para acessar o recurso compartilhado e, em seguida, encerra o pedido.


## Instalação


Necessário possuir Python, e as bibliotecas concurrent.futures, grpcio e grpcio-tools, e uuid instalados.


```
pip install grpcio grpcio-tools

```

## Execução

Dentro do diretório com os arquivos, entre eles o _exclusao_mutua.proto_ executar:
```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. exclusao_mutua.proto
```

Isso irá gerar os arquivos exclusao_mutua_pb2 e exclusao_mutua_pb2_grpc, dentro do diretório junto a todos os códigos.

Em prompts de comandos diferente executar o arquivo do servidor/cliente:

```
python servidor.py
```
```
python cliente.py
```

_Documentação gRPC em python:_ https://grpc.io/docs/languages/python/basics/
