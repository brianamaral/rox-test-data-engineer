# Minha solução para o teste técnico para vaga de Engenheiro de Dados Jr na Rox Partner

## Modelagem conceitual dos dados
![plot](./src/diagrama.png)

## Arquitetura do projeto
![plot](./src/arquitetura.png)

Para minha solução, criei a arquitetura acima, tomei a liberdade de considerar que os dados brutos viriam de um bucket do s3, por ser um serviço barato e prático de armazenamento em cloud
e vários outros serviços de dados da AWS se comunicam com facilidade com o mesmo. Após decidir a fonte das informações, ao pensar onde iria acontecer o processamento dos dados e o envio para o banco
pensei em usar o AWS Glue, porém pela precificação e poder de processamento (que justifica o preço), seria um desperdicio utilizar para uma carga de dados simples, então me veio a ideia de utilizar uma Lamba Function,
por ser um serviço que cobra apenas pelo tempo de processamento, com uma carga leve de trabalho, que hipoteticamente tenderia a rodar poucas ou apenas uma vez ao dia, a quantia cobrada seria ínfima e sem perder muita performance.
Considerei utilizar o RDS para dar deploy de um banco Postgresql, pois deixo o encargo da infraestrutura e configuração do banco toda a encargo do serviço da AWS, tornando o processo mais simples. E por fim, utilizei o Apache Airflow para orquestrar a execução dessa Lambda por meio de um endpoint.

## Implementação

