from pessoa import Pessoa

def test_get_cpf():
    p = Pessoa("João", 25, "123.456.789-00", "")
    assert p.get_cpf() == "123.456.789-00"

def test_set_cpf_valido():
    p = Pessoa("João", 25, "123.456.789-00", "")
    p.set_cpf("987.654.321-00")
    assert p.get_cpf() == "987.654.321-00"

def test_set_cpf_invalido():
    p = Pessoa("João", 25, "123.456.789-00", "")
    p.set_cpf("invalido")
    # CPF não deve mudar
    assert p.get_cpf() == "123.456.789-00"