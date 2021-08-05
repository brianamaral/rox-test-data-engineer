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

* Para a implementação, inicialmente enviei os csv's para um bucket do s3 com a seguinte estrutura de diretórios:
```sh
|--person
  |--Person.Person.csv
|--production
  |--Production.Product.csv
|--sales
  |--Sales.Customer.csv
  |--Sales.SalesOrderDetail.csv
  |--Sales.SalesOrderHeader.csv
  |--Sales.SpecialOfferProduct.csv
```

* Em seguida, subi uma instância do Postgres pelo RDS, e abri o acesso público do mesmo.

* Posteriormente, segui para a construção da lambda function. Inicialmente tive alguns problemas em colocar bibliotecas externas, porém conseguir resolver o problema utilizando o sistema de layers para cada biblioteca utilizada. A abordagem é bem direta, primeiro me conecto com o bucket do s3 pela lib boto3 e baixo os arquivos de dados, em seguida faço a conexão com o postgres pelo SQLAlchemy, após isso utilizo o pandas para carregar os csv's como DataFrames, para simplificar a manipulação, e por fim, dou insert no banco em batch.

* Para a Lambda, reservei 512 mb de ram, a mesma demora 3 minutos para rodar. Com mais tempo eu teria conseguido otimizar, porém tinham outras partes do projeto a serem desenvolvidas.
* E por fim


