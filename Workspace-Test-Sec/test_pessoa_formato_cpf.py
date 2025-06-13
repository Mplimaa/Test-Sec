from pessoa import Pessoa


def test_set_cpf_formato_incorreto():
    p = Pessoa("Maria", 30, "123.456.789-00", "")
    p.set_cpf("12345678900")  # formato inválido
    assert p.get_cpf() == "123.456.789-00" 

def test_set_cpf_valido_formatado():
    p = Pessoa("Carlos", 40, "111.222.333-44", "")
    p.set_cpf("999.888.777-66")  # formato válido
    assert p.get_cpf() == "999.888.777-66"

