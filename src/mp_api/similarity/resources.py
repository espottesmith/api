from mp_api.core.resource import Resource
from mp_api.similarity.models import SimilarityDoc
from mp_api.core.query_operator import PaginationQuery, SparseFieldsQuery


def similarity_resource(similarity_store):
    resource = Resource(
        similarity_store,
        SimilarityDoc,
        query_operators=[
            PaginationQuery(),
            SparseFieldsQuery(SimilarityDoc, default_fields=["task_id"]),
        ],
        tags=["Similarity"],
        enable_default_search=False,
    )

    return resource
