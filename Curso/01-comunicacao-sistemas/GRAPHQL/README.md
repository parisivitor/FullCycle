Usando o projeto pronto:

Para dar inicio a aplicação:  ```run cmd/server/server.go```

Para fazer o generate do schema.resolvers.go:  ```go run github.com/99designs/gqlgen generate```



Configuração inicial:

iniciar projeto go: ```go mod init github.com/fullcycle/02/graphql```

baixar projeto qglgen: ```printf '// +build tools\npackage tools\nimport (_ "github.com/99designs/gqlgen"\n _ "github.com/99designs/gqlgen/graphql/introspection")' | gofmt > tools.go```

baixar dependencias do go: ```go mod tidy```

BANCO

Criar banco:  ```sqlite3 data.db```

Dentro do terminal:
    - criar tabela: ```create table courses;```
    - deletar tabela: ```drop table courses;```
    - listar tableas: ```.tables;```
    - visualizar dadaos tableas: ```select * from courses;```
