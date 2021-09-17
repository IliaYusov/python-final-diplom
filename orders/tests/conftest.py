import pytest
from model_bakery import baker
from rest_framework.test import APIClient
from django.conf import settings


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture(scope='session')
def celery_config():
    return {
        'broker_url': 'memory://',
        'result_backend': 'rpc',
    }


@pytest.fixture
def user_factory():
    def factory(**kwargs):
        return baker.make('backend.User', **kwargs)

    return factory


@pytest.fixture
def category_factory():
    def factory(**kwargs):
        return baker.make('backend.Category', **kwargs)

    return factory


@pytest.fixture
def shop_factory():
    def factory(**kwargs):
        return baker.make('backend.Shop', **kwargs)

    return factory


@pytest.fixture
def product_factory():
    def factory(**kwargs):
        return baker.make('backend.Product', **kwargs)

    return factory


@pytest.fixture
def product_info_factory():
    def factory(**kwargs):
        return baker.make('backend.ProductInfo', **kwargs)

    return factory
