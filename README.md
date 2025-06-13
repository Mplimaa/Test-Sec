# Test-Sec

Repositório de Análise de Desempenho, Segurança e Usabilidade em Python

Este projeto reúne scripts Python com foco em análise de desempenho de websites, testes unitários, boas práticas de segurança, orientação a objetos e verificação de compatibilidade de sistema operacional.

## Estrutura do Projeto

.
├── desempenho.py
├── pessoa.py
├── seguranca.py
├── test_pessoa.py
├── test_pessoa_formato_cpf.py
└── usabilidade.py

---

##  Descrição dos Arquivos

### `desempenho.py`
Mede o tempo de resposta de um site realizando múltiplas requisições HTTP.

- Requisitos: `requests`
- Execução:
  instalar o framework requests
  pip install requests
  python desempenho.py
  

Classe Pessoa com encapsulamento de dados e validação de CPF e endereço. -> pessoa.py

Métodos principais:

falar(), andar(), get_cpf(), set_cpf(), get_endereco(), set_endereco()

test_pessoa.py e test_pessoa_formato_cpf.py
Testes unitários simples para validar o comportamento da classe Pessoa.


 Testes:

Formato correto e incorreto de CPF

Getter e setter do atributo cpf

seguranca.py
Exemplo de código propositalmente vulnerável usado para análise com o Bandit.


 Análise de segurança:

instalar framework bandit
pip install bandit
bandit -r seguranca.py
usabilidade.py
Detecta o sistema operacional do usuário e imprime uma mensagem específica.


Como Executar os Testes?
Você pode usar pytest para executar os arquivos de teste:
Instalar o framework pytest -> pip install pytest , após executar os arquivos.
pytest test_pessoa.py
pytest test_pessoa_formato_cpf.py


 Possíveis Melhorias

Adicionar logs aos scripts.

Implementar outros testes de desempenho automatizados.

Refatorar seguranca.py para boas práticas seguras.

Substituir eval() por parsing seguro com ast.literal_eval.

 Aviso de Segurança
O script seguranca.py contém código propositalmente inseguro com o uso de eval() — não use em produção.


 Todos os diretos reservados, Michele Lima, uso somente para fins didáticos.
