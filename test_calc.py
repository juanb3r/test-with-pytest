import calculador


def test_suma():
    # Arrange
    numero_de_prueba = 4

    # Act
    numero_obtenido = calculador.suma(2, 2)

    # Assert
    assert numero_de_prueba == numero_obtenido


def test_resta():
    # Arrange
    numero_de_prueba = 0

    # Act
    numero_obtenido = calculador.resta(3, 2)

    # Assert
    assert numero_de_prueba == numero_obtenido
