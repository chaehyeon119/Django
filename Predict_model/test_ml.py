import pytest
from ml import predict

"""'
print(predict("33.jpg"))
print(predict("44.jpg"))
"""


@pytest.mark.parametrize("image_path, expected", [("33.jpg", 3), ("44.jpg", 4)])
def test_predict(image_path, expected):
    assert predict(image_path) == expected

