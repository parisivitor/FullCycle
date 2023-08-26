Necessario protoc instalado no go!!:```protoc --version```

Iniciar projeto: ```go mod init github.com/fullcycle/02/gRPC```
instalar dependencias: ```go mod tidy```
configurar o rpc sobre nossa entidade: ```protoc --go_out=. --go-grpc_out=. proto/course_category.proto```
baixar pacotes necessarios: ```go mod tidy```
