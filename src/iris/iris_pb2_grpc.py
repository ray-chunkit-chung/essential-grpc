# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import iris_pb2 as iris__pb2


class IrisPredictorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PredictIris = channel.unary_unary(
                '/ml.IrisPredictor/PredictIris',
                request_serializer=iris__pb2.IrisPredictRequest.SerializeToString,
                response_deserializer=iris__pb2.IrisPredictReply.FromString,
                )


class IrisPredictorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PredictIris(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IrisPredictorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PredictIris': grpc.unary_unary_rpc_method_handler(
                    servicer.PredictIris,
                    request_deserializer=iris__pb2.IrisPredictRequest.FromString,
                    response_serializer=iris__pb2.IrisPredictReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ml.IrisPredictor', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class IrisPredictor(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PredictIris(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ml.IrisPredictor/PredictIris',
            iris__pb2.IrisPredictRequest.SerializeToString,
            iris__pb2.IrisPredictReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
