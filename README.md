# Команды Docker

## Введение 
Docker - это платформа для разработки, доставки и эксплуатации приложений в контейнерах. Контейнеры - это изолированные, легкие, исполняемые среды, содержащие все необходимое для запуска приложения.

В этом документе представлены основные команды Docker:

### 1. Управление образами

### `docker build`:
- Описание: Собирает образ из Dockerfile.
- Пример: `sudo docker build -t my-app .`


#### `docker pull`:
- Описание: Загружает образ из реестра Docker Hub.
- Пример: `sudo docker pull docker.io/library/postgres:latest`

#### `docker push`:
- Описание: Отправляет образ в реестр Docker Hub.
- Пример: `sudo docker push my-app`

#### `docker images`:
- Описание: Выводит список образов на локальной машине.

#### `docker rmi`:
- Описание: Удаляет образ с локальной машины.
- Пример: `sudo docker rmi my-app`

### 2. Управление контейнерами:

#### `docker run`:
- Описание: Запускает контейнер из образа.
- Пример: `sudo docker run -p 8000:8000 my-app`

#### `docker ps`:
- Описание: Выводит список запущенных контейнеров.

#### `docker stop`:
- Описание: Останавливает контейнер.
- Пример: `sudo docker stop my-app`

#### `docker start`:
- Описание: Запускает остановленный контейнер.
- Пример: `sudo docker start my-app`

#### `docker restart`:
- Описание: Перезапускает контейнер.
- Пример: `sudo docker restart my-app`

#### `docker logs`:
- Описание: Выводит логи контейнера.
- Пример: `sudo docker logs my-app`

#### `docker exec`:
- Описание: Выполняет команду в контейнере.
- Пример: `sudo docker exec -it my-app bash`

#### `docker rm`:
- Описание: Удаляет контейнер.
- Пример: `sudo docker rm my-app`

### 3. Дополнительные команды:

#### `docker inspect`:
- Описание: Выводит подробную информацию о контейнере или образе.
- Пример: `sudo docker inspect my-app`

#### `docker history`:
- Описание: Выводит историю изменений образа.
- Пример: `sudo docker history my-app`

#### `docker login`:
- Описание: Авторизуется в реестре Docker Hub.

#### `docker logout`:
- Описание: Выходит из учетной записи Docker Hub.

#### `docker help`:
- Описание: Выводит справку по командам Docker.

### Важно:

- `sudo` используется для выполнения команд с правами root.
- `-t` в команде `docker run` указывает имя контейнера.
- `-p` в команде `docker run` публикует порт контейнера на хост-машине.

### Дополнительные команды:

#### `docker-compose`:
- Описание: Инструмент для управления сложными приложениями, состоящими из нескольких контейнеров.

### Ссылки:

- Docker Documentation: [https://docs.docker.com/](https://docs.docker.com/)
- Docker Compose Documentation: [https://docs.docker.com/compose/](https://docs.docker.com/compose/)
