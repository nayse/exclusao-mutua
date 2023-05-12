import grpc
import exclusao_mutua_pb2
import exclusao_mutua_pb2_grpc
import time

def cliente():
    channel = grpc.insecure_channel('localhost:50051')
    stub = exclusao_mutua_pb2_grpc.ServicoEleicaoStub(channel) 
    request = exclusao_mutua_pb2.PedidoRequest(id_do_processo=1)     #envia pedido p/ iniciar a exclusao mutua
    response = stub.IniciarPedido(request)
    print("o processo --- {} --- iniciou o pedido de exclusão mútua".format(request.id_do_processo))
    request = exclusao_mutua_pb2.PedidoRequest(id_do_processo=1)     
    response = stub.EncerrarPedido(request) #envia pedido p/ acessar o recurso compartilhado
    print("o processo --- {} --- acessou o recuso compartilhado".format(request.id_do_processo))
    request = exclusao_mutua_pb2.PedidoRequest(id_do_processo=1) 
    response = stub.EncerrarPedido(request) # envia pedido p/ liberar o recurso
    print("o processo --- {} --- encerrou pediu exclusão mútua".format(request.id_do_processo))

if __name__ == '__main__':
    cliente()
