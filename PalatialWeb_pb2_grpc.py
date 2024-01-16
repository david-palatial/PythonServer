# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import PalatialWeb_pb2 as PalatialWeb__pb2


class PalatialWebCommunicationStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StartImport = channel.unary_unary(
                '/palatialrpc.PalatialWebCommunication/StartImport',
                request_serializer=PalatialWeb__pb2.ImportInfo.SerializeToString,
                response_deserializer=PalatialWeb__pb2.Ack.FromString,
                )


class PalatialWebCommunicationServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StartImport(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PalatialWebCommunicationServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StartImport': grpc.unary_unary_rpc_method_handler(
                    servicer.StartImport,
                    request_deserializer=PalatialWeb__pb2.ImportInfo.FromString,
                    response_serializer=PalatialWeb__pb2.Ack.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'palatialrpc.PalatialWebCommunication', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PalatialWebCommunication(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StartImport(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/palatialrpc.PalatialWebCommunication/StartImport',
            PalatialWeb__pb2.ImportInfo.SerializeToString,
            PalatialWeb__pb2.Ack.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class PalatialServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendEditingCommand = channel.unary_unary(
                '/palatialrpc.PalatialServer/SendEditingCommand',
                request_serializer=PalatialWeb__pb2.EditingAction.SerializeToString,
                response_deserializer=PalatialWeb__pb2.Ack.FromString,
                )
        self.CommitEdits = channel.unary_unary(
                '/palatialrpc.PalatialServer/CommitEdits',
                request_serializer=PalatialWeb__pb2.CommitAction.SerializeToString,
                response_deserializer=PalatialWeb__pb2.Ack.FromString,
                )


class PalatialServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendEditingCommand(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CommitEdits(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PalatialServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendEditingCommand': grpc.unary_unary_rpc_method_handler(
                    servicer.SendEditingCommand,
                    request_deserializer=PalatialWeb__pb2.EditingAction.FromString,
                    response_serializer=PalatialWeb__pb2.Ack.SerializeToString,
            ),
            'CommitEdits': grpc.unary_unary_rpc_method_handler(
                    servicer.CommitEdits,
                    request_deserializer=PalatialWeb__pb2.CommitAction.FromString,
                    response_serializer=PalatialWeb__pb2.Ack.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'palatialrpc.PalatialServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PalatialServer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendEditingCommand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/palatialrpc.PalatialServer/SendEditingCommand',
            PalatialWeb__pb2.EditingAction.SerializeToString,
            PalatialWeb__pb2.Ack.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CommitEdits(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/palatialrpc.PalatialServer/CommitEdits',
            PalatialWeb__pb2.CommitAction.SerializeToString,
            PalatialWeb__pb2.Ack.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
