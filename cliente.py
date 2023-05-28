import grpc
import exclusao_mutua_pb2
import exclusao_mutua_pb2_grpc

def run_client():

    channel = grpc.insecure_channel('localhost:90000')

    stub = exclusao_mutua_pb2_grpc.ExclusaoMutuaStub(channel)

    cliente_id = 123
    op = False
    while op == False:
        requisicao_acesso = exclusao_mutua_pb2.RequisicaoAcesso(cliente_id=cliente_id)


        resposta_acesso = stub.SolicitarAcesso(requisicao_acesso)


        if resposta_acesso.permitido:
            print(f"Cliente {cliente_id} obteve acesso à seção crítica.")
            liberacao = input("Digite 'l' para liberar o acesso: ")
            if liberacao == 'l':
                requisicao_liberacao = exclusao_mutua_pb2.RequisicaoLiberacao(cliente_id=cliente_id)
                stub.LiberarAcesso(requisicao_liberacao)
                print(f"Cliente {cliente_id} liberou o acesso à seção crítica.")
                print()
            op = True
        else:
            print(f"Acesso negado para o cliente {cliente_id}. Aguardando para obter acesso à seção crítica.")

if __name__ == '__main__':
    run_client()
