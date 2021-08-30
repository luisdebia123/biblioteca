import pytest
from app_libros.models import Autor


@pytest.mark.django_db
def test_user_creation():
    autor = Autor.objects.create(
        nombre = 'gggg',
        apellidos = 'ggggg'
    )

    assert autor.nombre == 'gggg'

