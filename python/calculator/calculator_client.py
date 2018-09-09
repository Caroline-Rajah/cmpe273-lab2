import grpc

import calculator_pb2
import calculator_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub=calculator_pb2_grpc.CalculatorStub(channel)
        response=stub.add(calculator_pb2.AddRequest(a=4,b=8))
        print(f"The sum of 4 and 8 is {response.c}")

if __name__ == '__main__':
    run()
