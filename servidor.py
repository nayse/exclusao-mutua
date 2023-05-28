import grpc
from concurrent import futures
import threading
import time

import exclusao_mutua_pb2
import exclusao_mutua_pb2_grpc

tempo_espera = 60 * 60 * 24

class ExclusaoMutuaServicer(exclusao_mutua_pb2_grpc.ExclusaoMutuaServicer):
    def __init__(self):
        self.clientes = []
        self.mutex = threading.Lock()
        self.token = False
        self.cliente_atual = None
        self.thread_repasse_token = threading.Thread(target=self.repasse_token)
        self.thread_repasse_token.start()

    def RegistrarCliente(self, request, context):
        cliente_id = request.cliente_id
        print(f"Cliente {cliente_id} conectado.")
        self.clientes.append(cliente_id)
        return exclusao_mutua_pb2.RespostaRegistro()

    def SolicitarAcesso(self, request, context):
        cliente_id = request.cliente_id
        print(f"Cliente {cliente_id} solicitou acesso.")

        with self.mutex:
            if not self.token:
                self.token = True
                self.cliente_atual = cliente_id
                print(f"Cliente {cliente_id} obteve acesso à seção crítica.")
                return exclusao_mutua_pb2.RespostaAcesso(permitido=True)
            else:
                print(f"Acesso negado para o cliente {cliente_id}. Aguardando para obter acesso à seção crítica.")
                return exclusao_mutua_pb2.RespostaAcesso(permitido=False)

    def LiberarAcesso(self, request, context):
        cliente_id = request.cliente_id
        print(f"Cliente {cliente_id} liberou acesso.")

        with self.mutex:
            if cliente_id == self.cliente_atual:
                self.token = False
                self.cliente_atual = None
                print(f"Cliente {cliente_id} liberou o acesso à seção crítica.")

        return exclusao_mutua_pb2.RespostaLiberacao()

    def repasse_token(self):
        while True:
            if not self.token and self.clientes:
                self.cliente_atual = self.clientes[0]
                self.token = True
                print(f"Cliente {self.cliente_atual} obteve acesso à seção crítica.")
                self.clientes = self.clientes[1:] + [self.clientes[0]]
            time.sleep(1)  # Intervalo de repasse do token

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    exclusao_mutua_pb2_grpc.add_ExclusaoMutuaServicer_to_server(
        ExclusaoMutuaServicer(), server
    )
    server.add_insecure_port("[::]:90000")
    server.start()
    print("Servidor em execução...")
    try:
        while True:
            time.sleep(tempo_espera)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()
