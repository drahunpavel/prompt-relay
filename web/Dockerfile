FROM node:22-alpine AS builder

WORKDIR /app

COPY web/package.json web/yarn.lock ./

RUN yarn install

COPY web .

RUN yarn build

FROM nginx:alpine

RUN rm /etc/nginx/conf.d/default.conf

COPY /nginx/default.conf /etc/nginx/conf.d/default.conf

COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]