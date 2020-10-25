# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from technews_api.v1alpha1.search.article import services_pb2 as technews__api_dot_v1alpha1_dot_search_dot_article_dot_services__pb2
from technews_api.v1alpha1.search.category import services_pb2 as technews__api_dot_v1alpha1_dot_search_dot_category_dot_services__pb2


class SearchServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ListCategories = channel.unary_unary(
        '/technews_api.v1alpha1.search.SearchService/ListCategories',
        request_serializer=technews__api_dot_v1alpha1_dot_search_dot_category_dot_services__pb2.ListCategoriesRequest.SerializeToString,
        response_deserializer=technews__api_dot_v1alpha1_dot_search_dot_category_dot_services__pb2.ListCategoriesResponse.FromString,
        )
    self.ListArticles = channel.unary_unary(
        '/technews_api.v1alpha1.search.SearchService/ListArticles',
        request_serializer=technews__api_dot_v1alpha1_dot_search_dot_article_dot_services__pb2.ListArticlesRequest.SerializeToString,
        response_deserializer=technews__api_dot_v1alpha1_dot_search_dot_article_dot_services__pb2.ListArticlesResponse.FromString,
        )


class SearchServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def ListCategories(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListArticles(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SearchServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ListCategories': grpc.unary_unary_rpc_method_handler(
          servicer.ListCategories,
          request_deserializer=technews__api_dot_v1alpha1_dot_search_dot_category_dot_services__pb2.ListCategoriesRequest.FromString,
          response_serializer=technews__api_dot_v1alpha1_dot_search_dot_category_dot_services__pb2.ListCategoriesResponse.SerializeToString,
      ),
      'ListArticles': grpc.unary_unary_rpc_method_handler(
          servicer.ListArticles,
          request_deserializer=technews__api_dot_v1alpha1_dot_search_dot_article_dot_services__pb2.ListArticlesRequest.FromString,
          response_serializer=technews__api_dot_v1alpha1_dot_search_dot_article_dot_services__pb2.ListArticlesResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'technews_api.v1alpha1.search.SearchService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
