import grpc
import concurrent.futures as futures
import exclusao_mutua_pb2
import exclusao_mutua_pb2_grpc
import time

class ServicoEleicao(exclusao_mutua_pb2_grpc.ServicoEleicaoServicer):
    def __init__(self):
        self.process_id = None
        self.recurso_compartilhado = 0  # recurso que vai ser compartilhado
        self.flag = [False, False]  # flag pra entrar na seção

    def IniciarPedido(self, request, context):
        self.process_id = request.id_do_processo
        print("O processo {} acabou de iniciar o pedido de exclusão mútua.".format(self.process_id))
        # entrando na seção
        self.flag[self.process_id] = True
        self.turn = 1 - self.process_id
        while self.flag[1 - self.process_id] and self.turn == 1 - self.process_id:
            pass
        #sessão critica
        self.recurso_compartilhado += 1
        print("O processo {} acessou o recurso compartilhado".format(self.process_id))
        print("O recurso compartilhado foi acessado {} vezes.".format(self.recurso_compartilhado))
        time.sleep(1)  
        #saindo 
        self.flag[self.process_id] = False

        return exclusao_mutua_pb2.PedidoResponse()

    def EncerrarPedido(self, request, context):
        self.process_id = None
        print("O processo {} encerrou o pedido de exclusão mútua.".format(request.id_do_processo))
        return exclusao_mutua_pb2.PedidoResponse()


def rodar_servidor():
    server = grpc.server(futures.ThreadPoolExecutor())
    exclusao_mutua_pb2_grpc.add_ServicoEleicaoServicer_to_server(ServicoEleicao(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor em execução...")
    server.wait_for_termination()

if __name__ == '__main__':
    rodar_servidor()
