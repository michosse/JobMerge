FROM node:latest as angular
ARG API_URL
ENV API_URL=${API_URL}
WORKDIR /app
COPY . /app
RUN npm install
RUN npm run build --prod
FROM nginx:latest
COPY --from=angular /app/dist/merger /usr/share/nginx/html
EXPOSE 80
