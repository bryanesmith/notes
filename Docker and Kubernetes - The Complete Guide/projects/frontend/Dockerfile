# >>> STAGE 1: build <<<
FROM node:16-alpine as builder
WORKDIR '/app'

# install dependencies
COPY package.json .
RUN npm install

# build website -> /app/build
COPY . .
RUN npm run build

# >>> STAGE 2: deploy <<<
FROM nginx
COPY --from=builder /app/build /usr/share/nginx/html
# default command of nginx container will start the server, so no CMD required
